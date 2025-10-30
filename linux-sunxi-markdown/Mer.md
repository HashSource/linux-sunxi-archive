# Mer
## Current Status of Mer on linux-sunxi
Booloader, kernel, graphics drivers, tools, xorg drivers have been packaged thanks to mdfe - now moved to a Nemo Adaptation layer <https://build.merproject.org/project/show?project=nemo%3Adevel%3Ahw%3Aallwinner%3Aa20%3Aeoma68>
Images which boot to xterm with working 3d drivers can be found at <ftp://5.9.162.110/nemo/> . If you don't see your device ping vgrade on #mer IRC Images with Mer and Plasma Active can be found at <http://makeplaylive.com/~notmart/Improv/>
Instructions for a Qt5 eglfs (ie no X) setup can be found at <http://martinbrook.blogspot.co.uk/2013/04/adventures-with-libhybris-and-andriod.html> \- Video at <http://www.youtube.com/watch?v=4PEIg6wOgWY>
come and discuss on [http://webchat.freenode.net/?channels=#mer][37575]
Images of both SD cards and images that can be flashed on the internal NAND can be found at <http://makeplaylive.com/~notmart/Improv/>
Here, in structions on how to produce images based on Mer and Plasma Active, tested on the Eoma68 (should be easy to adapt to other devices): [Mer and Plasma Active][37576]
## Old Content
this is a quick hack (November 2012): <http://www.youtube.com/watch?v=TWFvkZniHZc>
its performance can be improved to an acceptable state (and even beyond that) due to these developments (February 2013): <http://ssvb.github.com/2013/02/01/new-xf86-video-sunxifb-ddx-driver.html>
mer-test images: <http://pengpod.com/dl/images/>
all you need to start building a Mer HA repo: <https://github.com/linux-sunxi>
from <http://pengpod.com/blog/entry/new-images-uploaded>: 
Mer: This is a work in progress. This is a basically a snapshot of my previous attempts to use Mer. It will boot to a console but X will not start. I'm not quite sure what is wrong, maybe someone with more experience with Mer can work it out and share how they did it. This will only work on the 1000 right now but if you copy the 700s script.bin from the boot partition over I think it will work the same on there, this is an older image from before U-boot became device dependent.
