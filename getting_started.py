import numpy as np
from qiskit import(
  QuantumCircuit,
  execute,
  Aer)
from qiskit.visualization import plot_histogram
from qiskit.visualization import plot_state_city

backend = Aer.get_backend('statevector_simulator')

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(3)


circuit.h(0)
circuit.cx(0, 1)
circuit.cx(0, 2)

# Map the quantum measurement to the classical bits
# circuit.measure([0,1], [0,1])

# Execute the circuit on the qasm simulator
#job = execute(circuit, simulator, shots=1000)

job = execute(circuit, backend)

# Grab results from the job
result = job.result()

outputstate = result.get_statevector(circuit, decimals=3)
# Returns counts
#counts = result.get_counts(circuit)
#print("\nTotal count for 00 and 11 are:",counts)

print(circuit)
print(outputstate)


backend = Aer.get_backend('unitary_simulator')
job = execute(circuit,backend)
result = job.result()

print(result.get_unitary(circuit,decimals=3))


