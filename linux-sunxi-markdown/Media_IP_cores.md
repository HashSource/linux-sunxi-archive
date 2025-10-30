# Media IP cores
## Contents
  * [1 Video and graphics acceleration relationships][35734]
    * [1.1 2D Acceleration (G2D)][35735]
    * [1.2 3D Acceleration (Mali)][35736]
    * [1.3 Video Acceleration (Video decoding/ encoding)][35737]

# Video and graphics acceleration relationships
Each of the following [IP cores][35738] is dedicated to its special usecase and works separately from each other!
## 2D Acceleration (G2D)
[![MBOX icon important.png][35739]][35740] | Not available in mainline kernel   
---|---  
  * **Hardware:** 2D graphics acceleration is done by the mixer processor (G2D). It can do hardware accelerated operations, such as blitting, rotating, alpha blending, scaling, mirroring and color conversion. It is only available on some SoC variants (A10/A20/?)
  * **Software:** G2D acceleration is provided via the (legacy/3.4-only) kernel driver, which makes the mixer processor accessible from userspace via ioctl.

## 3D Acceleration ([Mali][35741])
[![MBOX icon important.png][35739]][35740] | Not available in mainline kernel - only out-of-tree driver possible   
---|---  
  * **Hardware:** 3D graphics acceleration is done by [ ARM's Mali-400/450][35741] through the OpenGL/ES 1.1/2.0 API.
  * **Software:** To use OpenGL/ES, you need a mali kernel driver (GPLv2) and a corresponding [ userspace library][35742] (closed source).

(According to the datasheet, Mali can provide 2D vector graphics acceleration through the OpenVG API. Atm, there is no userspace library known/ available, to use this feature.) 
## Video Acceleration (Video decoding/ encoding)
[![MBOX icon important.png][35739]][35740] | Not available in mainline kernel - mainlining effort started   
---|---  
  * **Hardware:** Hardware accelerated video de-/encoding is done by the [ VE (Video Engine)][35743] aka VPU (Video Processing Unit) in hardware.
  * **Software:** The VE can be used via direct register access using [libvdpau-sunxi][35744] which is a (proof-of-concept) result of the [Cedrus][35745] project. This is completely open source code.

A [ V4L2 kernel driver][35746] has already been started, to bring the results of the reverse engineering effort in a mainlineable state.
