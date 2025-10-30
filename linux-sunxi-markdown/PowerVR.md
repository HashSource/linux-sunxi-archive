# PowerVR
This page is still mostly a stub, please add to it! 
# Overview
PowerVR is a line of GPU by Imagination Technologies. It has zero Free Software/Open Source support right now, and the associated development effort seems to be regarded as very high. Imagination has hinted they were considering addressssing the problem[[1]][45570] but today the position seem to be still open[[2]][45571]
It is regarded as more powerful than the [Mali400][45572] GPU found in other SoCs (needs ref). 
A Free Software driver for PowerVR is considered as a high priority project by the FSF[[3]][45573] and a project has indeed been setup[[4]][45574]. 
Imagination Technologies published a linux driver for their binary microkernel under a dual license: MIT & GPL v2. [[5]][45575]
on 2022 Imagination Tech is publishing a new open-source driver, both on DRM side [[6]][45576] and Mesa Vulkan driver [[7]][45577]. Imagination's driver focus on their newer PowerVR "Rogue" GPUs starting from series6XT (for example the GX6250, dated Jan 2014), but maybe with minor modification this driver can be used on older series6 (like G6230, dated Jun 2012). 
  
Allwinner SoC with a PowerVR GPU: 
SOC  | PowerVR GPU  | Revision   
---|---|---  
[A31][45578] | SGX544 or [SGX544MP2][45579] | 1.1.5   
[A83T][45580] | [SGX544MP1][45579] | 1.1.5   
[A80][45581] | G6230  | ?   
# References
  1. [↑][45582] <http://www.cnx-software.com/2015/06/18/open-source-linux-drivers-for-powervr-gpus-might-be-in-the-works/> CNX blog entry
  2. [↑][45583] [https://careers.imgtec.com/#/vacancy/details/2619][45584] Open position at Imagination Technologies
  3. [↑][45585] <http://www.fsf.org/campaigns/priority.html> High Priority Free Software Projects
  4. [↑][45586] <http://powervr.gnu.org.ve/doku.php> Collecting information about the PowerVR architecture
  5. [↑][45587] <https://github.com/LeMaker/linux-actions/tree/linux-3.10.y/drivers/gpu/pvr> LeMaker Integrated it into their 3.10.y kernel
  6. [↑][45588] [https://lore.kernel.org/all/[email protected]/][45589]
  7. [↑][45590] <https://lists.freedesktop.org/archives/mesa-dev/2022-March/225699.html>

# External links
  * <https://libreplanet.org/wiki/Group:PowerVR_drivers>
