# New Device page
This page contains a guide for creating a new device page, or for improving existing pages. 
## Contents
  * [1 Goals][39652]
  * [2 Legal][39653]
  * [3 Featured Community or Open Source hardware][39654]
  * [4 Page naming][39655]
  * [5 Starting point][39656]
  * [6 Guidelines for different fields][39657]
    * [6.1 Infobox][39658]
    * [6.2 Identification][39659]
    * [6.3 Sunxi support][39660]
    * [6.4 Tips, Tricks, Caveats][39661]
    * [6.5 Adding a serial port][39662]
    * [6.6 Pictures][39663]
    * [6.7 Also known as][39664]
    * [6.8 See also][39665]
    * [6.9 Categories][39666]

# Goals
The goal of a device page is not only to gather information about a device, but to clearly present the necessary information to the user. A page filled with marketing mumble, even when there is some valuable information in there, is just as useful as no page at all. 
So please, try to keep structure and presentation tight, and provide the relevant information in the relevant sections. Further down, an example page, which can simply be copied, is provided, which should help you create a useful device page. 
# Legal
All contributions to linux-sunxi.org are considered to be released under the Creative Commons Attribution (see sunxi:Copyrights for details). If you do not want your writing to be edited mercilessly and redistributed at will, then do not submit it here. You are also promising us that you wrote this yourself, or copied it from a public domain or similar free resource. Do not submit copyrighted work without permission! 
Under no circumstances should you include pictures or documents that were not created by yourself. Either you get the express permission of the owner of the material, or you should use a link. 
Similarly, unless you get express permission to reproduce certain information verbatim, you should not copy external information or howtos. If you do, either get permission from the original author, or make sure that it is a complete rewrite/rephrasing of the original document. 
# Featured Community or Open Source hardware
The sunxi project rewards those companies that are actively working with the sunxi community, not only by providing guidance and software development, but also by clearly showing what hardware is either Open Source, or hardware that was created in close cooperation with the sunxi community. 
If you are a device manufacturer, then simply adding your board to our wiki does not mean that it is community hardware. Similarly, plainly adding an OSHW logo to your silkscreen does not make your hardware open source. 
# Page naming
Before you do anything else, try to determine whether your device is also available under other names (as described in our [New Device Howto][39667]). 
If the original manufacturer and device name can be retrieved (which only rarely is possible for cheap chinese devices), then that should be used. Failing that, try to name the page according to either the most popular name, or the name under which it was first marketed. If that fails, any unique markings on the device will work. 
If your device is a plain rebadge job, then just add the name of your device to the "Similar Devices" section of an already existing page. If your device shares the motherboard, but has different hardware included, then create a new page, but frequently mention and crosslink to the existing device page. 
As for page naming, put the manufacturer name at the front, followed by the device name. Use underscores instead of spaces. 
If you cannot figure out what your tablet is named, temporarily place it under your user page until you do know exactly what it's called. E.g. at somewhere like [User:YOU/Unknown_Device][39668]
# Starting point
To create your new page, open a new window or tab in your browser, type _[http://linux-sunxi.org/][39669]_ , immediately followed by the _Manufacturer_ of your device, then an underscore ___ , then the _Name_ of your device, and go to that URL. The wiki will then offer you to create that page. 
Open the [Device Page Example][39670], and copy the contents of the _View source_ tab to your newly created device page. Then start fleshing out the different parts. 
Begin by filling in the infobox, as most of this general information should be known to you already. The rest can be filled out as you go along with the [New Device howto][39667]. 
# Guidelines for different fields
## Infobox
All possible fields, and some examples of content, are included in the [Device Page Example][39670]. Fields that do not apply for your device can be removed, and will subsequently not turn up in your infobox. 
## Identification
Because many tablets are hard to identify going from the outside alone, this section should list how to identify a given device from within Android. This usually means going to _Settings_ and under _About tablet" you will find 'Model Number_ and _Build number_. 
These values are set by software, so it is possible that physically completely equal devices have different values in these sections. It is fine to list multiple entries in this section. 
If you are running Cyanogenmod, then your settings will not be useful. So please only provide the values for the stock image, or do not provide values at all. 
## Sunxi support
This is perhaps the most important section of any device page. Here the reader should be informed about the status of support of the device, and given concise information on how to set-up things on their device. 
Try to refer to existing guides, and point out the device specific differences in your device page. 
Please limit the explanations here to only the bare minimum. Add changes or suggestions, which are nice to have, but not absolutely necessary to the Tips, Tricks, Caveats section. 
## Tips, Tricks, Caveats
This section should add more information on top of the basics which were described in the above section. It should be a grab bag of many things that are device specific but which might interest others, be it hardware or software. 
## Adding a serial port
Here you should always provide a picture of the serial port pins or pads, and you should always reference our [UART howto][39671]. 
## Pictures
This section should provide all the pictures anyone could need for successful identification of the device. For tablets, make sure that you also have the back and the buttons/connectors, as all tablets pretty much look the same from the front. It also really pays to open up the device and provide interior and PCB pictures. 
Note that if you are not the author of the pictures, that they are licensed that allows distribution. So **do not pluck pictures of the interweb** , take them yourself. 
## Also known as
This section should list the manufacturers and names of rebadged devices. Spend a bit of time on google for this. 
## See also
Here the following should be listed: 
  * local links to related but not similar devices.
  * further information found on android forums.
  * manufacturer links.

Here is a list of links of known [ Chinese tablet manufacturers][39672]. 
## Categories
You need to always keep the **Devices** category. 
Main categories make sure that the device is properly listed on the front page. Possible options for main categories are: 
[code] 
    [[Category:A10 Boards]]
    [[Category:A10 HTPC]]
    [[Category:A10 Tablets]]
    [[Category:A13 Boards]]
    [[Category:A13 Tablets]]
    [[Category:A10s Boards]]
    [[Category:A10s HTPC]]
    [[Category:A20 Boards]]
    [[Category:A20 HTPC]]
    [[Category:A20 Tablets]]
    [[Category:A23 Tablets]]
    [[Category:A31 Boards]]
    [[Category:A31 Tablets]]
    
[/code]
These categories add further information: 
[code] 
    [[Category:Devices with Ethernet port]]
    [[Category:Devices with Wifi]]
    [[Category:Devices with SATA port]]
    [[Category:Devices with HDMI port‏‎]]
    [[Category:Devices with VGA port]]
    [[Category:Devices with LVDS port]]
    [[Category:Devices with SPDIF port]]
    
[/code]
The **{{Remove_only_when_finished}}** template at the top of the page should be kept until the page is fully filled and all patches have been committed. This allows for easier tracking of which devices/pages need help still (by adding a **NDH_TODO** category to the page).
