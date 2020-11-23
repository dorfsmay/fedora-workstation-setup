# Laptop Setup Fedora

Install and customize [Fedora Workstation](https://getfedora.org/en/workstation/).

## Customization
The [instructions](./INSTRUCTIONS) and [scripts](idempotent) are specific to my needs and differ from a default setup:
* using standard partitions instead of LVM
* using ext4 instead of brtfs
* /boot on the root partition
* defaults to X.org instead of Wayland
* gnome customization???
* set default local language to en\_CA.UTF-8 (canadian English)
* Setup dual language keyboard for English and French
* Change GNOME terminal to dark-on-light mode
* Changes GNOME terminal default font

## Why using Bash

It was a conscious decision to use GNU Bash as the programming language despite its many flaws for reasons which distinguish it from recent build systems:

* Bash is well known and an integral part of Linux systems. Anybody familiar with customizing Linux systems has already been exposed to Bash.

* Perennity: [Bash has been around for a long time, since 1988](https://en.wikipedia.org/wiki/Bash_\(Unix_shell\)#History) (note: [Linux was created in 1991](https://en.wikipedia.org/wiki/Linux#Creation)). [Lindy effect](https://en.wikipedia.org/wiki/Lindy_effect) predicts that it will be around for at least another 30 years.




