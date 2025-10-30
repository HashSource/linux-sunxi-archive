# Mailing list
The linux-sunxi community primarly uses [a kernel.org mailing list called `[email protected]`][33669] This mailing list is meant for technical discussion pertaining to sunxi, and for patch review and submission. Subscription is required. 
## Contents
  * [1 History][33670]
  * [2 Subscription][33671]
  * [3 Proper conduct][33672]
  * [4 Submitting patches][33673]
    * [4.1 Configuring git for send-email][33674]
  * [5 External links][33675]
  * [6 See Also][33676]

# History
Traditionally we used [`[email protected]`][33677] (Subscription required) as our mailing list for general discussions. But to not overwhelm it with **sunxi** (Allwinner A10, A13, ...) specifics, and to allow more technical discussions and patch reviews, a new list was created dedicated to this [family of SoCs][33678]. 
The previous mailing list was [a googlegroups mailing list called `[email protected]`][33679], but it is unused now. 
# Subscription
You can send an empty email to [`[email protected]`][33680] and follow the instructions to subscribe. 
# Proper conduct
For everyone's sanity please be sure to follow [proper netiquette][33681] when posting or replying to a post. 
# Submitting patches
Please follow [Linux's submitting patches rules][33682] when sending code. 
## Configuring git for send-email
Edit .git/config and add the following, replacing the smtpserver and from entries: 
[code] 
    [sendemail]
            smtpserver = smtp.server.domain
            to = [[email protected]][33683]
            from = Your Name <[[email protected]][33683]>
            chainreplyto = false
            suppressfrom = true
            suppresscc = self
    
[/code]
You should then be able to just git send-email your patches. 
# External links
  * [Mailing List posting netiquette][33681]
  * [Email Guide and Email Tutorials][33684]
  * [arm-netbook mailing list][33677]
  * [arm-netbook archive on Gmane][33685]
  * [linux-sunxi developers mailing list][33679]

# See Also
  * [Sunxi Community][33686]
  * [IRC][33687]
