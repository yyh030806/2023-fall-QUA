# Quipper

嵌入式、函数式量子编程语言

## The Circ monad

- data **Circ** a

  the circ monad封装量子操作类型。例如，一个输入两个Qubit并输出一个Qubit和一个Bit的量子操作具有以下类型：

  ```
  (Qubit, Qubit) -> Circ (Qubit, Bit)
  ```

  `(Qubit, Qubit)`表示输入参数，`Circ`表示电路计算的上下文，`(Qubit, Bit)`表示输出结果。在Circ monad中，可以编写一系列量子操作，然后使用运算符组合它们以构建更复杂的电路。

Circ单子的主要目的是管理量子计算的序列和状态。它提供了一种符号化的方式来描述和操作量子电路。通过使用Circ单子，可以将多个量子操作组合成一个整体，确保它们按照正确的顺序执行，并对其状态进行管理。

在具体的Circ计算中，可以使用一系列的量子门操作（如Hadamard门、CNOT门等）以及测量、重置等操作来构建量子电路。Circ单子还提供了一些有用的函数和组合子，用于操作量子状态，并将其转换为其他类型（如经典位）。

## Basic types

### data Qubit

量子比特类型，quipper提供的部分常见类型及可用方法如下：

- Eq Qubit
  - (==) :: Qubit -> Qubit -> Bool
  - (/=) :: Qubit -> Qubit -> Bool
- Ord Qubit
  - [compare](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#v:compare) :: [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit) -> [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit) -> [Ordering](http://hackage.haskell.org/package/base-4.12.0.0/docs/Data-Ord.html#t:Ordering)
  - [(<)](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#v:-60-) :: [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit) -> [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit) -> [Bool](http://hackage.haskell.org/package/base-4.12.0.0/docs/Data-Bool.html#t:Bool)
  - [(<=)](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#v:-60--61-) :: [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit) -> [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit) -> [Bool](http://hackage.haskell.org/package/base-4.12.0.0/docs/Data-Bool.html#t:Bool)
  - [(>)](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#v:-62-) :: [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit) -> [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit) -> [Bool](http://hackage.haskell.org/package/base-4.12.0.0/docs/Data-Bool.html#t:Bool)
  - [(>=)](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#v:-62--61-) :: [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit) -> [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit) -> [Bool](http://hackage.haskell.org/package/base-4.12.0.0/docs/Data-Bool.html#t:Bool)
  - [max](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#v:max) :: [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit) -> [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit) -> [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit)
  - [min](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#v:min) :: [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit) -> [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit) -> [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit)
- Show Qubit
  - [showsPrec](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#v:showsPrec) :: [Int](http://hackage.haskell.org/package/base-4.12.0.0/docs/Data-Int.html#t:Int) -> [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit) -> [ShowS](http://hackage.haskell.org/package/base-4.12.0.0/docs/Text-Show.html#t:ShowS)
  - [show](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#v:show) :: [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit) -> [String](http://hackage.haskell.org/package/base-4.12.0.0/docs/Data-String.html#t:String)
  - [showList](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#v:showList) :: [[Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit)] -> [ShowS](http://hackage.haskell.org/package/base-4.12.0.0/docs/Text-Show.html#t:ShowS)
- ControlSource Qubit
  - [to_control](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#v:to_control) :: [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit) -> [ControlList](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:ControlList)
- QCLeaf Qubit
- [CircLiftingUnpack](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper-Internal-CircLifting.html#t:CircLiftingUnpack) ([Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit)) ([Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit))
  - [unpack](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#v:unpack) :: [Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit) -> [Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit)
  - [pack](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#v:pack) :: [Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit) -> [Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit)
- ……

### data Bit

运行时经典比特的类型（即电路中的线）。

部分类型如下，其中各类型包含的方法与对应`Qubit`类型类似：

- Eq Bit
- Ord Bit
- Show Bit
- ControlSource Bit
- ……

### type Qulist

`type Qulist = [Qubit]`

### type Bitlist

`type Bitlist = [Bit]`

## Basic gates

包含可用于构建电路和构建块的各种基本门。

`type Timestep = Double`

时间步长是一个小的浮点数，用作一些门的参数，如旋转门或$e^{-iZt}$门。

### 函数型可逆门

这类门有返回值，如：`qnot`门输入一个`Qubit`，对其执行一个操作，输出一个新的`Qubit`，使用方式如下：
```
output <- qnot input
```

二元门：

```
(out0, out1) <- gate_W in0 in1
```

**部分门举例：**

- `qnot :: Qubit -> Circ Qubit`: qnot作用在一个量子比特上

- `hadamard :: Qubit -> Circ Qubit`/`gate_H :: Qubit -> Circ Qubit`

   Hadamard门作用在一个量子比特上

- `gate_X/Y/Z :: Qubit -> Circ Qubit`: 使用Pauli X/Y/Z门

- `gate_S :: Qubit -> Circ Qubit`: Clifford S-gate

- `rGate :: Int -> Qubit -> Circ Qubit`: 绕z轴旋转$2\pi i/2^n$

  ![img](quipper.assets/rGate.png)

- `qmultinot :: QData qa => qa -> Circ qa`: 对量子数据结构中所有量子比特取反

- `cnot :: Bit -> Circ Bit`: 将NOT门作用于经典量子比特

- `swap :: QCData qc => qc -> qc -> Circ (qc, qc)`

- ……

### 命令式可逆门

采用命令式方式实现的门，对量子比特“就地”运算，不产生返回值，使用方法：

```
qnot_at q
```

对二元门：

```
gate_W_at q0 q1
```

同样，quipper也提供了这类门的函数形式，见上一部分。

**部分门举例：**（门的作用和**函数式**中对应的门一致，这里不再另外说明）

- `qnot_at :: Qubit -> Circ ()`
- `hadamard_at :: Qubit -> Circ ()`/`gate_H_at :: Qubit -> Circ ()`
- `gate_X/Y/Z_at :: Qubit -> Circ ()`
- `qmultinot_at :: QData qa => qa -> Circ ()`
- `swap_at :: QCData qc => qc -> qc -> Circ ()`
- ……

### 用于状态准备和状态终止的门

### 经典电路的门

用于构建经典电路，不改变或丢弃其输入，每个门产生一个包含输出值的wire

如：

- `cgate_eq :: Bit -> Bit -> Circ Bit`: 测试两个比特是否相等，相等返回True。

- `cgate_not :: Bit -> Circ Bit`: 返回输入的否定

  与`cnot`/`cnot_at`不同：该操作步改变输入，而是为输出创建一个新的比特。

- `cgate_xor/and/or :: [Bit] -> Circ Bit`

- `cgate_if :: CData ca => Bit -> ca -> ca -> Circ ca`: 

  ```
  output <- cgate_if a b c
  (out0, out1) <- cgate_if a (b0, b1) (c0, c1)
  [out0, out1, out2] <- cgate_if a [b0, b1, b2] [c0, c1, c2]
  ```

  若a为真，返回b，否则返回c。b和c可以是任何包含Bits的数据结构，但必须有相同数据类型和形状（如若都是列表，需要长度相等）

- `circ_if :: CData ca => Bit -> Circ ca -> Circ ca -> Circ ca`: 经典电路的if-then-else函数，是对`cgate_if`的包装，使用方法：

  ```
  result <- circ_if <<<condition>>> (
    <<then-part>>>
    )(
    <<<else-part>>>
    )
  ```

  与`cgate_if`不同，这是一个元操作，即`then`和`else`部分可以是电路构建操作。

  和一般布尔型的`if-then-else`不同的是：这里条件是`Bit`类型，即它只在电路执行时已知。因此，生成的电路既有`then`又有`else`部分，同样要求`then`和`else`部分有相同的数据类型和形状。

### 用户自定义门

- `named_gate :: QData qa => String -> qa -> Circ qa`

  定义给定名称的新函数式门，用法：

  - 定义新的一元门Q：

  ```
  my_unary_gate :: Qubit -> Circ Qubit
  my_unary_gate = named_gate "Q"
  ```

  - 定义新的二元门R：

  ```
  my_binary_gate :: (Qubit, Qubit) -> Circ (Qubit, Qubit)
  my_binary_gate = named_gate "R"
  ```

- `named_gate_at :: QData qa => String -> qa -> Circ ()`

  定义给定名称的命令式门，用法：

  - 定义新的一元门Q：

  ```
  my_unary_gate_at :: Qubit -> Circ ()
  my_unary_gate_at = named_gate_at "Q"
  ```

  - 定义新的二元门R：

  ```
  my_binary_gate_at :: (Qubit, Qubit) -> Circ ()
  my_binary_gate_at = named_gate_at "R"
  ```

- `named_rotation :: QData qa => String -> Timestep -> qa -> Circ qa`

  定义给定名称的新的函数式门，并以实值参数参数化。常用于按角度参数化的旋转或相位门。名称中可以用`%`作为参数的占位符。用法如下：

  ```
  my_unary_gate :: Qubit -> Circ Qubit
  my_unary_gate = named_rotation "exp(-i%Z)" 0.123
  ```

  ```
  my_binary_gate :: TimeStep -> (Qubit, Qubit) -> Circ (Qubit, Qubit)
  my_binary_gate t = named_rotation "Q(%)" t
  ```

- `named_rotation_at :: QData qa => String -> Timestep -> qa -> Circ ()`

  定义给定名称的新的命令式门，并以实值参数参数化。使用方法类似函数式门。

  ```
  my_unary_gate_at :: Qubit -> Circ ()
  my_unary_gate_at = named_rotation "exp(-i%Z)" 0.123
  ```

  ```
  my_binary_gate_at :: TimeStep -> (Qubit, Qubit) -> Circ ()
  my_binary_gate_at t = named_rotation "Q(%)" t
  ```

- `extended_named_gate :: (QData qa, QData qb) => String -> qa -> qb -> Circ qa`

  定义新函数式门，和`named_gate`类似，只是生成的门用`generalized controls`扩展。`generalized controls`是门的其他输入，如果他们处于计算基状态则一定不会被修改。在电路图中以特殊方式呈现。用法如下：

  ```
  my_new_gate :: (Qubit,Qubit) -> Qubit -> Circ (Qubit,Qubit)
  my_new_gate = extended_named_gate "Q"
  ```

  定义了一个新的门Q，有两个输入和一个`generalized`输入。

- `extended_named_gate_at :: (QData qa, QData qb) => String -> qa -> qb -> Circ ()`

  上一定义的命令形式，用法如下：

  ```
  my_new_gate_at :: (Qubit,Qubit) -> Qubit -> Circ ()
  my_new_gate_at = extended_named_gate_at "Q"
  ```

### 动态提升

- `dynamic_lift :: QShape ba qa ca => ca -> Circ ba`

  将一个`Bit`类型（布尔电路输出）转换为一个`Bool`类型（布尔型参数）。更一般的说，即将 Bits 的数据结构转换为 Bools 的相应数据结构。主要用于需要将测量结果用于电路生成参数的情况。

  注意这不是一个门，而是一个元操作，输入由经典电路端点组成（其值在电路执行时已知），输出为布尔参数 （其值在电路生成时已知）。

  使用该操作意味着电路执行和电路生成之间交错进行。因此，它（物理上）操作成本高昂，应谨慎使用。使用该操作会中断 量子设备（提前生成电路），以及强制交互操作（量子设备必须等待电路的下一部分生成）。在当前电路包含未测量的量子比特时，该操作的代价尤其高；在这种情况下，在量子设备保持待机状态等待时必须保存量子比特。

## Other circuit-building functions

- qinit_plusminus :: [Bool](http://hackage.haskell.org/package/base-4.12.0.0/docs/Data-Bool.html#t:Bool) -> [Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit)

  生成一个新量子比特，当b=F时初始化为$|+〉$，b=T时初始化为$|-〉$

- qinit_of_char :: [Char](http://hackage.haskell.org/package/base-4.12.0.0/docs/Data-Char.html#t:Char) -> [Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit)

  生成新量子比特初始化为 $|0〉$、$|1〉$、$|+〉$或$|−〉$，取决于字符 *C*为“0”、“1”、“+”或“-”

- qinit_of_string :: [String](http://hackage.haskell.org/package/base-4.12.0.0/docs/Data-String.html#t:String) -> [Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) [[Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit)]

  生成量子比特列表，值为 $|0〉$、$|1〉$、$|+〉$、$|−〉$组成的序列，由一个字符串定义，如：`00+0+++`

- map_hadamard :: [QData](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:QData) qa => qa -> [Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) qa

  将 Hadamard 门应用于量子数据结构中的每个量子比特。

- controlled_not :: [QCData](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:QCData) qc => qc -> qc -> [Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) (qc, qc)

  将受控非门应用于每对量子比特或经典比特，第一个变量是目标，第二个是（正）控制量。

  现在我们要求两个QCData类型相同（即经典比特只能被经典比特控制，量子比特只能被量子比特控制）

  例：

  ```
  ((a',b'), (x,y)) <- controlled_not (a,b) (x,y)
  ```

  相当于

  ```
  a' <- qnot a `controlled` x
  b' <- qnot b `controlled` y
  ```

- bool_controlled_not :: [QCData](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:QCData) qc => qc -> [BType](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper-Internal-QData.html#t:BType) qc -> [Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) qc

  controlled_not中控制量包含布尔型。

  例：

  ```
  bool_controlled_not (q, r, s) (True, True, False)
  ```

  否定q和r，但不否定s

- qc_copy :: [QCData](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:QCData) qc => qc -> [Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) qc

  为一段量子数据创建一个新的“副本”，复制通过`controlled-not`操作完成，且不是克隆。和`qc_copy_fun`类似，但后者返回原数据和拷贝结果，前者只返回拷贝结果。如下所示：

  ```
  b <- qc_copy a
  (orig, copy) <- qc_copy_fun orig
  ```

- qc_uncopy :: [QCData](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:QCData) qc => qc -> qc -> [Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) ()

  可以看作`qc_copy`的反向。如果后者已经是拷贝的结果，则终止拷贝。例：

  ```
  b <- qc_copy a
  qc_uncopy a b
  ```

  这两行操作可以看作一个判别函数。

- mapUnary :: [QData](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:QData) qa => ([Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit) -> [Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit)) -> qa -> [Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) qa

  将一个单比特门映射到数据结构中的每个量子比特上。

- mapBinary :: [QData](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:QData) qa => ([Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit) -> [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit) -> [Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) ([Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit), [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit))) -> qa -> qa -> [Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) (qa, qa)

  将一个二元门映射到两个形状相同的量子数据结构的每对量子比特上。

- mapBinary_c :: [QShape](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:QShape) ba qa ca => ([Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit) -> [Bit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Bit) -> [Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) ([Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit), [Bit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Bit))) -> qa -> ca -> [Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) (qa, ca)

  和`mapBinary`类似，只是第二个数据结构是经典类型。

- qc_mapBinary :: [QCData](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:QCData) qc => ([Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit) -> [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit) -> [Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) ([Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit), [Qubit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Qubit))) -> ([Bit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Bit) -> [Bit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Bit) -> [Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) ([Bit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Bit), [Bit](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Bit))) -> qc -> qc -> [Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) (qc, qc)

  `mapBinary`的异构版本，对于两个形状相同的量子数据结构，将一个二元门f映射到每对相应`qubits`上，二元门g映射到每对相应的`bits`上。

## Notation of controls

电路执行时，一些门可以被一个或多个“控制”量子比特/经典比特限制，也可以被电路生成时的布尔型条件控制（此时当控制条件为False时们不会被生成）。

- class **ControlSource** a where

  control source指任何可以被用作控件作用在门上的东西。构造control source的最常见方法是用`.==.`、`./=.`、`.&&.`。

  - to_control :: a -> [ControlList](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:ControlList)

    将条件转换为控件。

- data **ControlList**

  Quipper内部表示联合控制的形式。

Quipper中，控制可以用类似二元布尔表达式的方式表示。例如：

```
q1 .==. 0 .&&. q2 .==. 1   for Qubits q1, q2
```

```
q .&&. p                   means  q .==. 1  .&&.  p .==. 1
```

```
[p,q,r,s]                  a list of positive controls
```

```
q1 .==. 0 .&&. z <= 7      combines quantum and classical controls
```

在这些中缀运算符中，`(.&&.)`连接比 `(.==.)`、`(./=.)`弱。

- (.&&.) :: ([ControlSource](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:ControlSource) a, [ControlSource](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:ControlSource) b) => a -> b -> [ControlList](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:ControlList)

  连接两个控制，形成逻辑连接。

- (.==.) :: [QCData](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:QCData) qc => qc -> [BType](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper-Internal-QData.html#t:BType) qc -> [ControlList](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:ControlList)

  `(qx .==. x)`:当量子数据$qx$处于$x$状态时为真。

- (./=.) :: [QCLeaf](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper-Internal-QData.html#t:QCLeaf) q => q -> [Bool](http://hackage.haskell.org/package/base-4.12.0.0/docs/Data-Bool.html#t:Bool) -> [ControlList](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:ControlList)

  当x是布尔参数时，`(q ./=. x)`是`(q .==. not x)`的简写。

  和`.==.`定义在所有类型的量子数据结构上不同，`./=.`只在一位控制比特或量子比特上有定义。

- controlled :: [ControlSource](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:ControlSource) c => [Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) a -> c -> [Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) a 

  将controls绑定到门上。

  ```
  gate `controlled` <<controls>>
  ```

  对函数型的门也适用：

  ```
  result <- gate `controlled` <<controls>>
  ```

  该中缀运算符是左结合的，可以多次应用，以下两种表达等价：

  ```
  result <- gate `controlled` <<controls1>> `controlled` <<controls2>>
  ```

  ```
  result <- gate `controlled` <<controls1>> .&&. <<controls2>>
  ```

## Signed items

- data **Signed** a

  `Signed X True`代表一个正项，`Signed X False`代表一个负项。

  当和电路中的线一起使用时，正项表示正控制（如实心点），负项表示负控制（如空心点）。

- from_signed :: Signed a -> a

  从Signed类型中提取底层数据项

- get_sign :: Signed a -> Bool

  提取 Signed 类型中的符号信息：True 表示正数，False 表示负数。

## 注释和标签

## 分层电路

- box :: (QCData qa，QCData qb，QCurry qa_qb qa qb) => String -> qa_qb -> qa_qb

  将电路生成函数封装为一个命名的子程序的通用接口。它接受一个名称和一个电路生成函数，并返回一个具有相同类型的新的电路生成函数，但是它插入的是一个封装的子程序，而不是实际的子程序主体。

  使用方式：

  ```
  somefunc :: Qubit -> Circ Qubit
  somefunc a = do ...
  
  somefunc_boxed :: Qubit -> Circ Qubit
  somefunc_boxed = box "somefunc" somefunc
  ```

  这里somefunc 的类型只是一个示例；实际上可以是具有任意数量和类型参数的函数，只要参数和返回类型是量子数据。

  也可以直接内联 box 运算符，如下所示：

  ```
  somefunc :: Qubit -> Circ Qubit
  somefunc = box "somefunc" $ \a -> do ...
  ```

  注意：box 运算符包围了一个完整的函数，包括所有的参数。在某些量子变量已经定义的情况下应用 box 运算符是不正确的。

  错误用法：

  ```
  incorrect_somefunc :: Qubit -> Circ Qubit
  incorrect_somefunc a = box "somefunc" $ do ...
  ```

  不同的子程序应使用不同的名称。如果多次使用相同的名称和输入形状调用 box，Quipper 将假设（未经检查）它们是对同一子程序的连续调用。

  box 运算符的类型是重载的，并且相当难以读取。它可以具有以下类型的形式：

  ```
  box :: String -> (Qubit -> Circ Qubit) -> (Qubit -> Circ Qubit)
  box :: String -> (QDInt -> QDInt -> Circ (QDInt,QDInt,QDInt)) -> (QDInt -> QDInt -> Circ (QDInt,QDInt,QDInt))
  ```

- nbox :: QCData qa => String -> Integer -> (qa -> Circ qa) -> qa -> Circ qa

  带有迭代功能的 box 版本，第二个参数是迭代次数。只能应用于具有单个参数且输入输出类型相同的函数。

- box_loopM :: (Integral int, QCData qa) => String -> int -> qa -> (qa -> Circ qa) -> Circ qa

  具有与 loopM 相同类型的 box 版本。

- loopM_boxed_if :: (Integral int, QCData qa) => Bool -> String -> int -> qa -> (qa -> Circ qa) -> Circ qa

  带有条件的 loopM 版本，根据布尔条件进行封装。典型用法：

  ```
  loopM_boxed_if (s > 1) "name" s x $ \x -> do
    <<<body>>>
    return x
  ```

## Block structure

Quipper提供一些高阶函数，提供一种将量子程序结构化为块的方式。一个块可以包含本地辅助比特或本地控制。

### Ancillas

使用 with_ancilla 系列运算符比直接使用 qinit 和 qterm 更可取。特别是可以在使用 with_ancilla 系列运算符创建的块中添加控制，而单独使用 qinit 和 qterm 时无法控制。

- with_ancilla :: (Qubit -> Circ a) -> Circ a

  对 qinit 和 qterm 的便捷包装。可以用它来引入一个具有局部作用域的ancilla，像这样：

  ```
  with_ancilla $ \h -> do {
    <<<code block using ancilla h>>>
  }
  ```

  辅助比特将在块开始时初始化为$ |0〉$，程序员有责任确保在块结束时将其返回到状态$ |0〉$。

  使用 with_ancilla 创建的块可控的前提是其主体是可控的。

- with_ancilla_list :: Int -> (Qulist -> Circ a) -> Circ a

  类似于 with_ancilla，但创建一个包含 n 个辅助比特的列表，所有辅助比特都初始化为$ |0〉$。用法：

  ```
  with_ancilla_list n $ \a -> do {
    <<<code block using list of ancillas a>>>
  }
  ```

- with_ancilla_init :: QShape a qa ca => a -> (qa -> Circ b) -> Circ b

  使用本地辅助比特执行一个块。打开一个块，用指定的经典值初始化一个辅助比特，并在块关闭时以相同的值终止它。注意：程序员有责任确保在封闭块的结尾将辅助比特返回到其原始状态。用法：

  ```
  with_ancilla_init True $ \a -> do {
    <<<code block using ancilla a initialized to True>>>
  }
  ```

  ```
  with_ancilla_init [True,False,True] $ \a -> do {
    <<<code block using list of ancillas a initialized to [True,False,True]>>>
  }
  ```

### Automatic uncomputing

- with_computed_fun :: (QCData x, QCData y) => x -> (x -> Circ y) -> (y -> Circ (y, b)) -> Circ (x, b)

  `with_computed_fun` x f g'：计算 x' := f(x)；然后计算 g(x')，其中 g 应该组织为一对 (x',y)；然后将 x' 反向计算回 x，并返回 (x,y)。

  使用时的重要细微之处：f 中引用的所有量子数据，即使作为控制也必须由 f 显式绑定和返回，否则反向计算可能会错误重新绑定它。另一方面，g 可以安全地引用当前环境中的任何内容。

- with_computed :: QCData x => Circ x -> (x -> Circ b) -> Circ b

  `with_computed` computation code：执行计算（结果为 x），然后执行代码 x，最后执行计算的反向过程，例如：

  <img src="quipper.assets/with_computed.png" alt="img" style="zoom:80%;" />

  计算和代码都可以引用当前环境中存在的任何比特，它们还可以创建新的比特。计算除了输出之外，还可能产生任意垃圾。

  这是一个非常通用但相对不安全的操作。用户有责任确保计算确实可以被撤销。特别是，如果计算包含任何初始化操作，那么代码必须确保在计算的反向过程中满足相应的断言。

  相关的更专门但潜在更安全的操作是：

  - `with_basis_change`，类似于` with_computed`，但假设计算是酉的
  - `classical_to_reversible`，假设计算是经典的（或伪经典的），代码是一个简单copy-by-controlled-not 操作。

- with_basis_change :: [Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) () -> [Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) b -> [Circ](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:Circ) b

  `with_basis_change` basischange code: 操作对应的是基态变换操作。它执行一个基态变换，然后执行代码块，最后执行基态变换的逆操作。基态变换和代码块都是以命令式风格编写的。用户有责任确保代码块的映射包含在基态变换的映射中，否则将出现断言错误或运行时错误。使用方法如下：

  ```
  with_basis_change basischange $ do
    <<<code>>>
  
  where
    basischange = do
      <<<gates>>>
  ```

### Controls

- Controls with_controls :: ControlSource c => c -> Circ a -> Circ a

  使用 "if" 的控制的语法（经典和量子）。可按如下方式使用：

  ```
  gate1
  with_controls <<controls>> $ do {
    gate2
    gate3
  }
  gate4
  ```

  指定的控制将应用于 gate2 和 gate3。对于不能被控制的门（如测量），指定控制是错误的。

- with_classical_control :: QCData qa => Bit -> String -> qa -> (qa -> Circ qa) -> Circ qa

  对具有相同输入和输出形状的函数进行经典控制：如果控制位为 true，则执行该函数，否则使用恒等映射。注意：类型约束在运行时进行动态检查。

- without_controls :: Circ a -> Circ a

  在临时暂停应用控制的情况下应用一组门，可以用于在已知不需要控制的门上省略控制。这是一个相对较低级的函数，通常不应直接由用户代码调用。相反，最好使用更高级的函数，如 `with_basis_change`。但是在某些情况下，`without_controls `运算符很有用，例如它可以用于在定义变换器时保留` NoControlFlag`。

  用法：

  ```
  without_controls $ do 
    <<code block>>
  ```

  或

  ```
  without_controls (gate)
  ```

  注意，在`without_controls `块中，将禁用周围代码中指定的所有控制。即使` without_controls `块出现在子程序中，并且稍后在受控上下文中调用该子程序，也是如此。另一方面，可以在` without_controls `块内部指定控制。

  示例：

  ```
  my_subcircuit = do
    gate1
    without_controls $ do {
      gate2
      gate3 `controlled` <<controls1>>
    }
    gate4
  
  my_circuit = do
    my_subcircuit `controlled` <<controls2>>
  ```

  在该示例中，控制 1 将应用于 gate 3，控制 2 将应用于 gate 1 和 gate 4，而 gate 2 不会应用任何控制。

- without_controls_if :: NoControlFlag -> Circ a -> Circ a

  如果 NoControlFlag 为 True，则应用 without_controls，否则不执行任何操作。

### Loops

- for :: Monad m => Int -> Int -> Int -> (Int -> m ()) -> m ()

  for 循环。从 a 计数到 b，以 s 为增量。

  标准写法：

  ```
  for i = a to b by s do
    commands             
  end for
  ```

  Quipper写法：

  ```
  for a b s $ \i -> do
    commands
  endfor
  ```

- endfor :: Monad m => m ()

  表示 "for" 循环的结束。该命令实际上不执行任何操作，但可以使循环看起来更美观。

- foreach :: Monad m => [a] -> (a -> m b) -> m ()

  在值列表上迭代一个参数，可按如下方式使用：

  ```
  foreach [1,2,3,4] $ \n -> do
    <<<loop body depending on the parameter n>>>
  endfor
  ```

  循环体将对 n ∈ {1,2,3,4} 的每个 n 执行一次。

- loop :: (Eq int, Num int) => int -> t -> (t -> t) -> t

  迭代一个函数 n 次。例如：

  ```
  loop 3 x f = f (f (f x))
  ```

- loop_with_index :: (Eq int, Num int) => int -> t -> (int -> t -> t) -> t

  类似于 loop，但它还将循环计数器传递给被迭代的函数。例如：

  ```
  loop_with_index 3 x f = f 2 (f 1 (f 0 x))
  ```

- loop_with_index 3 x f = f 2 (f 1 (f 0 x))
  loopM :: (Eq int, Num int, Monad m) => int -> t -> (t -> m t) -> m t

  loop 的单子版本。

- loop_with_indexM :: (Eq int, Num int, Monad m) => int -> t -> (int -> t -> m t) -> m t

  loop_with_index 的单子版本。因此，`loop_with_indexM 3 x0 f`
  将执行以下操作：

  ```
  do
    x1 <- f 0 x0
    x2 <- f 1 x1
    x3 <- f 2 x2    
    return x3
  ```

## Operations on circuits

### Reversing

- reverse_generic :: (QCData x, QCData y, TupleOrUnary xt x, QCurry x_y x y, Curry x_y_xt x (y -> Circ xt)) => x_y -> x_y_xt

  反转电路生成的函数，反转后的函数需要一个形状参数，该形状参数是原始函数的输入类型。

  这个高度重载的函数的类型很难阅读。例如，它可以具有以下类型：

  ```
  reverse_generic :: (QCData x, QCData y) => (x -> Circ y) -> x -> (y -> Circ x) 
  reverse_generic :: (QCData x, QCData y, QCData z) => (x -> y -> Circ z) -> x -> y -> (z -> Circ (x,y)) 
  ```

- reverse_simple :: (QCData_Simple x, QCData y, TupleOrUnary xt x, QCurry x_y x y) => x_y -> y -> Circ xt

  类似于reverse_generic，但仅适用于简单类型，因此不需要形状参数。典型实例：

  ```
  reverse_simple :: (QCData_Simple x, QCData y) => (x -> Circ y) -> (y -> Circ x)
  reverse_simple :: (QCData_Simple x, QCData_Simple y, QCData z) => (x -> y -> Circ z) -> (z -> Circ (x,y))
  ```

- reverse_generic_endo :: (QCData x, TupleOrUnary xt x, QCurry x_xt x xt) => x_xt -> x_xt

  类似于reverse_generic，但专门适用于端态电路（endomorphic circuits），即输入和输出具有相同类型（可能通过柯里化）和形状的电路。与reverse_generic不同，它不需要附加的形状参数，并且反转函数如果原始函数是柯里化的，则也是柯里化的。典型实例：

  ```
  reverse_generic_endo :: (QCData x) => (x -> Circ x) -> (x -> Circ x)
  reverse_generic_endo :: (QCData x, QCData y) => (x -> y -> Circ (x,y)) -> (x -> y -> Circ (x,y))
  ```

- reverse_generic_imp :: (QCData x, QCurry x__ x ()) => x__ -> x__

  类似于reverse_generic_endo，但适用于以命令式风格表达的端态电路。典型实例：

  ```
  reverse_generic_endo :: (QCData x) => (x -> Circ ()) -> (x -> Circ ())
  reverse_generic_endo :: (QCData x, QCData y) => (x -> y -> Circ ()) -> (x -> y -> Circ ())
  ```

- reverse_generic_curried :: (QCData x, QCData y, TupleOrUnary xt x, Tuple yt y, QCurry x_yt x yt, QCurry y_xt y xt, Curry x_y_xt x y_xt) => x_yt -> x_y_xt

  类似于reverse_generic，但接受输出为元组的函数，并对反转函数进行柯里化。下面的例子说明与reverse_generic的区别：

  ```
  f                         :: (x -> y -> Circ (z,w))
  reverse_generic f         :: x -> y -> ((z,w) -> Circ (x,y))
  reverse_generic_curried f :: x -> y -> (z -> w -> Circ (x,y))
  ```

  注意：输出必须是n元组，其中n = 0或n ≥ 2。将其应用于输出为非元组类型的电路是类型错误的；在这种情况下，应使用reverse_generic。

- reverse_simple_curried :: (QCData_Simple x, QCData y, TupleOrUnary xt x, Tuple yt y, QCurry x_yt x yt, QCurry y_xt y xt) => x_yt -> y_xt

  类似于reverse_simple，但接受输出为元组的函数，并对反转函数进行柯里化。

- reverse_endo_if :: ([QCData](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:QCData) x, [TupleOrUnary](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper-Utils-Tuple.html#t:TupleOrUnary) xt x, [QCurry](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper-Internal-Generic.html#t:QCurry) x_xt x xt) => [Bool](http://hackage.haskell.org/package/base-4.12.0.0/docs/Data-Bool.html#t:Bool) -> x_xt -> x_xt

  `reverse_generic_endo`的条件版本。根据一个布尔值的真假来选择是否反转端态（endomorphic）量子电路。如果布尔值为true，则反转电路；否则，插入非反转的电路。

- reverse_imp_if :: ([QCData](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper.html#t:QCData) qa, [QCurry](https://www.mathstat.dal.ca/~selinger/quipper/doc/Quipper-Internal-Generic.html#t:QCurry) fun qa ()) => [Bool](http://hackage.haskell.org/package/base-4.12.0.0/docs/Data-Bool.html#t:Bool) -> fun -> fun

  `reverse_generic_imp`的条件版本。根据一个布尔值的真假来选择是否反转以命令式风格表达的量子电路。如果布尔值为true，则反转电路；否则，插入非反转的电路。

  这两个函数提供了根据条件选择是否反转电路的能力。

### Classical circuits

以下函数可以用于在经典电路和量子电路之间进行转换。

- classical_to_cnot :: (QCData qa, QCData qb, QCurry qfun qa qb) => qfun -> qfun

  将电路中的所有经典门转换为等效的控制非门（controlled-not gates）。

  更易读的形式：

  ```
  classical_to_cnot :: (QCData qa) => Circ qa -> Circ qa
  classical_to_cnot :: (QCData qa, QCData qb) => (qa -> Circ qb) -> (qa -> Circ qb)
  classical_to_cnot :: (QCData qa, QCData qb, QCData qc) => (qa -> qb -> Circ qc) -> (qa -> qb -> Circ qc)
  ```

- classical_to_quantum :: (QCData qa, QCData qb, QCurry qfun qa qb, QCurry qfun' (QType qa) (QType qb)) => qfun -> qfun'

  用等效的量子门替换电路中的所有经典门。

  更易读的形式：

  ```
  classical_to_quantum :: (QCData qa) => Circ qa -> Circ (QType qa)
  classical_to_quantum :: (QCData qa, QCData qb) => (qa -> Circ qb) -> (QType qa -> Circ (QType qb))
  classical_to_quantum :: (QCData qa, QCData qb, QCData qc) => (qa -> qb -> Circ qc) -> (QType qa -> QType qb -> Circ (QType qc))
  ```

### Ancilla uncomputation

- classical_to_reversible :: (QCData qa, QCData qb) => (qa -> Circ qb) -> (qa, qb) -> Circ (qa, qb)

  将经典（或伪经典）电路转换为可逆电路的通用函数。输入是一个经典布尔函数 x ↦ f(x)，以非必须可逆的电路形式给出（但是，电路应该是一对一的，即不应明确擦除任何“垃圾”）。输出是相应的可逆函数 (x,y) ↦ (x,y ⊕ f(x))。qa和qb可以是任何量子数据类型。函数classical_to_reversible本身不会将经典位转换为量子比特；可以使用classical_to_quantum进行转换。

## Circuit transformers

转换器是定义电路映射的一种非常通用的方式。可能的用途包括：

- 门变换，其中整个电路通过将每种类型的门替换为另一个门或电路来进行转换；
- 错误纠正编码，整个电路通过将每个比特替换为一些固定数量的比特，并将每个门替换为电路来进行转换
- 模拟，整个电路通过为每个门指定一个语义函数将其映射到语义函数。

Quipper中要定义特定的转换，程序员只需指定三个信息：

- type a=⟦Qubit⟧和 b=⟦Bit⟧，作为语义域。

- A Monad m，从而允许翻译具有副作用（如果需要的话）；否则可以使用Identity Monad。

- 对于每个门G，对应的语义函数⟦G⟧。此函数的类型取决于门G的类型。例如：

  ```
  If G :: Qubit -> Circ Qubit, then ⟦G⟧ :: a -> m a. 
  If G :: (Qubit, Bit) -> Circ (Bit, Bit), then ⟦G⟧ :: (a, b) -> m (b, b).
  ```

程序员通过定义类型为Transformer m a b的函数来提供这些信息，一旦定义了特定的转换器，就可以将其应用于整个电路。例如，对于具有1个输入和2个输出的电路：

```
If C :: Qubit -> (Qubit, Qubit), then ⟦C⟧ :: a -> m (a, a).
```

Quipper中支持用户自定义转换器和使用已定义的转换器。

## Automatic circuit generation from classical code

`Quipper.Internal.CircLifting`和`Quipper.Utils.Template`两个模块提供从经典代码自动生成电路的功能。

## Extended quantum data types

Quipper中提供扩展量子数据类型，包括同质和异质的类型。



