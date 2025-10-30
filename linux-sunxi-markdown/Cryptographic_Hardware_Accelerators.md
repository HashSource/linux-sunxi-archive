# Cryptographic Hardware Accelerators
Linux provides a cryptography framework in the kernel that can be used for e.g. IPsec and dm-crypt. Some SoCs, co-prosessors, and extension boards provide hardware acceleration for speeding up cryptographic operations. The Allwinner boards provide varying degrees of hardware support for such operations (e.g. AES/DES/3DES, MD5/SHA1/SHA224/SHA256/SHA384/SHA512, and random number generation). The current status of the sunxi support in mainline kernels is documented in [http://sunxi.montjoie.ovh/#support_overview][13441]
# Support status
Driver  | sun4i-ss  | sun8i-ss  | sun8i-ce  |   
---|---|---|---|---  
Category  | Name  | A20  | A10  | A10S  | A31  | A33  | V3S  | A80  | A83T  | H3  | A64  | H5  | H6  | Note   
AES/DES/3DES  | CBC  | 4.3  | 4.3  | NT  | 4.3  | 4.3  | WIP  | 5.5  | 5.5  | 5.5  | 5.5  | 5.5  | 5.5  |   
ECB  | 4.3  | 4.3  | NT  | 4.3  | 4.3  | WIP  | 5.5  | 5.5  | 5.5  | 5.5  | 5.5  | 5.5  |   
CTS  | NO(1)(2)  | NO  | NO  | NO  | NO  | NO  | NT  | WIP  | OK  | OK  | OK  | WIP  | (1)(2)   
CTR  | NO(1)(3)  | NO  | NO  | NO  | NO  | NO  | NT  | WIP  | OK  | OK  | OK  | WIP  | (1)(3)   
OFB  |  |  |  |  |  |  |  |  | WIP  |  |  | WIP  |   
CFB  |  |  |  |  |  |  |  |  | WIP  |  |  | WIP  |   
CBC-MAC  |  |  |  |  |  |  |  |  | WIP  |  |  | WIP  |   
XTS  |  |  |  |  |  |  |  |  |  |  |  | OK  |   
HASH  | MD5  | 4.3  | 4.3  | NT  | 4.3  | 4.3  | WIP  | NT  | 5.10  | 5.10  | 5.10  | 5.10  | 5.10  |   
SHA1  | 4.3  | 4.3  | NT  | 4.3  | 4.3  | WIP  | NT  | 5.10  | 5.10  | 5.10  | 5.10  | 5.10  |   
SHA224  |  |  |  |  |  |  | NT  | 5.10  | 5.10  | 5.10  | 5.10  | 5.10  |   
SHA256  |  |  |  |  |  |  | NT  | 5.10  | 5.10  | 5.10  | 5.10  | 5.10  |   
SHA384  |  |  |  |  |  |  |  |  | 5.10  |  |  | 5.10  |   
SHA512  |  |  |  |  |  |  |  |  | 5.10  |  |  | 5.10  |   
HMAC-SHA1  |  |  |  |  |  |  |  |  | WIP  | WIP  | WIP  | WIP  |   
HMAC-SHA256  |  |  |  |  |  |  |  |  |  |  | WIP  | WIP  |   
RNG  | PRNG  | 4.14  | 4.14  | 4.14  | 4.14  | 4.14  | WIP  | NT  | 5.10  | 5.10  | 5.10  | 5.10  | 5.10  | (8)   
TRNG  |  |  |  |  |  |  | NO  | ??(10)  | ??(10)  | ??(10)  | ??(10)  | 5.10  |   
RSA  | 512  |  |  |  |  |  |  |  | WIP  | SNW (9)  | OK  | OK  | WIP  |   
1024  |  |  |  |  |  |  |  | WIP  | SNW (9)  | OK  | OK  | WIP  |   
2048  |  |  |  |  |  |  | NO  | WIP  | SNW (9)  | OK  | OK  | WIP  |   
3072  |  |  |  |  |  |  |  | WIP  | SNW (9)  |  | SNW  | WIP  |   
4096  |  |  |  |  |  |  |  |  | SNW (9)  |  | SNW  | WIP  |   
ECC  | 160  |  |  |  |  |  |  |  |  |  |  |  | WIP  |   
224  |  |  |  |  |  |  |  |  |  |  |  | WIP  |   
256  |  |  |  |  |  |  |  |  |  |  |  | WIP  |   
384  |  |  |  |  |  |  |  |  |  |  |  | WIP  |   
521  |  |  |  |  |  |  |  |  |  |  |  | WIP  |   
CRC  | CRC32  |  |  |  |  |  |  |  | WIP  |  |  |  |  |   
Note  |  |  | (7)  | (5)  | (6)  |  |  |  |  |  |  |  |   
Legend 
  * 4.3 support is available since Linux x
  * OOT support is available via an out of source patch
  * NO support is not written
  * WIP support is being written
  * NT Need hardware for testing
  * SNW Unsupported according to datasheet, but work. (Need extended testing)

Read the datasheet for more details. 
Notes 
  * (1): CTR and CTS are not available due to hardware bug see this answer on linux-crypto
  * (2): CTS block mode is not available for DES/3DES according to datasheet
  * (3): CTR mode is referenced as CNT mode in the datasheet
  * (7): The PRNG does not seem to work on A10 for the moment
  * (8): See the PRNG section
  * (9): Allwinner have removed all RSA documentation from the H3 user manual 1.2
  * (10): The TRNG is not really random due do lack of documentation
