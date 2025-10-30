# PSCI
PSCI is the **Power State Coordination Interface** on ARM-based devices. It defines a standard interface for power management, designed to work across various operating systems and privilege levels. 
See: 
  * [Linux kernel documentation on PSCI][43855]
  * [ARM Infocenter document DEN 0022C][43856]

  

## Contents
  * [1 U-Boot and PSCI][43857]
    * [1.1 Boot modes][43858]
    * [1.2 Mainline kernel][43859]
    * [1.3 3.4.x kernels][43860]

# U-Boot and PSCI
## Boot modes
On architectures that support it (e.g. _sun7i_), recent [mainline U-Boot][43861] allows booting in two different modes: the normal kernel mode, also known as "supervisor" (**SVC**) mode, and a "hypervisor" (**HYP**) mode. Hypervisor is a more privileged mode (designed to even control _SVC_ operation, e.g. for virtualization). 
For these platforms, and with standard U-Boot configuration (_CONFIG_ARMV7_NONSEC_ set, and _CONFIG_ARMV7_BOOT_SEC_DEFAULT_ absent), the hypervisor boot mode will be the default. Note that U-Boot labels it non-secure (**"nonsec"**), in contrast to secure (**"sec"**) operation which corresponds to _SVC_. The boot mode can also be specified by explicitly setting the **bootm_boot_mode** environment variable. (<http://git.denx.de/?p=u-boot.git;a=blob;f=arch/arm/cpu/armv7/Kconfig>) 
The U-Boot PSCI interface is currently only available in "nonsec" (_HYP_) mode, which will cause the bootloader to automatically provide PSCI functions and corresponding device tree nodes. 
see also: 
  * [lwn.net: Supporting KVM on the ARM architecture][43862]
  * [Linux kernel documentation on ARM booting][43863]

## Mainline kernel
With some combinations of **mainline kernel** version and architecture, PSCI may be required for SMP (i.e. to bring up more than one CPU). For example Linux 3.19.x and sun7i/A20 have been observed to show this behaviour. If the Linux kernel doesn't initialize the secondary core(s), you might want to double-check the boot mode and presence of the _/psci_ node in the device tree. 
To verify the actual boot mode, examine the mainline kernel boot messages (`dmesg | grep -E 'psci|started in'`). Search for a line that says 
[code] 
    CPU: All CPU(s) started in <X> mode.
[/code]
where _< X>_ will be _SVC_ for secure, and _HYP_ for non-secure boot mode. 
## 3.4.x kernels
Older kernels might not support non-secure boot mode, and thus may require the **bootm_boot_mode=sec** setting instead.
