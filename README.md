# vm-osinstall-configs

OS install configurations for my local VMs that I use for testing.

## How to use

### Arch Linux

1. Boot up from [ISO](https://archlinux.org/download/)
1. Run the command:
```bash
archinstall --config https://osinstall.jacken.men/arch/config.json
```
1. Wait for the installation to finish.

### Ubuntu Linux 18.04

1. Boot up from [ISO](https://cdimage.ubuntu.com/releases/18.04/release/) (Note: the "**Live** Server" ISO won't work)
1. Choose English as the language.
1. Edit the default boot commands by hitting F6, followed by Esc key.

    Append this to the end of the boot options:
    ```
    auto locale=en_US keymap=pl interface=auto hostname=ubuntu1804 url=https://osinstall.jacken.men/ubuntu1804/preseed.cfg
    ```
    Hit Enter key.

1. Wait for the installation to finish.

### Ubuntu Linux 20.04

1. Boot up from [ISO](https://releases.ubuntu.com/focal/)

    Hold Shift key while booting in order to show the boot menu.
1. Choose English as the language.
1. Edit the default boot commands by hitting F6, followed by Esc key.

    Append this to the end of the boot options (slash at the end is important):
    ```
    ds=nocloud-net;s=https://osinstall.jacken.men/ubuntu2004/
    ```
    Hit Enter key.
1. Wait for the installation to finish.
