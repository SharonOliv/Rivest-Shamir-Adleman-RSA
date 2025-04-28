# Rivest-Shamir-Adleman-RSA
This repository designs and implements the **RSA algorithm** for **key generation**, and demonstrates the **encryption** and **decryption** processes by encrypting both a **number** and an **alphabet** character.

## Overview

The goal of this project is to:
- Generate public and private keys using the RSA algorithm.
- Encrypt a given **number** and a **single alphabet character**.
- Decrypt the encrypted values back to their original form.
- Understand the working of RSA encryption in practical applications.

This project provides a simple demonstration of how asymmetric encryption using RSA works in practice.

## Features

- Generate RSA key pairs (public key and private key).
- Encrypt a numerical value.
- Encrypt an alphabet character.
- Decrypt both values to retrieve the original inputs.
- Show step-by-step RSA operations: key generation, encryption, and decryption.

## Technologies Used

- Python 3
- `random` and `math` libraries (for prime number generation and modular calculations)
- Basic understanding of number theory (prime numbers, modular arithmetic)

## How to Run

1. Clone the repository
2. Navigate to the project directory
3. Run the RSA script:
   ```bash
   python RSA.py
   ```

---

## Notes

- This RSA implementation is simplified for educational purposes and not intended for real-world secure communications.
- The prime numbers chosen for key generation are relatively small for demonstration purposes. In practical scenarios, much larger primes are used for security.
