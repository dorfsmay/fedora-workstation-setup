# Install Fedora
*Updated on 2025/12/12 for Fedora 43*

## Note about swap space
How much swap sapce do you need: short answer, use 8 GiB.

There isn't a universal long answer, unless you know you what hibernate is and you know you will use it, otherwise the answer varies from 8 GiB, to square root of physical memory to 20% of physical memory!

## How to check amount of physical memory during install
**If**, during the install, you wanted to know  how much memory is installed on your laptop, for example to decide on how much swap space to use, use the folloing steps:

* ctrl-alt-F1
* use root to login, no passwd
* `free -h` and note the total for Mem
* `exit`
* ctrl-alt-f2

## Install

1. Install Default OS
  - boot from USB
  - Start Fedora-Workstation-Live
  - Install to Hard Drive
  - What language would you like to use during the installation process?
      - English, English (Canada)
      - Continue

  - LOCALIZATION
    - Time & Date
        - Americas / Edmonton
        - "Network Time" Should be enabled, if not, enable it
        - Done (upper left-hand corner)

  - SYSTEM
    - Installation Destination
      - Local Standard Disks
        - The disk should already be selected (checkmark)
      - Storage Configuration
        - Advanced Custom
        - Done
        - **If** different than goal, delete all partitions (select partition, hit the delete key, or right click + delete)
        - create new (if not already existing):
            - partition, 512 MiB, EFI System Partition, Label: EFI, Moutpoint: /boot/efi
            - Calculate the size for the main partition by substracting what you want for swap (use 8 GiB for swap if you're not sure)
            - partition, xxx GiB, EFI System Partition, Label: root, Moutpoint: /
            - partition, size: rest (click on + if needed) , Filesystem: swap, Label: swap
        - Done
        - Accept Changes

    - Begin Installation
    - Finish Installation
  - Restart

1. Set wifi, user id, password, etc...
  - Start Setup
    - setup wifi, next
    - Privacy
      - Location Services: off
      - Automatic Problem Reporting: on
      - Next
    - Third-Party Repositories
      - enable
    - Connect Your Online Accounts
      - skip
    - About You
      - fill in name and user id
      - Next
    - Set a password
      - *not password*
      - *not password*
      - Next
   - Start Using Fedora

1. Host name and customization
  - open terminal (hit the Windows key, then type `terminal`, then type enter)
  - change host name:
```
hostnamectl set-hostname some-cool-name
```

You can now start customizing. Check the [instructions for the customization scripts](run_scripts.md), or the [scripts themselves](../idempotent).
