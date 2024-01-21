import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit import ParameterVector
from qiskit.primitives import Estimator
from qiskit.utils import algorithm_globals
from qiskit_nature.second_q.drivers import PySCFDriver
from qiskit_nature.second_q.mappers import JordanWignerMapper
from qiskit_nature.units import DistanceUnit
from scipy.optimize import minimize

# 定义LiH分子的几何结构和基组

# specify driver
driver = PySCFDriver(
    atom="Li 0 0 0; H 0 0 1.6",
    basis="sto3g",
    charge=0,
    spin=0,
    unit=DistanceUnit.ANGSTROM,
)

# 生成分子的哈密顿量
# 将哈密顿量转换为泡利算符的线性组合
problem = driver.run()
fermionic_op = problem.hamiltonian.second_q_op()
mapper = JordanWignerMapper()
repulsion_energy = problem.nuclear_repulsion_energy
pauli_op = mapper.map(fermionic_op)

# 设计一个参数化的量子电路作为变分形式
num_qubits = pauli_op.num_qubits
# 选择一个经典优化器
optimizer = minimize


# 定义一个损失函数
def my_vqe(params):
    qc = QuantumCircuit(num_qubits)
    theta = ParameterVector('theta', 3 * num_qubits)

    for i in range(num_qubits - 1):
        qc.cx(i, i + 1)
    qc.cx(num_qubits - 1, 0)

    for i in range(num_qubits):
        qc.ry(theta[i], i)

    for i in range(num_qubits - 1):
        qc.cx(i, i + 1)
    qc.cx(num_qubits - 1, 0)

    for i in range(num_qubits):
        qc.rz(theta[i + num_qubits], i)

    for i in range(num_qubits - 1):
        qc.cx(i, i + 1)
    qc.cx(num_qubits - 1, 0)

    for i in range(num_qubits):
        qc.rx(theta[i + 2 * num_qubits], i)

    estimator = Estimator()
    job = estimator.run(qc, pauli_op, parameter_values=params)
    values = job.result().values
    energy = values[0] + repulsion_energy
    return energy


# 设置随机种子
seed = 42
algorithm_globals.random_seed = seed

# 初始化电路参数
params_value = np.random.rand(3 * num_qubits)

# 使用优化器对损失函数进行最小化
result = optimizer(my_vqe, params_value, method='COBYLA', options={'maxiter': 20000})

# 输出最优的电路参数和最低的能量本征值
print(result)
