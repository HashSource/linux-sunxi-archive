# Temperature Calibration
The A10 and A20 temperature sensor is currently uncalibrated. We have basically no idea what the register value corresponds to. Because of this, the sensor requires some calibration. Here are my results. 
To attempt to get some initial data, was done using an Olimex OLinuXino A10-Lime-4G using a combination of cpuburn-a8 and lima-textured-cube 100M. Two tests where performed, one using an IR camera and one using an thermocouple. It should be noted that on average, the IR camera was 15 degree's to high and was thus a bad device to do temperature measurments with. 
[![][54825]][54826]
[][54827]
Temperature Calibration Setup using IR Camera A10 Lime
[![][54828]][54829]
[][54830]
Temperature Calibration Setup using thermocouple A10 Lime
Initial data can be found here: <http://dl.linux-sunxi.org/users/oliver/Temperature_Measurments_A10_Lime.ods>
