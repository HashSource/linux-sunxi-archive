# Packaging
# Libv's ultra simplistic reprepro workflow
This is my ultra-simplistic, non-scalable reprepro workflow, which is currently responsible for [ubuntu repo][44019]. This is not a workflow proposal, it is documenting what is behind the current respository, before we start throwing stuff around. 
Alejandro kindly linked /srv/http/sunxi/linux-sunxi.org/packages/ubuntu to ~/ubuntu 
I have a directory called reprepro, and a .bash_profile which reads: 
[code] 
     export REPREPRO_BASE_DIR=/home/libv/reprepro 
[/code]
So that i avoid accidentally recreating a new database and config somewhere else, leaving the whole thing in a disjoined state. 
In ~/reprepro/conf/options, it reads: 
[code] 
    outdir /home/libv/ubuntu
    keepunreferencedfiles
    
[/code]
I like to keep "older" packages around, so that people with slightly older package lists, or people who wish to compare different versions of the same code, can all be happy campers. 
In ~/reprepro/conf/distributions, it reads: 
[code] 
    Origin: packages.linux-sunxi.org
    Label: Linux-sunxi ubuntu precise repository
    Codename: precise
    Architectures: armhf source
    Components: main
    Description: Linux-sunxi ubuntu Precise Pangolin package repo
    
    Origin: packages.linux-sunxi.org
    Label: Linux-sunxi ubuntu quantal repository
    Codename: quantal
    Architectures: armhf source
    Components: main
    Description: Linux-sunxi ubuntu Quantal Quetzal package repo
    
    Origin: packages.linux-sunxi.org
    Label: Linux-sunxi ubuntu raring repository
    Codename: raring
    Architectures: armhf source
    Components: main
    Description: Linux-sunxi ubuntu Raring Ringtail package repo
    
    Origin: packages.linux-sunxi.org
    Label: Linux-sunxi ubuntu saucy repository
    Codename: saucy
    Architectures: armhf source
    Components: main
    Description: Linux-sunxi ubuntu Saucy Salamander package repo
[/code]
Note that SignWith directives are lacking, i am currently not signing packages. 
I then manually scp packages into ~/incoming/ and manually run, for instance: 
[code] 
    reprepro -V includedeb saucy *.deb
    reprepro -V includedsc saucy *.dsc
    
[/code]
while clearing out ~/incoming manually afterwards.
