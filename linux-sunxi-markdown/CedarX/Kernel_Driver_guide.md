# CedarX/Kernel Driver guide
< [CedarX][11580]
 
## Contents
  * [1 Driver IOCTL guide][11583]
    * [1.1 CORE IOCTL][11584]
    * [1.2 AVS2 IOCTL][11585]
    * [1.3 ENGINE IOCTL][11586]
    * [1.4 Kernel driver init procedure][11587]
    * [1.5 MMAP procedure][11588]

# Driver IOCTL guide
Blob mostly use MMIO Access but CedarX should be gate-on and support PLLs should be confugired before 
## CORE IOCTL
IOCTL_GET_ENV_INFO = 0x101 
copy memory configuration info to userspace struct: 
[code] 
    typedef struct ve_info{
      unsigned int reserved;
      int reserved_size;
      unsigned int io_base;
    } cedar_env_info_t;
    
[/code]
  

[code] 
    c_info.io_base - constain ioremapped  cedarx hw registers offset. 
    Must be used for cedarX hw registers access using mmio
    
[/code]
[code] 
    c_info.reserved - constain cedarx reserved memory offset. 
    Must be used for hw register access using mmio
    
[/code]
  

[code] 
    c_info.reserved_size - constain cedarx reserved memory size  
    
[/code]
  
Example: 
[code] 
    ve_info c_info;
    ioctl(cedar, IOCTL_GET_ENV_INFO, (unsigned long)&c_info);
    
[/code]
  
IOCTL_WAIT_VE = 0x102 
[code] 
    used for cedar IRQ wait, when some operation ends, for example,
    end jpeg decoding process end. don't forget clean IRQ flag after.
    
[/code]
IOCTL_RESET_VE = 0x103 
do reset cedarx engine 
IOCTL_ENABLE_VE = 0x104 
start base clocks for cedarx 
IOCTL_DISABLE_VE = 0x105 
disable base clocks for cedarx 
IOCTL_SET_VE_FREQ = 0x106 
config cedarx frequency, get in argument freqency in Mhz 
for A13 freq are 180 Mhz 
Example 
[code] 
    ioctl(cedar, IOCTL_SET_VE_FREQ, freq);
    
[/code]
## AVS2 IOCTL
IOCTL_CONFIG_AVS2 = 0x200 
IOCTL_GETVALUE_AVS2 = 0x201 
IOCTL_PAUSE_AVS2 = 0x202 
IOCTL_START_AVS2 = 0x203 
IOCTL_RESET_AVS2 = 0x204 
IOCTL_ADJUST_AVS2 = 0x205 
## ENGINE IOCTL
IOCTL_ENGINE_REQ = 0x206 
count references to cedar hardware and more important start some clocks that required for cedar init 
IOCTL_ENGINE_REL = 0x207 
decrement reference count 
IOCTL_ENGINE_CHECK_DELAY = 0x208 
IOCTL_GET_IC_VER = 0x209 
IOCTL_ADJUST_AVS2_ABS = 0x20a 
IOCTL_FLUSH_CACHE = 0x20b do invalidate CPU cache for internal cedar dma 
## Kernel driver init procedure
This required for make CedarX hardware regs in workable state 
[code] 
       ioctl(cedar, IOCTL_ENABLE_VE,0); /*en*/
       ioctl(cedar, IOCTL_ENGINE_REQ,0);/*eng req*/
       ioctl(cedar, IOCTL_SET_VE_FREQ,180); /*set freq in Mhz*/
       ioctl(cedar, IOCTL_RESET_VE,0); /*ve reset*/
    
[/code]
after this step user-space lib must mmap /dev/cedar_dev and get direct access to hardware registers 
## MMAP procedure
You must request ioremaped cedar base address using IOCTL_GET_ENV_INFO that will fill flowing struct 
[code] 
    typedef struct cedarv_env_info{
      unsigned int phymem_start;
      int phymem_total_size;
      unsigned int address_macc;
    } cedar_env_info_t;
    
[/code]
[code] 
    cedarx_env_info c_info;
    
[/code]
  

[code] 
    ioctl(cedar, IOCTL_GET_ENV_INFO, (unsigned long)&c_info);
    
[/code]
Than you must do mmap like that: 
[code] 
    io_base = mmap(0, MAP_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, cedar, c_info.address_macc);
    
[/code]
Same for reserved memory buffer: 
[code] 
    data_base = mmap(NULL, c_info.phymem_total_size, PROT_READ | PROT_WRITE, MAP_SHARED, fd, c_info.phymem_start);
    
[/code]
and after than cedarx version show be checked by reading "VE Revision register" [CEDAR_BASE+0xf2] that constain chip version 
[code] 
    0x1623 for a10, 0x1625 for a13
    
[/code]
