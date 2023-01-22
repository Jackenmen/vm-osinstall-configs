# vm-osinstall-configs

OS install configurations for my local VMs that I use for testing.

## How to use

### AlmaLinux 8

1. Boot up from [ISO](https://mirrors.almalinux.org/isos/x86_64/8.4.html)
1. Edit the default boot commands by hitting Tab key.

    Append this to the end of the boot options:
    ```
    inst.ks=https://osinstall.jacken.men/alma8/ks.cfg
    ```
    Hit Enter key.

1. Wait for the installation to finish.

### Arch Linux

1. Boot up from [ISO](https://archlinux.org/download/)
1. Run the command:
```bash
archinstall --config https://osinstall.jacken.men/arch/config.json
```
1. Wait for the installation to finish.

### CentOS 7

1. Boot up from [ISO](http://isoredirect.centos.org/centos/7/isos/x86_64/)
1. Edit the default boot commands by hitting Tab key.

    Append this to the end of the boot options:
    ```
    ip=eth0:dhcp inst.ks=https://osinstall.jacken.men/centos7/ks.cfg
    ```
    Hit Enter key.

1. Wait for the installation to finish.

### CentOS 8

1. Boot up from [ISO](http://isoredirect.centos.org/centos/8/isos/x86_64/)
1. Edit the default boot commands by hitting Tab key.

    Append this to the end of the boot options:
    ```
    inst.ks=https://osinstall.jacken.men/centos8/ks.cfg
    ```
    Hit Enter key.

1. Wait for the installation to finish.

### CentOS Stream 8

1. Boot up from [ISO](http://isoredirect.centos.org/centos/8-stream/isos/x86_64/)
1. Edit the default boot commands by hitting Tab key.

    Append this to the end of the boot options:
    ```
    inst.ks=https://osinstall.jacken.men/centos8-stream/ks.cfg
    ```
    Hit Enter key.

1. Wait for the installation to finish.

### CentOS Stream 9

1. Boot up from [ISO](http://mirror.stream.centos.org/9-stream/BaseOS/x86_64/iso/)
1. Edit the default boot commands by hitting Tab key.

    Append this to the end of the boot options:
    ```
    inst.ks=https://osinstall.jacken.men/centos9-stream/ks.cfg
    ```
    Hit Enter key.

1. Wait for the installation to finish.

### Debian 10 Buster

1. Boot up from [ISO](https://www.debian.org/releases/buster/debian-installer/)
1. Choose Advanced options->Automated install
1. (if on VirtualBox) Choose ``enp0s3`` interface in the installer.
1. Input the URL of preconfiguration file:

    ```
    https://osinstall.jacken.men/debian10/preseed.cfg
    ```
1. Wait for the installation to finish.

### Debian 11 Buster

1. Boot up from [ISO](https://www.debian.org/releases/bullseye/debian-installer/)
1. Choose Advanced options->Automated install
1. (if on VirtualBox) Choose ``enp0s3`` interface in the installer.
1. Input the URL of preconfiguration file:

    ```
    https://osinstall.jacken.men/debian11/preseed.cfg
    ```
1. Wait for the installation to finish.

### Fedora Server 33

1. Boot up from [ISO](https://download.fedoraproject.org/pub/fedora/linux/releases/33/Server/x86_64/iso/)
1. Edit the default boot commands by hitting Tab key.

    Append this to the end of the boot options:
    ```
    inst.ks=https://osinstall.jacken.men/fedora33/ks.cfg
    ```
    Hit Enter key.

1. Wait for the installation to finish.

### Fedora Server 34

1. Boot up from [ISO](https://download.fedoraproject.org/pub/fedora/linux/releases/34/Server/x86_64/iso/)
1. Edit the default boot commands by hitting Tab key.

    Append this to the end of the boot options:
    ```
    inst.ks=https://osinstall.jacken.men/fedora34/ks.cfg
    ```
    Hit Enter key.

1. Wait for the installation to finish.

### Fedora Server 35

1. Boot up from [ISO](https://download.fedoraproject.org/pub/fedora/linux/releases/35/Server/x86_64/iso/)
1. Edit the default boot commands by hitting Tab key.

    Append this to the end of the boot options:
    ```
    inst.ks=https://osinstall.jacken.men/fedora35/ks.cfg
    ```
    Hit Enter key.

1. Wait for the installation to finish.

### Oracle Linux 8

1. Boot up from [ISO](https://yum.oracle.com/oracle-linux-isos.html)
1. Edit the default boot commands by hitting Tab key.

    Append this to the end of the boot options:
    ```
    inst.ks=https://osinstall.jacken.men/ol8/ks.cfg
    ```
    Hit Enter key.

1. Wait for the installation to finish.

### openSUSE Leap 15.2

1. Boot up from [ISO](https://download.opensuse.org/distribution/leap/15.2/iso/openSUSE-Leap-15.2-NET-x86_64-Current.iso)
1. Select **Installation**, type these boot options and hit Enter key:

    ```
    autoyast=https://osinstall.jacken.men/opensuse-leap152/autoinst.xml
    ```

1. Wait for the installation to finish.

### openSUSE Leap 15.3

1. Boot up from [ISO](https://download.opensuse.org/distribution/leap/15.3/iso/openSUSE-Leap-15.3-NET-x86_64-Current.iso)
1. Select **Installation**, type these boot options and hit Enter key:

    ```
    autoyast=https://osinstall.jacken.men/opensuse-leap153/autoinst.xml
    ```

1. Wait for the installation to finish.

### openSUSE Tumbleweed

1. Boot up from [ISO](https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-NET-x86_64-Current.iso)
1. Select **Installation**, type these boot options and hit Enter key:

    ```
    autoyast=https://osinstall.jacken.men/opensuse-tumbleweed/autoinst.xml
    ```

1. Wait for the installation to finish.

### Red Hat Enterprise Linux 8

1. Boot up from [ISO](https://developers.redhat.com/products/rhel/download)
1. Edit the default boot commands by hitting Tab key.

    Append this to the end of the boot options:
    ```
    inst.ks=https://osinstall.jacken.men/rhel8/ks.cfg
    ```
    Hit Enter key.

1. Click on **Connect to Red Hat** and register this RHEL installation.
1. Click on **Begin Installation**.
1. Wait for the installation to finish.

### Rocky Linux 8

1. Boot up from [ISO](https://rockylinux.org/download/)
1. Edit the default boot commands by hitting Tab key.

    Append this to the end of the boot options:
    ```
    inst.ks=https://osinstall.jacken.men/rocky8/ks.cfg
    ```
    Hit Enter key.

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

### Ubuntu Linux 22.04

1. Boot up from [ISO](https://releases.ubuntu.com/jammy/)
1. Edit the default boot commands by hitting e.

    Go to the line starting with `linux` and append this to the end of it (slash at the end is important):
    ```
    autoinstall ds='nocloud-net;s=https://osinstall.jacken.men/ubuntu2204/'
    ```
    Hit F10 key.
1. Wait for the installation to finish.
