# MTD Driver
[![MBOX icon important.png][33456]][33457] | This work is not stable at the moment. This both means that these instructions might change arbitrarily in the future, and that you might lose data by upgrading your kernel to some newer work or because they got corrupt.   
---|---  
The **sunxi-nand MTD Linux driver** is the MTD driver for the NAND controller present in the Allwinner A20 chip. It is meant to replace the Allwinner driver present in linux-sunxi-3.4 programmed by Allwinner. In contrast with the Allwinner driver, this driver exposes the underlying NAND device using the standard [Linux MTD interface][33458] and not as an emulated block device. Also, this driver allows reading and writing to the whole NAND flash from Linux, including the [boot0 bootloader][33459] which is loaded by [eGON][33460]. 
## Contents
  * [1 Kernel][33461]
  * [2 Booting][33462]
  * [3 Vocabulary][33463]
    * [3.1 Erase Blocks][33464]
    * [3.2 Pages][33465]
    * [3.3 OOB area][33466]
    * [3.4 Bitflips][33467]
    * [3.5 Error Correcting Code (ECC)][33468]
    * [3.6 Bad Blocks][33469]
    * [3.7 Bad Block Marker (BBM)][33470]
    * [3.8 Bad Block Table (BBT)][33471]
  * [4 Challenges][33472]
    * [4.1 Supporting the hardware randomizer][33473]
    * [4.2 BROM/eGON limitations][33474]
    * [4.3 Preventing uncorrectable errors][33475]
    * [4.4 Paired pages][33476]
    * [4.5 Unstable bits][33477]
  * [5 How to][33478]
  * [6 External Links][33479]

## Kernel
The main work on the MTD driver is done by [bbrezillon][33480]. In order to test the driver you'll have to compile a kernel from these [sources][33481] and use the dtb compiled for your board as well. Since version 3.19 of the Mainline Kernel SLC NAND is supported.  

TODO: create a branch containing up-to-date developments [here][33482]
## Booting
TODO: dtb, u-boot, boot0/sunxi-spl, special hw-randomization for boot partitions  
TODO: create a branch containing up-to-date developments [here][33483]
## Vocabulary
NAND devices being very different from traditional block devices, require specific vocabulary in order to be able to talk about them. Making sure you use the right word helps both getting your message across and also getting help faster without wasting time describing what you're trying to talk about. Below is some common terminology used when talking about MTD devices in general. 
### Erase Blocks
An MTD device consists of a number of **erase blocks**. An **erase block** is the minimum I/O unit of an **erase operation**. An erase operation sets all the bits of an **erase block** to 1s. You can think of them like the blocks of traditional block devices but in reality they behave very differently. See this [FAQ][33484] for a list of differences between the two. 
### Pages
An **erase block** consists of a number of **pages**. A **page** is the minimum I/O unit of a **read/write operation**. When a page is written bits can only change from 1 to 0. In order to change a bit in a page from 0 to 1 a full erase block erase is required before rewriting the block again (and possibly the other blocks that were in the erase block) with the specific bit flipped. 
### OOB area
A **page** consists of a data area and a **out of band (OOB)** area. NAND devices do not store data reliably. Some of the bits you write or read might get flipped. The OOB area is some extra space per page provided by the NAND manufacturer to save **Error Correcting Code (ECC)** bytes. This though is not something enforced and is completely controlled by software. In theory one could use the whole page to write data but with the caveat of getting bits flipped undetectably. 
### Bitflips
This is a symptom observed on modern NAND chips. Some of the bits you have written to a NAND section may flip from one to zero or vice versa.  
This can be caused by various factors: 
  1. Read/write disturbance: when you read or write a NAND page, you may flip some bits in adjacent pages
  2. Data retention lifetime: a NAND device cannot retain data for an infinite time, because NAND cells may loose their charge over time

### Error Correcting Code (ECC)
**ECC** is written in the **OOB area** of each page to provide detection and correction of bit flips in the data area of the page. The **ECC** is characterized by its strength and step size, (e.g. 40 bits / 1024 bytes, where the strength is 40 bits, and the step size is 1024 bytes). These values are usually dictated by the NAND's datasheet. The amount of **ECC** bytes required to achieve the desired bit strength depends on the algorithm used. The most common algorithms use BCH code and more rarely Reed-Solomon code. The **ECC** algorithm can be implemented either in software or in hardware if a the SoC features an **ECC** generator. 
### Bad Blocks
As we already saw, an erase block wears-off as erase operations happen. At some point the erase block will fail to turn all its bits to 1 after an erase operation. When this happens we say that we have a **bad block** and we must avoid using it for our data. **bad blocks** are very common and NAND chips usually ship with **bad blocks** in them from the manufacturer. 
### Bad Block Marker (BBM)
In order to identify **bad blocks** , **bad block markers** are used. The marker is implemented by writing 0x00 on the first 2 bytes of the OOB of the first, last or the first two pages of a block. When a block is marked as bad it is not used for IO operations. 
### Bad Block Table (BBT)
In order to cope with the fact that bad blocks exist and new might appear in the future the system stores information about which blocks are bad in a **Bad Block Table (BBT)**. This table is consulted before any I/O operation and updated whenever an erase operation fails. This table can be either regenerated every time the device starts up or it can be persisted on the NAND chip itself. Regenerating the table on each boot takes a considerable amount of time as the whole NAND has to be scanned and usually an on-nand BBT is used. The table is stored in the last two good erase blocks of the NAND and is preserved across reboots. 
## Challenges
A lot of people are asking why the boards already supported in mainline does not have the NAND related stuff defined in their device trees. There a simple answer to that question: using the current NAND driver with the usual UBI/UBIFS layers to interface with MLC NANDs is simply not reliable enough, and we don't want people to start deploying/using this NAND driver unless they really know what they are doing.  
This being said, if you feel like you don't care about the reliability issues, or just want to test it on your platform you can follow the "how to" section.  
  
Now let's get back to the missing things to get a reliable solution for all allwinner platforms using one or several MLC chips. 
### Supporting the hardware randomizer
Some MLC chips are sensitive to repeated patterns. In other words, when writing too many times the same pattern in a given NAND block, you'll experience a high number of bitflips. So high that even the ECC engine cannot correct them.  
To address that you have to randomize your data before storing them in your NAND, and this is exactly what the hardware randomizer embedded in the NAND controller is meant for. Note that this is not required on all MLC chips: some of them are not sensitive to reapeted patterns (older MLC chips), and some directly embed the randomizer in their die, thus removing the need for an external randomizer (this is the case for some Micron chips).  
  
Status: [Submitted][33485], waiting for reviews. 
### BROM/eGON limitations
TODO: describe the BROM limitations in term of ECC and randomizer config, and the possible incompatibility with the NAND requirements. Explain how to overcome that and allow BOOT0/SPL flashing (raw access mode). 
### Preventing uncorrectable errors
As described above, ECC algorithms are here to correct a certain amount of bitflips, but if the number of bitflips exceeds the ECC strength, you experience data loss. While data retention issues are common to all NAND chips, MLC NANDs are way more exposed to read/write disturbance.  
In order to prevent uncorrectable errors, we have to regularly scan all NAND blocks and detect those where we have reached a critical limit (called bitflip theshold), and move data to another block.  

Status: Richard Weinberger proposed a solution to handle that at the UBI level. His solution is involving [trivial changes to the UBI code][33486] to expose new ioctls to userspace and a [userspace daemon][33487] which is reponsible for doing the hard work. 
### Paired pages
TODO: describe the "paired pages" concept and the associated constraints 
### Unstable bits
TODO: describe the "unstable bits" problem 
## How to
[Mainline NAND Howto][33488] contains some bits and pieces on how to set up NAND. 
## External Links
  * [Flash memory][33489]
  * [Bad blocks][33490]
