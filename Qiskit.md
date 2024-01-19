# Qiskit

Qiskit 是由 IBM 提供的开源量子计算软件开发工具包

##Quantum Circuit Construction

###Qubit

```
qiskit.circuit.Qubit(register=None, index=None)
```

量子位的实现，创建一个量子位。

####参数

- **register**  - 可选。包含该位的量子寄存器。
- **index**  - 可选。位在其包含寄存器中的索引。

####属性

- **index**

  获取旧式比特在拥有它的寄存器中的索引。在现代的 Qiskit Terra（0.17版及以后），比特是基本对象，而寄存器是对比特集合的别名。一个比特可以根据电路的不同而在多个寄存器中，因此单个包含寄存器不再是比特的属性。在未被寄存器“拥有”构造的比特上访问此属性是错误的。自0.17版起已弃用`qiskit.circuit.bit.Bit.index` 属性自 qiskit-terra 0.17版起已弃用。它将在发布日期后不早于3个月被移除。相反，使用 `find_bit()` 来在电路中找到所有包含寄存器及比特在电路中的索引。

- **register**

  获取旧式比特的寄存器。在现代的 Qiskit Terra（0.17版及以后），比特是基本对象，而寄存器是对比特集合的别名。一个比特可以根据电路的不同而在多个寄存器中，因此单个包含寄存器不再是比特的属性。在未被寄存器“拥有”构造的比特上访问此属性是错误的。自0.17版起已弃用`qiskit.circuit.bit.Bit.register` 属性自 qiskit-terra 0.17版起已弃用。它将在发布日期后不早于3个月被移除。相反，使用 `find_bit()` 来在电路中找到所有包含寄存器及比特在电路中的索引。

###QuantumRegister

```
qiskit.circuit.QuantumRegister(size=None, name=None, bits=None)
```

量子寄存器的实现，创建一个新的通用寄存器。必须提供 `size` 或 `bits` 参数之一。如果 `size` 非空，则寄存器将预先填充正确类型的比特。

####参数

- **size** ([*int*](https://docs.python.org/3/library/functions.html#int)) - 可选。寄存器中包含的比特数。
- **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - 可选。寄存器的名称。如果未提供，则会自动生成一个基于寄存器类型的唯一名称。
- **bits** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*Bit*](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.Bit)*]*) - 可选。用于填充寄存器的 Bit() 实例列表。

####属性

**instances_counter**

```
= count(6)
```

**name**

获取寄存器名称。

**name_format**

```
= re.compile('[a-z][a-zA-Z0-9_]*')
```

**prefix**

```
= 'q'
```

**size**

获取寄存器大小。

####方法

**index**

```
index(bit)
```

在此寄存器中找到提供的比特的索引。

**qasm**

```
qasm()
```

返回此寄存器的 OPENQASM 字符串表示。

###QuantumCircuit

```
qiskit.circuit.QuantumCircuit(*regs, name=None, global_phase=0, metadata=None)
```

创建一个新的线路。一个线路是一个绑定于寄存器的指令列表

####参数

- **regs** (list([`Register`](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.Register)) 或 list(`int`) 或 list(list([`Bit`](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.Bit))))：

  要包含在电路中的寄存器。

  - 如果是 [`Register`](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.Register) 对象的列表，代表要包含在电路中的 [`QuantumRegister`](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.QuantumRegister) 和/或 [`ClassicalRegister`](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.ClassicalRegister) 对象。

    例如：

    > - `QuantumCircuit(QuantumRegister(4))`
    > - `QuantumCircuit(QuantumRegister(4), ClassicalRegister(3))`
    > - `QuantumCircuit(QuantumRegister(4, 'qr0'), QuantumRegister(2, 'qr1'))`

  - 如果是 `int` 的列表，表示电路中包含的量子比特和/或经典比特的数量。可以是单个 int（仅表示量子比特的数量），或者是两个 int 分别表示量子比特和经典比特的数量。

    例如：

    > - `QuantumCircuit(4) # 一个含有4个量子比特的量子电路`
    > - `QuantumCircuit(4, 3) # 一个含有4个量子比特和3个经典比特的量子电路`

  - 如果是包含 [`Bit`](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.Bit) 对象的 python 列表的列表，表示要添加到电路中的 [`Bit`](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.Bit) 集合。

- **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - 量子电路的名称。如果未设置，将自动分配一个生成的字符串。

- **global_phase** ([*float*](https://docs.python.org/3/library/functions.html#float) *或* [*ParameterExpression*](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.ParameterExpression)) - 电路的全局相位（以弧度为单位）。

- **metadata** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) - 与电路关联的任意键值元数据。这将作为自由格式数据存储在 [`metadata`](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.QuantumCircuit#qiskit.circuit.QuantumCircuit.metadata) 属性中的字典里。它不会直接用于电路。

* 示例：

搭建一个贝尔态生成线路

```
from qiskit import QuantumCircuit
 
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])
qc.draw('mpl')
```

![../_images/qiskit-circuit-QuantumCircuit-1.png](https://docs.quantum.ibm.com/_next/image?url=%2Fimages%2Fapi%2Fqiskit%2Fqiskit-circuit-QuantumCircuit-1.png&w=750&q=75)

搭建一个5-qubit的GHZ线路

```
from qiskit import QuantumCircuit
 
qc = QuantumCircuit(5)
qc.h(0)
qc.cx(0, range(1, 5))
qc.measure_all()
```



使用寄存器搭建一个4-qubit 的Bernstein-Vazirani线路

```
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
 
qr = QuantumRegister(3, 'q')
anc = QuantumRegister(1, 'ancilla')
cr = ClassicalRegister(3, 'c')
qc = QuantumCircuit(qr, anc, cr)
 
qc.x(anc[0])
qc.h(anc[0])
qc.h(qr[0:3])
qc.cx(qr[0:3], anc[0])
qc.h(qr[0:3])
qc.barrier(qr)
qc.measure(qr, cr)
 
qc.draw('mpl')
```

![../_images/qiskit-circuit-QuantumCircuit-2.png](https://docs.quantum.ibm.com/_next/image?url=%2Fimages%2Fapi%2Fqiskit%2Fqiskit-circuit-QuantumCircuit-2.png&w=1920&q=75)

####属性

**ancillas**

返回按照寄存器添加顺序的辅助比特列表。

**calibrations**

返回校准字典。

给定门的自定义脉冲定义形式为 `{'gate_name': {(qubits, params): schedule}}`

**clbits**

返回按照寄存器添加顺序的经典比特列表。

**data**

返回电路数据（指令和上下文）。

**return**

一个类似列表的对象，包含每个指令的 [`CircuitInstruction`](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.CircuitInstruction)。

**Return type**

QuantumCircuitData

**extension_lib**

```
= 'include "qelib1.inc";'
```

**global_phase**

以弧度为单位返回当前电路范围的全局相位。

**header**

```
= 'OPENQASM 2.0;'
```

**instances**

```
= 183
```

**layout**

返回有关电路的任何关联布局信息，此属性包含一个可选的 [`TranspileLayout`](https://docs.quantum.ibm.com/api/qiskit/qiskit.transpiler.TranspileLayout) 对象。这通常在 [`transpile()`](https://docs.quantum.ibm.com/api/qiskit/compiler#qiskit.compiler.transpile) 或 [`PassManager.run()`](https://docs.quantum.ibm.com/api/qiskit/qiskit.transpiler.PassManager#run) 的输出上设置，以保留有关通过转换对输入电路造成的排列的信息。[`transpile()`](https://docs.quantum.ibm.com/api/qiskit/compiler#qiskit.compiler.transpile) 函数引起的排列有两种类型，一种是初始布局，它根据在 [`Target`](https://docs.quantum.ibm.com/api/qiskit/qiskit.transpiler.Target) 上选择的物理量子比特排列量子比特，另一种是最终布局，这是由在路由过程中插入的 [`SwapGate`](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.SwapGate) 引起的输出排列。

**metadata**

与电路关联的用户提供的元数据。

电路的元数据是用户为电路提供的 `dict` 形式的元数据。它不会用于影响电路的执行或操作，但预期会在电路的所有转换（例如转换）之间传递，并且供应商将与其执行的电路结果关联任何电路元数据。

**num_ancillas**

返回辅助量子比特的数量。

**num_clbits**

返回经典比特的数量。

**num_parameters**

电路中的参数对象数量。

**num_qubits**

返回量子比特的数量。

**op_start_times**

返回操作开始时间列表。

一旦调度分析通过之一在量子电路上运行后，此属性将被启用。

**parameters**

电路中定义的参数。此属性返回按字母顺序排序的电路中的 [`Parameter`](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.Parameter) 对象。请注意，即使是使用 [`ParameterVector`](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.ParameterVector) 实例化的参数也仍然按数字顺序排序。

*  示例

下面的代码片段显示参数的插入顺序并不重要。

```
>>> from qiskit.circuit import QuantumCircuit, Parameter
>>> a, b, elephant = Parameter("a"), Parameter("b"), Parameter("elephant")
>>> circuit = QuantumCircuit(1)
>>> circuit.rx(b, 0)
>>> circuit.rz(elephant, 0)
>>> circuit.ry(a, 0)
>>> circuit.parameters  # 按字母顺序排序！
ParameterView([Parameter(a), Parameter(b), Parameter(elephant)])
```

请记住，在数字方面，字母排序可能会有些不直观。在严格的字母排序中，“10”在“2”之前。

```
>>> from qiskit.circuit import QuantumCircuit, Parameter
>>> angles = [Parameter("angle_1"), Parameter("angle_2"), Parameter("angle_10")]
>>> circuit = QuantumCircuit(1)
>>> circuit.u(*angles, 0)
>>> circuit.draw()
   ┌─────────────────────────────┐
q: ┤ U(angle_1,angle_2,angle_10) ├
   └─────────────────────────────┘
>>> circuit.parameters
ParameterView([Parameter(angle_1), Parameter(angle_10), Parameter(angle_2)])
```

要尊重数字排序，可以使用 [`ParameterVector`](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.ParameterVector)。

```
>>> from qiskit.circuit import QuantumCircuit, Parameter, ParameterVector
>>> x = ParameterVector("x", 12)
>>> circuit = QuantumCircuit(1)
>>> for x_i in x:
...     circuit.rx(x_i, 0)
>>> circuit.parameters
ParameterView([
    ParameterVectorElement(x[0]), ParameterVectorElement(x[1]),
    ParameterVectorElement(x[2]), ParameterVectorElement(x[3]),
    ..., ParameterVectorElement(x[11])
])
```

**返回**

电路中排序的 [`Parameter`](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.Parameter) 对象。

**prefix**

```
= 'circuit'
```

**qubits**

返回按照寄存器添加顺序的量子比特列表。

####方法

**add_bits**

```
add_bits(bits)
```

向电路中添加比特。

**add_calibration**

```
add_calibration(gate, qubits, schedule, params=None)
```

为给定的门注册低级别的自定义脉冲定义。

**add_register**

```
add_register(*regs)
```

添加寄存器。

**append**

```
append(instruction, qargs=None, cargs=None)
```

在电路末尾附加一个或多个指令，修改电路本身。

**gate**

添加各种类型的量子门

## Gates and Instructions

###Gate

```
qiskit.circuit.Gate(name, num_qubits, params, label=None, duration=None, unit='dt')
```

####**参数**

- **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - 门的Qobj名称。
- **num_qubits** ([*int*](https://docs.python.org/3/library/functions.html#int)) - 门作用的量子位数。
- **params** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) - 参数列表。
- **label** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *或 None*) - 门的可选标签。

#### 属性

- base_class

获取此指令的基类。这一定是`self`继承树中的一个类。

例如：

```
>>> isinstance(XGate(), XGate)
True
>>> type(XGate()) is XGate
False
>>> XGate().base_class is XGate
True
```

一般来说，你不应该依赖于指令的确切类别；在给定的电路中，[`Instruction.name`](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.Instruction#name)应该在大多数情况下是更合适的区分器。

- condition

指令的经典条件。

- condition_bits

获取条件中的Clbits。

- decompositions

从SessionEquivalenceLibrary获取指令的分解。

- definition

以其他基本门的定义返回。

- duration

获取持续时间。

- label

返回指令标签

- mutable

此实例是否是一个可变的唯一实例。

如果此属性为`False`，则门实例是一个共享的单例，不可变。

- name

返回名称。

- num_clbits

返回clbits的数量。

- num_qubits

返回量子位的数量。

- params

返回指令参数。

- unit

获取持续时间的时间单位。

#### 方法

- add_decomposition

```
add_decomposition(decomposition)
```

向SessionEquivalenceLibrary添加指令的分解。

- assemble

```
assemble()
```

组装一个QasmQobjInstruction

- broadcast_arguments

```
broadcast_arguments(qargs, cargs)
```

验证和处理参数及其关系。

例如，`cx([q[0],q[1]], q[2])`意味着`cx(q[0], q[2]); cx(q[1], q[2])`。这个方法按正确的分组生成参数。在给定的例子中：

```
输入: [[q[0],q[1]], q[2]], []
输出: [q[0], q[2]], []
      [q[1], q[2]], []
```

广播的一般规则是：

> - 如果len(qargs) == 1:
>
>   ```
>   [q[0], q[1]] -> [q[0]],[q[1]]
>   ```
>
> - 如果len(qargs) == 2:
>
>   ```
>   [[q[0], q[1]], [r[0], r[1]]] -> [q[0], r[0]], [q[1], r[1]]
>   [[q[0]], [r[0], r[1]]]       -> [q[0], r[0]], [q[0], r[1]]
>   [[q[0], q[1]], [r[0]]]       -> [q[0], r[0]], [q[1], r[0]]
>   ```
>
> - 如果len(qargs) >= 3:
>
>   ```
>   [q[0], q[1]], [r[0], r[1]],  ...] -> [q[0], r[0], ...], [q[1], r[1], ...]
>   ```

**参数**

- **qargs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – 量子位参数列表。
- **cargs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – 经典位参数列表。

**返回值**

带有单个参数的元组。

- c_if

```
c_if(classical, val)
```

在此指令上设置一个经典等值条件，条件是寄存器或cbit `classical`和值`val`之间的比较。

注意

这是一个设置方法，而不是一个添加方法。多次调用这个方法会无声地覆盖之前设置的任何条件；它不会叠加。

- control

```
control(num_ctrl_qubits=1, label=None, ctrl_state=None)
```

返回门的受控版本。使用情况请见 [`ControlledGate`](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.ControlledGate)。

**参数**

- **num_ctrl_qubits** ([*int*](https://docs.python.org/3/library/functions.html#int)) – 要添加到门上的控制量的数量（默认值：`1`）
- **label** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *或 None*) – 可选门标签
- **ctrl_state** ([*int*](https://docs.python.org/3/library/functions.html#int) *或*[*str*](https://docs.python.org/3/library/stdtypes.html#str) *或 None*) – 控制状态，用十进制或比特字符串表示（例如 `'111'`）。如果为`None`，使用`2**num_ctrl_qubits-1`。

**返回值**

门的受控版本。这个默认算法使用`num_ctrl_qubits-1`个辅助量子位，因此返回的门的大小为`num_qubits + 2*num_ctrl_qubits - 1`。

- copy

```
copy(name=None)
```

指令的副本。

**参数**

**name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 要赋予副本电路的名称，如果为`None`，则名称保持不变。

**返回值**

当前指令的副本，如果提供了名称，则更新名称。

- inverse

```
inverse()
```

反转此指令。

如果指令是复合的（即有定义），那么其定义将被递归反转。

特殊的继承自Instruction的指令可以实现它们自己的反转（例如 T 和 Tdg, Barrier 等）。

**返回值**

反转后的新指令

- is_parameterized

```
is_parameterized()
```

如果指令是参数化的，则返回True，否则返回False。

- power

```
power(exponent)
```

创建一个作为门的指数次方的幺正门。

- qasm

```
qasm()
```

返回指令的默认OpenQASM字符串。

- repeat

```
repeat(n)
```

创建一个重复了n次的指令。

- reverse_ops

```
reverse_ops()
```

对于复合指令，反转子指令的顺序。

- soft_compare

```
soft_compare(other)
```

门之间的软比较。它们的名称、量子位数量和经典位数量必须匹配。参数的数量必须匹配。

###ControlledGate

```
qiskit.circuit.ControlledGate(name, num_qubits, params, label=None, num_ctrl_qubits=1, definition=None, ctrl_state=None, base_gate=None, duration=None, unit=None, *, _base_label=None)
```

#### 翻译

- **name** (*str*) - 门的名称。
- **num_qubits** (*int*) - 门作用的量子位数量。
- **params** (*list*) - 门的参数列表。
- **label** (*str，可选*) - 门的可选标签。
- **num_ctrl_qubits** (*int，可选*) - 控制量子位的数量。
- **definition** (*QuantumCircuit，可选*) - 实现此门的门规则列表。列表中的元素是（[`Gate()`](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.Gate), [qubit_list], [clbit_list]）的元组。
- **ctrl_state** (*int 或 str，可选*) - 控制状态，可以是十进制或者位字符串（例如 '111'）。如果指定为位字符串，则长度必须等于 num_ctrl_qubits，最高有效位在左侧。如果为 None，则使用 2**num_ctrl_qubits - 1。
- **base_gate** (*Gate，可选*) - 要控制的门对象。

示例：

创建一个受控的标准门并将其应用于电路。

```
pythonfrom qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library.standard_gates import HGate

qr = QuantumRegister(3)
qc = QuantumCircuit(qr)
c3h_gate = HGate().control(2)
qc.append(c3h_gate, qr)
qc.draw('mpl')
```

![量子电路图示例1](https://docs.quantum.ibm.com/_next/image?url=%2Fimages%2Fapi%2Fqiskit%2Fqiskit-circuit-ControlledGate-1.png&w=384&q=75)

创建一个受控的自定义门并将其应用于电路。

```
pythonfrom qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library.standard_gates import HGate

qc1 = QuantumCircuit(2)
qc1.x(0)
qc1.h(1)
custom = qc1.to_gate().control(2)

qc2 = QuantumCircuit(4)
qc2.append(custom, [0, 3, 1, 2])
qc2.draw('mpl')
```

![量子电路图示例2](https://docs.quantum.ibm.com/_next/image?url=%2Fimages%2Fapi%2Fqiskit%2Fqiskit-circuit-ControlledGate-2.png&w=640&q=75)

#### 属性

- base_class

获取此指令的基类。这保证是其继承树中的最低类。

例如：

```
python>>> isinstance(XGate(), XGate)
True
>>> type(XGate()) is XGate
False
>>> XGate().base_class is XGate
True
```

通常，你不应该依赖于指令的精确类；在给定电路中，通常情况下 [`Instruction.name`](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.Instruction#name) 应该是更合适的区分器。

- condition

指令的经典条件。

- condition_bits

获取条件中的 Clbits。

- ctrl_state

以十进制整数返回门的控制状态。

- decompositions

从 SessionEquivalenceLibrary 中获取指令的分解。

- definition

以其他基本门的形式返回定义。如果门具有开放控制，如 self.ctrl_state 所确定，返回的定义将与 X 结合，但不改变内部的 _definition。

- duration

获取持续时间。

- label

返回指令标签。

- mutable

此实例是否是可变的唯一实例。

如果此属性为 `False`，则门实例为共享的单例，不可变。

- name

获取门的名称。如果门具有开放控制，则门名称将变为：

- num_clbits

返回 clbits 的数量。

- num_ctrl_qubits

获取控制量子位的数量。

- num_qubits

返回量子位的数量。

- params

从 base_gate 获取参数。

- unit

获取持续时间的时间单位。

#### 方法

- add_decomposition

  ```
  add_decomposition(decomposition)
  ```

  向 SessionEquivalenceLibrary 添加指令的分解。

- assemble

  ```
  assemble()
  ```

  组装一个 QasmQobjInstruction。

- broadcast_arguments

  ```
  broadcast_arguments(qargs, cargs)
  ```

  验证和处理参数及其关系。

  例如，`cx([q[0],q[1]], q[2])` 表示 `cx(q[0], q[2]); cx(q[1], q[2])`。此方法以正确的分组生成参数。在给定的示例中：

  ```
  输入: [[q[0],q[1]], q[2]], []
  输出: [q[0], q[2]], []
        [q[1], q[2]], []
  ```

  广播规则通常为：

  > - 如果 len(qargs) == 1：
  >
  >   ```
  >   [q[0], q[1]] -> [q[0]],[q[1]]
  >   ```
  >
  > - 如果 len(qargs) == 2：
  >
  >   ```
  >   [[q[0], q[1]], [r[0], r[1]]] -> [q[0], r[0]], [q[1], r[1]]
  >   [[q[0]], [r[0], r[1]]]       -> [q[0], r[0]], [q[0], r[1]]
  >   [[q[0], q[1]], [r[0]]]       -> [q[0], r[0]], [q[1], r[0]]
  >   ```
  >
  > - 如果 len(qargs) >= 3：
  >
  >   ```
  >   [q[0], q[1]], [r[0], r[1]],  ...] -> [q[0], r[0], ...], [q[1], r[1], ...]
  >   ```

- c_if

  ```
  c_if(classical, val)
  ```

  在此指令上设置一个经典等式条件，条件是寄存器或 cbit `classical` 与值 `val` 之间。

  注意

  这是一个设置方法，而不是一个累加方法。多次调用将静默覆盖之前设置的任何条件；它不会累积。

- control

  ```
  control(num_ctrl_qubits=1, label=None, ctrl_state=None)
  ```

  返回门的受控版本。有关使用，请参阅 [`ControlledGate`](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.ControlledGate#qiskit.circuit.ControlledGate)。

- copy

  ```
  copy(name=None)
  ```

  指令的副本。

- inverse

  ```
  inverse()
  ```

  通过对基础门调用 inverse 来反转此门。

- is_parameterized

  ```
  is_parameterized()
  ```

  如果指令是参数化的，则返回 True，否则返回 False。

## Control Flow Operations

### IfElseOp

```
qiskit.circuit.IfElseOp(condition, true_body, false_body=None, label=None)
```

这是一个电路操作，它在提供的条件（`condition`）评估为真时执行一个程序（`true_body`），并且在条件不满足时可选地评估另一个程序（`false_body`）。

**参数**

- **condition** ([*元组*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*ClassicalRegister*](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.ClassicalRegister)*,* [*整型 |* [*元组](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*Clbit*](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.Clbit)*,* [*整型*](https://docs.python.org/3/library/functions.html#int)*] |* [*expr.Expr*](https://docs.quantum.ibm.com/api/qiskit/circuit_classical#qiskit.circuit.classical.expr.Expr)) - 在电路运行时评估的条件，如果为真，则触发`true_body`的评估。可以指定为测试`ClassicalRegister`与给定`int`的等价性的元组，或者比较`Clbit`与`bool`或`int`的元组。
- **true_body** ([*QuantumCircuit*](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.QuantumCircuit)) - 如果`condition`评估为真时执行的程序。
- **false_body** ([*QuantumCircuit*](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.QuantumCircuit) *| None*) - 可选的在`condition`评估为假时执行的程序。
- **label** ([*字符串*](https://docs.python.org/3/library/stdtypes.html#str) *| None*) - 用于识别指令的可选标签。

如果提供，`false_body`必须与`true_body`具有相同的`num_qubits`和`num_clbits`。

在`condition`中使用的经典位必须是附加到将此`IfElseOp`追加到的电路的那些的子集。

**电路符号：**

```
     ┌───────────┐
q_0: ┤0          ├
     │           │
q_1: ┤1          ├
     │  if_else  │
q_2: ┤2          ├
     │           │
c_0: ╡0          ╞
     └───────────┘
```

创建一个新指令。

**参数**

- **name** ([*字符串*](https://docs.python.org/3/library/stdtypes.html#str)) - 指令名称
- **num_qubits** ([*整型*](https://docs.python.org/3/library/functions.html#int)) - 指令的量子位宽度
- **num_clbits** ([*整型*](https://docs.python.org/3/library/functions.html#int)) - 指令的经典位宽度
- **params** ([*列表*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*整型)](https://docs.python.org/3/library/functions.html#int)*|*[*浮点型*](https://docs.python.org/3/library/functions.html#float)*|*[*复数型*|[*字符串*](https://docs.python.org/3/library/stdtypes.html#str)*|ndarray|*[*列表*](https://docs.python.org/3/library/stdtypes.html#list)*|*[*ParameterExpression*](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.ParameterExpression)*]*) - 参数列表
- **duration** ([*整型*](https://docs.python.org/3/library/functions.html#int) *或*[*浮点型*](https://docs.python.org/3/library/functions.html#float)) - 指令的持续时间。如果`unit`是‘dt’，则必须是整数
- **unit** ([*字符串*](https://docs.python.org/3/library/stdtypes.html#str)) - 持续时间的时间单位
- **label** ([*字符串*](https://docs.python.org/3/library/stdtypes.html#str) *或 None*) - 用于识别指令的可选标签。

### WhileLoopOp

```
qiskit.circuit.WhileLoopOp(condition, body, label=None)
```

基于：ControlFlowOp

这是一个电路操作，它重复执行一个子电路（`body`），直到条件（`condition`）评估为False。

**参数**

- **condition** ([*元组*(在新标签页中打开)](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*ClassicalRegister*](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.ClassicalRegister)*,* [*整型*(在新标签页中打开)](https://docs.python.org/3/library/functions.html#int)*] |* [*元组*(在新标签页中打开)](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*Clbit*](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.Clbit)*,* [*整型*(在新标签页中打开)](https://docs.python.org/3/library/functions.html#int)*] |* [*expr.Expr*](https://docs.quantum.ibm.com/api/qiskit/circuit_classical#qiskit.circuit.classical.expr.Expr)) - 在执行`body`之前要检查的条件。可以指定为测试`ClassicalRegister`与给定`int`的等价性的元组，或者比较`Clbit`与`bool`或`int`的元组。
- **body** ([*QuantumCircuit*](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.QuantumCircuit)) - 要重复执行的循环体。
- **label** ([*字符串*(在新标签页中打开)](https://docs.python.org/3/library/stdtypes.html#str) *| None*) - 用于识别指令的可选标签。

在`condition`中使用的经典位必须是附加到`body`的那些的子集。

**电路符号：**

```
     ┌─────────────┐
q_0: ┤0            ├
     │             │
q_1: ┤1            ├
     │  while_loop │
q_2: ┤2            ├
     │             │
c_0: ╡0            ╞
     └─────────────┘
```

创建一个新指令。

**参数**

- **name** ([*字符串*(在新标签页中打开)](https://docs.python.org/3/library/stdtypes.html#str)) - 指令名称
- **num_qubits** ([*整型*(在新标签页中打开)](https://docs.python.org/3/library/functions.html#int)) - 指令的量子位宽度
- **num_clbits** ([*整型*(在新标签页中打开)](https://docs.python.org/3/library/functions.html#int)) - 指令的经典位宽度
- **params** ([*列表*(在新标签页中打开)](https://docs.python.org/3/library/stdtypes.html#list)*[*[*整型*(在新标签页中打开)](https://docs.python.org/3/library/functions.html#int)*|*[*浮点型*(在新标签页中打开)](https://docs.python.org/3/library/functions.html#float)*|*[*复数型*(在新标签页中打开)](https://docs.python.org/3/library/functions.html#complex)*|*[*字符串*(在新标签页中打开)](https://docs.python.org/3/library/stdtypes.html#str)*|ndarray|*[*列表*(在新标签页中打开)](https://docs.python.org/3/library/stdtypes.html#list)*|*[*ParameterExpression*](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.ParameterExpression)*]*) - 参数列表
- **duration** ([*整型*(在新标签页中打开)](https://docs.python.org/3/library/functions.html#int) *或*[*浮点型*(在新标签页中打开)](https://docs.python.org/3/library/functions.html#float)) - 指令的持续时间。如果`unit`是‘dt’，则必须是整数
- **unit** ([*字符串*(在新标签页中打开)](https://docs.python.org/3/library/stdtypes.html#str)) - 持续时间的时间单位
- **label** ([*字符串*(在新标签页中打开)](https://docs.python.org/3/library/stdtypes.html#str) *或 None*) - 用于识别指令的可选标签。

### SwitchCaseOp

```
qiskit.circuit.SwitchCaseOp(target, cases, *, label=None)
```

基于：ControlFlowOp

这是一种电路操作，根据与有序值列表的匹配来执行特定的电路块。可以使用特殊值`CASE_DEFAULT`来表示默认条件。

这是创建switch-case语句的低级接口；通常，应该使用电路方法`QuantumCircuit.switch()`作为上下文管理器来访问构建器接口。在低级别，你必须确保所有电路块包含相同数量的量子位和经典位，并且包含电路的虚拟位的顺序对于所有块是相同的。这可能意味着每个电路块比其自然宽度更宽，因为每个块必须覆盖任何块所覆盖的所有空间的并集。

**参数**

- **target** ([*Clbit*](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.Clbit) *|* [*ClassicalRegister*](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.ClassicalRegister) *|* [*expr.Expr*](https://docs.quantum.ibm.com/api/qiskit/circuit_classical#qiskit.circuit.classical.expr.Expr)) – 运行时要切换的值。
- **cases** (*可迭代的*[*元组*[任意类型, [*QuantumCircuit*](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.QuantumCircuit)]]) – 有序可迭代对象，对应于目标的值和在匹配时应执行的电路块。块之间没有穿透，顺序很重要。

创建一个新指令。

**参数**

- **name** ([*字符串*(在新标签页中打开)](https://docs.python.org/3/library/stdtypes.html#str)) - 指令名称
- **num_qubits** ([*整型*(在新标签页中打开)](https://docs.python.org/3/library/functions.html#int)) - 指令的量子位宽度
- **num_clbits** ([*整型*(在新标签页中打开)](https://docs.python.org/3/library/functions.html#int)) - 指令的经典位宽度
- **params** ([*列表*(在新标签页中打开)](https://docs.python.org/3/library/stdtypes.html#list)*[*[*整型*(在新标签页中打开)](https://docs.python.org/3/library/functions.html#int)*|*[*浮点型*(在新标签页中打开)](https://docs.python.org/3/library/functions.html#float)*|*[*复数型*(在新标签页中打开)](https://docs.python.org/3/library/functions.html#complex)*|*[*字符串*(在新标签页中打开)](https://docs.python.org/3/library/stdtypes.html#str)*|ndarray|*[*列表*(在新标签页中打开)](https://docs.python.org/3/library/stdtypes.html#list)*|*[*ParameterExpression*](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.ParameterExpression)*]*) - 参数列表
- **duration** ([*整型*(在新标签页中打开)](https://docs.python.org/3/library/functions.html#int) *或*[*浮点型*(在新标签页中打开)](https://docs.python.org/3/library/functions.html#float)) - 指令的持续时间。如果`unit`是‘dt’，则必须是整数
- **unit** ([*字符串*(在新标签页中打开)](https://docs.python.org/3/library/stdtypes.html#str)) - 持续时间的时间单位
- **label** ([*字符串*(在新标签页中打开)](https://docs.python.org/3/library/stdtypes.html#str) *或 None*) - 用于识别指令的可选标签。
