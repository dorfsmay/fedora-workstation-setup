# Fedora Workstation Setup

Install and customize [Fedora Workstation](https://getfedora.org/en/workstation/).

## Customization
The [instructions](./INSTRUCTIONS/README.md) and [scripts](idempotent) are specific to my needs and differ from a default setup:
* using standard partitions instead of LVM
* using ext4 instead of brtfs
* /boot on the root partition
* gnome customization
* set default local language to en\_CA.UTF-8 (canadian English)
* Setup dual language keyboard for English and French
* Change GNOME terminal to dark-on-light mode
* Changes GNOME terminal default font

## Why using Bash

It was a conscious decision to use GNU Bash as the programming language despite its many flaws for reasons which distinguish it from recent build systems:

* Bash is well known and an integral part of Linux systems. Anybody familiar with customizing Linux systems has already been exposed to Bash.

* Perennity: [Bash has been around for a long time, since 1988](https://en.wikipedia.org/wiki/Bash_\(Unix_shell\)#History) (note: [Linux was created in 1991](https://en.wikipedia.org/wiki/Linux#Creation)). [Lindy effect](https://en.wikipedia.org/wiki/Lindy_effect) predicts that it will be around for at least another 30 years.

## Other Fedora customization pages

* https://github.com/wz790/Fedora-Noble-Setup

* https://github.com/devangshekhawat/Fedora-43-Post-Install-Guide

## Upgrading from Fedora 43 to Fedora 44
* in a terminal and run:
  ```
  hostnamectl
  ```
  Ensure the "Operating System" is "Fedora Linux 43". **Do not proceed** if it is a different name or version.
* in a terminal, run:  
  ```
  sudo dnf upgrade --refresh
  ```
* reboot
* open a terminal and run - the last step takes a while. Run this while on wifi, do **not** run it while on phone data plan:
  ```
  sudo dnf install dnf-plugin-system-upgrade
  sudo dnf remove tlp
  sudo dnf system-upgrade download --releasever=44
  ```
* Once the step above is complete, run:  
  ```
  sudo dnf system-upgrade reboot
  ```
  The machine will reboot and spend some time upgrading all the packages.
* Once you can log back in, open a terminal and run:
  ```
  systemctl --user stop localsearch-3.service
  systemctl --user mask localsearch-3.service
  gsettings set org.gnome.desktop.interface gtk-enable-primary-paste true
  sudo dnf install @workstation-product-environment
  ```

#### Optional: terminal preferences
* preferences, at the top, click left-handed circle (Follow System Style)
* preferences, preferences, Appearance tab, click on "All Palettes", select "Everforest"
* preferences, preferences, Behavior tab:
  * Restore Window Size, off
  * Shell, Use Login Shell
