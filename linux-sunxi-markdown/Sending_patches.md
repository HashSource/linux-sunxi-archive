# Sending patches
The final destination for every change these days are the mainline repositories of the involved projects, there are no relevant linux-sunxi specific repositories anymore. 
Project | Purpose | git branch to patch against | work flow   
---|---|---|---  
[U-Boot][49244] | SPL initial loader and U-Boot bootloader | <https://source.denx.de/u-boot/u-boot> master | git / email   
[Crust][49245] | ARISC management processor firmware | <https://github.com/crust-firmware/crust> master | Github pull requests   
[TF-A][49246] | EL3 secure runtime firmware (PSCI) | <https://git.trustedfirmware.org/TF-A/trusted-firmware-a.git> master | [gerrit][49247]  
[Linux kernel][49248] | Kernel drivers and devicetrees | <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git> master | git / email   
[sunxi-tools][49249] | sunxi-fel and other development tools | <https://github.com/linux-sunxi/sunxi-tools> master | Github pull requests   
## Contents
  * [1 git / email based workflow][49250]
    * [1.1 Setting up git send-email][49251]
    * [1.2 Changes structure][49252]
    * [1.3 Creating patch emails][49253]
    * [1.4 Sending out patch emails][49254]
    * [1.5 Versioning][49255]
  * [2 More information][49256]

## git / email based workflow
U-Boot and the Linux kernel use an email based workflow, that sends git-formatted patches in email threads to maintainers and mailing lists. The process is explained in detail in the [kernel documentation][49257], the summary here provides a quick overview. 
### Setting up git send-email
While you can send the emails manually, this is tedious and error-prone. Using git-send-email simplifies the process significantly. To use the tool, you need to set this up (once), to tell git about the email server to use for sending out the emails. The configuration is held in the .gitconfig file in the home directory, which can be edited with any editor. Alternatively a git command can store each setting: 
[code] 
       git config --global sendemail.from _[[email protected]][49258]_
    
[/code]
The following settings (in the `[sendemail]` section) need to be set, please replace the placeholder values with the respective values for your setup: 
[code] 
       from = "_First Last <[[email protected]][49258]>_"
       smtpencryption = tls
       smtpserver = _smtp.yourprovider.com_
       smtpuser = _yourusernameforsmtp_
       smtpserverport = 587
       chainreplyto = false
    
[/code]
An example for GMail is shown in the [Git documentation][49259]. 
### Changes structure
  * The changes need to be initially in separate patches in a repository branched of the master branch. Sometimes other kernel.org branches like linux-next/master or sunxi/sunxi/for-next are better suited.
  * Each patch should cover a single, contained change.
  * Each patch needs to have at least a Signed-off-by: line from the patch author. You can also use the git commit `-s` (or `--signoff`) parameter in order to reduce typo's.
  * Each patch must have a short subject with a subsystem prefix: `mmc: sunxi-mmc: Add D1 MMC variant`
  * Each patch must have a descriptive commit message, explaining the reason for the patch and providing as much extra information as possible. (Trimmed) kernel error messages are OK to include. Commit messages can be elaborate.

### Creating patch emails
Each patch will be send in a separate email, with the body consisting of the commit message, followed by the actual patch, inlined to the email. No attachments! 
The `git format-patch` command takes care of creating those emails (as files), in the correct format. To prepare the emails for the 5 top patches of the current branch: 
[code] 
       $ git format-patch -5 --cover-letter HEAD
    
[/code]
You can change `HEAD` to point to any commit, as per git syntax. If you are sending follow-up versions of the same series, add `-v 2` to automatically insert the version number. 
For a single patch you can omit the `--cover-letter` option, any process related comments can go in the section after the three dashes in the email. 
The created email files should be briefly inspected, and _can_ be changed manually, although any changes should be done in the git repository, to allow re-creating the email files, for future resubmissions. 
### Sending out patch emails
You might need to install the git-email addon using your favorite package manager first. 
Always send the email files to yourself first, then skim through the mails in your (web) email client. This helps to spot any errors before the patches hit the list: 
[code] 
       $ git send-email --to [[email protected]][49258] --suppress-cc=all 00??-*.patch
    
[/code]
Make sure you don't have email files from previous submission lying around in the same directory. 
To learn about the recipients of the patches, use the `scripts/get_maintainer.pl` command in the Linux kernel (or U-Boot) source directory: 
[code] 
       $ scripts/get_maintainer.pl 00??-*.patch
    
[/code]
This will generate a long list of people and lists to include, along with a short rationale for their inclusion. Always include maintainers, best in To:, as they are the ones that need to deal with your patches. Include mailing lists in Cc:. Add people that you want to notify, that have been involved in the patches, that you hope to get reviews from, or that have hardware and can provide a Tested-by: tag, in Cc:. Do not include your managers or colleagues, unless they took part in the creation of the patches. If you need to notify people, put them in Bcc:, or send them a link to the thread in the mailing list archives. 
Eventually send the patches out: 
[code] 
       $ git send-email --to "Jane Maintainer <[[email protected]][49258]>" --to "Joe Maintainer <[[email protected]][49258]>" --cc [[email protected]][49258] --cc [[email protected]][49258] --cc [[email protected]][49258] --suppress-cc=all 00??-*.patch
    
[/code]
If you add `--bcc [[email protected]][49258]`, you will receive the patches in your regular inbox, so you can copy them to your Sent folder, and follow the correct threading in your email client. 
### Versioning
In case you get comments back from the community and you need to modify your patches and/or commit message you will need to supply versioning information on your attempts. The first go contains no versioning information and is considered version 1. All subsequent attempts need to include the increased version number. For later reference it might be a good idea to create separate branches for subsequent versions. Then regenerate the patch emails, specifying the version number in the format-patch command: 
[code] 
      $ git format-patch -5 -v 2 --cover-letter HEAD
    
[/code]
This will automatically change the subject prefix in the patch emails, and names the patch files with a version prefix, so they don't clash with previous versions. Alternatively, though that is not recommended, the version number could also be included in the `send-email` command: 
[code] 
      $ git send-email -v2 --subject-prefix="PATCH v2" [....] 00??-*.patch
    
[/code]
## More information
  * [(Old!) git send-email tricks][49260]
  * [Linux Documentation: Submitting patches][49257]
  * [(2010!)Youtube: Write and Submit your first Linux kernel Patch By Greg Kroah-Hartman][49261]
