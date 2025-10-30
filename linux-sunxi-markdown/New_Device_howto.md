# New Device howto
This page contains a clear guide for bringing up a previously unsupported and unknown device, and for getting support into the sunxi repositories. 
If you have problem following this howto don't hesitate to ask on irc or mailing list. However, in order for anybody to help you it is necessary to have as much information as possible about your device at hand. That's what steps 1 and 2 in this howto are for. 
If you are still not convinced [ go here for a more in depth list of reasons explaining why you need to do this.][39596]
## Contents
  * [1 Step 1: Find out all you can][39597]
  * [2 Step 2: Create a wiki page][39598]
  * [3 Step 3: Retrieve crucial information from the stock OS][39599]
  * [4 Step 4: Get a serial console][39600]
  * [5 Step 5: Add support to u-boot][39601]
  * [6 Step 6: Add support to sunxi-boards][39602]
  * [7 Step 7: run through a full manual build][39603]
  * [8 Frequently Asked Questions][39596]
    * [8.1 "Why should i do this?"][39604]
    * [8.2 "This text is long, i do not want to do all that!"][39605]
    * [8.3 "I don't care about any of this, make my device work."][39606]
    * [8.4 "Why do people keep on telling me to NDH while I have a specific question!"][39607]

# Step 1: Find out all you can
Before you rush into things, it really pays to find out all you can about your device. Bringing up a new board is not rocket science, but it is non-trivial and time consuming, so it pays to spend a few hours on google and on our wiki to find out what is publicly known about your device. 
When googling, you will find that android forum posts are a treasure trove of badly dispersed information. This ranges from basic android usage information all the way to device disassembly and pictures of the mainboard. If you are really lucky, someone will have posted information on how to expose the [UART][39608] (serial). Part of your task is making this horribly inaccessible information easily and neatly available, at least for those bits that are relevant for the sunxi project. 
As for the sunxi website, it is a really good idea to investigate similar devices with the same [SoC][39609]. It often happens that devices get rebranded ([Identification guide][39610]). If you are really lucky, you might find that your hardware is already supported. If not, you will be able to find out what other names your device was branded under, and you can include that information on the wiki page which you will create in step 2. You might also find similar devices with similar mainboards, but with just different bits bolted on, in which case you still might find some valuable information (like how to wire up the UART). 
It also pays to check out board [defconfig files in the U-Boot repository][39611], and see if your device is already listed there. Similarly, have a look through our [Boards repository][39612] to see whether your device [fex][39613] is listed there. 
# Step 2: Create a wiki page
If you have determined that your device is unique, then go ahead and create a new page. If your device is similar to an already documented device, then still create a new page and crosslink the two under a "See also" section. If it is just a rebadged version of some other device, then add it to the "Also known as" section of an existing wiki page. 
The process of and details for creating a new device page is described in our [ new device page howto][39614], an easy to hack template is provided. 
**You must do this now.** This wiki page allows you to document things as you go along, and this way you will not forgot any details, and people will ask for and refer to this page when you ask for any help. You also should make exterior device pictures now, before disassembling the device. Similarly, you need to get all the identification information from the stock OS before you replace it with something else. 
# Step 3: Retrieve crucial information from the stock OS
If you are not using a development board, then Android will be the stock OS. You will need to gather the identification strings from the stock OS for [ the device page in the previous step][39598]. 
You will also need to use [our retrieving device information howto][39615] to retrieve the bootinfo and .fex files. You will need them later on in [Step 5][39601] and [Step 6][39602]. 
# Step 4: Get a serial console
Like any ARMv7 system, you are pretty much lost when anything goes wrong, unless you have access to a serial console ([UART][39608]). If you intend to bring up a new device, it will really pay off to spend the time and effort to try to gain access to the serial console. So while this step is optional, it is usually quite crucial. 
You will need a 3.3V TTL UART to USB converter usually, or a level changer to standard RS232 to be able to successfully talk to the serial port on sunxi hardware. 
Some devices directly expose their UART, so all you really need to do is hook things up. Mobile devices never export a UART directly, or do not provide easy access to the UART. Here you will need to disassemble your device, locate the UART pins (if there are any) on the motherboard, solder on some wires and route them to the outside. This is a lot more work, but not impossible. 
All of the above is explained in detail in our [UART howto][39608]
# Step 5: Add support to u-boot
Please refer to [ the adding a new device to u-boot howto][39616] with the information retrieved in [ Step 3][39599]. 
**Note: no u-boot patches are accepted without[ a complete device page][39598] in place.**
# Step 6: Add support to sunxi-boards
Get the sunxi boards repository by running: 
[code] 
    git clone git://github.com/linux-sunxi/sunxi-boards.git
    
[/code]
Adding device support to the sunxi-boards repository is as simple as placing the [ acquired .fex file][39599] in the right directory and git adding the file. 
You can now commit your changes, and with: 
[code] 
    git format-patch -M -C HEAD^
    
[/code]
You will create a git mbox patch file which you can mail to [ our mailinglist][39617]. If you have [ set up git correctly][39618], you can just run: 
[code] 
    git send-email 0001-*.patch
    
[/code]
**Note: no sunxi-boards patches are accepted without[ a complete device page][39598] in place.**
# Step 7: run through a full manual build
Please work through our [ Manual build howto][39619] to verify your handiwork. 
You will be left with a fully working linux system on what was previously an android only device. Congratulations! 
# Frequently Asked Questions
## "Why should i do this?"
This is a concise guide for bringing up your hardware, and for documenting your hardware in one swoop. It is not rocket-science and some basic linux skills will suffice. All you need to do is meticulously follow the text here. 
## "This text is long, i do not want to do all that!"
In the process of working through this guide, you will also document your device and provide 2 patches to sunxi repositories. You are not doing this to help others, you are primarily doing this to help yourself, and only as a consequence helping others. Afterwards, you will be able to fall back to the information that you so handily gathered here instead of having lost this information for all time. And others who come by might help to improve the support for your specific device. 
Finally, think of all the code and information that linux-sunxi so handily gathers for you. Working through this howto is the least thing you can do to give something back. 
## "I don't care about any of this, make my device work."
Linux-sunxi is a community, and it is mostly peoples spare time that is sunk into it. Only very few people here work for hardware manufacturers. So no-one here has an obligation to help you. 
By not working through this guide, you effectively tell the people behind sunxi that they should waste their time on helping you, and only you, and that you will then plan to run off without giving even a tiny bit of time back. Why would anyone then spend their time helping you? 
## "Why do people keep on telling me to NDH while I have a specific question!"
This document explains how to gather a lot of important information on your device, and packages it up in a nice wiki page. When you ask a specific question on IRC or the mailinglist, people tend to first look up your hardware on the wiki and look at the details of your hardware which could relate to your issue. From the information gathered on these device pages, many issues have been immediately spotted and solved already. If the issue cannot be spotted quickly, people will have had a quick overview of the hardware, and thus can make more educated guesses of what the possible causes of the issue could be, and they can then provide better directives to help identify and fix the issue. 
But if you expect people to work blind and waste their time trying to help you, do keep on refusing to work through this document. Just don't expect anyone to help you.
