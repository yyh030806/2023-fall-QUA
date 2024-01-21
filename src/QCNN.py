# Update package resources to account for version changes.
import importlib, pkg_resources
from typing import Union, Tuple, Any

from sympy import Symbol

importlib.reload(pkg_resources)
import tensorflow as tf
import tensorflow_quantum as tfq

import cirq
import sympy
import numpy as np
import tensorflow as tf
import tensorflow_quantum as tfq

import cirq
import sympy
import numpy as np

# visualization tools
import matplotlib.pyplot as plt

# visualization tools
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import collections
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Rescale the images from [0,255] to the [0.0,1.0] range.
x_train, x_test = x_train[..., np.newaxis]/255.0, x_test[..., np.newaxis]/255.0

print("Number of original training examples:", len(x_train))
print("Number of original test examples:", len(x_test))

def filter_36(x, y):
    keep = (y == 3) | (y == 6)
    x, y = x[keep], y[keep]
    y = y == 3
    return x,y
x_train, y_train = filter_36(x_train, y_train)
x_test, y_test = filter_36(x_test, y_test)

print("Number of filtered training examples:", len(x_train))
print("Number of filtered test examples:", len(x_test))

x_train_small = tf.image.resize(x_train, (4,4)).numpy()
x_test_small = tf.image.resize(x_test, (4,4)).numpy()


def remove_contradicting(xs, ys):
    mapping = collections.defaultdict(set)
    orig_x = {}
    # Determine the set of labels for each unique image:
    for x,y in zip(xs,ys):
       orig_x[tuple(x.flatten())] = x
       mapping[tuple(x.flatten())].add(y)

    new_x = []
    new_y = []
    for flatten_x in mapping:
      x = orig_x[flatten_x]
      labels = mapping[flatten_x]
      if len(labels) == 1:
          new_x.append(x)
          new_y.append(next(iter(labels)))
      else:
          # Throw out images that match more than one label.
          pass


    num_uniq_3 = sum(1 for value in mapping.values() if len(value) == 1 and True in value)
    num_uniq_6 = sum(1 for value in mapping.values() if len(value) == 1 and False in value)
    num_uniq_both = sum(1 for value in mapping.values() if len(value) == 2)


    return np.array(new_x), np.array(new_y)



x_train_nocon, y_train_nocon = remove_contradicting(x_train_small, y_train)


def convert_to_circuit(image):
    """Encode truncated classical image into quantum datapoint."""
    values = np.ndarray.flatten(image)
    qubits = cirq.GridQubit.rect(4, 4)
    circuit = cirq.Circuit()
    for i, value in enumerate(values):
            circuit.append(cirq.rx(value)(qubits[i]))
    return circuit

x_train_circ = [convert_to_circuit(x) for x in x_train_nocon]
x_test_circ = [convert_to_circuit(x) for x in x_test_small]


x_train_tfcirc = tfq.convert_to_tensor(x_train_circ)
x_test_tfcirc = tfq.convert_to_tensor(x_test_circ)


def one_qubit_unitary(bit, symbols):
    """Make a Cirq circuit enacting a rotation of the bloch sphere about the X,
    Y and Z axis, that depends on the values in `symbols`.
    """
    return cirq.Circuit(
        cirq.X(bit)**symbols[0],
        cirq.Y(bit)**symbols[1],
        cirq.Z(bit)**symbols[2])


def two_qubit_unitary(bits, symbols):
    """Make a Cirq circuit that creates an arbitrary two qubit unitary."""
    circuit = cirq.Circuit()
    circuit += cirq.ry(symbols[0])(bits[0])
    circuit += cirq.ry(symbols[1])(bits[1])
    circuit += cirq.CNOT(control=bits[0],target=bits[1])
    return circuit


def two_qubit_pool(source_qubit, sink_qubit):
    """Make a Cirq circuit to do a parameterized 'pooling' operation, which
    attempts to reduce entanglement down from two qubits to just one."""
    pool_circuit = cirq.Circuit()
    pool_circuit.append(cirq.CNOT(control=source_qubit, target=sink_qubit))
    return pool_circuit

def quantum_conv_circuit(bits, symbols):
    """Quantum Convolution Layer following the above diagram.
    Return a Cirq circuit with the cascade of `two_qubit_unitary` applied
    to all pairs of qubits in `bits` as in the diagram above.
    """
    circuit = cirq.Circuit()
    i=0
    for first, second in zip(bits[0::2], bits[1::2]):
        circuit += two_qubit_unitary([first, second], [symbols[i],symbols[i+1]])
        i=i+2
    for first, second in zip(bits[1::2], bits[2::2] + [bits[0]]):
        circuit += two_qubit_unitary([first, second], [symbols[i],symbols[i+1]])
        i=i+2
    return circuit

def quantum_pool_circuit(bits, symbols):
    """A layer that specifies a quantum pooling operation.
    A Quantum pool tries to learn to pool the relevant information from two
    qubits onto 1.
    """
    circuit = cirq.Circuit()
    i=0
    for first, second in zip(bits[0::2], bits[1::2]):
        circuit += cirq.rz(symbols[i])(second).controlled_by(first)
        circuit += cirq.X(first)
        circuit += cirq.rx(symbols[i+1])(second).controlled_by(first)
        i=i+2
    return circuit
def four_bits_filter(bits, symbols) :
   circuit= cirq.Circuit()
   circuit += quantum_conv_circuit(bits,symbols[0:8])
   circuit += quantum_pool_circuit(bits,symbols[8:12])
   circuit += two_qubit_unitary([bits[1],bits[3]],[symbols[12],symbols[13]])
   circuit += quantum_pool_circuit(bits[2:],symbols[14:16])
   return circuit
def model_creat():
    qubits=cirq.GridQubit.rect(4,4)
    symbols = sympy.symbols('qconv0:112')
    model_circuit = cirq.Circuit()
    model_circuit += four_bits_filter([qubits[0],qubits[1],qubits[4],qubits[5]], symbols[0:16])
    model_circuit += four_bits_filter([qubits[2],qubits[3], qubits[6], qubits[7]], symbols[16:32])
    model_circuit += four_bits_filter([qubits[8], qubits[9], qubits[12], qubits[13]], symbols[32:48])
    model_circuit += four_bits_filter([qubits[10], qubits[11], qubits[14], qubits[15]], symbols[64:80])
    model_circuit += four_bits_filter([qubits[5], qubits[7], qubits[13], qubits[15]], symbols[96:112])
    print(model_circuit)
    return model_circuit,cirq.Z(qubits[15])

model_circuit, model_readout = model_creat()

# Build the Keras model.
model = tf.keras.Sequential([
    # The input is the data-circuit, encoded as a tf.string
    tf.keras.layers.Input(shape=(), dtype=tf.string),
    # The PQC layer returns the expected value of the readout gate, range [-1,1].
    tfq.layers.PQC(model_circuit, model_readout),
])

def hinge_accuracy(y_true, y_pred):
    y_true = tf.squeeze(y_true) > 0.0
    y_pred = tf.squeeze(y_pred) > 0.0
    result = tf.cast(y_true == y_pred, tf.float32)

    return tf.reduce_mean(result)

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.03),
    loss=tf.keras.losses.Hinge(),
    metrics=[hinge_accuracy])


y_train_hinge = 2.0*y_train_nocon-1.0
y_test_hinge = 2.0*y_test-1.0

NUM_EXAMPLES = 500

x_train_tfcirc_sub = x_train_tfcirc[:NUM_EXAMPLES]
y_train_hinge_sub = y_train_hinge[:NUM_EXAMPLES]

history = model.fit(
      x_train_tfcirc_sub, y_train_hinge_sub,
      batch_size=32,
      epochs=20,
      verbose=1,
      validation_data=(x_test_tfcirc, y_test)
)
results = model.evaluate(x_test_tfcirc, y_test)

plt.plot(history.history['accuracy'])
plt.title("QCNN for MNIST")
plt.xlabel("epochs")
plt.ylabel("accuracy")
plt.show()

