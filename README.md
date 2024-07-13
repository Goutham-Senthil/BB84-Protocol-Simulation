# BB84 Protocol Simulation

This project is a simulation of the BB84 quantum key distribution protocol. The BB84 protocol, developed by Charles Bennett and Gilles Brassard in 1984, is the first quantum cryptography protocol, designed to securely distribute a private key between two parties. This simulation includes the roles of Alice (sender), Bob (receiver), and Eve (eavesdropper), as well as the behavior of qubits.

## About BB84
BB84 is a quantum key distribution scheme that relies on the principles of quantum mechanics, such as superposition and the no-cloning theorem, to securely transmit a private key. The protocol is considered secure due to the disturbance of quantum states when measured, which alerts the communicating parties to the presence of an eavesdropper.The advent of quantum computers, which can efficiently solve problems that are infeasible for classical computers, poses a threat to current cryptographic systems like RSA. Shor's algorithm, for instance, can break RSA encryption in polynomial time. This necessitates the development of new cryptographic methods like BB84, which leverage quantum mechanics to ensure security.

## Overview
The BB84 protocol involves the following steps:
1. Alice generates a random bit string and encodes it in qubits using random bases (horizontal/vertical or diagonal).
2. Alice sends the encoded qubits to Bob.
3. Bob measures the received qubits using his randomly chosen bases.
4. Alice and Bob compare their bases over a public channel and discard the bits where their bases do not match.
5. The remaining bits form the shared secret key.

This project simulates the above steps and includes an eavesdropper, Eve, who attempts to intercept and measure the qubits.

## Architecture
The project consists of four main components:
1. **Qubit**: Represents a quantum bit with properties like superposition and measurement.
2. **Alice**: The sender who prepares and sends qubits to Bob.
3. **Bob**: The receiver who measures the received qubits and collaborates with Alice to generate the shared key.
4. **Eve**: The eavesdropper who intercepts and measures the qubits to try and gain information about the key.

## Project Structure

.
├── main.py
├── alice.py
├── bob.py
├── eve.py
└── qubit.py


## Usage
To run the simulation, use the following command:
```bash
python main.py <key_amount> <key_size> [-v] [-e]
```

- `key_amount`: The number of keys to create.
- `key_size`: The size of each key in bytes.
- `-v, --verbose`: (Optional) Enables verbose output.
- `-e, --eve`: (Optional) Includes Eve in the simulation.

## Example

```bash
python main.py 10 16 -v -e
```

This command simulates the creation of 10 keys, each 16 bytes in size, with verbose output and Eve included in the simulation.

## Requirements

```bash
pip install -r requirements.txt
```


