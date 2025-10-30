# Identification guide
There are several different options to attempt to identify your device. 
## Contents
  * [1 Search for marketing name][25637]
  * [2 Search for Android model number][25638]
  * [3 Search by classification][25639]
    * [3.1 Boards][25640]
    * [3.2 HTPCs][25641]
    * [3.3 Tablets][25642]
    * [3.4 Netbooks][25643]
  * [4 When all fails][25644]

# Search for marketing name
Many of the devices we have listed are often rebadged. This means that one company (a good example is Inet-tek) builds the tablet for a customer, and provides the customers desired logo and printing on the device. 
A good example is the [Inet 86vz][25645], which is sold as (at least) both the "Freelander PH20" and the "Storex TAB LC7". Both rebadgers come with slightly redesigned back covers, with the respective marketing information printed on the back, but they are 100% clones. 
This is why each documented device has an "Also known as" section, so that this can aid device identification. You can most easily search for the marketing names, by using google and a search prefix: 
[code] 
    site:linux-sunxi.org Freelander PH20
[/code]
# Search for Android model number
When you boot your device under the stock android, you can check "Settings", "About Tablet", to find out the following: 
  * Model Number: SXZ-PH20
  * Build Number: A13_86VZ_M758C2_*.*

We collect these Model/Build Numbers on our Device pages as well, so you can google for those strings, or parts of those strings: 
[code] 
    site:linux-sunxi.org SXZ
[/code]
[code] 
    site:linux-sunxi.org PH20
[/code]
[code] 
    site:linux-sunxi.org 86VZ
[/code]
[code] 
    site:linux-sunxi.org M758C2
[/code]
# Search by classification
If the above fails, you have no option but to manually check the list of available devices. There should be exterior and interior pictures of each device available. 
It pays to know what the interior of your device looks like at this point, refer to the [device disassembly guide][25646] for more information on that. 
At sunxi, we first break up devices in 4 categories, and then subdivide those categories per SoC. 
## Boards
This category is development boards of all kinds. 
► [A10 Boards][25647]
► [A10s Boards][25648]
► [A13 Boards][25649]
► [A13 Ereaders][25650]
► [A20 Boards][25651]
► [A31 Boards][25652]
► [A31s Boards][25653]
► [A527 Boards][25654]
► [A64 Boards][25655]
► [A80 Boards][25656]
► [A83T Boards][25657]
► [D1 Boards][25658]
► [D1s Boards][25659]
► [H2+ Boards][25660]
► [H3 Boards][25661]
► [H5 Boards][25662]
► [H6 Boards][25663]
► [H616 Boards][25664]
► [H8 Boards][25665]
► [R329 Boards][25666]
► [T113-s3 Boards][25667]
► [T527 Boards][25668]
► [V3s Boards][25669]
## HTPCs
Home theater PCs means all set-top-boxes and HDMI sticks and similar devices. 
There are a few cases where the same housing/case is re-used multiple times, with different internals. It pays to have a look through those common HTPC formats first, as they could potentially vastly speed up identification. 
[Format MK802][25670]
If your HTPC is not one of the common case designs, then you will have to look through the full list. 
► [A10 HTPC][25671]
► [A10s HTPC][25672]
► [A20 HTPC][25673]
► [A31 HTPC][25674]
► [A31s HTPC][25675]
► [A80 HTPC][25676]
► [H3 HTPC][25677]
► [H64 HTPC][25678]
## Tablets
This naturally means those flat oblong things which have a big display on one side. 
There are a few cases where the same exterior tablet design is re-used multiple times, with different internals. It pays to have a look through those common tablet formats first, as they could potentially vastly speed up identification. 
[Format Q8][25679]
If your tablet is not one of the common case designs, then you will have to look through the full list. 
► [A10 Tablets][25680]
► [A13 Tablets][25681]
► [A20 Tablets][25682]
► [A23 Tablets][25683]
► [A31 Tablets][25684]
► [A31s Tablets][25685]
► [A33 Tablets][25686]
► [A63 Tablets][25687]
► [A83T Tablets][25688]
[Eken t01a][25689]
[Fukuda FCT94AW8][25690]
[Teclast P50Ai][25691]
[Teclast P85T][25692]
## Netbooks
Although rare, there are some netbooks with allwinner chips out there. 
► [A10 Netbooks][25693]
# When all fails
When your device still cannot be found, then it probably is not known to our community, or not documented yet. In this case you will need to work through our [New Device Howto][25694].
