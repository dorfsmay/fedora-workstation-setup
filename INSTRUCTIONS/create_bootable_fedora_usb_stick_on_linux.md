# Create a bootable Fedora USB stick on Linux

## On Fedora

**This is the easier method**.

* Use Fedora Media Writer. To install type the following in a terminal: `sudo dnf install mediawriter`
* hit the meta key (key on the left side of the left Alt key), and type `mediawriter` in the seachr bar, followed by the enter key

Once the mediawriter is runing:

* "Download automatically"
* Official Editions
* Write Options
    * Version: current version (eg: 38)
    * Hardware Architecture: Intel/AMD 64bit
    * USB Drive: the USB drive you inserted - **this will destroy everything on your USB stick**
* click on the "Write" button

Once finished:

* In File Manage (Nautilus), click on the USB dirve labeleed "Fedora-WS-Live" and eject. Accept to tempty trash if prompted
* remove drive


## Using the command line

1. Download Fedora Workstation ISO file from <https://getfedora.org/en/workstation/download/>

1. Insert USB stick

1. Use `lsblk -S` to find which device is Linux using for your USB device

1. **WARNING**: *The following step will* **destroy** *the content of* `/dev/sd�*`
    ```
    sudo dd bs=4M conv=fsync status=progress if=~/Downloads/Fedora-Workstation-xxx of=/dev/sd�
    ```

1. Either use "Eject" from the graphical file manager or run `sync` in a terminal

1. Remove USB stick
