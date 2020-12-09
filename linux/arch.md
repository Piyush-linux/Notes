# Arch Linux
---
## pacman
__Install__ : `pacman -S _package_name1_ _package_name2_ ...`
  - S : synchronization.

__Remove__ : `pacman -R package_name_`
__Remove_dependencies__ : `pacman -Qdtq | pacman -Rs -`
__Upgrade__ : `pacman -Syu`
  - S stands for sync
    y is for refresh (local
    u is for system update
    
__search__ : `pacman -Ss _string1_ _string2_ ...`
  -a installed : `pacman -Qs _string1_ _string2_ ...`
  - 