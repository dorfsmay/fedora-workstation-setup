# pCloud

## Installation
1. Download "pCloud Drive for Linux 64bit" from <https://www.pcloud.com/download-free-online-cloud-file-storage.html>  
In "Choose your version", select "Linux 64bit"

1. in a terminal:
```
mkdir -p ~/.local/bin
chmod +x ~/Downloads/pcloud
mv ~/Downloads/pcloud ~/.local/bin/.
```

## Upgrade
1. Right click on the pCloud icon
1. Preferences
1. About
1. Upgrade

If it does not restart automatically, start it manually.

## Start manually
[Alt] + [F2] → pcloud → `[Enter]

## Kill the process
If the process does not terminate when doind right-click-exit, open a terminal and:
```
pkill -f pcloud
```
