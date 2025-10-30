# Security System
## Introduction
The Security System (SS) is an encryption, decryption, hashing and PRNG hardware accelerator present on most Allwinner SoCs. Supported by mainline since 4.3. 
More information on [authors website][48960]. 
## Supported algorythms
The hardware supports AES, DES, 3DES on EBC, CBC modes. For hashing, SHA-1 and MD5 are supported, both with standard and custom IVs. AES key sizes supported are 128-bits, 192-bits and 256-bits. The hardware PRNG features 160-bits support with 192-bits seed. 
## Communication
Communication with the SS may be done via a 32-words RX FIFO and a 32-words TX FIFO. The system supports interrupt signaling for (almost-)empty FIFOs.
