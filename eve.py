import random
from qubit import Qubit

class Eve:
    def __init__(self):
        pass

    def measure_qubits(self, received_qubits):
        orientations = []
        for _ in range(len(received_qubits)):
            orientations.append(random.randint(0, 1))
        
        for i in range(len(received_qubits)):
            if orientations[i] == 0:
                received_qubits[i].measure("horizontal")
            else:
                received_qubits[i].measure("vertical")
        
        return received_qubits
