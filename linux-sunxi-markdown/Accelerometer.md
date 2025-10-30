# Accelerometer
This page is an attempt to collect all the information about the various accelerometers in use on Sunxi hardware. 
## Contents
  * [1 Manufacturers][6028]
    * [1.1 Bosch][6029]
      * [1.1.1 BMA250][6030]
    * [1.2 Domintech][6031]
      * [1.2.1 DMARD06][6032]
      * [1.2.2 DMARD09][6033]
      * [1.2.3 DMARD10][6034]
    * [1.3 Freescale][6035]
      * [1.3.1 MMA7660][6036]
      * [1.3.2 MMA8452][6037]
      * [1.3.3 MMA8652][6038]
      * [1.3.4 MMA8653][6039]
    * [1.4 Memsic][6040]
      * [1.4.1 MXC622X][6041]
    * [1.5 Sensortek][6042]
      * [1.5.1 STK8312][6043]
    * [1.6 STMicroelectronics][6044]
      * [1.6.1 LIS3DH][6045]
    * [1.7 Unknown][6046]
      * [1.7.1 sc7660][6047]

# Manufacturers
## Bosch
### BMA250
Supported in mainline kernel (via bma180 driver). 
Devicetree example (from [Gemei G9][6048]): 
[code] 
    &i2c1 {
        /* ... */
        bma250@18 {
            compatible = "bosch,bma250";
            reg = <0x18>;
        };
    };
    
[/code]
## Domintech
Domintech has [[Github page][6049]] which contains repositories with Android drivers. 
### DMARD06
DMARD06 is a ±2g tri-axial digital accelerometer. 
Driver for sunxi-3.4 can be found on our [mailinglist][6050]
Driver for mainline can be found [here][6051] and landed in 4.9 
### DMARD09
Driver supported since 4.9 
### DMARD10
TODO 
## Freescale
### MMA7660
Datasheet: <http://cache.freescale.com/files/sensors/doc/data_sheet/MMA7660FC.pdf>
### MMA8452
Driver in mainline kernel available. 
Datasheet: <http://cache.freescale.com/files/sensors/doc/data_sheet/MMA8452Q.pdf>
### MMA8652
Datasheet: <http://cache.freescale.com/files/sensors/doc/data_sheet/MMA8652FC.pdf>
### MMA8653
Datasheet: <http://cache.freescale.com/files/sensors/doc/data_sheet/MMA8653FC.pdf>
## Memsic
### MXC622X
TODO 
Driver can be found [here][6052]. 
## Sensortek
### STK8312
TODO 
## STMicroelectronics
### LIS3DH
Driver in mainline kernel available. 
## Unknown
### sc7660
Links: Used by [A33_Q7_V1.0][6053]
