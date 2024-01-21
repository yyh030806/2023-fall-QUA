# Q#

Q#量子编程语言是 Azure Quantum Development Kit的一部分，Azure 为程序可视化和分析提供丰富的 IDE 支持和工具。 使用 Q# 和 Quantum Development Kit (QDK) 可以使用 Azure Quantum 编写量子程序并在实际量子硬件上运行它们。

### 命名空间

Q# 程序通常以命名空间开头，例如：

```C++
namespace Superposition {
    // Your code goes here.
}
```

命名空间是由用户自定义的，每个 qsharp (*.qs) 文件只能有一个命名空间。

### EntryPoint ()

特性 `@EntryPoint()` 告知 Q# **编译器**从何处开始执行程序。 在具有多个函数和操作定义的程序中， `@EntryPoint()` 可以放在任何函数或操作之前，使程序流从那里开始并按顺序继续。

```c++
    ...
    @EntryPoint()
    operation MeasureOneQubit() : Result {
        ...
```

### %%qsharp 命令

默认情况下， 要在 Jupyter Notebook 中将代码添加到 Q# 笔记本单元格，需要使用 `%%qsharp` 命令，该命令通过 `qsharp` Python 包启用。

Jupyter Notebook中的上一个示例代码如下所示：

```python
import qsharp
```

```C++
%%qsharp

    operation MeasureOneQubit() : Result {
        // 分配一个量子比特，默认为0     
        use q = Qubit();  
        // H门  
        H(q);
    	// 测量
        let result = M(q);
        // 再释放这个比特之前Reset它
        Reset(q);
        // 打印结果
        Message($"Result is {result}");
        return result;
    }
    MeasureOneQubit();
```

注意，这里没有添加命名空间或 `@EntryPoint()`，Jupyter Notebooks 不需要这些内容。 操作不需要通过入口点进入，而是直接在最后一行中调用。 

使用 `%%qsharp` 命令时：

- 必须先运行 `import qsharp` 才能启用 `%%qsharp` 命令。
- 命令 `%%qsharp` 的范围限定为显示命令的整个单元格。
- 命令后面的 Q# 代码必须遵循标准的 Q# 编码语法。 例如，注释由 `//` 而不是python的`#`表示，并且代码行必须以分号 `;` 结尾。
- `%%qsharp` 命令在其单元格中不能位于 Python 语句之前或之后。

### 类型

Q# 提供了许多大多数语言通用的内置类型，包括 `Int`、 `Double`、 `Bool`和 `String`，以及范围、数组和元组等较为复杂的类型，特别地，还包含特定的量子计算的类型。 例如， `Result` 类型表示任何量子比特度量的结果，并且可以具有两个可能定义的值之一： `One` 和 `Zero`。 在示例程序中，运算`MeasureOneQubit()`的返回类型就是`Result`，通过`M`作用于量子比特来获取。

```C++
operation MeasureOneQubit() : Result {
    ...
    let result = M(q);
    return result;
}
```

### 分配量子位

在 Q# 中，通过 `use`关键字分配量子比特。

定义单个量子比特：

```C++
use q = Qubit();
```

分配多个量子比特，并通过其索引访问每个量子比特：

```C++
use qubits = Qubit[2];
X(qubits[1]);
H(qubits[0]);
```

默认情况下，使用 `use` 关键字分配的每个量子位最初都为 0 态。 在程序结束时释放每个量子比特之前， **必须** 重置回零状态。 未能重置量子比特将触发运行时错误。

```C++
// Reset
Reset(q);
```

### 量子操作

分配后，可以将量子比特传递到操作和函数，也称为可调用对象。 **操作**(Operation) 是 Q# 程序的基本构建模块。 一个Q# 操作是一个量子子例程。 也就是说，它是一个包含修改量子位寄存器状态的量子操作。

要定义 Q# 操作，你需要指定运算的名称及其输入和输出。下面是一个没有参数，并且预期返回类型为`Result` 的操作，此时，单个操作实质上就是整个程序：

```qsharp
operation MeasureOneQubit() : Result {
    ...
}
```

下面无任何参数，也没有返回值的操作。 在这里 `Unit` 等效于 `NULL` 。

```qsharp
operation SayHelloQ() : Unit {
    Message("Hello quantum world!");
}
```

Q#库提供了很多可以直接使用的操作，例如 Hadamard (`H` )。 在 Z 基指定一个量子比特，`H` 操作会将量子比特置于平均的量子态中，即量子比特被测量为 0 或 1 的几率是 50%。

### 测量量子比特

有许多种类的量子测量，但 Q# 侧重于单个量子比特（也称为Pauli 测量）的投影测量。 在给定基（例如计算基 |0⟩,|1⟩）上进行测量时，量子比特状态将投影到所测量的任何基状态，从而破坏两者之间的叠加。

我们的示例程序使用 `M` 运算，该运算对 Pauli Z 基中的单个量子比特执行测量并返回类型 `Result` 。

### 库

Q# 广泛使用库。 库是一个包，包含了可在量子程序中使用的函数和操作。

可以通过指定完整的命名空间来调用函数或操作，或使用 `open` 语句使该库的所有函数和操作都可用，并使代码更易于阅读。 这两个示例调用相同的操作：

```C++
 Microsoft.Quantum.Intrinsic.Message("Hello quantum world!");
```

```C++
open Microsoft.Quantum.Intrinsic;
Message("Hello quantum world!");
```

请注意，在示例程序中， `open` 实际上没有后缀上完整的命名空间。 这是因为 Q# 开发环境默认自动加载两个包含常用函数和操作的通用库和：`Microsoft.Quantum.Core`和  `Microsoft.Quantum.Intrinsic` 。

例如，可以利用`Microsoft.Quantum.Measurement`库中的 `MResetZ`操作来优化示例程序中的代码。 `MResetZ` 将度量和`Reset`操作合并为一个步骤，如下所示：

```C++
namespace Superposition {
	// 打开库
    open Microsoft.Quantum.Measurement;

    @EntryPoint()
    operation MeasureOneQubit() : Result {
        use q = Qubit();  
        H(q);   
        return MResetZ(q);
    }
}
```

### Q#运行

Q#可以在 VS Code 的本地模拟器上运行，也可以在微软提供的 Azure Quantum 硬件资源或第三方模拟器上运行程序。

如上面所介绍的，Q#可以除了可以直接构建*.qs项目外，也可以通过Python 程序或Jupyter Notebook访问项目。

下面是一个Q#项目示例：

目录结构：

- Teleportation_project
  - *qsharp.json*（包含*作者*和*许可证*字段）
  - src
    - *RunTeleport.qs*
    - TeleportOperations
      - *Teleport.qs*
      - PrepareState
        - *PrepareState.qs*

main文件 *RunTeleport.qs* 包含入口点，并引用*Teleport.qs*中的命名空间 `TeleportLib`。

```C++
namespace RunTeleport {

    open TeleportLib;   // Teleport.qs中的命名空间

    @EntryPoint()
    operation RunTeleportationExample() : Unit {
        use msg = Qubit();
        use target = Qubit();

        H(msg);
        Teleport(msg, target);    // TeleportLib中的操作
        H(target);

        if M(target) == Zero {
            Message("Teleported successfully!");
        
        Reset(msg);
        Reset(target);
        }
    }
}
```

*Teleport.qs* 利用*PrepareState.qs* 中的`PrepareBellPair()`操作定义操作`Teleport()` 。

```C++
namespace TeleportLib {

    open PrepareBell;     // 利用PrepareState.qs中的命名空间

    operation Teleport(msg : Qubit, target : Qubit) : Unit {	// 将msg量子比特的状态传送到target量子比特上
        use here = Qubit();
        PrepareBellPair(here, target);      // PrepareBell中的操作，here和target两个量子比特制备成 Bell 对
        Adjoint PrepareBellPair(msg, here);	// 使用Adjoint关键字对PrepareBellPair进行逆操作，将msg量子比特恢复到原始状态
		
        if M(msg) == One { Z(target); }
        if M(here) == One { X(target); }

        Reset(here);
    }
}
```

*PrepareState.qs* 文件包含用于创建 Bell 对的标准可重用操作。Bell 对是一种特殊的纠缠态，当其中一个量子比特进行测量时，它的状态就会立刻确定，并且另一个量子比特的状态也会发生相应的改变。

在*PrepareBellPair*的返回类型中：

`Adj`表示该操作是可逆的。在量子计算中，所有的操作都应该是可逆的，这是因为量子计算的基本操作必须能够逆转。

`Ctl`表示该操作是控制操作。在量子计算中，控制操作是一种特殊的操作，它会根据一个或多个控制位的状态来决定是否执行。在这个上下文中，"Ctl" 表示 *PrepareBellPair* 操作是一个控制操作，在这部分中*left*是控制位。

```C++
namespace PrepareBell {    
    
    operation PrepareBellPair(left : Qubit, right : Qubit) : Unit is Adj + Ctl {
        H(left);
        CNOT(left, right);
        // CNOT 是两比特门，控制比特left为1时，目标比特right的状态进行翻转，得到叠加态(|00⟩ + |11⟩) / √2
    }
}
```

### 库

Q#有非常丰富的库，主要分为标准库和量子数字库。

#### 标准库

##### Prelude

`prelude`是标准库中十分重要的组成部分，提供了一组非常有用的基本函数和运算，可将其用于在 Q# 中编写量子程序。

例如， `Microsoft.Quantum.Intrinsic` 命名空间包括 Pauli 运算符 (X、 Y 和 Z、 Hadamard 运算、旋转运算（如 S]、 T ）和常规 R 运算。 还可以查找双量子比特操作，例如 CNOT 和 SWAP 操作。 本节还定义了对一个或多个量子比特执行联合测量的 Measure 操作。

##### 量子算法

标准库中有量子算法库，可以编写一些常用且非常有用的量子算法。 例如， `Microsoft.Quantum.Canon`命名空间提供 ApproximateQFT 操作，这是量子傅立叶变换的近似泛化。

除此之外，标准库还提供了经典数学、类型转换、数据结构、高阶控制流等库。

#### 量子数字库

量子数字库库由三个组件组成：

1. **基本整数算法**，带有整数添加器和比较运算符
2. **高级整数功能**，它建立在基本功能之上，包括有符号和无符号整数的乘法、除法、求逆等。
3. **定点算术功能**，包含定点初始化、加法、乘法、倒数、多项式求值和度量。

可以使用单个 `open` 语句访问所有这些组件：

```qsharp
open Microsoft.Quantum.Arithmetic;
```

功能：

能够实现对量子比特构成的量子整数的加法、乘法、除法、比较等操作，是对底层电路的复杂构造实现的等价操作，类比地实现了量子的数字计算。