# Touchscreen
This page collects all the information about the various touch screen controllers in use on sunxi hardware. 
## Contents
  * [1 General information][55527]
    * [1.1 Hardware][55528]
    * [1.2 Startup Procedure][55529]
    * [1.3 Touchscreen profiles][55530]
    * [1.4 Touchscreen modes][55531]
    * [1.5 Hardware Configuration and Fex][55532]
      * [1.5.1 Step 1][55533]
      * [1.5.2 Step 2][55534]
      * [1.5.3 Step 3][55535]
    * [1.6 Software Calibration][55536]
  * [2 Manufacturers][55537]
    * [2.1 ChipOne][55538]
    * [2.2 Elan][55539]
      * [2.2.1 EKT3632][55540]
    * [2.3 Focaltech][55541]
      * [2.3.1 FT5301][55542]
      * [2.3.2 FT5302][55543]
      * [2.3.3 FT5402DQT][55544]
      * [2.3.4 FT5x06][55545]
        * [2.3.4.1 sunxi-3.4][55546]
    * [2.4 Goodix][55547]
      * [2.4.1 GT801][55548]
      * [2.4.2 GT801 2+1][55549]
      * [2.4.3 GT811][55550]
      * [2.4.4 GT818][55551]
      * [2.4.5 GT828][55552]
      * [2.4.6 GT9xx][55553]
    * [2.5 Ilitek][55554]
      * [2.5.1 aimvf][55555]
    * [2.6 Silead][55556]
    * [2.7 Solomon Systech Limited][55557]
      * [2.7.1 SSD2533][55558]
    * [2.8 TCM][55559]
      * [2.8.1 tc1680][55560]
    * [2.9 ZEITEC Semiconductor][55561]
      * [2.9.1 zet6221][55562]
      * [2.9.2 zet6223][55563]
    * [2.10 Hynitron][55564]
      * [2.10.1 cst2xx][55565]
  * [3 See also][55566]

# General information
In general touchscreens are configured by the ctp_para in the fex file. There's also support for resistive touch panels by setting rtp_para in the fex. An example for built in RTP (resistive touch panel) built in controller can be found in the [Fex Guide][55567]. 
An example (for ft5x) would be: 
[code] 
    [ctp_para]
    ctp_used = 1 #enable or disable the touchscreen
    ctp_name = "ft5x_ts" #model of the touchscreen
    ctp_twi_id = 2 #I2C Interface
    ctp_twi_addr = 0x70 #I2C Address
    ctp_screen_max_x = 800 #X Settings
    ctp_screen_max_y = 480 #Y Settings
    ctp_revert_x_flag = 0 #Set this and ctp_revert_y_flag to 1 to flip x and y axis
    ctp_revert_y_flag = 0
    ctp_exchange_x_y_flag = 0 
    ctp_int_port = port:PH21<6><default><default><default> #INT port settings
    ctp_wakeup = port:PB13<1><default><default><1> #Wakeup port settings
    ctp_io_port = port:PH21<0><default><default><default> #IO Port Settings
    rst_port = port:PH20<1><default><default><default> #RST port settings
    
[/code]
Example for built in RTP: 
[code] 
    [rtp_para]
    rtp_used = 0
    rtp_screen_size = 7
    rtp_regidity_level = 7
    rtp_press_threshold_enable = 0
    rtp_press_threshold = 0x1f40
    rtp_sensitive_level = 0xf
    rtp_exchange_x_y_flag = 0
    
[/code]
## Hardware
In general a capacitive touchscreen hardware consists of 6 Pins: 
  * RST - Reset Pin (Input), Used by the CPU to reset the touchscreen.
  * SDA - I2C SDA (IO)
  * SCL - I2C SDL (Input)
  * INT - Interrupt Pin (Output, can be input during startup), used by the Touchscreen to indicate to the CPU that there are new events
  * VCC - Power Supply
  * GND - GND

Some touchscreen have wakeup pins to allow the touchscreen to go to sleep mode to save battery. 
Mainly the I2C pins are connected to any i2c port on the CPU and is used to communicate with the touchscreen. 
In the other way a resistive touchscreen has 4 wires. Details can be found in the user manuals for Allwinner chips, in the section TP (touch panel). The interesting thing is that sun4i, sun6i and sun7i have essentially the same RTP controllers so the sun4i_ts driver can work for all of them. Testing was done on an A20 platform and gave exceptionally good results. 
## Startup Procedure
Usually any touchscreen has a startup procedure during which resets are sent to the touchscreen by the cpu to indicate this procedure. During the reset/startup procedure usually the touchscreen profile data is sent to the touchscreen. Also in some cases the I2C address is set by this rest procedure (for instance, GT911). 
The interrupt Pin can be part of the startup procedure for handshakes or indications. In some cases the interrupt pin is also used as input to read additional data from the cpu during reset. 
## Touchscreen profiles
Some touchscreen (for instance, GT911) require a so call Touchscreen Profile/Configuration. This configuration is sent during or right after the reset procedure of the touchscreen and is usually written to the controller memory (in some cases selectable persistent in eeprom). The Profile/Config defines the parameters of the touchscreen (such as physical size, active area(s). also it can include touchscreen button areas, touchscreen mode and more. 
**THIS CONFIGURATION MUST BE PROVIDED BY THE TOUCHSCREEN PRODUCER!**
Example: 
[code] 
    #define CTP_CFG_GROUP1 {\
    0x00,0x58,0x02,0x00,0x04,0x05,0x30,0x08,0x03,0x9F,0x14,\
    0x0F,0x8C,0x64,0x03,0x05,0x00,0x00,0x00,0x00,0x00,0x00,\
    0x00,0x18,0x1A,0x1E,0x14,0x8C,0x28,0x0C,0x18,0x14,0xD1,\
    0x0B,0x00,0x00,0x01,0x9C,0x02,0x35,0x00,0x00,0x00,0x00,\
    0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x14,0x64,0x94,0x85,\
    0x02,0x08,0x00,0x00,0xCD,0x07,0x16,0xBF,0x09,0x19,0xFC,\
    0x0C,0x1B,0xE7,0x0D,0x22,0x77,0x0E,0x2D,0x00,0x00,0x00,\
    0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,\
    0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,\
    0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,\
    0x00,0x00,0x02,0x04,0x06,0x08,0x0A,0x0C,0x0E,0x10,0x12,\
    0x14,0x16,0x18,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,\
    0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0x00,\
    0x02,0x04,0x06,0x08,0x0A,0x0C,0x0F,0x10,0x12,0x13,0x14,\
    0x16,0x18,0x1C,0x1D,0x1E,0x1F,0x20,0x21,0xFF,0xFF,0xFF,\
    0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,\
    0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0x7C,0x01\
    }
    
[/code]
## Touchscreen modes
There is 2 modes a touchscreen can work in: 
  * Polling Mode
  * Interrupt Mode

This mode is usually defined by the Touchscreen profile/config or the startup/reset procedure. 
The preferred mode a capacitive touchscreen should work in is always interrupt mode. In Interrupt mode every time an event on the touchscreen occurs the INT pin triggers and notifies the CPU. the cpu then read the new event from the touchscreen. 
In Polling mode the cpu periodically requests the touchscreen data from the touchscreen. This means that there will be a lot of communication on the i2c port since this has to happen once every few ms. 
As stated above whenever possible use interrupt mode! 
## Hardware Configuration and Fex
It is very important to configure the FEX file correctly for your touchscreen. 
### Step 1
In your hardware schematics identify the I2C pins of your touchscreen and see which I2C it is connected to and set the _ctp_twi_id_ to the id of i2c port. Now you need to find our your i2c address of your touchscreen. this is something you can get out of the chip datasheet or your touchscreen manufacture. 
Remember that the address of the touchscreen might be changed when sending the profile/config or via the reset procedure. 
### Step 2
In your schematics find out which GPIO Pin the INT Pin is connected to. 
Define: 
[code] 
    ctp_int_port = port:<text>PH21</text><6><default><default><default>
[/code]
please also note the _< 6>_ part in the line above. Verify that the Interrupt setting of your Int pin is Function number 6 of the mux setting or modify the _< X>_ according. 
Note that on some touchscreens (ft5x) it is required to define another port called the IO port on the same port as the interrupt port: 
[code] 
    ctp_io_port = port: PH21<0><default><default><default>
[/code]
This setting will define the same port with mux setting 0 as output to allow the driver to switch to IO mode. 
### Step 3
In your schematics find out which GPIO Pin the RST Pin is connected to. 
[code] 
    rst_port = port:PH20<1><default><default><default> #RST port settings
[/code]
Note that <1> sets the port as an output. 
It might be required to define additional pins for your touchscreen 
## Software Calibration
Calibration of a touchscreen device can be done with the [xinput_calibrator][55568]. The xinput_calibrator is very simple tool which enables you to go through standard calibration procedure (press a few points on the screen) and then produces a snippet for xorg.conf. 
There can be problems with produced configuration so it's good to test and see what's actually happening. Try to move your finger over the screen and see if there's some sings of miscalibration. Produced config actually scales values from touchscreen controller to map to the screen so it may happen that one axis works ok and another doesn't. Anyways, xinput_calibrator can give you good hint for start and you can tweak it further manually. Detailed list of options can be found in the [evdev manual page][55569]. 
# Manufacturers
## ChipOne
  * Mainline kernel driver: **icn8138**
  * WIP drivers: 
    * **icn85xx** \- [WIP branch][55570] ([announcement][55571])

## Elan
[Elan Microelectronics Corporation][55572]
### EKT3632
## Focaltech
[Link][55573]
Support is available for [sunxi-3.4][55574]. 
### FT5301
Supported in sunxi-3.4 
### FT5302
??? 
### FT5402DQT
Supported in sunxi-3.4 
### FT5x06
**Supported** in mainline kernel. 
  * FT5206GE1
  * FT5306DE4
  * FT5406EE8

You should need to add in dtb node for support(example for a Q8 tablet): 
[code] 
    &i2c1{
       clock-frequency = <400000>;
             polytouch: edt-ft5x06@38 {
                  compatible = "edt,edt-ft5406", "edt,edt-ft5x06";
                  reg = <0x38>;
    	       pinctrl-names = "default";
    	       pinctrl-0 = <&edt_ft5x06_pins>;
    	       interrupt-parent = <&pio>;
    	       interrupts = <6 11 IRQ_TYPE_EDGE_FALLING>; /*PG11 */
    	       wake-gpios = <&pio 1 3 GPIO_ACTIVE_HIGH>; /* PB3 */
                  touchscreen-size-x = <800>;
                  touchscreen-size-y = <480>;
                  touchscreen-inverted-x;
                  touchscreen-inverted-y;
                  /* touchscreen-swapped-x-y;*/
           };
    };
    
[/code]
  

#### sunxi-3.4
Supported, but the driver does not load on [A20][55575] without the following patch. See this [conversation][55576] for more information. 
[code] 
    diff --git a/drivers/input/touchscreen/ft5x_ts.c b/drivers/input/touchscreen/ft5x_ts.c
    index 5d8dc97..3d88694 100644
    --- a/drivers/input/touchscreen/ft5x_ts.c
    +++ b/drivers/input/touchscreen/ft5x_ts.c
    @@ -1762,7 +1762,7 @@ ft5x_ts_probe(struct i2c_client *client, const struct i2c_device_id *id)
                    pr_info("%s:ctp_ops.set_irq_mode err.\n", __func__);
                    goto exit_set_irq_mode;
            }
    -       err = request_irq(SW_INT_IRQNO_PIO, ft5x_ts_interrupt, IRQF_TRIGGER_FALLING | IRQF_SHARED, "ft5x_ts", ft5x_ts);
    +       err = request_irq(SW_INT_IRQNO_PIO, ft5x_ts_interrupt, IRQF_SHARED, "ft5x_ts", ft5x_ts);
    
            if (err < 0) {
                    dev_err(&client->dev, "ft5x_ts_probe: request irq failed\n");
[/code]
This driver does not support transformations (e.g. x-revert), but generates events complying to the [multi touch protocol][55577]. 
## Goodix
[Manufacturer's website][55578]
[Datasheets][55579] for various GT9xx devices. 
Driver for most of the **Goodix 9xx** chips (see below) is available in mainline. It is quite possible that all the 9xx-series chips are supported by this driver because they seem to have a common register layout. Goodix 8xx is currently unsupported by mainline. 
For older chips there are various driver sources targeting older kernel versions (linux-3.3 or linux-3.4) scattered around in different vendor-provided source trees or SDKs. 
### GT801
No mainline support. Driver available in sunxi-3.4 
### GT801 2+1
No mainline support. [RFC patch][55580] that needs to be adapted to work alongside gt9xx chips. 
Driver available in sunxi-3.4 
### GT811
No mainline support. Driver available in sunxi-3.4 
### GT818
No mainline support. Driver available in sunxi-3.4 
### GT828
No mainline support. No driver in sunxi-3.4, [WIP patch][55581]
### GT9xx
Support for various Goodix GT9xx chips is available since Linux-4.1 via common **`[goodix][55582]`** driver: 
  * gt911
  * gt9110
  * gt912
  * gt927
  * gt9271
  * gt928
  * gt967

For `sunxi-3.4`, there's [WIP driver][55583]. 
## Ilitek
### aimvf
## Silead
Supported in [mainline kernel][55584] (gsl1680, gsl1688, gsl3670, gsl3675, gsl3692 and also MSSL1680, MSSL0001, MSSL0002, MSSL0017 variants). 
Please note that you need device-specific firmware stored under `/lib/firmware/silead/` which should be extracted from original software on the device. 
If you get lucky, you might find [firmware supporting your device from this repository][55585]. 
  * Datasheet for GSL1680 / GSL1688: [GSL1680, GSL1688 datasheet, rev A1.6 – Oct 2012][55586]
  * Datasheet for GSL3680: <http://dl.linux-sunxi.org/touchscreen/GSL3680_touch-screen-controller-ic-DataSheet_Chinese_RevA1.2.pdf>

See also: 
  * [GSL1680][55587] \- capacitive, multitactile touchscreen controller

## Solomon Systech Limited
This [Hong Kong based company][55588] creates various LCD/OLED driver and touchscreen chips. 
### SSD2533
## TCM
TrueCore Microelectronics 
### tc1680
Chip marked tc1680j i2c@0x20 The driver for tc1680 is named tc1126 , there's a driver for allwinner kernel 3.4 (lichee) that supports A23 A33 A31 ,Here's The driver: <https://github.com/xchetah/tc1126-sunxi>
Mainline WIP driver ported from BSP :<https://github.com/miky2k/tc1126>
See also: [A33_Q7_V1.0][55589] tablet. 
## ZEITEC Semiconductor
### zet6221
  * WiP and more info: <https://github.com/jelly/linux-zet62xx>
  * Datasheet: <http://linux-sunxi.org/images/2/22/ZP-HW-PS-0003_ZET6221_Product_Spec_v1_2.pdf>
  * Driver: <https://github.com/wingrime/zet6221-ts-drv>
  * WiP driver for all zet62xx chips with firmwares loading for linux-sunxi-3.4 legacy kernel: <https://github.com/xchetah/zet6221-sunxi/>

### zet6223
Supported in **mainline** Linux 4.11 ([**zet6223.c**][55590]). No firmware (blob) required. 
## Hynitron
### cst2xx
Mainline driver: <https://gitlab.com/ariarolin/cst2xx-touchscreen-driver>
# See also
