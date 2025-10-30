# Arm64
## Contents
  * [1 ARM64 primer][7947]
    * [1.1 ARM64 cheat sheet][7948]
    * [1.2 ARM(32) comparison][7949]
      * [1.2.1 Instruction set architecture][7950]
    * [1.3 Naming conventions][7951]
    * [1.4 Boot modes][7952]

# ARM64 primer
This is meant as an brief introduction to the ARM64 architecture, mostly to bring people with ARM(32) background up to speed. 
## ARM64 cheat sheet
This table is somewhat simplified to give a quick overview. For more information refer to either Wikipedia, the [ARM Architecture Reference Manual (ARM ARM)][7953] or the sections below. 
ARMv7 name | AArch64/ARMv8 name | remarks   
---|---|---  
monitor mode | EL3 | highest exception level, mostly for firmware   
HYP mode | EL2 | exception level for hypervisors like Xen (or parts of KVM)   
SVC mode | EL1 | the Linux kernel is running in this   
USR mode | EL0 | for unprivileged userland   
## ARM(32) comparison
| AArch32 | AArch64 | remarks   
---|---|---|---  
32-bit General purpose registers | r0 - r14 | w0 - w30 | aliased to lower half of each 64-bit register in AArch64   
64-bit General purpose registers | - | x0 - x30 |   
Program counter | r15 aka. pc | PC | not directly accessible in AArch64   
Zero register | - | x31 / w31 aka. xzr / wzr | in most instructions, except as a base register for address generation   
Stack pointer | r13 | SP | encoded as x31 on address generation   
Procedure call link register | r14 | x30 |   
### Instruction set architecture
Though the mnemonics for the assembly instructions are somewhat similar, AArch32 and AArch64 assembly code are ultimately incompatible due to the different register naming (r0 vs. x0/w0). Also the instruction encoding is completely different. The generic, but rarely used coprocessor interface on ARMv7 is replaced with a dedicated system register access scheme, with the system registers official identified as (mostly architectural) strings by the assembler, but eventually encoded similar to the ARMv7 CP15 interface. While AArch32 features conditional execution for almost every instruction, AArch64 uses those extra bits to address more registers and encode the 32 or 64-bit operand size. So branches and some selected instructions like "conditional set" are the only instructions which can execute conditionally. 
## Naming conventions
There is an updated ARM architecture revision called "ARMv8", which evolved from the ARMv7 architecture. Among other things it introduces a new execution state called "AArch64", which provides a full 64-bit architecture. 
ARMv8 compliant implementations can provide this state or not, also they are free to implement the "AArch32" state, which closely resembles the ARMv7 architecture. So both 32-bit and 64-bit states are optional - but you should of course have at least one ;-). ARM Cortex cores provide both states, while there are implementations from other vendors which do not provide AArch32, for instance. 
The Linux kernel chose to call this new architecture "arm64", the same name got picked up by Debian for their architecture port name. 
The GNU toolchain however elected the official "aarch64" name for the port, so the GCC (cross-)compiler is usually called "aarch64-linux-gnu-gcc". So although the arm64 name is not official, it can be used interchangeably for aarch64. 
## Boot modes
In cores implementing both AArch32 and AArch64, it is IMPLEMENTATION DEFINED in which state they start execution when coming out of reset after power up. ARM Cortex cores feature a (RTL defined) pin, which determines the initial execution state. Usually SoC vendors don't connect this to a real pin on the SoC's package, but tie it to a fixed level during integration. The Allwinner [A64][7954] SoC for instance chose to come up in the AArch32 state, so the BROM code is standard 32-bit ARM code, as are the following parts of the Allwinner firmware stack, including U-Boot. 
It is always possible to "decrease the bitness" when dropping down from a higher privileged execution level, but one can't grow bigger this way. This for instance allows 64-bit firmware to boot 32-bit kernels, 64-bit hypervisors with 32-bit guests or 64-bit kernels with 32-bit userland programs, but not the other way round. 
To switch execution state from AArch32 back to AArch64, one has to either call into a higher execution level (given that this level is using AArch64) or do a warm reset using the RMR register. The Allwinner implementation of ARM Trusted Firmware uses the first technique by providing a SMC call which returns into non-secure world, executing in AArch64 mode at an address passed in register r0. This is used by Allwinner's U-Boot to start 64-bit kernels from an otherwise complete 32-bit U-Boot. 
The [RMR][7955] register allows to trigger a warm reset of the processor core, allowing to change the initial execution state of the core directly after it comes out of the (warm) reset condition. Execution starts at the address in the [RVBAR][7956] register, in the highest implemented exception level, which is EL3 for the ARM Cortex cores used in the Allwinner SoCs. Architecturally this RVBAR register is a read-only system register, but Allwinner chose to have it mirrored as a read/write MMIO mapped register per core at 0x01700CA0 (+ 8 * <corenr>), so one can set a (potentially different) start address for every core. Allwinner's boot0 code uses this technique to switch to 64-bit mode for the first time after boot, the code executed is then ARM Trusted Firmware.
