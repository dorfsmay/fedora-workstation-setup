# Install Fedora

*Updated on 2020/11/22 for Fedora 33*

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
        - Done

  - SYSTEM
    - Installation Destination
      - Local Standard Disks
        - The disk should already be selected (checkmark)
      - Storage Configuration
        - Advanced Custom
        - **If** different than goal, delete all partitions
        - create new (if not already existing):
            - partition, 512 MiB, EFI System Partition, Label: EFI, Moutpoint: /boot/efi
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

1. Set up X.org
  - LOG OUT
  - type your username
  - click on the cogwheel/gear symbol at the bottom-right and select "GNOME on Xorg"
  - type your password, and enter

1. Host name and customization
  - open terminal
  - change host name:
```
hostnamectl set-hostname some-cool-name
```

You can now start customizing. Check the [instructions for the customization scripts](run_scripts.md), or the [scripts themselves](../idempotent).
