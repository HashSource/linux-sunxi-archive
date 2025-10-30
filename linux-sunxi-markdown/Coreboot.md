# Coreboot
This page is to be considered DUSTY due to CONSTRUCTION. 
Arguably it is even obsolete: Seems Coreboot dropped support for Cubieboard since release 4.11: [https://doc.coreboot.org/releases/coreboot-4.11-relnotes.html?highlight=cubieboard#new-devices][13267]
It is possible to bring up a limited number of board (currently, only cubieboard) using coreboot with a uboot payload. Please see [coreboot instructions][13268] for more details. 
## Hacks'n'tips
### Using coreboot for NAND access
coreboot (mrnuke's github branch) operates from MMC. It can load any uboot elf file included as the coreboot payload. This means that besides the regulat sunxi uboot, it can also load the non-SPL part of the lichee uboot. 
From a checkout of sunxi/uboot do: 
[code] 
    $ git checkout origin/lichee-dev -b lichee
    $ make CROSS_COMPILE=arm-linux-gnu- sun4i
    $ file u-boot                                                                                                                              
    u-boot: ELF 32-bit LSB shared object, ARM, EABI5 version 1 (SYSV), statically linked, not stripped
    
[/code]
Now take the resulting 'u-boot' file, and use it as the coreboot payload. Install as usual and monitor the serial console 
[code] 
    coreboot-4.0-5661-ge282828-nuclearis Wed Mar 12 01:02:50 CDT 2014 starting...
    No valid CBFS master header at 7efbfe30
    Calling sunxi to init out MMC
    In sunxi MMC init. FUCK YEAH!!!
    Calling generic MMC init
    [mmc] mmc_init: 0, time 0
    Copying coreboot.rom to RAM
    MMC bread, no butter
    default_media->open()
    default_media->map(0x10, 0x20)
    default_media->close()
    default_media->open()
    default_media->map(0x5fd8, 0x20)
    default_media->map(0x5fc0, 0x6524)
    default_media->close()
    CBFS: loading stage fallback/romstage @ 0x41000000 (25808 bytes), entry @ 0x41000000
    
    
    coreboot-4.0-5661-ge282828-nuclearis Wed Mar 12 01:02:50 CDT 2014 starting...
    VDD CPU (DCDC2): 1400mv
    VDD DLL (DCDC3): 1250mv
    AVCC    (LDO2) : 3000mv
    CSI1-IO (LDO4) : 2800mv
    (LDO3) : 2800mv
    CPU: 1008 MHz, AXI 336 Mhz, AHB: 168 MHz APB0: 84 MHz
    Already have CBFS master header at 7efbfe30
    default_media->open()
    default_media->map(0x10, 0x20)
    default_media->close()
    default_media->open()
    default_media->map(0x5fd8, 0x20)
    default_media->map(0xc518, 0x20)
    default_media->map(0xc500, 0x6a3c)
    default_media->close()
    CBFS: loading stage fallback/coreboot_ram @ 0x40000000 (89184 bytes), entry @ 0x40000000
    entry is 0x40000000, leaving romstage.
    coreboot-4.0-5661-ge282828-nuclearis Wed Mar 12 01:02:50 CDT 2014 booting...
    CBMEM: root @ 7ffff000 254 entries.
    BS: BS_PRE_DEVICE times (us): entry 0 run 0 exit 0
    BS: BS_DEV_INIT_CHIPS times (us): entry 0 run 0 exit 0
    Enumerating buses...
    Show all devs...Before device enumeration.
    Root Device: enabled 1
    CPU_CLUSTER: 0: enabled 1
    I2C: 00:34: enabled 1
    Compare with tree...
    Root Device: enabled 1
     CPU_CLUSTER: 0: enabled 1
     I2C: 00:34: enabled 1
    scan_static_bus for Root Device
    CPU_CLUSTER: 0 enabled
    smbus: Root Device[0]->I2C: 00:34 enabled
    scan_static_bus for Root Device done
    done
    BS: BS_DEV_ENUMERATE times (us): entry 0 run 0 exit 0
    Allocating resources...
    Reading resources...
    Root Device read_resources bus 0 link: 0
    I2C: 00:34 missing read_resources
    Root Device read_resources bus 0 link: 0 done
    Done reading resources.
    Show resources in subtree (Root Device)...After reading.
     Root Device child on link 0 CPU_CLUSTER: 0
      CPU_CLUSTER: 0
      I2C: 00:34
    Setting resources...
    Root Device assign_resources, bus 0 link: 0
    Root Device assign_resources, bus 0 link: 0
    Done setting resources.
    Show resources in subtree (Root Device)...After assigning values.
     Root Device child on link 0 CPU_CLUSTER: 0
      CPU_CLUSTER: 0
      I2C: 00:34
    Done allocating resources.
    BS: BS_DEV_RESOURCES times (us): entry 0 run 0 exit 0
    Enabling resources...
    done.
    BS: BS_DEV_ENABLE times (us): entry 0 run 0 exit 0
    Initializing devices...
    Root Device init
    Root Device init 3221171766 usecs
    CPU_CLUSTER: 0 init
    CPU_CLUSTER: 0 init 4294967116 usecs
    Devices initialized
    Show all devs...After init.
    Root Device: enabled 1
    CPU_CLUSTER: 0: enabled 1
    I2C: 00:34: enabled 1
    BS: BS_DEV_INIT times (us): entry 0 run 0 exit 0
    Finalize devices...
    Devices finalized
    BS: BS_POST_DEVICE times (us): entry 0 run 0 exit 0
    BS: BS_OS_RESUME_CHECK times (us): entry 0 run 0 exit 0
    Writing coreboot table at 0x7fffd000
    rom_table_end = 0x7fffd000
    ... aligned to 0x80000000
     0. 0000000040000000-000000007fffcfff: RAM
     1. 000000007fffd000-000000007fffffff: CONFIGURATION TABLES
    Wrote coreboot table at: 7fffd000, 0x1b8 bytes, checksum 7fb6
    coreboot table: 464 bytes.
    CBMEM ROOT  0. 7ffff000 00001000
    COREBOOT    1. 7fffd000 00002000
    BS: BS_WRITE_TABLES times (us): entry 0 run 0 exit 0
    Already have CBFS master header at 7efbfe30
    default_media->open()
    default_media->map(0x10, 0x20)
    default_media->close()
    default_media->open()
    default_media->map(0x5fd8, 0x20)
    default_media->map(0xc518, 0x20)
    default_media->map(0x12f58, 0x20)
    default_media->map(0x12f40, 0x19e0a)
    default_media->close()
    CBFS: located payload @ 7efd2d98, 105938 bytes.
    Loading segment from rom address 0x7efd2d98
      code (compression=1)
      New segment dstaddr 0x4a000000 memsize 0x3fe6c srcaddr 0x7efd2dd0 filesize 0x19d9a
      (cleaned up) New segment addr 0x4a000000 size 0x3fe6c offset 0x7efd2dd0 filesize 0x19d9a
    Loading segment from rom address 0x7efd2db4
      Entry Point 0x4a000000
    Bounce Buffer at 7ffd1000, 178368 bytes
    Loading Segment: addr: 0x000000004a000000 memsz: 0x000000000003fe6c filesz: 0x0000000000019d9a
    lb: [0x0000000040000000, 0x0000000040015c60)
    Post relocation: addr: 0x000000004a000000 memsz: 0x000000000003fe6c filesz: 0x0000000000019d9a
    using LZMA
    [ 0x4a000000, 4a03fe6c, 0x4a03fe6c) <- 7efd2dd0
    dest 4a000000, end 4a03fe6c, bouncebuffer 7ffd1000
    Loaded segments
    BS: BS_PAYLOAD_LOAD times (us): entry 0 run 0 exit 0
    Jumping to boot code at 4a000000
    CPU0: stack: 00006000 - 00008000, lowest used address 00007c04, stack used: 1020 bytes
    entry    = 4a000000
    
    
    U-Boot 2011.09-rc1-00000-gbaa70c6 (Mar 12 2014 - 00:57:18) Allwinner Technology 
    
    CPU:   SUNXI Family
    Board: A10-EVB
    DRAM:  1 GiB
    boot type: 2
    NAND:  3896 MiB
    MMC:   SUNXI SD/MMC: 0
    *** Warning - bad CRC, using default environment
    
    In:    serial
    Out:   serial
    Err:   serial
    --------fastboot partitions--------
    -total partitions:0-
    -name-        -start-       -size-      
    -----------------------------------
    no misc partition is found
    Hit any key to stop autoboot:  0 
    sun4i#
    
[/code]
TADA! NAND access without boot0/boot1. What happens is that coreboot boots from the MMC card, as usual, loads lichee uboot, which can now access the MMC. My NAND partition was previously wiped, hence the warning about "no misc partition is found".
