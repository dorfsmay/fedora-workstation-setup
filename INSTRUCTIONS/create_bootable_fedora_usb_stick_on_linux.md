# Create a bootable Fedora USB stick on Linux

1. Download Fedora Workstation ISO file from <https://getfedora.org/en/workstation/download/>

1. Insert USB stick

1. Use `lsblk -S` `df -Th` to find which device is Linux using for your USB device

1. **WARNING**: *The following step will* **destroy** *the content of* `/dev/sd�*`
    ```
    sudo dd bs=4M conv=fsync status=progress if=~/Downloads/Fedora-Workstation-xxx of=/dev/sd�
    ```

1. Either use "Eject" from the graphical file manager or run `sync` in a terminal

1. Remove USB stick
