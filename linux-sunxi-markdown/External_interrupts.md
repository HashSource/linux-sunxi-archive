# External interrupts
This is not meant to be comprehensive guide about the external interrupts (EINT0..EINT31), just some notes in getting them to work with the 3.19 stock kernel. 
## Contents
  * [1 Pin support][18479]
    * [1.1 A10][18480]
    * [1.2 A10s][18481]
    * [1.3 A13][18482]
    * [1.4 A20][18483]
    * [1.5 A31][18484]
    * [1.6 A23][18485]
    * [1.7 A33][18486]
    * [1.8 A83t][18487]
    * [1.9 A80][18488]
  * [2 Setup][18489]
    * [2.1 Device Tree Entries][18490]
    * [2.2 A Simple Platform Driver][18491]
    * [2.3 Using the right clock][18492]
  * [3 External Links][18493]

## Pin support
Not all pins are available for handling of edges and interrupts. 
Most up-to-date information (due to errors in official manuals) can be obtained from the mainline Linux kernel sources: ([drivers/pinctrl/sunxi][18494]). 
### A10
External interrupts on PH0..PH21, PI10..PI19 
### A10s
External interrupts on PG0..PG13, PE0..PE1, PB2..PB14, PB19..PB20, PA17 
### A13
External interrupts on PG0..PG4, PG10..PG12, PE0..PE1, PB2..PB4, PB10 
### A20
External interrupts on PH0..PH21, PI10..PI19 
Note: User manual also erroneously states that PC19..PC22 supports external interrupts. 
### A31
External interrupts on PA, PB, PE, PG, PL5..PL8, PM0..PM7 
  

### A23
External interrupts on PB, PG, PL 
### A33
External interrupts on PB, PG, PL 
### A83t
External interrupts on PB, PG, PH 
### A80
External interrupts on PA, PB, PE, PG, PH8..PH18 
## Setup
I have three interrupt inputs that were used on the linux-sunxi-3.4.102 kernel that needed to be ported onto the recent 3.19 kernel. As you may know, the 3.4.102 uses the FEX files, and direct bit-banging to get things configured. The 3.19 kernel uses the device tree (dts) files to describe the hardware. Yes, you can still bang hardware, but I was having issues with interrupt lockup with the 3.4.102 kernel. 
### Device Tree Entries
As my system, the [AW-SOM A20 DIMM][18495], is similar to the cubieboard2, I started with that file and copied it to a new name (cd arch/arm/boot/dts ; cp sun7i-a20-cubieboard2.dts sun7i-a20-prismlx.dts). My board uses EINT16, EINT18 and EINT20 for external interrupts. So, here are the additions made to the dts file: 
` `
`
[code]
     pinctrl@01c20800 {
            ...
            ...
            init_pins_cubieboard2: init_pins@0 {
               allwinner,pins = "PH20";
               allwinner,function = "irq";
               allwinner,drive = <0>;
               allwinner,pull = <1>;
            };
            uart_pins_cubieboard2: uart_pins@0 {
               allwinner,pins = "PH18";
               allwinner,function = "irq";
               allwinner,drive = <0>;
               allwinner,pull = <1>;
            };
            aic_pins_cubieboard2: aic_pins@0 {
               allwinner,pins = "PH16";
               allwinner,function = "irq";
               allwinner,drive = <0>;
               allwinner,pull = <1>;
            };
     };
     
      rebooter {
         compatible = "prismlx-rebooter";
         pinctrl-names = "default";
         pinctrl-0 = <&init_pins_cubieboard2>;
         interrupts-extended = <&pio 20 0>;
         interrupt-names = "restart";
      };
     
      senseb {
         compatible = "prismlx-senseb";
         pinctrl-names = "default";
         pinctrl-0 = <&uart_pins_cubieboard2>;
         interrupts-extended = <&pio 18 0>;
         interrupt-names = "uarts";
      };
     
      sensea {
         compatible = "prismlx-sensea";
         pinctrl-names = "default";
         pinctrl-0 = <&aic_pins_cubieboard2>;
         interrupts-extended = <&pio 16 0>;
         interrupt-names = "alarm-monitor";
      };
    
[/code]
```
`` The above describes my board configuration for the interrupts. Each interrupt input pin is listed in the pinctrl list and is linked to the platform driver code via the **compatible** entry. Thus, if your platform driver simply asks for 'platform_get_irq(pdev, 0)', the irq returned would be that which matched the driver .compatible of_device_id with that of the device tree. It appears that you could use platform_get_irq_byname() to get several interrupts into a single platform driver? 
~~Note, the entry for interrupts-extended in the rebooter description has**< &pio 20 0>**? The **20** is the external interrupt number (EINT20) and the **0** is irrelevant, this value has no affect on the interrupt line sensing. The PIO_INT_CFG register trigger value is set by the IRQF_<flag> when you use request_irq() in your driver (e.g. IRQF_TRIGGER_HIGH sets a value of 0x02 in the PIO_INT_CFGx register for that external pin).~~ _This doesn't seem to be correct anymore since the new 4.x kernel_ [hp197][18496] ([talk][18497]) 
### A Simple Platform Driver
This is a simple driver which requests the 'rebooter' IRQ (EINT20). ` `
`
[code]
    #include <linux/interrupt.h>
    #include <linux/of.h>
    #include <linux/of_platform.h>
    #include <linux/of_gpio.h>
    #include <linux/sched.h>
    
    #include <linux/fs.h>
    #include <linux/cdev.h>
    #include <linux/module.h>
    
    static int	irq = -1;
    
    /* respond to the INIT button pressed. */
    
    
    static irqreturn_t irqHandlerInit (int irq, void *dev_id)
    {
    	printk (KERN_NOTICE "EINT20 interrupt fired\n");
    	return IRQ_HANDLED;
    }
    
    static int __init rebooter_probe(struct platform_device *pdev)
    {
    	irq = platform_get_irq_byname (pdev, "restart");
    	if (request_irq(irq, &irqHandlerInit, IRQF_TRIGGER_FALLING, "rebooter_irq", NULL)) {
    		printk(KERN_ERR "rebooter-irq: cannot register IRQ %d\n", irq);
    		return -EIO;
    	}
    	return 0;
    }
    
    static int rebooter_remove(struct platform_device *pdev)
    {
    	free_irq (irq, NULL);
    	return 0;
    }
    
    #if defined(CONFIG_OF)
    static const struct of_device_id rebooter_dt_ids[] = {
    	{ .compatible = "prismlx-rebooter" },
    	{ /* sentinel */ }
    };
    MODULE_DEVICE_TABLE(of, rebooter_dt_ids);
    #endif
    
    static struct platform_driver rebooter_driver = {
    	.remove		= rebooter_remove,
    	.driver		= {
    		.name	= "prismlx-rebooter",
    		.of_match_table	= of_match_ptr(rebooter_dt_ids),
    	},
    };
    
    module_platform_driver_probe(rebooter_driver, rebooter_probe);
    
    MODULE_LICENSE("GPL");
    MODULE_AUTHOR("Tom Walsh");
    MODULE_DESCRIPTION("PrismLX Init Switch Monitor");
    
[/code]
```
`` What you should note is the IRQF_TRIGGER_FALLING of request_irq. It is in the call to request_irq() that the active level / edge of the interrupt request (input pin) is specified. 
  
Doing an ismod of the driver should give you something like this in /proc/interrupts: ` `
`
[code]
    root@prismLX:~# cat /proc/interrupts 
              CPU0       CPU1       
    17:          0          0       GIC  29  arch_timer
    18:      32144      16029       GIC  30  arch_timer
    21:          0          0       GIC  54  sun4i_timer0
    22:          0          0       GIC 113  sun5i_timer0
    26:       6549          0       GIC  64  sunxi-mmc
    27:          0          0       GIC  71  ehci_hcd:usb1
    28:          0          0       GIC  96  ohci_hcd:usb3
    29:          0          0       GIC  88  1c18000.sata
    30:          2          0       GIC  72  ehci_hcd:usb2
    31:        110          0       GIC  97  ohci_hcd:usb4
    34:          0          0       GIC  56  1c20d00.rtc
    40:        102          0       GIC  33  serial
    41:         96          0       GIC  39  mv64xxx_i2c
    42:          0          0       GIC  40  mv64xxx_i2c
    43:        349          0       GIC 117  eth0
    68:          0          0         -  20  rebooter_irq
    80:          0          0  interrupt-controller   0  axp20x_irq_chip
    IPI0:        0          0  CPU wakeup interrupts
    IPI1:        0          0  Timer broadcast interrupts
    IPI2:       1548       1619  Rescheduling interrupts
    IPI3:        0          0  Function call interrupts
    IPI4:        2          6  Single function call interrupts
    IPI5:        0          0  CPU stop interrupts
    IPI6:        0          0  IRQ work interrupts
    IPI7:        0          0  completion interrupts
    Err:         0
    
[/code]
```
`` Of course, if you tap on the EINT20 pin with a wire to GROUND, you should see the 'rebooter_irq' count change. 
### Using the right clock
On the 3.19 kernel, the PIO interrupt sampling clock is set to the default value of 32KHz. This is probably "good enough" if you were to only have some push buttons tied to those external interrupts, but, not good enought if you hang a serial UART on one of those interrupt lines. The sampling rate of 32KHz would have you missing some of the interrupts as data comes in, so, you better have a pretty deep fifo in that UART... 
This patch made by Maxime Ripard will allow you to change the PIO Interrupt Debounce clock from 32KHz to 24MHz (tested on kernel 4.1rc1, Hans' branch sunxi-wip): 
` `
`
[code]
    diff --git a/drivers/pinctrl/sunxi/pinctrl-sunxi.c b/drivers/pinctrl/sunxi/pinctrl-sunxi.c
    index f09573e13203..a02e0a457b11 100644
    --- a/drivers/pinctrl/sunxi/pinctrl-sunxi.c
    +++ b/drivers/pinctrl/sunxi/pinctrl-sunxi.c
    @@ -1005,6 +1005,9 @@ int sunxi_pinctrl_init(struct platform_device *pdev,
     		writel(0xffffffff,
     			pctl->membase + sunxi_irq_status_reg_from_bank(i));
     
    +		/* Set Interrupt clock to 24MHz */
    +		writel(1, pctl->membase + sunxi_irq_debounce_reg_from_bank(i));
    +
     		irq_set_chained_handler_and_data(pctl->irq[i],
     						 sunxi_pinctrl_irq_handler,
     						 pctl);
    diff --git a/drivers/pinctrl/sunxi/pinctrl-sunxi.h b/drivers/pinctrl/sunxi/pinctrl-sunxi.h
    index e248e81a0f9e..502a5c678380 100644
    --- a/drivers/pinctrl/sunxi/pinctrl-sunxi.h
    +++ b/drivers/pinctrl/sunxi/pinctrl-sunxi.h
    @@ -68,6 +68,7 @@
     #define IRQ_STATUS_IRQ_PER_REG		32
     #define IRQ_STATUS_IRQ_BITS		1
     #define IRQ_STATUS_IRQ_MASK		((1 << IRQ_STATUS_IRQ_BITS) - 1)
    +#define IRQ_DEBOUNCE_REG	0x218
     
     #define IRQ_MEM_SIZE		0x20
     
    @@ -283,6 +284,11 @@ static inline u32 sunxi_irq_status_offset(u16 irq)
     	return irq_num * IRQ_STATUS_IRQ_BITS;
     }
     
    +static inline u32 sunxi_irq_debounce_reg_from_bank(u8 bank)
    +{
    +	return IRQ_DEBOUNCE_REG + bank * IRQ_MEM_SIZE;
    +}
    +
     int sunxi_pinctrl_init(struct platform_device *pdev,
     		       const struct sunxi_pinctrl_desc *desc);
    
[/code]
```
``
Starting from [4.10 kernel][18498] there is a `input-debounce` device tree property that allows configuring the debounce register. [Armbian forum user Dennboy][18499] did some investigation and found out that the current mainline code always sets the prescaler. That means that you never can reach full 24Mhz sampling rate of the irq pins. There is a patch in the same thread or you can also use [devmem2][18500] command to enable 24Mhz clock from userspace. 
` `
`
[code]
    # Allwinner A20
    # PIO_BASE = 0x01C20800
    # PIO_INT_DEB = 0x218
    sudo ./devmem2 0x1C20A18 w 0x1
    
[/code]
```
``
## External Links
  * [Simple tutorial by patwood][18501]
