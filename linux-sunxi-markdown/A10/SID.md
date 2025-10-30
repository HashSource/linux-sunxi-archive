# SID Register Guide
(Redirected from [A10/SID][823])
 
## Contents
  * [1 Security ID][826]
    * [1.1 A10/A20/A33][827]
      * [1.1.1 SID Registers][828]
        * [1.1.1.1 SID_KEY[0-3]][829]
        * [1.1.1.2 SID_WRITE_DATA][830]
        * [1.1.1.3 SID_WRITE_CTRL][831]
    * [1.2 A83T/A64/H3/H6][832]
      * [1.2.1 Registers][833]
        * [1.2.1.1 SID_PRCTL][834]
        * [1.2.1.2 SID_PRKEY][835]
        * [1.2.1.3 SID_RDKEY][836]
  * [2 eFUSE Contents][837]
    * [2.1 eFUSE Region Overview][838]
      * [2.1.1 SoCs before H6][839]
      * [2.1.2 H6][840]
    * [2.2 Specific eFUSE Values][841]
      * [2.2.1 ROTPK_HASH][842]
      * [2.2.2 LCJS][843]
      * [2.2.3 BROM CONFIG][844]
  * [3 Currently known SID's][845]

# Security ID
So far, all Allwinner A-series SoCs come with a bit of memory called 'SID'. So far, for all chips this is 128-512 bytes of usable memory, with a catch. These bytes of memory are not in RAM or ROM, they are so called [e-fuses][846]. Each bit of an e-fuse can only transition from 0 -> 1 once. Writing 0 to a bit does nothing, but once a bit is set to 1, it is set permanently. Therefore, extreme care must be taken when writing any of the areas referenced below. 
By default, the chip ID or revision is written to these fuses, as well as a serial number and [Thermal Sensor][847] calibration data. While modifying is mostly untested at this moment, it is possible to read the fuses. Note that there are two ways to read the fuses, and some chips have a silicon bug that requires using a specific method of reading. 
A few use cases for the SID are, but not limited to: 
  * Generate per-device unique MAC address
  * Store/use as an RSA etc key
  * Write in-house serial numbers
  * Control [Boot ROM][848] behavior

## A10/A20/A33
SID Base address: **0x01c23800**
### SID Registers
Register Name  | Offset  | Size  | Description  | Note   
---|---|---|---|---  
`SID_KEY0` | `0x00` | `4 B` | Key0 [0:31]  |   
`SID_KEY1` | `0x04` | `4 B` | Key1 [32:63]  |   
`SID_KEY2` | `0x08` | `4 B` | Key2 [64:95]  |   
`SID_KEY3` | `0x0c` | `4 B` | Key3 [96:127]  |   
`SID_WRITE_DATA` | `0x40` | `4 B` | Data [0:31]  | NOT VERIFIED   
`SID_WRITE_CTRL` | `0x44` | `4 B` | SID Program Control register  |   
  

##### SID_KEY[0-3]
Default value: undefined  
Offset: 0x0{0, 4, 8, c} 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`KEY[0-3]` | `0:31` | `Read` | `` | `` | 32 bits for SID   
  

##### SID_WRITE_DATA
Default value: 0x00000000  
Offset: 0x40 
We think this is the data register used when programming the SID efuses. 
There is also a EFUSE_VDDQ pin (pin T9 on A10) which is normally tied to GND but which we guess needs to have suitable power to enable efuse programming. Details unknown. 
##### SID_WRITE_CTRL
Default value: 0x00000000  
Offset: 0x44 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`SID_WRITE_START` | `0` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = done writing
        0x01 = start writing
      
    
[/code]
| Writes when enabled, returns to 0 after writing.   
`no operation` | `1:3` | `` | `` | `` |   
`SID_WRITE_POS` | `4:7` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = macrocell 0
        0x01 = macrocell 1
        0x02 = macrocell 2
        0x03 = macrocell 3
      
    
[/code]
| Index of which of the 4 hardware macrocell fuses to burn. It is currently unknown where to obtain said value from but a guess is register 0x40.   
`no operation` | `8:31` | `` | `` | `` |   
## A83T/A64/H3/H6
Newer SoCs have a 2 kbit eFUSE area with a new controller. 
For Allwinner [A83T][849] and [H3][850] the SID address space starts at 0x01c14000, and the e-fuses are at offset 0x200 - so the address to use for these SoCs is **0x01c14200**. 
### Registers
Base address: `0x01c14000`
Register Name | Offset | Size | Description   
---|---|---|---  
[SID_PRCTL][834] | 0x40 | 4B | Control register   
[SID_PRKEY][835] | 0x50 | 4B | Program data   
[SID_RDKEY][836] | 0x60 | 4B | Read data   
#### SID_PRCTL
Offset | `0x40`  
---|---  
Name | Bits | R/W | Default | Values | Description  
` ` | `31:24` | `RW` | `` |  | _reserved_  
` SID_PRCTL_OFFSET ` | `23:16` | `RW` | `` |  | eFUSE offset  
` SID_PRCTL_OP_LOCK ` | `15:8 ` | `W` | `` | 
[code]
    0xac
[/code]
| magic value to prevent accidental programming  
` ` | ` 7:2 ` | `RW` | `` |  | _reserved_  
` SID_PRCTL_READ ` | ` 1 ` | `RW` | `` |  | write 1 to read eFUSE, clears after finish  
` SID_PRCTL_WRITE ` | ` 0 ` | `RW` | `` |  | write 1 to program eFUSE, clears after finish  
#### SID_PRKEY
Offset | `0x50`  
---|---  
Name | Bits | R/W | Default | Values | Description  
` SID_PRKEY ` | `31:0 ` | `RW` | `` |  | data to program to eFUSE  
#### SID_RDKEY
Offset | `0x60`  
---|---  
Name | Bits | R/W | Default | Values | Description  
` SID_RDKEY ` | ` 31:0 ` | `RW` | `` |  | data read from eFUSE  
# eFUSE Contents
## eFUSE Region Overview
### SoCs before H6
Name | Offset | Size | Description   
---|---|---|---  
CHIPID | 0x00 | 128 bit | Chip-ID, also known as SID   
OEM_PROGRAM | 0x10 | 32 bit | _unknown_  
NV1 | 0x14 | 32 bit | _unknown_  
NV2 | 0x18 | 64 bit | BSP Wi-Fi MAC address (according to SDK)   
RSAKEY_HASH | 0x20 | 160 bit | _unknown_  
THERMAL_SENSOR | 0x34 | 64 bit | Thermal sensor calibration data   
RENEWABILITY | 0x3c | 64 bit | _unknown_  
HUK | 0x44 | 256 bit | Hardware Unique Key, later split in IN(192), IDENTIFI(32), ID(32)   
[ROTPK_HASH][842] | 0x64 | 256 bit | SHA256 hash of the "Root of Trust" public key   
SSK | 0x84 | 128 bit | _unknown_  
RSSK | 0x94 | 256 bit | _unknown_  
HDCP_HASH | 0xb4 | 128 bit | _unknown_  
EK_HASH | 0xc4 | 128 bit | _unknown_  
SN | 0xd4 | 192 bit | _unknown, RESERVED before A64_  
NV2_BACKUP | 0xec | ? bit | _unknown, RESERVED before A64_  
[LCJS][843] | 0xf4 | 32 bit | Flags (secure boot mode, ...)   
DEBUG | 0xf8 | 32 bit | _unknown_  
CHIP_CONFIG | 0xfc | 32 bit | Status of the keys (already written, read allowed, etc)   
### H6
Name | Offset | Size | Description   
---|---|---|---  
CHIPID | 0x00 | 128 bit | Chip-ID, also known as SID   
[BROM_CONFIG][844] | 0x10 | 32 bit | _unknown_ , "16 bits config, 16 bits try"   
THERMAL_SENSOR | 0x14 | 64 bit | Thermal sensor calibration data   
TF_ZONE | 0x1c | 128 bit | _unknown_ , probably reserved for Trusted Firmware   
OEM_PROGRAM | 0x2c | 160 bit | _unknown_ , "emac 16 + tvout 32 + reserv 112"   
MAC | 0x38 | 64 bit | MAC address, overlaps OEM_PROGRAM   
WRITE_PROTECT | 0x40 | 32 bit | _unknown_ , possibly a new CHIP_CONFIG   
READ_PROTECT | 0x44 | 32 bit | _unknown_ , possibly a new CHIP_CONFIG   
[LCJS][843] | 0x48 | 32 bit | Flags (secure boot mode, ...)   
ATTR | 0x4c | 32 bit | _unknown_  
HUK | 0x50 | 256 bit | Hardware Unique Key, later split in IN(192), IDENTIFI(32), ID(32)   
VENDOR_ID | 0x5C | 32 bit | Read by SBROM to check [TOC0][851] key item, overlaps HUK   
[ROTPK_HASH][842] | 0x70 | 256 bit | SHA256 hash of the "Root of Trust" public key   
SSK | 0x90 | 128 bit | _unknown_  
RSSK | 0xa0 | 256 bit | _unknown_  
HDCP_HASH | 0xc0 | 128 bit | _unknown_  
EK_HASH | 0xd0 | 128 bit | _unknown_  
SN | 0xe0 | 192 bit | _unknown_  
NV1 | 0xf8 | 32 bit | _unknown_  
NV2 | 0xfc | 224 bit | _unknown_  
HDCP_PKF | 0x118 | 128 bit | _unknown_  
HDCP_DUK | 0x128 | 128 bit | _unknown_  
BACKUP_KEY | 0x138 | 576 bit | _unknown_  
SCK0 | 0x180 | 256 bit | _unknown_  
SCK0_MASK | 0x1a0 | 256 bit | _unknown_  
SCK1 | 0x1c0 | 256 bit | _unknown_  
SCK1_MASK | 0x1e0 | 256 bit | _unknown_  
## Specific eFUSE Values
### ROTPK_HASH
Contains the SHA256 hash of the 2048-bit RSA public key used to verify the signature of the first code executed after BROM, the so-called [TOC0][851]. In the case of a TOC0 containing a key item, the ROTPK is used to sign the key item, and the secondary key in the key item is used to sign the TOC0 firmware contents. 
ROTPK_HASH = SHA256([Byte 0-255] = RSA modulus || [Byte 256-x] = RSA public exponent || [Byte x-511] filled with 0x91) 
The hash isn't checked as long as all 32-bit words in this eFUSE have the same value. This means, only the signature is verified, but not the key used to sign, so any key can be used. 
### LCJS
Name | Bits | Values | Description   
---|---|---|---  
LCJS_CUSTOM_DMA_WAIT | 31:30  | 
[code]
      0x2  = custom wait cycles (para0 * para1)
     other = fixed wait cycles (32)
    
[/code]
| BROM flag: DMA wait cycles   
LCJS_CE_CLK_SRC | 29:28  | 
[code]
      0x2  = PLL_PERIPH0/4
     other = OSC24M
    
[/code]
| SBROM flag: CE clock source   
LCJS_DMA_WAIT_PARA1 | 27:24  |  | BROM param: DMA wait cycles   
LCJS_DMA_WAIT_PARA0 | 23:20  |  | BROM param: DMA wait cycles   
LCJS_SW_SHA256 | 19:18  | 
[code]
      0x2  = software SHA256
     other = CE hardware SHA256
    
[/code]
| SBROM flag: use software SHA256 instead of CE   
LCJS_MAGIC_FEL_FLAG | 17:16  | 
[code]
      0x2  = set flag
     other = don't set flag
    
[/code]
| SBROM flag: write magic value at 0x2800, which is checked by FEL code (what does FEL do with it?)   
LCJS_SECURE_BOOT | 11 | 
[code]
     0x1 = secure boot
     0x0 = normal boot
    
[/code]  
### BROM CONFIG
Note: Addresses below come from the H6 SBROM. 
Name | Bits | Values | Description   
---|---|---|---  
UNKNOWN | 31:29 | unknown | probably unused   
BOOT_SELECT | 28:16 | unknown | See Manual for details   
UNKNOWN | 15 | 
[code]
    0x0: boot toc0 with 0x10303
    0x1: boot toc0 without 0x10303
    
[/code]
|   
CE_CLK_DIV | 14 | 
[code]
    When BROM_CONFIG[13] is clear:
      0x0: ??? Clock init
      0x1: ??? Clock init
    When BROM_CONFIG[13] is set:
      0x0: CE_SCLK = PLL_PERIPH0 / 4
      0x1: CE_SCLK = PLL_PERIPH0 / 6
    
[/code]
|   
CE_CLK_SRC | 13 | unknown | Controls clock init in FUN_00001164   
MAGIC_FEL_FLAG | 12 | 
[code]
    0x0: don't copy magic
    0x1: copy magic
    
[/code]
| SBROM: write magic values to 0x22800, 0x22804   
SW_SHA256 | 11 | 
[code]
    0x0: CE sha256
    0x1: software sha256
    
[/code]
|   
DMA0_WAIT_CYCLES | 10:8 | 
[code]
    (integer)
[/code]
| Only used when bits 5 and 7 are set   
DMA0_WAIT_FLAG | 7 | 
[code]
    0x0: Use 0x20
    0x1: Use BROM_CONFIG[10:8] * 0x10
    
[/code]
| Only used when bit 5 is set   
DMA0_MODE_1 | 6 | 
[code]
    0x0: Set DMA0 to Handshake Mode
    0x1: Set DMA0 to Wait Mode
    
[/code]
| Used in FUN_000005a4   
DMA0_MODE_0 | 5 | 
[code]
    0x0: Set DMA0 to Handshake Mode
    0x1: Set DMA0 to Wait Mode
    
[/code]
| Used in FUN_000040d8   
UNKNOWN | 4 | 
[code]
    0x0: Use the first 2 entries of each table
    0x1: Use the first 4 entries of each table
    
[/code]
| Chooses which part of the tables at 0x9a14-0x9c1c will be used when iterating in FUN_0000595c   
UNKNOWN | 3 | unknown | FUN_000007dc, used at 0x5d80 by NAND code   
UNKNOWN | 2 | unknown | FUN_000007b4, used at 0x6B00: possibly SMHC / DMA related ?   
UNKNOWN | 1 | 
[code]
    0x0: Do not add delay
    0x1: Add delay and a debug callout at several places in the BROM
    
[/code]
|   
BOOT_MODE | 0 | 
[code]
    0x0: GPIO Pin Select
    0x1: eFuse Select
    
[/code]
|   
# Currently known SID's
You may try to retrieve the SID value via our [sunxi-tools][852] (`./sunxi-fel sid`) - or dump it from within U-Boot using the corresponding, SoC-specific address (e.g. `md.l 0x01c23800 4`). If running a mainline kernel hexdump should be sufficient. 
[code] 
    hexdump -C /sys/bus/nvmem/devices/sunxi-sid0/nvmem
    00000000  16 51 66 c6 80 51 77 89  54 53 48 48 0a 40 f2 67  |[[email protected]][853]|
    00000010  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
    
[/code]
Simple script to run on legacy kernel with devmem2: 
[code] 
    d0=`./devmem2 0x01c14200 w|grep Value|sed 's/^.*: 0x/ /'`
    d1=`./devmem2 0x01c14204 w|grep Value|sed 's/^.*: 0x/ /'`
    d2=`./devmem2 0x01c14208 w|grep Value|sed 's/^.*: 0x/ /'`
    d3=`./devmem2 0x01c1420c w|grep Value|sed 's/^.*: 0x/ /'`
    echo $d0 $d1 $d2 $d3
    
[/code]
  

Board | eeprom | package batch | notes   
---|---|---|---  
**A10**  
Cubieboard 1.0 1024 (A10) | `16236747 80728452 50574848 064163D5`  
Cubieboard 1.0 1024 (A10) | `162367C7 80778052 50554848 0201DDC3`  
Cubieboard 1.0 1024 (A10) | `16236750 80758352 52574848 08025081`  
Cubieboard 1.0 1024 (A10) | `16236745 80778052 50554848 07C171AD`  
Cubieboard 1.0 1024 (A10) | `16236743 80758952 54544848 0642d3e9`  
Cubieboard 1.0 1024 (A10) | `16236790 80758952 54544848 03c21c4e`  
Cubieboard 1.0 1024 (A10) | `162367d9 80758952 54544848 08c21483`  
Cubieboard 1.0 1024 (A10) | `16236798 80758952 54544848 0781186a`  
Cubieboard 1.0 1024 (A10) | `1623674c 80758952 54544848 0a02c845`  
Cubieboard 1.0 1024 (A10) | `1623670f 80758952 54544848 0981e268`  
Cubieboard 1.0 1024 (A10) | `1623678b 80778251 54534848 0a4285d6`  
Cubieboard 1.0 1024 (A10) | `16236743 80758952 54544848 06410f3d`  
Gemei G9 (A10) | `16236712 80726652 57524848 04c29968`  
Mele A1000 (A10) early version | `00000000 00000000 00000000 00000000`  
pcDuino (A10) | `16236755 80758952 53554848 0a41e8c9 `  
A10-Lime (A10) | `16236782 80778350 51504848 0a0274fa` |  | [Tkaiser][854], via hexdump   
**A10s**  
R7 hdmi-stick (A10s) | `16254157 504B4133 30397030 0A41FA85`  
mk802 hdmi-stick (A10s) | `16254115 50484E39 35397030 0D02F6E8`  
OlinuXino (A10S) | `162541d3 50485937 30357030 04020663`  
**A13** / **R8**  
A13B tablet (A13) | `16254216 504E4837 39313030 06819C58`  
OlinuXIno (A13) | `16254147 50475838 36313030 0341B75D`  
OlinuXIno (A13) | `16254159 50475838 36313030 0B4181E9`  
OlinuXIno (A13) | `16254158 504B4E39 35303030 0A0185F5`  
OlinuXIno Micro (A13) | `16254187 504b4e39 35303030 094313f2`  
NextThingCo CHIP v1.0 (R8) | `1625420f 50303647 36363030 0400b0b0`  
NextThingCo CHIP v1.0 (R8) | `16254293 50303858 31333030 0282919a`  
Nolimbook (A13) | `162542c1 50525039 30313030 06420e6b`  
**A20**  
EOMA68-A20 (A20) | `165165c7 80807552 55564848 0842c7fb`  
Cubietruck (A20) | `16516683 80485172 49514848 0940e0da ` |  | [plaes][855], via sunxi-fel   
Cubietruck (A20) | `16516507 80808952 56524848 03c18168`  
Cubietruck (A20) | `16516581 80808952 56524848 0583548e `  
Cubietruck (A20) | `16516587 80808952 56524848 0b81d536 `  
Banana Pi (A20) | `1651664f 80485686 53504848 0702dde9`  
Banana Pi (A20) | `1651668a 80485788 51484848 02825172`  
Banana Pi M1 (A20) | `165166cc 80485666 53564848 09c255a3` |  | kc's   
Banana Pi R1 (A20) | `16516604 80485686 52524848 0641E864` |  | kc's bpi-r1 (using devmem2)   
A20-OLinuXIno-LIME2 (A20) | `16516608 80485172 49484848 0800ccfc` |  | [Tkaiser][854], via hexdump   
A20-OLinuXIno-LIME2 (A20) | `165166c6 80517789 54534848 0a40f267`  
A20-OLinuXino-MICRO (A20) | `00000000 00000000 00000000 00000000 ` |  | (2 verified)   
Cubieboard 2.0 1024 (A20) | `00000000 00000000 00000000 00000000 ` |  | (3 verified)   
**A31s** , SID in AXP221/AXP221s   
CSQ CS908 (A31s) | `16524251 434e3038 34010088 080d81eb`  
Mele A1000G quad (A31) | `16524251 43423635 32000045 060a7a38`  
**A33** /**R16**  
Aoson M751S (A33) | `0461872a 034c0106 9b486765 00000000`  
iNet D978 Rev02 (A33) | `0461872a 03386006 1846b855 00000000`  
Nintendo NES Classic (R16) | `0461872a 86583185 9ae7d847 6c118000`  
**H2+**  
Orange Pi Zero | `02004620 3435c614 5030034e 58000032`  
Orange Pi Zero | `02c00042 34004620 5035c614 0439098e` | `G6079BA 67B1`  
Banana Pi M2 Zero (early sample without VDD-CPUX regulation) | `02c00042 44004620 78674320 041e044e` | `G9035BA 6CD5`  
Banana Pi M2 Zero | `02C00042 14004620 78870618 0C190412`  
**H3**  
Banana Pi M2+ | `02004620 94358000 502d05ce 5800006c`  
Banana Pi M2+ | `02004620 94358000 50350a8e 4c000022`  
HYH-TBH3 | `02C00081 00004620 51900618 a058e187` |  | BroderTuck's 'Smart Android Box' (using devmem2)   
NanoPi NEO | `02004620 24358810 502405ce 2800000a`  
NanoPi NEO | `02c00081 44004620 5035c204 2c2e0c4e` | G5071BA 65L3 | Lion's batch -- #1   
NanoPi NEO | `02c00081 44004620 5035c204 2417068e` | G5071BA 65L3 | Lion's batch -- #2   
NanoPi NEO | `02c00081 44004620 5035c204 242301ce` | G5071BA 65L3 | Lion's batch -- #3   
NanoPi M1 | `02004620 64358720 50320c8e 40000069`  
Orange Pi PC | `02004620 94340508 5040068e 54000000`  
Orange Pi PC | `02004620 94340508 502b0a8e 24000000`  
Orange Pi PC | `02004620 24340408 50330d0e 60000000`  
Orange Pi PC | `02004620 34344314 503a04ce 80000000`  
Orange Pi PC | `02004620 34344314 503b0c0e 80000000`  
Orange Pi PC | `02c00081 94004620 50340508 3035080e` | `F7008BA 68E3` | kc's opipc#1   
Orange Pi PC | `02c00081 54004620 50354520 1033080e` | `G2064BA 62T3` | kc's opipc#2   
Orange Pi PC | `02c00081 54004620 50354520 1c34020e` |  | NiteHawk's OPiPC, (incorrect) value before was  
`02004620 54354520 5034020e 1c000000`  
Orange Pi PC | `02c00081 54004620 50358720 4c1c058e` | `G4075BA 64P3`  
Orange Pi PC Plus | `02004620 1435811c 50340a0e 4c00006f`  
Orange Pi PC Plus | `02004620 1435811c 5024010e 5c000080`  
Orange Pi Plus | `02004620 94340508 501a050e 4000006d`  
Orange Pi Plus 2 | `02004620 34344314 5021034e 5c000000`  
Orange Pi Plus 2E | `02004620 1435811c 501d078e 4c000060`  
Orange Pi Plus 2E | `02004620 1435811c 503f050e 48000085`  
Orange Pi Plus 2E | `02c00081 14004620 5035811c 4423098e` | `G4060BA-64H3` | kc's opi+2e   
Orange Pi Lite | `02004620 1435811c 5022018e 64000022`  
Orange Pi Lite | `02004620 1435811c 5018050e 3c000011`  
Orange Pi Lite | `02c00081 14004620 50354718 3422048e`  
Orange Pi One | `02004620 9435430c 502e034e 58000000`  
Orange Pi One | `02004620 4435c204 502404ce 20000065`  
Orange Pi One | `02c00081 74004620 50358720 3c27048e` | `G5039BA 6593`  
Orange Pi 2 | `02004620 34900700 51360a0c 0c000050`  
NanoPi NEO | `02c00081 24004620 50358810 282405ce` |  | [Tkaiser][854], via hexdump   
NanoPi M1 Plus | `02c00081 74004620 5035c504 6416090e` |  | [Tkaiser][854], via hexdump   
**H5**  
Orange Pi PC 2 | `82800001 24004704 5035c120 303403cc`  
Orange Pi PC 2 | `82800001 44004704 5035c120 2c2d07cc`  
Orange Pi PC 2 | `82800001 34004704 5035c120 1c2d02cc` | `G7015AA 67E1`  
Orange Pi Prime | `82800001 34004704 5035c200 382f020c` | `G8112AA 6AU2`  
NanoPi NEO2 | `82800001 34004704 5035c200 3c2b068c` | `G8112AA 6AU2` | FriendlyELEC sent to Icenowy, #1   
NanoPi NEO2 | `82800001 34004704 5035c200 303a080c` | `G8112AA 6AU2` | FriendlyELEC sent to Icenowy, #2, in the same order with #1   
NanoPi K1 Plus | `82800001 64004704 5036c304 082a068e` |  | [Tkaiser][854], via hexdump   
**A64**  
Pine64 sample (green LED) | `92c000ba 24104620 51900808 14160acb`  
Pine64+ sample (green LED) | `92c000ba 24004620 51900808 141709cb`  
Pine64+ (red LED) | `92c000ba 04004620 51900804 0805070b`  
Pine64+ 2GB (red LED) | `92c000ba 04004620 51900804 040905cb`  
Pine64+ 2GB (red LED) | `92c000ba 54104620 51900808 581802cb` | `F8059BA 4977`  
Pine64+ 2GB (red LED) | `92c000ba 54104620 51900808 280c094b` | `F8059BA 4977`  
SoPine RevC | `92c000ba 84004620 50344424 141908cd` | `F9192BA 4967`  
Banana Pi M64 | `92c000ba 84104620 51900800 6020024b`  
**H64**  
Jide Remix Mini | `92c000bb 44004620 51900808 1011028b`  
**H6**  
Pine H64 | `82c00001 0c004708 0141043e 24881dcb` |  | [Tkaiser][854], early developer sample, via hexdump   
Orange Pi Lite 2 | `82c00001 0c004708 0141043e 5474224b` |  | [Tkaiser][854], early developer sample, via hexdump   
Pine H64 | `82c00007 4c004708 01414109 447f210f`  
OrangePi 3 LTS | `82c00007 8c004708 01480944 0c981ed3` |  | [Tkaiser][854], via hexdump   
OrangePi 3 LTS | `82c00007 8c004708 0146c430 1c731e13` |  | [Tkaiser][854], via hexdump   
**H313**  
Tanix TX1 | `32c05c00 cc004808 0145c33d 20952110` |  | apritzel   
X96Q Pro | `32c05000 ac004808 01412010 3c991e8e` |  | [codekipper][856], via hexdump   
**H616**  
OrangePi Zero 2 | `32c05000 fc004808 01454650 507e208f` |  | [ctag][857], via hexdump   
OrangePi Zero 2 | `32c05000 6c004808 0141db4c 489921ce` |  | [Tkaiser][854], via hexdump   
OrangePi Zero 2 | `32c05000 cc004808 01411a64 3c7f228e` |  | apritzel   
X96 Mate | `32c05000 5c004808 01411c74 2c7c1a8e` |  | apritzel   
**H618**  
OrangePi Zero 2W | `33802000 4c004808 01474228 146d2391` |  | [Tkaiser][854], via hexdump   
OrangePi Zero 2W | `33802000 4c004808 01474228 1c921fd1` |  | [Arthur Zheng][858], via hexdump   
OrangePi Zero 3 | `33802000 4c004808 01474788 546e1ed1` |  | apritzel   
OrangePi Zero 3 | `33802000 6c004808 01080100 4c731bd2` |  | ValdikSS   
Transpeed 8K618-T | `33802000 0c004808 0143005d 60861dd1` |  | apritzel   
**H700**  
Anbernic RG35XX-Plus | `33806c00 1c004808 01464541 5c7b2291` |  | acmeplus   
Anbernic RG35XX-H | `33806c00 6c004808 0106c504 48671e12` |  | acmeplus   
Anbernic RG35XX-Plus | `33806c00 6c004808 0106c504 508d1d92` |  | Tokyovigilante   
**R40**  
Banana Pi M2 Ultra | `12c00017 14104700 5190410c 2417088c`  
**V3s**  
Lichee Pi Zero | `12c00000 44104620 5033c810 5c23118d`  
**D1**  
Lichee 86 Panel | `00504093 1448005c 31624201 8b206238` |  | Jookia   
**T113-S3**  
Mango Pi MQ Dual | `93406000 1c004814 0147054c 28461a91` |  | Jookia   
Mango Pi MQ Dual | `93406000 0c004814 01464015 5469190c` |  | Jookia (ordered same time as previous)   
Mango Pi MQ Dual | `93406000 0c004814 01474331 583719d2` |  | Jookia   
Mango Pi MQ-R | `93406000 ac004814 01440821 4c66174b` |  | apritzel   
**T113-S4**  
EmbedSky TQT113 (M4020DC0) | `93407200 4c004814 01088f71 5c4f16d6` |  | Jookia   
**A523**  
Teclast P85T | `02c05200 70404824 75741408 48791e51` |  | apritzel   
Teclast P85T | `02c05200 91c04824 75744c18 38931ed1` |  | wingrime   
**A527**  
Radxa Cubie A5E | `0300ff10 80304824 7590d118 647e2313` |  | apritzel, A527 M00X0000   
Avaota A1 | `0300ff10 70c04824 7590d120 607d1dd4` |  | apritzel, A527 M00X000H   
**T527**  
Avaota A1 | `03005f30 70504824 75901010 50721fd3` |  | apritzel, T527 M00X0DCH   
**H728**  
X96QPro+ | `0300ff00 81c04824 75b09010 1c821cd6` |  | apritzel   
X96QPro+ | `0300ff00 81704824 75b09010 147f1cd6` |  | BroderTuck   
**B288**  
PocketBook Era | `93000000 24004624 7930860c 40140d4b` |  | ValdikSS   
    [![Sticky-note-pin.png][859]][860] _Note:_ The H3 SIDs starting with 02004620 are likely wrong due to a quirk of H3. A silicon bug manifests itself in a way that returns a garbled SID (root key) when reading the values solely via memory access. Accessing the SID _once_ via register access seems to fix this, even for subsequent memory reading - see the [discussion on the mailing list][861]. Corresponding entries in the table above therefore cannot be trusted, and need to be refreshed. A [fix for sunxi-fel][862] is now available.
Newer SoC families no longer seem to follow the above pattern of containing the SoC ID within the first value.  
However, the leading 32 bits still appear to be consistent among the same SoCs with the [potential exception of some bits used for SoC revision or batch number or something similar][863]: 
SoC | ID | SID key   
---|---|---  
A33 (R16) | 0x1667 | `0461872a [...]`  
A64 | 0x1689 | `92c000ba/92c001ba [...]`  
A83T | 0x1673 | `32c00401/32c00403 [...]`  
H2+ | 0x1680 | `02c00042/02c00142/02c00242 [...]`  
H3 | 0x1680 | `02c00081/02c00181 [...]`  
H5 | 0x1718 | `82800001 [...]`  
H6 | 0x1728 | `82c00001/82c00007 [...]`  
H64 | 0x1689 | `92c000bb [...]`  
R40 | 0x1701 | `12c00017 [...]`
