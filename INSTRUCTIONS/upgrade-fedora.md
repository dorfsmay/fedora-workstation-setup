# Upgrade Fedora

[Fedora creates two major OS releases every year, targeted for the fourth Tuesday in April and October](https://docs.fedoraproject.org/en-US/releases/), which are supported for the next 13 months. Make sure to upgrade before the release you use reaches [end-of-life](https://en.wikipedia.org/wiki/Fedora_Linux_release_history#Release_history). Trying to upgrade sometime in January and June should provide a good balance between being supported and not being burned by early bugs. Downloading the new release can take a long time, make sure you have a good internet connection and will be able to let your laptop on and open for a while, possibly overnight.

Unfortunately the "Software" app does not provide any feedback and can be stuck while not downloading anything hence preferring the use of the Command Line Interface. All the following commands need to be run from a "Terminal".


1. Update the current release:
    ```
    sudo dnf --refresh update
    sudo dnf upgrade
    ```

1. reboot

1. Download the new version (replace xx with the latest Fedora release):
    ```
    sudo dnf system-upgrade download --releasever=xx
    ```
This step can take a **very long time**. Do not close or shutdown your laptop while this is happening.

1. Reboot:
    ```
    dnf system-upgrade reboot
    ```

While rebooting the system will upgrade all its packages which will take 15 to 20 minutes.
