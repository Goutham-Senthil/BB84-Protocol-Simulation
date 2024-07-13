import random
from qubit import Qubit

class Bob:
    def __init__(self):
        self.bits = []
        self.orientations = []
        self.qubits = []
        self.indexes = []
        self.key = []

    def reset(self):
        self.bits = []
        self.orientations = []
        self.qubits = []
        self.indexes = []
        self.key = []

    def send_qubits(self, n):
        # generate n random bits and orientations
        for _ in range(n):
            self.bits.append(random.randint(0, 1))
            self.orientations.append(random.randint(0, 1))

        for i in range(len(self.bits)):
            if self.orientations[i] == 1:
                self.qubits.append(Qubit(0 + (self.bits[i] * 180)))
            else:
                self.qubits.append(Qubit(90 + (self.bits[i] * 180)))

        return self.qubits

    def compare_orientations(self, received_orientations):
        for i in range(len(received_orientations)):
            if received_orientations[i] == self.orientations[i]:
                self.indexes.append(i)
        return self.indexes

    def create_key(self, length):
        for i in self.indexes:
            self.key.append(self.bits[i])

        byte_array = []
        try:
            for i in range(0, len(self.key), 8):
                tmp = ""
                for b in range(8):
                    tmp += str(self.key[i + b])
                byte_array.append(int(tmp, 2))
                if len(byte_array) == length:
                    break
        except IndexError:
            pass

        return byte_array
