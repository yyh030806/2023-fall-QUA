# SILQ

## 基本语法

### 类型

##### 量子整数

在量子语言中，变量分为量子的和经典的，经典类型和我们常用的语言中的类型类似，但是量子类型只能出现整数和由整数构成的类型。

例如在 `Silq` 中，这些整数类型可以表示为 `int[n]` 和 `uint[n]`。`n` 表示整数的位数，例如，`int[8]` 表示一个 8 位的整数，可以表示从 -128 到 127 的所有整数。

“量子” 是指这些整数被存储在量子比特（qubits）上，而不是传统的经典比特上，可以存在于多个状态的叠加态。

##### 类型限制

`Silq` 支持固定大小的量子整数类型 `int[n]`（包含 n 位整数）和 `uint[n]`（包含 n 位无符号整数）的量子值，但它不允许类型为 `ℤ`（包含所有整数）或 `ℕ`（包含所有自然数）的量子值，因为`Silq` 不支持那些需要动态分配内存来存储的类型的量子值。

### 标识符

##### 经典类型

在量子计算语言中，参数可能是经典的，也可能是量子的，如果想要像我们常用的语言中那样自由地对经典参数进行访问和操作，需要显式地声明它是经典的，否则，就需要用量子地方式对量子态进行操作和测量。比如`1+2`的类型是`!int[n]`，`f: !B !→ !B`是一个输入和输出都是经典Boolean类型的经典函数。

`Silq` 要求泛型参数必须是经典的。

##### `qfree`

如果一个函数被标注为`qfree`，那么说明这个函数既不引入也不销毁叠加态。

例如`X`门就是`qfree`函数，它的作用是$\sum_{v=0}^{1} \gamma_v |v\rangle \text{ 转换为 } \sum_{v=0}^{1} \gamma_v |1-v\rangle$。

而`H`门不是`qfree`的，因为它将基态$|0\rangle$映射为叠加态$$\frac{1}{\sqrt{2^n}} \left( |0\rangle + |1\rangle \right)$$。

##### `mfree`

`mfree`表示一个函数可以在不进行任何测量的情况下进行评估。

在量子计算中，"测量"是一个特殊的操作，它可以将一个处于叠加态的量子比特塌缩到一个确定的基态。如果一个函数被标记为`mfree`，那么我们可以在不需要进行任何测量的情况下计算该函数的结果。

##### `1`

如果一个函数显式声明类型为1，那么这个函数没有返回值，示例如下：

```javascript
def Func[n:!ℕ](const b:!𝔹, x:uint[n]):𝟙{
  if b{
    x := measure(x);
  }
}
```

##### `const`

如果一个参数或者变量被`const`修饰，这意味着这些参数和变量的值在给定的上下文中是保持不变的。一般来说，经典变量一般默认是`const`的。

如果函数参数没有被标注为 `const`，那么在调用函数后，这些参数将不再可访问，也就是说，函数会消耗它们。

例如对于一个量子态`cand`，对它进行测量就将消耗它：

```javascript
measure(cand)
```

##### `lifted`

 `lifted` 用来标识只有`const`参数的 `qfree` 函数。

如下，`MyFunc`是`lifted`的：

```javascript
def MyOr(x:!𝔹, y:!𝔹)lifted{ // x和y默认是const的
  return x||y;
}
```

### 变量赋值

##### 初始化与类型转换

```javascript
  a:=0:!𝔹; // 经典比特，值为0
  b:=a:𝔹; // 量子比特，状态为0
  c:=0:uint[3]; // 3比特量子无符号数，状态为000
  d:=vector(4,false):𝔹[]; // 4比特量子向量
```

`Silq`允许在静态类型转换的条件下重新定义变量类型。

更一般的安全类型转换需要在特定的变量之间进行，如下：

```javascript
  // !int[32] to !ℤ
  a:=0:!int[32];
  b:=a as !ℤ;

  // !ℤ to !int[32]
  c:=0:!ℤ;
  d:=c as !int[32];

  // 𝔹^10 to int[10]
  e:=vector(10,0:𝔹);
  f:=e as int[10];

  // int[10] to 𝔹^10
  g:=0:int[10];
  h:=g as 𝔹^10;

  // convert element-wise
  i:=(0,1,2):!ℕ^3;
  j:=i as !ℕ×!ℤ×!int[3];
}
```

##### 量子常量和经典常量

`x := false`默认`x`是经典类型，如果需要一个量子常量，需要显式修改为`x := false:𝔹`。

对于一个非`qfree`的函数，比如`H(x)`，若x是经典类型常量则会报错。

##### 向量/数组

`Silq`允许对向量/数组的每一位进行单独操作：

```javascript
def uniformSuperposition[n:!ℕ]():𝔹^n{
  vec := vector(n,0:𝔹);
  for i in [0..n){
    vec[i] := H(vec[i]);
  }
  return vec;
}
```

##### 电路对应

以下代码片段将 `Hadamard` 变换应用于量子比特，并且为结果指定名称为`y`，此代码片段编译到电路会产生一个单比特`Hadamard`门，输入为量子变量`x`，输出为量子变量`y`。

```javascript
y:=H(x);
```

下面写法表示消耗了原始的x，但是将输出重新命名为`x`。

```javascript
x:=H(x);
```

### 控制流

#### 条件语句

##### 基本语法

和经典语言不同，量子语言的控制流同时支持经典的和量子的流控制，如下两种条件语句均是合法的：

```javascript
def measureInBasis(b:!𝔹,x:𝔹):!𝔹{
  if b{
    x := H(x);
    return measure(x);
  }else{
    return measure(x);
  }
}

def cnot(const x:𝔹,y:𝔹):𝔹{
  if x{
    y := X(y);
  }
  return y;
}
```

值得注意的是，量子语言不允许在由量子条件控制的条件语句中出现对量子态的测量，从语义上来说这是合法的，但是从物理实现上来说这无法实现，即下列语句是非法的：

```javascript
def conditionalMeasure[n:!ℕ](const b:𝔹, x:uint[n]):𝟙{
  if b{
    x := measure(x);
  }
}
```

##### 电路对应

以下代码片段执行受`x`控制的 `Hadamard` 变换。

```javascript
if x {     // controlled on x,
  y:=H(y); // apply H to y
}
```

<img src="./img/basic-ite.svg" width="100" height="100">

#### 循环语句

##### 基本语法

- `while e {...}`: `e`必须是经典的。
- `for i in [e1..e2) {...}`:  `e1` 和 `e2` 必须是经典的。
- `for i in (e1..e2] {...}`: `e1` 和 `e2` 必须是经典的。

下列为一个量子算法模拟概率为0.5的几何分布的例子：

```javascript
def geometric():!ℕ{
    count := 0;
    ok := true;
    while ok{
        count += 1;
        ok = measure(H(false));
    }
    return count;
}
```

### 函数

##### 可逆性

在量子计算过程中，函数在底层电路的实现其实是各种量子门的组合，这种计算是可逆的，相应的，`mfree`函数和由函数构成的过程也是可逆的。

例如，下面就是一个参数为precision的量子傅里叶变换函数的逆函数`reverse(QFT[precision])()`作用于参数`ancilla`的过程：

```javascript
ancilla := reverse(QFT[precision])(ancilla);
```

##### 常见函数

正如上面所说，量子语言中的函数一般在电路中有量子门组合与之对应，下面是一些常见的

| Function: Type                 | Explanation                                                  |
| ------------------------------ | ------------------------------------------------------------ |
| `measure: τ→!τ`                | 对量子态进行测量                                             |
| `H:𝔹→mfree 𝔹`                  | Hadamard门                                                   |
| `phase:!ℝ→mfree 𝟙`             | `phase`指的是一个量子态的相位，相位是一个复数。`phase(r)`操作会将当前量子态的相位乘以$e^{ir}$，改变相位，但不改变量子态概率幅度。phase只有在量子条件语句中执行时才会有可观察的效果，单独的相位变化不可观察，只有当两个量子态的相位差发生变化时，才能通过干涉效应观察到相位的变化。 |
| `rotX:!ℝ×𝔹→mfree 𝔹`            | eir`rotX(r,b)` 返回 `b:𝔹` 绕x轴旋转 `r:!ℝ`                   |
| `rotY:!ℝ×𝔹→mfree 𝔹`            | `rotY(r,b)` 返回 `b:𝔹` 绕`y`轴旋转 `r:!ℝ`                    |
| `rotZ:!ℝ×𝔹→mfree 𝔹`            | `rotZ(r,b)` 返回 `b:𝔹` 绕`z`轴旋转 `r:!ℝ`                    |
| `X:𝔹→qfree 𝔹`                  | `X(b)` 返回比特翻转：$|b\rangle \rightarrow|1-b\rangle$      |
| `Y:𝔹→mfree 𝔹`                  | `Y(b)` 返回 `b` 经过 `Y`门的结果: $|b\rangle\rightarrow i(-1)^b|1-b\rangle$ |
| `Z:𝔹→mfree 𝔹`                  | `Z(b)` 返回 `b` 经过 `Z`门的结果: $|b\rangle\rightarrow(-1)^b|b\rangle$ |
| `dup:const τ→qfree τ`          | `dup(v)`返回`v`的复制 `v`: $|v⟩↦|v⟩|v⟩$                      |
| `array:!ℕ×const τ×→qfree τ[]`  | `vector(m,v)` 返回一个由m个 `v`的复制组成的数组              |
| `vector:!ℕ×const τ×→qfree τ^n` | `vector(m,v)` 返回一个由m个 `v`的复制组成的向量              |

## 代码样例

下面是一个使用`Silq`语言编写`Grover’s algorithm`的例子，这是一个量子搜索算法，用于解决无结构搜索问题，给定了一组N个元素，希望找到一个被标记的元素。经典计算机需要搜索所有N个元素才能找到被标记的元素，需要O(N)的时间，而Grover’s algorithm可以在O($\sqrt{N}$)的时间内找到被标记的元素。

对于给定函数：
$$
f: \{-2^{n-1}, ..., 2^{n-1} - 1\} \rightarrow \{0, 1\}
$$
希望找到输入 $w^*$ 使得 $f(w^*) = 1$。为简单起见，我们只讨论 $w^*$ 是唯一的情况，即对所有 $v \neq w^*$，我们有 $f(v) = 0$。

**代码：**

```javascript
def grover[n:!N](f:const int[n]!→qfree 𝔹){
    nIterations:=ceil(pi/4*sqrt(2^n));
    // 初始化量子态为每一位为0
    cand:=0:int[n];
    // 利用H门对每一位进行运算，得到一个等概率分布的量子态
    for k in [0..n) {cand[k] := H(cand[k]); }
    for k in [0.. Iterations){
        // 迭代运算，增加w*系数的大小，增加测量的概率
        if f(cand) {
            phase(π);
        }
		cand:=groverDiff[n](cand);
    }
    return measure(cand);
}
```



