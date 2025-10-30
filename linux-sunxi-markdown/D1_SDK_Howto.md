# D1 SDK Howto
This page walks you through building Allwinners own SDK for the [D1][15841] SoC, using [the mirror we have on our server][15842], and [an adjusted git-repo manifest][15843]. 
The original SDK as created by Allwinner was behind a registration wall, which includes a click-through disclaimer that is at odds with the GPL. Since we have [our own mirror][15842], this is actually open, and this howto describes how to use it. 
## Contents
  * [1 Get git-repo][15844]
    * [1.1 Arch Linux based distributions][15845]
    * [1.2 Debian based distributions][15846]
      * [1.2.1 Caveat: python-3][15847]
  * [2 Point repo at the manifest][15848]
  * [3 Let repo get all the repositories][15849]
  * [4 See also][15850]

# Get git-repo
## Arch Linux based distributions
[code] 
    pacman -S repo
[/code]
## Debian based distributions
[code] 
    apt-get install repo
[/code]
### Caveat: python-3
Repo downloads a copy of itself to .repo, and that version will trip over on itself if it gets started with python-2 (which is the default still on debian stable/buster). 
When you run repo in the next section, and you get: 
[code] 
      File "/home/user/dir/.repo/repo/main.py", line 79
        file=sys.stderr)
            ^
    SyntaxError: invalid syntax
[/code]
Then you might need to switch to python-3. Here it cryptically tripped over the print() command which does not exist in python-2. 
To get around this, check what python versions are available: 
[code] 
    # ls /usr/bin/python*
    /usr/bin/python   /usr/bin/python2.7  /usr/bin/python3.7   /usr/bin/python3m
    /usr/bin/python2  /usr/bin/python3    /usr/bin/python3.7m
[/code]
And then point alternatives to the python-3 bin: 
[code] 
    update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1
[/code]
Verify: 
[code] 
    # python --version
    Python 3.7.3
[/code]
You will need to restore python-2, if you want to run the repo utility that your debian system knows, as that hard depends on python 2. 
[code] 
    update-alternatives --remove python /usr/bin/python3.7
    update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
[/code]
When you then run _sync_ again, you will have to dance the same dance all over again. WTF? Git-repo developers, WTF? 
# Point repo at the manifest
[code] 
    repo init -u https://github.com/linux-sunxi/d1-sdk-manifest.git -b master -m tina-d1-open.xml
[/code]
If all goes well, it will state: 
[code] 
    repo has been initialized in /home/user/dir
[/code]
# Let repo get all the repositories
[code] 
     repo sync 
[/code]
# See also
