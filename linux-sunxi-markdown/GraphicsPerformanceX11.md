# GraphicsPerformanceX11
## Contents
  * [1 Introduction][22242]
  * [2 Glossary][22243]
  * [3 Tuning memory bandwidth and screen resolution][22244]
  * [4 X11 DDX drivers][22245]
  * [5 Compositing window managers][22246]

# Introduction
This page tries to provide tips and tricks for getting best performance in the classic X11 based Linux desktop (XFCE, KDE, Ubuntu Unity, ...). X11 has been already ["Osborned"][22247] by Wayland/Mir/any-other-upcoming-graphics-stack-contender, but still remains the only realistically useful window system in the current Linux distros as of today. 
X11 is not an absolutely best solution for all cases. A plain fbdev driver is more simplistic and usually provides better performance for the applications, which are specifically designed to exclusively handle graphics in fullscreen mode without anything else interfering. For example, media players or OpenGL ES accelerated games can use non-portable sunxi specific display driver for perfectly smooth double buffered animation with scaling and colorspace conversion support. 
However if you want to run multiple applications at the same time, each having its own window (which can be arranged on the desktop, resized or moved) then one of the X11 desktop environments (KDE, Gnome, XFCE, LXDE, ...) is the way to go. 
# Glossary
Before we proceed, it makes sense to clarify some of the commonly used buzzwords and their relevance for sunxi hardware: 
[OpenGL][22248] \- the 3D API used in desktop linux systems. It's something that can't be hardware accelerated on sunxi hardware yet! Any OpenGL application is going to use the slow software implementation from Mesa as a backend. 
[OpenGL ES][22249] \- OpenGL for Embedded Systems (OpenGL ES) is a subset of the OpenGL 3D graphics application programming interface (API) designed for embedded systems such as mobile phones, PDAs, and video game consoles. 
[Mali400][22250] \- The 3D accelerator hardware in Allwinner A10, which has proprietary drivers for OpenGL ES. 
[OpenVG][22251] \- is an API designed for hardware-accelerated 2D vector graphics. It is not very popular in open source software in general. Or in other words, it is not going to accelerate anything even if we had good drivers for Mali400 drivers. 
[EXA][22252] \- despite having "acceleration" in its name, that's in fact a midlayer framework, which is providing convenience hooks for 2D acceleration in the X server to make drivers development easier. Activating empty EXA hooks (so that they do nothing and fallback to software rendering) is slower than just software rendering without EXA. The mileage may vary for activating EXA hooks and implementing hardware acceleration for only a small subset of operations (some operations become faster, everything else becomes a bit slower even without considering the migration overhead between hardware accelerated and software rendering backends). 
G2D - a dedicated 2D hardware accelerator ([MixerProcessor][22253]) 
# Tuning memory bandwidth and screen resolution
# X11 DDX drivers
# Compositing window managers
