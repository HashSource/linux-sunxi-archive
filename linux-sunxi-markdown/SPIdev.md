# SPIdev
The **SPI** bus (or **Serial Peripheral Interface bus**) is a synchronous serial data link originally created by motorola.  
For more information about SPI please refer to this link: <http://en.wikipedia.org/wiki/Serial_Peripheral_Interface>  
  
In the linux kernel the SPI works only in master mode.  
There is a way of using the spi kernel driver to work as a device in the userspace. It's called SPIdev.  
  

## Contents
  * [1 Configuring your kernel][48378]
  * [2 More information][48379]
  * [3 Configuring your FEX][48380]
  * [4 Configuring your device-tree (mainline)][48381]
    * [4.1 Example for pcDuino3][48382]
    * [4.2 Example for A10s Olinuxino Micro UEXT connector][48383]
  * [5 (For newer kernel) binding the spidev driver in sysfs to create /dev/spidevX.X][48384]
  * [6 Using the SPI bus][48385]
    * [6.1 In the user space][48386]
    * [6.2 In the kernel space][48387]
  * [7 SPI NOR Flash][48388]
  * [8 Bugs/Caveats][48389]
    * [8.1 HIGH on SCK line right before transfer][48390]
    * [8.2 LOW on SCK line on transfer start when using SPI-Mode3][48391]

# Configuring your kernel
For using it you will have to enable this options in your defconfig or manually in your kernel:  
  
CONFIG_SPI_SUN4I=y  
CONFIG_SPI_SUN6I=y  
CONFIG_SPI=y  
CONFIG_SPI_MASTER=y  
CONFIG_EXPERIMENTAL=y  
CONFIG_SPI_SPIDEV=y  
  

# More information
For more information about using SPIdev in the userspace please refer to (Documentation/spi/): <http://lxr.free-electrons.com/source/Documentation/spi/>  
  
You will find there:  

  * spidev (contains the documentantion about the spidev)  

  
In _tools/spi_ (<http://lxr.free-electrons.com/source/tools/spi/>) you will find: 
  * spidev_fdx.c (contains a simple example in C of a full duplex communication)
  * spidev_test.c (contains a simple example in C of a half duplex communication)

# Configuring your FEX
It is important to configure your .fex file to be able to do so:  
  
(if you are using spi0)  

[code] 
    [spi0_para]
    spi_used = 1
    spi_cs_bitmap = 1
    spi_cs0 = port:PI10<2><default><default><default>
    spi_sclk = port:PI11<2><default><default><default>
    spi_mosi = port:PI12<2><default><default><default>
    spi_miso = port:PI13<2><default><default><default>
    
[/code]
(here you will specify the number of spi devices your card will have, if you plan only to use the spidev just put 1): 
[code] 
    [spi_devices]
    spi_dev_num = 1
    
[/code]
(here you will have to put in the modalias "spidev") 
[code] 
    [spi_board0]
    modalias = "spidev"
    max_speed_hz = 12000000
    bus_num = 0
    chip_select = 0
    mode = 0
    full_duplex = 1
    manual_cs = 0
    
[/code]
For more information about editing the fex file: <http://linux-sunxi.org/Fex_Guide>  

# Configuring your device-tree (mainline)
For the most boards SPI is disabled by default. To enable it you have to modify the [device-tree][48392] of your board. 
### Example for pcDuino3
As an example, we will enable SPI0 for this board.   
We will have to modify _arch/arm/boot/dts/sun7i-a20-pcduino3.dts_.  

First of all, for aesthetic reasons, we want spi0 to appear as _/sys/class/spi_master/spi0_ and not as _ls /sys/class/spi_master/spi32766_ , therefore we add _spi0 = &spi0;_ in the aliases section.  

Second - we enable spi0 by adding _+ &spi0_ section. In example below spidev is also enabled, so that /dev/spidev0.0 could be accessible from the userspace (please note, that you must also enable CONFIG_SPI_SPIDEV in kernel configuration, and bind the spidev driver in sysfs, see below). If you don't need that functionality, you can omit _spidev@0x00_ section. 
For more examples, see the device tree overlays in [Armbian's sunxi-DT-overlays][48393] repository. 
[code] 
    --- a/arch/arm/boot/dts/sun7i-a20-pcduino3.dts
    +++ b/arch/arm/boot/dts/sun7i-a20-pcduino3.dts
    @@ -56,6 +56,7 @@
    
            aliases {
                    serial0 = &uart0;
    +               spi0 = &spi0;
            };
    
            chosen {
    @@ -230,6 +231,19 @@
            regulator-name = "avcc";
     };
    
    +&spi0 {
    +       pinctrl-names = "default";
    +       pinctrl-0 = <&spi0_pins_a>,
    +                   <&spi0_cs0_pins_a>;
    +       status = "okay";
    +
    +       spidev@0x00 {
    +               compatible = "spidev";
    +               spi-max-frequency = <1200000>;
    +               reg = <0>;
    +       };
    +};
    +
     &reg_usb1_vbus {
            status = "okay";
     };
    
[/code]
### Example for A10s Olinuxino Micro UEXT connector
[code] 
    --- a/arch/arm/boot/dts/sun5i-a10s.dtsi
    +++ b/arch/arm/boot/dts/sun5i-a10s.dtsi
    @@ -154,6 +154,20 @@
                            clocks = <&apb1_gates 18>;
                            status = "disabled";
                    };
    +
    +               spi2: spi@01c17000 {
    +                       compatible = "allwinner,sun4i-a10-spi";
    +                       reg = <0x01c17000 0x1000>;
    +                       interrupts = <12>;
    +                       clocks = <&ahb_gates 22>, <&spi2_clk>;
    +                       clock-names = "ahb", "mod";
    +                       dmas = <&dma SUN4I_DMA_DEDICATED 29>,
    +                              <&dma SUN4I_DMA_DEDICATED 28>;
    +                       dma-names = "rx", "tx";
    +                       status = "disabled";
    +                       #address-cells = <1>;
    +                       #size-cells = <0>;
    +               };
            };
     };
     
    @@ -198,4 +212,18 @@
                    allwinner,drive = <SUN4I_PINCTRL_30_MA>;
                    allwinner,pull = <SUN4I_PINCTRL_NO_PULL>;
            };
    +
    +       spi2_pins_a: spi2@0 {
    +               allwinner,pins = "PB11", "PB12", "PB13", "PB14";
    +               allwinner,function = "spi2";
    +               allwinner,drive = <SUN4I_PINCTRL_10_MA>;
    +               allwinner,pull = <SUN4I_PINCTRL_NO_PULL>;
    +       };
    +
    +       spi2_pins_b: spi2@1 {
    +               allwinner,pins = "PE00", "PE01", "PE02", "PE03";
    +               allwinner,function = "spi2";
    +               allwinner,drive = <SUN4I_PINCTRL_10_MA>;
    +               allwinner,pull = <SUN4I_PINCTRL_NO_PULL>;
    +       };
     };
    
    
    --- a/arch/arm/boot/dts/sun5i-a10s-olinuxino-micro.dts
    +++ b/arch/arm/boot/dts/sun5i-a10s-olinuxino-micro.dts
    @@ -182,6 +188,12 @@
            status = "okay";
     };
     
    +&spi2 {
    +       pinctrl-names = "default";
    +       pinctrl-0 = <&spi2_pins_a>;
    +       status = "okay";
    +};
    +
     &ohci0 {
            status = "okay";
     };
    
    --- a/arch/arm/boot/dts/sun5i-a10s-olinuxino-micro.dts
    +++ b/arch/arm/boot/dts/sun5i-a10s-olinuxino-micro.dts
    @@ -192,6 +192,15 @@
            pinctrl-names = "default";
            pinctrl-0 = <&spi2_pins_a>;
            status = "okay";
    +       spi2_0 {
    +               #address-cells = <1>;
    +               #size-cells = <0>;
    +
    +               compatible = "spidev";
    +
    +               reg = <0>;
    +               spi-max-frequency = <50000000>;
    +       };
     };
     
     &ohci0 {
    
[/code]
# (For newer kernel) binding the spidev driver in sysfs to create /dev/spidevX.X
According to Documentation/spi/spidev.rst in Linux source tree, _[i]t used to be supported to define an SPI device using the "spidev" name. For example, as .modalias = "spidev" or compatible = "spidev". But this is no longer supported by the Linux kernel and instead a real SPI device name as listed in one of the tables must be used._
As a result, in a newer kernel, if the "compatible" field in device tree does not contain a real SPI device which belongs to some specific device tables, the character device /dev/spidevX.X will not be created automatically. In this case, it is necessary to bind the spidev driver by running the following 2 commands[[1]][48394] (replace X.X with the SPI bus number and CS pin ID of you board): 
[code] 
    echo spidev > /sys/bus/spi/devices/spiX.X/driver_override
    echo spiX.X > /sys/bus/spi/drivers/spidev/bind
    
[/code]
After that, /dev/spidevX.X will be created, which can be accessed by user-space tools like _flashrom_. 
# Using the SPI bus
## In the user space
Once you will have this set you can boot your sunxi device and you will have in your dev in /dev/spidev**n**.0  

**Transfer size is limited to 64 bytes on sun4i and 128 bytes on sun6i**. You have to loop over longer messages in your code. Some SPI devices may require that you prefix each message fragment with a header, other may not. YMMV. Look up transfer diagrams in device datasheet.   
Known problems: Using the spidev_test.c example you will receive [spi]: drivers/spi/spi_sunxi.c(L1025) cpu tx data time out!  
Using the spidev_fdx.c method it works like a charm! :)  
  
I've made a user friendlier library (C functions) to comunicate using SPIdev:  
(Note, this library supose the read and write address to be 2 bytes) 
[code] 
    /*
        spidevlib.c - A user-space program to comunicate using spidev.
    				Gustavo Zamboni
    */
    #include <stdint.h>
    #include <unistd.h>
    #include <stdio.h>
    #include <stdlib.h>
    #include <getopt.h>
    #include <fcntl.h>
    #include <sys/ioctl.h>
    #include <linux/types.h>
    #include <linux/spi/spidev.h>
    
    char buf[10];
    char buf2[10];
    extern int com_serial;
    extern int failcount;
    
    struct spi_ioc_transfer xfer[2];
    
    
    //////////
    // Init SPIdev
    //////////
    int spi_init(char filename[40])
    	{
        	int file;
    	__u8	mode, lsb, bits;
    	__u32 speed=2500000;
    
        	if ((file = open(filename,O_RDWR)) < 0)
    		{
            	printf("Failed to open the bus.");
            	/* ERROR HANDLING; you can check errno to see what went wrong */
    		com_serial=0;
            	exit(1);
        		}
    
    		///////////////
    		// Verifications
    		///////////////
    		//possible modes: mode |= SPI_LOOP; mode |= SPI_CPHA; mode |= SPI_CPOL; mode |= SPI_LSB_FIRST; mode |= SPI_CS_HIGH; mode |= SPI_3WIRE; mode |= SPI_NO_CS; mode |= SPI_READY;
    		//multiple possibilities using |
    		/*
    			if (ioctl(file, SPI_IOC_WR_MODE, &mode)<0)	{
    				perror("can't set spi mode");
    				return;
    				}
    		*/
    
    			if (ioctl(file, SPI_IOC_RD_MODE, &mode) < 0)
    				{
    				perror("SPI rd_mode");
    				return;
    				}
    			if (ioctl(file, SPI_IOC_RD_LSB_FIRST, &lsb) < 0)
    				{
    				perror("SPI rd_lsb_fist");
    				return;
    				}
    		//sunxi supports only 8 bits
    		/*
    			if (ioctl(file, SPI_IOC_WR_BITS_PER_WORD, (__u8[1]){8})<0)	
    				{
    				perror("can't set bits per word");
    				return;
    				}
    		*/
    			if (ioctl(file, SPI_IOC_RD_BITS_PER_WORD, &bits) < 0) 
    				{
    				perror("SPI bits_per_word");
    				return;
    				}
    		/*
    			if (ioctl(file, SPI_IOC_WR_MAX_SPEED_HZ, &speed)<0)	
    				{
    				perror("can't set max speed hz");
    				return;
    				}
    		*/
    			if (ioctl(file, SPI_IOC_RD_MAX_SPEED_HZ, &speed) < 0) 
    				{
    				perror("SPI max_speed_hz");
    				return;
    				}
    	
    
    	printf("%s: spi mode %d, %d bits %sper word, %d Hz max\n",filename, mode, bits, lsb ? "(lsb first) " : "", speed);
    
    	//xfer[0].tx_buf = (unsigned long)buf;
    	xfer[0].len = 3; /* Length of  command to write*/
    	xfer[0].cs_change = 0; /* Keep CS activated */
    	xfer[0].delay_usecs = 0, //delay in us
    	xfer[0].speed_hz = 2500000, //speed
    	xfer[0].bits_per_word = 8, // bites per word 8
    
    	//xfer[1].rx_buf = (unsigned long) buf2;
    	xfer[1].len = 4; /* Length of Data to read */
    	xfer[1].cs_change = 0; /* Keep CS activated */
    	xfer[0].delay_usecs = 0;
    	xfer[0].speed_hz = 2500000;
    	xfer[0].bits_per_word = 8;
    
    	return file;
    	}
    
    
    
    //////////
    // Read n bytes from the 2 bytes add1 add2 address
    //////////
    
    char * spi_read(int add1,int add2,int nbytes,int file)
    	{
    	int status;
    
    	memset(buf, 0, sizeof buf);
    	memset(buf2, 0, sizeof buf2);
    	buf[0] = 0x01;
    	buf[1] = add1;
    	buf[2] = add2;
    	xfer[0].tx_buf = (unsigned long)buf;
    	xfer[0].len = 3; /* Length of  command to write*/
    	xfer[1].rx_buf = (unsigned long) buf2;
    	xfer[1].len = nbytes; /* Length of Data to read */
    	status = ioctl(file, SPI_IOC_MESSAGE(2), xfer);
    	if (status < 0)
    		{
    		perror("SPI_IOC_MESSAGE");
    		return;
    		}
    	//printf("env: %02x %02x %02x\n", buf[0], buf[1], buf[2]);
    	//printf("ret: %02x %02x %02x %02x\n", buf2[0], buf2[1], buf2[2], buf2[3]);
    
    	com_serial=1;
    	failcount=0;
    	return buf2;
    	}
    
    //////////
    // Write n bytes int the 2 bytes address add1 add2
    //////////
    void spi_write(int add1,int add2,int nbytes,char value[10],int file)
    	{
    	unsigned char	buf[32], buf2[32];
    	int status;
    
    	memset(buf, 0, sizeof buf);
    	memset(buf2, 0, sizeof buf2);
    	buf[0] = 0x00;
    	buf[1] = add1;
    	buf[2] = add2;
    	if (nbytes>=1) buf[3] = value[0];
    	if (nbytes>=2) buf[4] = value[1];
    	if (nbytes>=3) buf[5] = value[2];
    	if (nbytes>=4) buf[6] = value[3];
    	xfer[0].tx_buf = (unsigned long)buf;
    	xfer[0].len = nbytes+3; /* Length of  command to write*/
    	status = ioctl(file, SPI_IOC_MESSAGE(1), xfer);
    	if (status < 0)
    		{
    		perror("SPI_IOC_MESSAGE");
    		return;
    		}
    	//printf("env: %02x %02x %02x\n", buf[0], buf[1], buf[2]);
    	//printf("ret: %02x %02x %02x %02x\n", buf2[0], buf2[1], buf2[2], buf2[3]);
    
    	com_serial=1;
    	failcount=0;
    	}
    
[/code]
Usage example:  

[code] 
    char *buffer;
    char buf[10];
    
    file=spi_init("/dev/spidev0.0"); //dev
    
    buf[0] = 0x41;
    buf[1] = 0xFF;
    spi_write(0xE6,0x0E,2,buf,file); //this will write value 0x41FF to the address 0xE60E
    
    buffer=(char *)spi_read(0xE6,0x0E,4,file); //reading the address 0xE60E
    
    close(file);
    
[/code]
  
For info it is possible to use all the 12000000 Hz frequency limit transfers, however bear in mind, that frequency will not scale linearly. There are fixed frequencies you can select from, especially at the higher end: 
  * 100.00 MHz
  * 50.00 MHz
  * 33.33 MHz
  * 25.00 MHz
  * 20.00 MHz
  * 16.66 MHz
  * 14.28 MHZ
  * 12.50 MHz
  * 11.11 MHz
  * 10.00 MHz
  * 9.09 MHz
  * 8.33 MHz
  * 7.69 MHz
  * 7.14 MHz
  * 6.66 MHz
  * 6.25 MHz
  * 5.88 MHz
  * 5.55 MHz
  * 5.26 MHz
  * 5.00 MHz
  * 4.76 MHz
  * 4.54 MHz
  * 4.34 MHz
  * 4.16 MHz
  * 3.84 MHz
  * ...

## In the kernel space
If you are coding a driver for a SPI device, it makes most sense to code it as a kernel module. Instead of using /dev/spidevX.X you should register a new (slave) device and exchange data through it. If you are wondering what bus number you should use, you can find available buses by listing _/sys/class/spi_master_. There should be nodes like spi0, spi1... Number after spi is bus number. What number gets spi master depends on device-tree configuration. 
Here is an example of module, that writes 0x00 to SPI when module is initialized and 0xff when uninitialized. It is using bus number 0 and communicating at the speed of 1Hz: 
[code] 
    
    #include <linux/init.h>
    #include <linux/module.h>
    #include <linux/spi/spi.h>
    
    #define MY_BUS_NUM 0
    static struct spi_device *spi_device;
    
    static int __init spi_init(void)
    {
    	int ret;
    	unsigned char ch = 0x00;
    	struct spi_master *master;
    	
    	//Register information about your slave device:
    	struct spi_board_info spi_device_info = {
    		.modalias = "my-device-driver-name",
    		.max_speed_hz = 1, //speed your device (slave) can handle
    		.bus_num = MY_BUS_NUM,
    		.chip_select = 0,
    		.mode = 3,
    	};
    	
    	/*To send data we have to know what spi port/pins should be used. This information 
    	  can be found in the device-tree. */
    	master = spi_busnum_to_master( spi_device_info.bus_num );
    	if( !master ){
    		printk("MASTER not found.\n");
            	return -ENODEV;
    	}
    	
    	// create a new slave device, given the master and device info
    	spi_device = spi_new_device( master, &spi_device_info );
    
    	if( !spi_device ) {
    		printk("FAILED to create slave.\n");
    		return -ENODEV;
    	}
    	
    	spi_device->bits_per_word = 8;
    
    	ret = spi_setup( spi_device );
    	
    	if( ret ){
    		printk("FAILED to setup slave.\n");
    		spi_unregister_device( spi_device );
    		return -ENODEV;
    	}
    
    	spi_write(spi_device, &ch, sizeof(ch));
    	
    	return 0;
    }
    
    
    static void __exit spi_exit(void)
    {
    	unsigned char ch = 0Xff;
    
    	if( spi_device ){
    		spi_write(spi_device, &ch, sizeof(ch));
    		spi_unregister_device( spi_device );
    	}
    }
    
    module_init(spi_init);
    module_exit(spi_exit);
    
    MODULE_LICENSE("GPL");
    MODULE_AUTHOR("Piktas Zuikis <[email protected]>");
    MODULE_DESCRIPTION("SPI module example");
    
    
[/code]
# SPI NOR Flash
The [Allwinner Boot Rom][48395] can boot from NOR flash packaged over an SPI interface. [Booting devices from SPI flash][48396] is covered in this other article. 
# Bugs/Caveats
## HIGH on SCK line right before transfer
Starting an SPI transfer via sun6i-spi and sun4i-spi might raise the SCK line to HIGH shortly before transfer. Such behaviour might confuse slaves, especially when not using / ignoring chip-select. 
This is due to SUN6I_GBL_CTL_BUS_ENABLE being written into SUN6I_GBL_CTL_REG at an early stage. Moving that to the transfer function, hence, right before the transfer starts, mitigates that problem. 
The patch below does so for spi-sun6i. Note that the patch is in the mainline Linux kernel since 5.13: <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=0d7993b234c9fad8cb6bec6adfaa74694ba85ecb>
[code] 
    diff --git a/drivers/spi/spi-sun6i.c b/drivers/spi/spi-sun6i.c
    index 8533f4edd00a..6a14589cce32 100644
    --- a/drivers/spi/spi-sun6i.c
    +++ b/drivers/spi/spi-sun6i.c
    @@ -304,6 +304,9 @@ static int sun6i_spi_transfer_one(struct spi_master *master,
     
            sun6i_spi_write(sspi, SUN6I_CLK_CTL_REG, reg);
     
    +       /* Finally enable the bus - doing so before might raise SCK to HIGH */
    +       sun6i_spi_write(sspi, SUN6I_GBL_CTL_REG, sun6i_spi_read(sspi, SUN6I_GBL_CTL_REG) | SUN6I_GBL_CTL_BUS_ENABLE);
    +
            /* Setup the transfer now... */
            if (sspi->tx_buf)
                    tx_len = tfr->len;
    @@ -411,7 +414,7 @@ static int sun6i_spi_runtime_resume(struct device *dev)
            }
     
            sun6i_spi_write(sspi, SUN6I_GBL_CTL_REG,
    -                       SUN6I_GBL_CTL_BUS_ENABLE | SUN6I_GBL_CTL_MASTER | SUN6I_GBL_CTL_TP);
    +                       SUN6I_GBL_CTL_MASTER | SUN6I_GBL_CTL_TP);
     
            return 0;
    
[/code]
## LOW on SCK line on transfer start when using SPI-Mode3
When using SPI-Mode3, the SCK line idles on HIGH. With sun4i-spi on transfer start the SCK line will go LOW for a short duration before the actual transfer starts. Such behaviour might confuse slaves. 
This is due to static configuration beeing written to SUN4I_CTL_REG on every SPI resume within function sun4i_spi_runtime_resume. This always reconfigures the whole SPI system on every SPI resume which also configures SPI-Mode0 (SCK idles LOW) for a short duration before the actual transfer starts. 
Updating sun4i_spi_runtime_resume to read, manipulate, write SUN4I_CTL_REG fixes the problem. 
[code] 
    --- drivers/spi/spi-sun4i.c
    +++ drivers/spi/spi-sun4i.c
    @@ -393,6 +393,7 @@
            struct spi_master *master = dev_get_drvdata(dev);
            struct sun4i_spi *sspi = spi_master_get_devdata(master);
            int ret;
    +       u32 reg;
    
            ret = clk_prepare_enable(sspi->hclk);
            if (ret) {
    @@ -406,8 +407,10 @@
                    goto err;
            }
    
    +       reg = sun4i_spi_read(sspi, SUN4I_CTL_REG);
    +
            sun4i_spi_write(sspi, SUN4I_CTL_REG,
    -                       SUN4I_CTL_ENABLE | SUN4I_CTL_MASTER | SUN4I_CTL_TP);
    +                       reg | SUN4I_CTL_ENABLE | SUN4I_CTL_MASTER | SUN4I_CTL_TP);
    
            return 0;
    
[/code]
  1. [↑][48397] [[1]][48398]: _Sysfs also supports userspace driven binding/unbinding of drivers to devices that do not bind automatically using one of the tables above. To make the spidev driver bind to such a device, use the following: echo spidev > /sys/bus/spi/devices/spiB.C/driver_override; echo spiB.C > /sys/bus/spi/drivers/spidev/bind_.
