# FEL/Protocol
< [FEL][18838]
 
## Contents
  * [1 Overview][18841]
  * [2 Examples][18842]
  * [3 Definition of messages][18843]
  * [4 Requests][18844]
  * [5 Memory information][18845]
  * [6 Flashing][18846]

# Overview
The FEL is actually a tiny usb stack implementing a special USB protocol. 
Part of it is implemented in our [tools repository][18847] and can be used as reference code. 
Below is a specification for the protocol based on the official code. You can find it in [uboot][18848] source: ([usb_efex.h][18849]). 
# Examples
Communication always performs according to following routine (→ send, ← receive, => expected length of message): 
**Example 1**. FEL_VERIFY_DEVICE (get device info) 
1\. Send request 
[code] 
    → AWUSBRequest(cmd = AW_USB_WRITE, len = 16)   => len(sizeof(AWUSBRequest) => 32)
    → AWFELStandardRequest(FEL_VERIFY_DEVICE)      => len(sizeof(AWFELStandardRequest) => 16)
    ← AWUSBResponse(csw_status = 0)                => len(sizeof(AWUSBResponse) => 13)
    
[/code]
2\. Read response 
[code] 
    → AWUSBRequest(cmd = AW_USB_READ, len = 32)   => len(sizeof(AWUSBRequest) => 32)
    ← AWFELVerifyDeviceResponse                   => len(sizeof(AWFELVerifyDeviceResponse) => 32)
    ← AWUSBResponse(csw_status = 0)               => len(sizeof(AWUSBResponse) => 13)
    
[/code]
3\. Read status 
[code] 
    → AWUSBRequest(cmd = AW_USB_READ, len = 8)    => len(sizeof(AWUSBRequest) => 32)
    ← AWFELStatusResponse(mark=-1,state=0)        => len(sizeof(AWFELStatusResponse) => 8)
    ← AWUSBResponse(csw_status = 0)               => len(sizeof(AWUSBResponse) => 13)
    
[/code]
**Example 2**. FEL_DOWNLOAD (write data to device memory) 
1\. Send request 
[code] 
    → AWUSBRequest(cmd = AW_USB_WRITE, len = 16)            => len(sizeof(AWUSBRequest) => 32)
    → AWFELMessage(FEL_DOWNLOAD, address, length)   => len(sizeof(AWFELMessage) => 16)
    ← AWUSBResponse(csw_status = 0)                         => len(sizeof(AWUSBResponse) => 13)
    
[/code]
2\. Send data 
[code] 
    → AWUSBRequest(cmd = AW_USB_WRITE, len = <max 65536>)   => len(sizeof(AWUSBRequest) => 32)
    → data                                                  => len(<max 65536>)
    ← AWUSBResponse(csw_status = 0)                         => len(sizeof(AWUSBResponse) => 13)
    
[/code]
3\. Read status 
[code] 
    → AWUSBRequest(cmd = AW_USB_READ, len = 8)    => len(sizeof(AWUSBRequest) => 32)
    ← AWFELStatusResponse(mark=-1,state=0)        => len(sizeof(AWFELStatusResponse) => 8)
    ← AWUSBResponse(csw_status = 0)               => len(sizeof(AWUSBResponse) => 13)
    
[/code]
# Definition of messages
Default value is left after '=>' 
**AWUSBRequest** (size 32) 
[code] 
      string   magic(4)             => "AWUC"
      uint32le tag                  => 0
      uint32le len                  => [size of data written in next transfer]
      uint16le reserved1,           => 0
      uint8    reserved2,           => 0
      uint8    cmd_len,             => 0xC
      uint8    cmd                  => [request type AW_USB_READ (0x11) or AW_USB_WRITE(0x12)]
      uint8    reserved3,           => 0
      uint32le len2                 => len [same value]
      array    reserved4(uint8, 10) => {0}
    
[/code]
**AWUSBResponse** (size 13) 
[code] 
       string   magic(4)           => "AWUS"
       uint32le tag                => 0
       uint32le residue            => 0
       uint8    csw_status         => 0 (if != 0, then request failed)
    
[/code]
**AWFELStatusResponse** (size 8) 
[code] 
       uint16le mark               => 0xFFFF
       uint16le tag                => 0
       uint8    state              => 0 (if !=0, something wrong happened)
       array    reserved(uint8, 3) => {0}
    
[/code]
**AWFELStandardRequest** (size 16) 
[code] 
       uint16le cmd                 => [one of the request e.g. FEL_VERIFY_DEVICE]
       uint16le tag                 => 0 
       array    reserved(uint8, 12) => {0}
    
[/code]
**AWFELMessage** (size 16) 
[code] 
       uint16le cmd,                => [one of the request e.g. FEL_DOWNLOAD, FEL_UPLOAD, FEL_RUN]
       uint16le tag,                => 0 (unused?)
       uint32le address             => 0
       uint32le len                 => 0 (length of read/write, 0 for FEL_RUN)
       uint32le flags               => 0 (used in [FES][18850] mode)
    
[/code]
**AWFELVerifyDeviceResponse** (size 32) 
[code] 
       string   magic(8)           => "AWUSBFEX"
       uint32le board              => Allwinner A31s (0x161000)
       uint32le fw                 => 1
       uint16le mode               => AL_VERIFY_DEV_MODE_FEL (1)
       uint8    data_flag          => 0x44
       uint8    data_length        => 0x8
       uint32le data_start_address => 0x7E00
       array    reserved(uint8, 8) => {0}
    
[/code]
# Requests
Full list of FEL request: 
[code] 
    FEL_VERIFY_DEVICE                       = 0x1 (Read length 32 => AWFELVerifyDeviceResponse)
    FEL_SWITCH_ROLE                         = 0x2
    FEL_IS_READY                            = 0x3 (Read length 8)
    FEL_GET_CMD_SET_VER                     = 0x4
    FEL_DISCONNECT                          = 0x10
    FEL_DOWNLOAD                            = 0x101 (Write data to the device)
    FEL_RUN                                 = 0x102 (Execute code)
    FEL_UPLOAD                              = 0x103 (Read data from the device)
    
[/code]
# Memory information
Some useful info about memory of device in FEL mode. Dumped from A31 firmware image. 
[code] 
     
    # 0x2000 - 0x6000   : INIT_CODE (16384 bytes)
    # 0x7010 - 0x7D00   : FEL_MEMORY (3312 bytes)
    # => 0x7010 - 0x7210: SYS_PARA (512 bytes)
    # => 0x7210 - 0x7220: SYS_PARA_LOG (16 bytes)
    # => 0x7220 - 0x7D00: SYS_INIT_PROC (2784 bytes)
    # 0x7D00 - 0x7E00   : ? (256 bytes)
    # 0x7E00 - ?        : DATA_START_ADDRESS (obtained by FEL_VERIFY_DEVICE)
    # 0x40000000        : DRAM_BASE
    # 0x4A000000        : u-boot.fex
    # 0x4D415244        : SYS_PARA_LOG (second instance?)
    
[/code]
# Flashing
Before proper flash process begins, device must be turned into [FES][18850] mode. Here's exactly way how it's achieved based on [A31][18851] device flash USB communication 
  1. FEL_VERIFY_DEVICE => mode: AL_VERIFY_DEV_MODE_FEL, data_start_address: 0x7E00
  2. FEL_VERIFY_DEVICE (not sure why it's spamming with this again)
  3. FEL_UPLOAD: Get 256 bytes of data (filled 0xCC) from 0x7E00 (data_start_address)
  4. FEL_VERIFY_DEVICE
  5. FEL_DOWNLOAD: Send 256 bytes of data (0x00000000, rest 0xCC) at 0x7E00 (data_start_address)
  6. FEL_VERIFY_DEVICE
  7. FEL_DOWNLOAD: Send 16 bytes of data (filled 0x00) at 0x7210 (SYS_PARA_LOG)
  8. FEL_DOWNLOAD: Send 6496 bytes of data (fes1.fex) at 0x2000 (INIT_CODE)
  9. FEL_RUN: Run code at 0x2000 (fes1.fex). DRAM is initialized. You can manipulate memory on DRAM_BASE address
  10. FEL_UPLOAD: Get 136 bytes of data (DRAM) from 0x7210 (SYS_PARA_LOG). Its DRAM data in same form as in dram_para section in [script][18852]
  11. FEL_DOWNLOAD(12 times because u-boot.fex is 0xBC000 bytes): Send (u-boot.fex) 0x4A000000 in 65536 bytes chunks (last chunk is 49152 bytes and ideally starts at config.fex (also known as: script.bin) data)
  12. FEL_DOWNLOAD: Send 1 byte of data (0x10) at 0x0E offset of u-boot (0x4A00000E). This change uboot_spare_head.boot_data.work_mode to WORK_MODE_USB_PRODUCT (more ([cmd_irq.c][18853]) . **Important** : if you skip this step device will boot normally
  13. FEL_RUN: Run code at 0x4A000000 (u-boot.fex). **Pause** : [LiveSuit][18854] asks user if he would like to do format or upgrade
  14. FEL_VERIFY_DEVICE => mode: AL_VERIFY_DEV_MODE_SRV, you can send [FES][18850] commands now and you cannot send [FEL][18838] commands anymore except FEL_VERIFY_DEVICE

Every [LiveSuit image][18855] contains a compiled LUA plugin (aultools.fex) with a script. The script is loaded by [LiveSuit][18854] and executed when flash process starts. 
Check also legacy informations: [USB-protocol.txt][18856].
