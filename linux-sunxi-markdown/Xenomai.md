# Xenomai
## ipipe on A20
Cubietruck works with ipipe on mainline kernel 3.18.12. 
download kernel source from kernel.org 3.18.12 download ipipe-core-patch for arm 3.18.12 
unpack kernel 
[code] 
    patch -p1 < ../ipipe-core-3.18.12-arm-1.patch
    
[/code]
You need also to patch these files 
[code] 
    --- a/arch/arm/Kconfig     2015-05-12 09:05:30.566224133 +0200
    +++ b/arch/arm/Kconfig     2015-05-06 14:47:39.464380270 +0200
    @@ -1018,7 +1018,7 @@ config IPIPE_ARM_KUSER_TSC
            bool
            select GENERIC_TIME_VSYSCALL
            select IPIPE_HAVE_HOSTRT if IPIPE
    -       default y if ARCH_AT91 || ARM_TIMER_SP804 || ARCH_MXC || ARCH_OMAP || PLAT_PXA || PLAT_S3C24XX || ARCH_SA1100
    +       default y if ARCH_AT91 || ARM_TIMER_SP804 || ARCH_MXC || ARCH_OMAP || PLAT_PXA || PLAT_S3C24XX || ARCH_SA1100 || ARCH_SUNXI
     endif
    
[/code]
[code] 
    --- a/arch/arm/mach-sunxi/Kconfig  2015-04-20 21:48:02.000000000 +0200
    +++ b/arch/arm/mach-sunxi/Kconfig  2015-05-06 14:47:45.554380273 +0200
    @@ -33,6 +33,7 @@ config MACH_SUN7I
            select ARM_PSCI
            select HAVE_ARM_ARCH_TIMER
            select SUN5I_HSTIMER
    +       select IPIPE_ARM_KUSER_TSC if IPIPE
    
    config MACH_SUN8I
            bool "Allwinner A23 (sun8i) SoCs support"
    
[/code]
[code] 
    --- a/drivers/irqchip/irq-sunxi-nmi.c      2015-04-20 21:48:02.000000000 +0200
    +++ b/drivers/irqchip/irq-sunxi-nmi.c      2015-05-07 10:09:31.639805322 +0200
    @@ -77,8 +77,10 @@ static int sunxi_sc_nmi_set_type(struct
            u32 ctrl_off = ct->regs.type;
            unsigned int src_type;
            unsigned int i;
    +       unsigned long flags;
    
    -       irq_gc_lock(gc);
    +       /* Disable interrupt */
    +       flags = irq_gc_lock(gc);
    
            switch (flow_type & IRQF_TRIGGER_MASK) {
            case IRQ_TYPE_EDGE_FALLING:
    @@ -95,7 +97,7 @@ static int sunxi_sc_nmi_set_type(struct
                    src_type = SUNXI_SRC_TYPE_LEVEL_LOW;
                    break;
            default:
    -               irq_gc_unlock(gc);
    +               irq_gc_unlock(gc, flags);
                    pr_err("%s: Cannot assign multiple trigger modes to IRQ %d.\n",
                            __func__, data->irq);
                    return -EBADR;
    @@ -113,7 +115,7 @@ static int sunxi_sc_nmi_set_type(struct
            src_type_reg |= src_type;
            sunxi_sc_nmi_write(gc, ctrl_off, src_type_reg);
    
    -       irq_gc_unlock(gc);
    +       irq_gc_unlock(gc, flags);
    
            return IRQ_SET_MASK_OK;
     }
    
[/code]
  

[code] 
    make defconfig cubietruck
    make menuconfig
    
[/code]
enable ipipe patches 
compile kernel 
then you can try to boot your kernel If that works add xenomai patches to kernel source
