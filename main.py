import random
import base64
from alice import Alice
from bob import Bob
from eve import Eve
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Quantum key distribution with protocol BB84')
    parser.add_argument('key_amount', type=int, help="Amount of keys to create")
    parser.add_argument('key_size', type=int, help="Size of each key in bytes")
    parser.add_argument('-v', '--verbose', action="store_true", help="Verbose output")
    parser.add_argument('-e', '--eve', action="store_true", help="Eve is present")

    args = parser.parse_args()

    key_amount = args.key_amount
    key_size = args.key_size
    verbose = args.verbose
    eve_exists = args.eve
    detected = 0

    for i in range(key_amount):
        alice = Alice()
        bob = Bob()
        eve = Eve()

        alice.reset()
        bob.reset()
        qubits = bob.send_qubits(key_size * 8 * 4)

        # Eve's intervention
        if eve_exists:
            qubits = eve.measure_qubits(qubits)

        orientations = alice.measure_qubits(qubits)
        indexes = bob.compare_orientations(orientations)

        bob_key = bob.create_key(key_size)
        alice_key = alice.create_key(indexes, key_size)

        if alice_key != bob_key:
            detected += 1

        print(f"Alice's key: {alice_key}")
        print(f"Bob's key:   {bob_key}")
        print(f"Eve detected: {alice_key != bob_key}")
        print(f"Eve detected {detected}/{key_amount} times")
