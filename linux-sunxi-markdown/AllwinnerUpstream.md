# AllwinnerUpstream
This page keeps track of the work that AllwinnerTech engineers will be doing to assist in better upstream support for the [Allwinner SoC Family][6286]. 
Free and open-source software projects are continuously in development. When support for a hardware device is added to such a project, it can either be added to the main developing version (**upstream** or some cases called **mainline**) or it can be added to a specific (older) version. The benefit in adding support to the upstream/mainline is that automatically all newer versions will include support for the hardware. On the other hand, adding support to a specific (older) version has the disadvantage that software becomes obsolete, and the hardware is effectively not supported any more. This has been the case with hardware support in the Linux 3.4 kernel which has not been adapted to work with newer versions of the Linux kernel (currently, the latest version is 3.16). 
Currently, this page covers the content of the thread [Introductions and Allwinner documentation update][6287] at the [linux-sunxi Google Group][6288]. 
## Contents
  * [1 Small-sized Linux kernel tasks][6289]
  * [2 Medium-sized Linux kernel tasks][6290]
  * [3 u-boot tasks][6291]
  * [4 Documentation requests][6292]

# Small-sized Linux kernel tasks
  1. GPADC

# Medium-sized Linux kernel tasks
  1. Camera driver

# u-boot tasks
Hans de Goede (hdegoede at redhat dot com) writes: 
[code] 
    I think it is great that Allwinner wants to get more involved in
    upstream sunxi support.
    
    As one of the 2 custodians (maintainers) for the upstream u-boot
    support for sunxi devices, I would like to ask Allwinner to also
    get more involved in upstream u-boot support. Ideally Allwinner
    would switch to using upstream u-boot entirely, including using
    a standard u-boot SPL, rather then chainloading an older u-boot
    fork through boot0 and boot1.
    
    I can understand that completely switching to upstream u-boot
    will take time, and that you may need some additional features
    in upstream u-boot before you can switch. In the mean time it
    would be great if you could help us extend the existing sunxi
    support in upstream u-boot. Currently we support sun4i, sun5i
    and sun7i. We would love to also support sun6i and sun8i (and
    the A80).
    
    We already have some limited sun6i and sun8i support in the linux-sunxi
    u-boot-sunxi git repository. The biggest stumbling block keeping
    us from adding support for sun6i and sun8i is the lack of code
    to initialize the DRAM controller. It would be a big help for
    us if you could share the boot0 code for sun6i and sun8i with
    us, either under an open license, or with an explicit permission
    notice for copy and pasting parts of that code and releasing the
    result under a GPLv2+ license.
    
    If you've any questions about or suggestions for upstream
    sunxi u-boot support please send a mail to me and Ian Campbell
    (the other sunxi custodian, ijc at hellion dot org dot uk).
    
[/code]
# Documentation requests
  * See also: [Documentation Request][6293]

Enrico (ebutera at gmail dot com) writes: 
[code] 
    documentation about the A10/A20 tv decoder (tv in) would be great.
    I'm one of the maintainers of the meta-sunxi openembedded layer, you can contact me directly.
    
[/code]
