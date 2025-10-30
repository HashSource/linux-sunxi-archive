# TOC0
## Contents
  * [1 TOC0 Header][53383]
    * [1.1 Main Header][53384]
    * [1.2 Item Header][53385]
  * [2 TOC0 Items][53386]
    * [2.1 Certificate (ID 0x010101)][53387]
    * [2.2 Firmware Item (ID 0x010202)][53388]
    * [2.3 Key Item (ID 0x10303)][53389]
  * [3 TOC0 images generation][53390]
    * [3.1 U-Boot's mkimage][53391]
    * [3.2 TOC0 generator/converter in Ruby (Deprecated way)][53392]
  * [4 TOC0 vs. eGON.BT0][53393]
  * [5 ToDo][53394]
    * [5.1 Check if it is actually possible to configure secure peripherals after booting via eGON.BT0. Are there any other differences?][53395]
    * [5.2 Implement and test FEL boot for TOC0 bootloaders.][53396]

# TOC0 Header
The TOC0 header is made up of a main header followed immediately by two or more item headers. 
## Main Header
Name | Offset | Size | Values | Description   
---|---|---|---|---  
TOC0_NAME | 0x00 | 8B | 
[code]
    "TOC0.GLH"
[/code]
| Name   
TOC0_MAGIC | 0x08 | 4B | 
[code]
    0x89119800
[/code]
| Magic value   
TOC0_CHECK_SUM | 0x0c | 4B |  | Checksum, same algorithm as eGON.BT0 images   
TOC0_SERIAL_NUM | 0x10 | 4B |  | Possibly ignored by the SBROM   
TOC0_STATUS | 0x14 | 4B | 
[code]
    0x0: Not encrypted
    0x1: Encrypted with the SSK
    0x2: Encrypted with the BSSK
    
[/code]
| Possibly ignored by the SBROM   
TOC0_NUM_ITEMS | 0x18 | 4B | 2+ | Number of item headers following the main header. Since unknown item headers are ignored, this can be greater than the number of actual items to create gaps in the header.   
TOC0_LENGTH | 0x1c | 4B |  | Total length of the TOC0 image. This must be a multiple of the storage block size (e.g. 512B or 8KiB).   
TOC0_BOOT_MEDIA | 0x20 | 4B |  | The first byte is the boot device, written by SBROM. The meaning of the other three bytes is unknown.   
TOC0_RESERVED | 0x24 | 8B |  | Ignored by the SBROM   
TOC0_END | 0x2c | 4B | 
[code]
    "MIE;"
[/code]
| End marker   
## Item Header
The SBROM searches for items by name. This means item headers can appear in any order, and item headers with unknown IDs are ignored. 
Name | Offset | Size | Values | Description   
---|---|---|---|---  
TOC0_ITEMn_ID | 0x30 + n * 0x20 + 0x00 | 4B | 
[code]
     0x010101 = Certificate Item
     0x010202 = Firmware Item (code)
     0x010303 = Key Item (first used on H6)
    
[/code]
| Item ID, see descriptions below   
TOC0_ITEMn_OFFSET | 0x30 + n * 0x20 + 0x04 | 4B |  | Item data offset from start of TOC0. For the firmware item, this should be aligned to 32 bytes.   
TOC0_ITEMn_LENGTH | 0x30 + n * 0x20 + 0x08 | 4B |  | Item data length. For the firmware item, this should be aligned to 32 bytes.   
TOC0_ITEMn_STATUS | 0x30 + n * 0x20 + 0x0c | 4B | 
[code]
    0x0: Not encrypted
    0x1: Encrypted
    
[/code]
| Possibly ignored by the SBROM   
TOC0_ITEMn_TYPE | 0x30 + n * 0x20 + 0x10 | 4B | 
[code]
    0x0: Null
    0x1: Certificate
    0x2: Signed binary
    0x3: Binary
    
[/code]
| Appears to be ignored by the SBROM   
TOC0_ITEMn_RUN_ADDR | 0x30 + n * 0x20 + 0x14 | 4B |  | Address to copy firmware item to before running it   
TOC0_ITEMn_RESERVED | 0x30 + n * 0x20 + 0x18 | 4B |  | Ignored by the SBROM   
TOC0_ITEMn_END | 0x30 + n * 0x20 + 0x1c | 4B | 
[code]
    "IIE;"
[/code]
| End marker   
# TOC0 Items
## Certificate (ID 0x010101)
This is a DER-encoded X.509-like certificate containing a SHA256 hash of the firmware item. Only a few of the certificate fields are even read, and of those, some are ignored. The certificate has a similar structure to standard X.509 certificates, but is different in many important details: 
  * The public key is stored in a non-standard way.
  * The hash is added at the place of extensions, but not as a real extension.
  * The last 4 bytes of the certificate (which are the last 4 bytes of the firmware digest) are not signed.
  * The signature algorithm is prepended to the signature, but the two objects are not inside a sequence.

Below is the structure of the minimal certificate that is accepted by the SBROM: 
[code] 
        0:d=0  hl=4 l= 601 cons: SEQUENCE          #
        4:d=1  hl=4 l= 330 cons:  SEQUENCE         #
        8:d=2  hl=2 l=   3 cons:   cont [ 0 ]      #
       10:d=3  hl=2 l=   1 prim:    INTEGER        # "version"      -- Up to 4 bytes are read (but ignored); contents must be exactly 2 bytes into the sequence
       13:d=2  hl=2 l=   1 prim:   INTEGER         # "serialNumber" -- Up to 4 bytes are read (but ignored)
       16:d=2  hl=2 l=   0 cons:   SEQUENCE        # "signature"    -- Up to 255 bytes are read (but ignored)
       18:d=2  hl=2 l=   0 cons:   SEQUENCE        # "issuer"       -- The tag must be 0x30 (SEQUENCE), but the data is not read
       20:d=2  hl=2 l=   0 cons:   SEQUENCE        # "validity"     -- The tag must be 0x30 (SEQUENCE), but the data is not read
       22:d=2  hl=2 l=   0 cons:   SEQUENCE        # "subject"      -- The tag must be 0x30 (SEQUENCE), but the data is not read
       24:d=2  hl=4 l= 272 cons:   SEQUENCE        # "subjectPublicKeyInfo"
       28:d=3  hl=2 l=   0 cons:    SEQUENCE       # "algorithm"    -- Up to 255 bytes are read (but ignored); contents must follow exactly 6 bytes after "subject"
       30:d=3  hl=4 l= 266 cons:    SEQUENCE       #
       34:d=4  hl=4 l= 257 prim:     INTEGER       # Public key "n" -- Up to 400 bytes are read
      295:d=4  hl=2 l=   3 prim:     INTEGER       # Public key "e" -- Up to 400 bytes are read
      300:d=2  hl=2 l=  36 cons:   cont [ 3 ]      #
      302:d=3  hl=2 l=  34 cons:    SEQUENCE       #
      304:d=4  hl=2 l=  32 prim:     OCTET STRING  # Firmware hash  -- Contents must follow exactly 6 bytes after the key exponent
      338:d=1  hl=4 l= 263 cons:  SEQUENCE         #                -- The tag must be 0x03 (BIT STRING), but this is really a sequence
      342:d=2  hl=2 l=   0 cons:   SEQUENCE        #                -- The tag must be 0x30 (SEQUENCE)
      344:d=2  hl=4 l= 257 prim:   BIT STRING      # RSA signature  -- Up to 400 bytes are read
    
[/code]
When the SBROM reads a 256-byte or longer object such as the public key modulus or signature (i.e. when the first length byte is 0x82), if the length is odd, the first byte is ignored. This means a modulus with the high bit set can either be encoded as a negative INTEGER, or zero-extended to 257 bytes to remain positive. Both encodings are accepted. Similarly, the "bits remaining" field at the beginning of the inner signature BIT STRING is ignored. This does _not_ apply to the outer signature (fake) "BIT STRING", which must not have a "bits remaining" field at all. 
If the SBROM is configured to use a key item (this is the default on the H6; it is unavailable on older SoCs), the certificate must include (and be signed by) "KEY1" from the key item. Otherwise, it must include (and be signed by) the ROTPK. To make a TOC0 that will be accepted either way, fill both slots in the key item with the ROTPK. 
If a [ROTPK_HASH][53397] is programmed, only certificates (or key items) with that key are accepted. Otherwise, any key you generate can be the ROTPK. 
Certificates generated by the BSP do not use padding when computing the signature. However, because the SBROM only looks at the least-significant 32 bytes of the decrypted signature, any padding algorithm can be used. 
While the SBROM will read and parse a certificate containing 3072-bit RSA keys, it is hardcoded to perform 2048-bit modular arithmetic, so such a certificate will fail to verify. 
## Firmware Item (ID 0x010202)
This item has no specific format. After verifying against the SHA256 hash in the certificate, this item is memmove'd to the run address given in the item header and executed in secure mode. This run address can be anywhere in SRAM, except where it would overwrite the SBROM's stack. Note that the memmove happens after the SBROM stores the boot device in the main header, so if the run address is in the first 0x24 bytes of SRAM A1, that information will be lost. 
The only format requirement is that the item, as stored in the TOC0 image, must start and end on a 32-byte boundary. This requirement comes from the SHA256 implementation, which expects full, aligned blocks. 
## Key Item (ID 0x10303)
This item links two public keys together. It is signed by the first key. If the [VENDOR_ID][53398] eFUSE is programmed, the VENDOR_ID value in the key item is checked against it. 
The key item has the following format: 
Name | Offset | Size | Description   
---|---|---|---  
VENDOR_ID | 0x000 | 4B | Arbitrary identifier, must match eFUSE value if programmed   
KEY0_N_LEN | 0x004 | 4B | Length of KEY0 modulus, in bytes. In practice, only 2048-bit keys are supported.   
KEY0_E_LEN | 0x008 | 4B | Length of KEY0 exponent, in bytes   
KEY1_N_LEN | 0x00c | 4B | Length of KEY1 modulus, in bytes. In practice, only 2048-bit keys are supported.   
KEY1_E_LEN | 0x010 | 4B | Length of KEY1 exponent, in bytes   
SIG_LEN | 0x014 | 4B | Length of signature (signed by KEY0), in bytes. In practice, only 2048-bit signatures are supported.   
KEY0 | 0x018 | 512B | KEY0 modulus, followed by KEY0 exponent   
KEY1 | 0x218 | 512B | KEY1 modulus, followed by KEY1 exponent   
RESERVED | 0x418 | 32B | Ignored   
SIGNATURE | 0x438 | ... | SHA256+RSA signature of all other fields   
# TOC0 images generation
## U-Boot's mkimage
Since U-Boot v2022.07 the mkimage tool supports the TOC0 format. To generate a TOC0 image from a binary, you will need an RSA key (pair) file. As most secure-boot enabled devices do not burn the VENDOR_ID eFUSE, you can use any RSA key, so just generate one, for instance with the openssl tool (would only need to be done once): 
[code] 
       openssl genrsa -out root_key.pem
       mkimage -A arm -T sunxi_toc0 -a 0x20000 -d input.bin output.toc0
    
[/code]
The TOC0 format requires a fixed load address, so the generated image file will only work on devices where this address is located in some SRAM. 
When building a U-Boot image, setting CONFIG_SPL_IMAGE_TYPE_SUNXI_TOC0=y will automatically generate a TOC0 SPL (with the right load address) and will integrate this with U-Boot proper as usual. 
## TOC0 generator/converter in Ruby (Deprecated way)
There is a preliminary script: <https://gist.github.com/jemk/2abcab1359c4bce793679c5854062331>
Some notes: 
  * You may need to replace the ".sum" method with ".reduce(:+)" to run it with modern versions of Ruby
  * You may need to change the entry point address from 0x0 to 0x10000 if you want to run it on A64/H64/H5 (the default 0x0 value is used for H3)

The experimental branch <https://github.com/ssvb/sunxi-tools/commits/toc0> contains two scripts ([egon2toc.rb][53399] and [toc2egon.rb][53400], based on Jemk's library). They can be used to convert SPL binaries back and forth between these two formats. Usage example: 
[code] 
       git clone -b toc0 <https://github.com/ssvb/sunxi-tools.git>
       cd sunxi-tools
       ruby egon2toc.rb bin/uart0-helloworld-sdboot.sunxi bin/uart0-helloworld-sdboot.toc0
       ruby toc2egon.rb bin/uart0-helloworld-sdboot.toc0 roundtrip-conversion-output.sunxi
       cmp -b bin/uart0-helloworld-sdboot.sunxi roundtrip-conversion-output.sunxi
    
[/code]
The resulting file **bin/uart0-helloworld-sdboot.toc0** can be written to an SD card or to SPI NOR flash and successfully booted on Allwinner H3/A64/H64 devices with secure mode bit burned in the eFUSE. 
Doing conversion of the **u-boot-sunxi-with-spl.bin** files (not just SPL alone) back and forth between eGON and TOC0 formats requires a minor patch for U-Boot. 
# TOC0 vs. eGON.BT0
Feature  | Allwinner A64/H64/H5   
---|---  
eGON.BT0  | TOC0   
Boot time | [TBD][53401] | TBD (but worse than eGON)   
SPL size limit | 32 KiB (SRAM A1), H6 and newer chips may support larger | more than 100 KiB (SRAM A1 + SRAM C)   
SPL load address | Loaded into SRAM A1 and executed there. This address is may be different on different SoC types, but the same position independent code can run on multiple SoC types (see [uart0-helloworld-sdboot][53402] example) | The load & execute address is specified in the TOC0 item header and it should be set as SRAM A1 address of the SoC (or at least land into a valid SRAM address range). This is a little bit problematic, because it becomes difficult to boot the same image, for example, on H3 and A64 (but maybe we can load the SPL into SRAM A2 to overcome this?).   
Can boot from | Works with SD card, eMMC, eMMC boot partitions, SPI. NAND is untested. | Works with SD card, eMMC, eMMC boot partitions. SPI and NAND are still untested.   
Boot source detection | A 8-bit boot media type identifier is written by the BROM at the offset 0x28 in SRAM A1 | A 8-bit boot media type identifier is written by the BROM at the offset 0x20 in SRAM A1   
Secure peripherals | Access to SID and the other secure-only resources is allowed from both secure and non-secure mode, SPC settings are ignored. Investigation for a possible fix or workaround is underway. | Work correctly, SPC settings are respected.  
  
**Note:** some peripherals are switchable but the others are secure-only (such as SID). It means that secure boot is not a superset and the eGON-style non-secure boot configuration can't be replicated at the moment. This may cause inconveniences for the Linux kernel (reading SID is a perfect example) and some assistance from the firmware will be required.   
The currently used eGON.BT0 images can be wrapped into TOC0 containers with just a little bit of adaptation. As discussed in the irc log, a small extra stub code added to the TOC0 container can ensure that the eGON.BT0 image lands at the start of SRAM A1 and also the boot media identifier can be patched there at the expected offset 0x28. This way the differences between eGON.BT0 and TOC0 can be fully hidden and we can continue using eGON.BT0 as a single unified format for the SPL on Allwinner devices (the 32K size restriction can be lifted though). 
The task of converting from eGON.BT0 to TOC0 can be delegated to a smart flasher tool. For example, sunxi-fel can check whether the secure boot bit is set in [LCJS][53403] and automatically do conversion into the TOC0 format [when flashing SPI NOR][53404]. As an additional safety measure, it's also best if the tool can verify that the device is not locked down to only accept some particular key. 
U-Boot build may produce images in both formats, but a smart flasher tool can interchangeably use either of them if the conversion is straightforward (this way a possible user error is eliminated). 
This all is very similar in principle to what we have already done with FEL USB boot support (eliminate a special extra U-Boot build configuration and just use a single unified image for both SD card boot and FEL USB boot): <https://lists.denx.de/pipermail/u-boot/2015-February/204388.html>
U-Boot build generates a single unified ["payload"][53405]. And sunxi-tools provides a suitable ["delivery"][53406] method :-) 
# ToDo
## Check if it is actually possible to configure secure peripherals after booting via eGON.BT0. Are there any other differences?
Tried to dump and compare HW registers with/without TOC0: <https://gist.github.com/ssvb/88963c61c714068716412d828b9ff74e/revisions>
There was a hope to maybe find some magic bit, which will allow restricting access to peripherals in non-secure mode. 
This is a trivial quick and dirty test program, which can verify if such restrictions actually work as expected: <https://github.com/ssvb/sunxi-tools/commit/3ffc4fbc3e5448d3390052ad2aa553afe69fefe6>
Running it on [Jide Remix Mini][53407] (secure bit is set in eFUSE) via "sunxi-fel spl" after "sunxi-fel smc": 
[code] 
    Checking the current mode ... secure.
    Switching to non-secure ... done.
    Checking peripherals security ... SRAM A2 is not accessible (this is GOOD).
    
    Hello from Allwinner A64!
    Returning back to FEL.
    
[/code]
Running on [Pine64][53408] (secure bit is not set in eFUSE) via "sunxi-fel spl": 
[code] 
    Checking the current mode ... secure.
    Switching to non-secure ... done.
    Checking peripherals security ... SRAM A2 is accessible (this is BAD).
    
    Hello from Allwinner A64!
    Returning back to FEL.
    
[/code]
None of the attempts to toggle various bits in various HW registers helped so far on Pine64, restricting access to SRAM A2 does not work. 
Note: the test program does not work correctly on Jide Remix Mini when booting from SD card (deadlocks when trying to switch to non-secure, most likely the default settings are not the same as in FEL mode): 
[code] 
    Checking the current mode ... secure.
    Switching to non-secure ... 
    
[/code]
## Implement and test [FEL boot][53409] for TOC0 bootloaders.
We can in principle boot TOC0 images via sunxi-fel even on boards without the secure bit set in eFUSE (and can boot oversized TOC0 images too). This just needs to be implemented.
