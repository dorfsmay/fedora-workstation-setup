# Brother printer driver for Linux

*Instructions specific to the Brother DCP-L2550DW printer scanner*.

Download the driver from the Brother site:  
https://support.brother.com/g/b/downloadlist.aspx?c=ca&lang=en&prod=dcpl2550dw_us&os=127

1. From "Printer Drivers", download "Linux printer driver (rpm package)"

1. From "Scanner Drivers", download "Scanner driver 64bit (rpm package)"

1. Open a terminal and:
```
dpkg -i brscan4*.deb
brsaneconfig4 -q
brsaneconfig4 -a
```
A list scanners on the network will appear, select the one you want to use and click "OK".
