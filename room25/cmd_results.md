# Wyniki komend — 2026-09-06 01:21

## `cat /etc/passwd
`

```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:998:998:systemd Network Management:/:/usr/sbin/nologin
systemd-timesync:x:996:996:systemd Time Synchronization:/:/usr/sbin/nologin
dhcpcd:x:100:65534:DHCP Client Daemon,,,:/usr/lib/dhcpcd:/bin/false
messagebus:x:101:101::/nonexistent:/usr/sbin/nologin
syslog:x:102:102::/nonexistent:/usr/sbin/nologin
systemd-resolve:x:991:991:systemd Resolver:/:/usr/sbin/nologin
polkitd:x:990:990:User for polkitd:/:/usr/sbin/nologin
usbmux:x:103:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
tss:x:104:103:TPM software stack,,,:/var/lib/tpm:/bin/false
rtkit:x:105:104:RealtimeKit,,,:/proc:/usr/sbin/nologin
systemd-coredump:x:989:989:systemd Core Dumper:/:/usr/sbin/nologin
uuidd:x:106:107::/run/uuidd:/usr/sbin/nologin
cups-pk-helper:x:107:105:user for cups-pk-helper service,,,:/nonexistent:/usr/sbin/nologin
avahi-autoipd:x:108:111:Avahi autoip daemon,,,:/var/lib/avahi-autoipd:/usr/sbin/nologin
kernoops:x:109:65534:Kernel Oops Tracking Daemon,,,:/:/usr/sbin/nologin
avahi:x:110:112:Avahi mDNS daemon,,,:/run/avahi-daemon:/usr/sbin/nologin
dnsmasq:x:999:65534:dnsmasq:/var/lib/misc:/usr/sbin/nologin
_flatpak:x:111:115:Flatpak system-wide installation helper,,,:/nonexistent:/usr/sbin/nologin
nm-openvpn:x:112:116:NetworkManager OpenVPN,,,:/var/lib/openvpn/chroot:/usr/sbin/nologin
lightdm:x:113:117:Light Display Manager:/var/lib/lightdm:/bin/false
tcpdump:x:114:119::/nonexistent:/usr/sbin/nologin
speech-dispatcher:x:115:29:Speech Dispatcher,,,:/run/speech-dispatcher:/bin/false
fwupd-refresh:x:988:988:Firmware update daemon:/var/lib/fwupd:/usr/sbin/nologin
geoclue:x:116:120::/var/lib/geoclue:/usr/sbin/nologin
cups-browsed:x:117:105::/nonexistent:/usr/sbin/nologin
saned:x:118:123::/var/lib/saned:/usr/sbin/nologin
hplip:x:119:7:HPLIP system user,,,:/run/hplip:/bin/false
colord:x:120:124:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
red:x:1000:1000:red,,,:/home/red:/bin/bash
sssd:x:121:126:SSSD system user,,,:/var/lib/sss:/usr/sbin/nologin
swtpm:x:122:127:virtual TPM software stack,,,:/var/lib/swtpm:/bin/false
libvirt-qemu:x:64055:993:Libvirt Qemu,,,:/var/lib/libvirt:/usr/sbin/nologin
libvirt-dnsmasq:x:123:129:Libvirt Dnsmasq,,,:/var/lib/libvirt/dnsmasq:/usr/sbin/nologin
ollama:x:997:986::/usr/share/ollama:/bin/false
```

## `grep -vE 'nologin|false' /etc/passwd
`

```
root:x:0:0:root:/root:/bin/bash
sync:x:4:65534:sync:/bin:/bin/sync
red:x:1000:1000:red,,,:/home/red:/bin/bash
```

## `getent group sudo
`

```
sudo:x:27:red
```

## `getent group adm
`

```
adm:x:4:syslog,red
```

## `awk -F: '$3 == 0 {print $1}' /etc/passwd
`

```
root
```

## `sudo -l
`

```
Matching Defaults entries for red on wra:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty, pwfeedback

User red may run the following commands on wra:
    (ALL : ALL) ALL
    (root) NOPASSWD: /usr/bin/mintdrivers-remove-live-media
    (root) NOPASSWD: /usr/bin/mintdrivers-load-broadcom-modules
    (root) NOPASSWD: /usr/bin/mint-refresh-cache
    (root) NOPASSWD: /usr/lib/linuxmint/mintUpdate/dpkg_lock_check.sh
```

## `sudo cat /etc/sudoers
`

```
sudo: a terminal is required to read the password; either use the -S option to read from standard input or configure an askpass helper
sudo: a password is required
```

## `sudo ls -la /etc/sudoers.d/
`

```
sudo: a terminal is required to read the password; either use the -S option to read from standard input or configure an askpass helper
sudo: a password is required
```

## `sudo systemctl status ssh
`

```
sudo: a terminal is required to read the password; either use the -S option to read from standard input or configure an askpass helper
sudo: a password is required
```

## `sudo grep -E '^{PermitRootLogin|PasswordAuthentication|PubkeyAuthentication)' /etc/ssh/sshd_config
`

```
sudo: a terminal is required to read the password; either use the -S option to read from standard input or configure an askpass helper
sudo: a password is required
```

## `find /home /root -name authorized_keys -type f 2>/dev/null
`

```

```

## `systemctl list-units --type=service --state=running
`

```
  UNIT                          LOAD   ACTIVE SUB     DESCRIPTION
  accounts-daemon.service       loaded active running Accounts Service
  avahi-daemon.service          loaded active running Avahi mDNS/DNS-SD Stack
  colord.service                loaded active running Manage, Install and Generate Color Profiles
  cron.service                  loaded active running Regular background program processing daemon
  cups-browsed.service          loaded active running Make remote CUPS printers available locally
  cups.service                  loaded active running CUPS Scheduler
  dbus.service                  loaded active running D-Bus System Message Bus
  fwupd.service                 loaded active running Firmware update daemon
  getty@tty1.service            loaded active running Getty on tty1
  irqbalance.service            loaded active running irqbalance daemon
  kerneloops.service            loaded active running Tool to automatically collect and submit kernel crash signatures
  lightdm.service               loaded active running Light Display Manager
  ModemManager.service          loaded active running Modem Manager
  NetworkManager.service        loaded active running Network Manager
  ollama.service                loaded active running Ollama Service
  polkit.service                loaded active running Authorization Manager
  power-profiles-daemon.service loaded active running Power Profiles daemon
  rsyslog.service               loaded active running System Logging Service
  rtkit-daemon.service          loaded active running RealtimeKit Scheduling Policy Service
  switcheroo-control.service    loaded active running Switcheroo Control Proxy service
  systemd-journald.service      loaded active running Journal Service
  systemd-logind.service        loaded active running User Login Management
  systemd-machined.service      loaded active running Virtual Machine and Container Registration Service
  systemd-resolved.service      loaded active running Network Name Resolution
  systemd-timesyncd.service     loaded active running Network Time Synchronization
  systemd-udevd.service         loaded active running Rule-based Manager for Device Events and Files
  touchegg.service              loaded active running Touchégg Daemon
  udisks2.service               loaded active running Disk Manager
  upower.service                loaded active running Daemon for power management
  user@1000.service             loaded active running User Manager for UID 1000
  virtlockd.service             loaded active running libvirt locking daemon
  virtlogd.service              loaded active running libvirt logging daemon
  wpa_supplicant.service        loaded active running WPA supplicant

Legend: LOAD   → Reflects whether the unit definition was properly loaded.
        ACTIVE → The high-level unit activation state, i.e. generalization of SUB.
        SUB    → The low-level unit activation state, values depend on unit type.

33 loaded units listed.
```

## `sudo ss -tulpn
`

```
sudo: a terminal is required to read the password; either use the -S option to read from standard input or configure an askpass helper
sudo: a password is required
```

## `apt list --upgradable
`

```
Listing...
attr/noble-updates,noble-security 1:2.5.2-1ubuntu0.1 amd64 [upgradable from: 1:2.5.2-1build1.1]
bind9-dnsutils/noble-updates,noble-security 1:9.18.39-0ubuntu0.24.04.7 amd64 [upgradable from: 1:9.18.39-0ubuntu0.24.04.6]
bind9-host/noble-updates,noble-security 1:9.18.39-0ubuntu0.24.04.7 amd64 [upgradable from: 1:9.18.39-0ubuntu0.24.04.6]
bind9-libs/noble-updates,noble-security 1:9.18.39-0ubuntu0.24.04.7 amd64 [upgradable from: 1:9.18.39-0ubuntu0.24.04.6]
bsdextrautils/noble-updates,noble-security 2.39.3-9ubuntu6.6 amd64 [upgradable from: 2.39.3-9ubuntu6.5]
bsdutils/noble-updates,noble-security 1:2.39.3-9ubuntu6.6 amd64 [upgradable from: 1:2.39.3-9ubuntu6.5]
coreutils/noble-updates,noble-security 9.4-3ubuntu6.3 amd64 [upgradable from: 9.4-3ubuntu6.2]
cpio/noble-updates,noble-security 2.15+dfsg-1ubuntu2.1 amd64 [upgradable from: 2.15+dfsg-1ubuntu2]
diffutils/noble-updates,noble-security 1:3.10-1ubuntu0.1 amd64 [upgradable from: 1:3.10-1build1]
dirmngr/noble-updates,noble-security 2.4.4-2ubuntu17.6 amd64 [upgradable from: 2.4.4-2ubuntu17.4]
dnsmasq-base/noble-updates 2.91-0ubuntu0.24.04.1 amd64 [upgradable from: 2.90-2ubuntu0.4]
eject/noble-updates,noble-security 2.39.3-9ubuntu6.6 amd64 [upgradable from: 2.39.3-9ubuntu6.5]
fdisk/noble-updates,noble-security 2.39.3-9ubuntu6.6 amd64 [upgradable from: 2.39.3-9ubuntu6.5]
firefox-locale-en/zara 155.0.1+linuxmint1+zena amd64 [upgradable from: 154.0.1+linuxmint1+zena]
firefox/zara 155.0.1+linuxmint1+zena amd64 [upgradable from: 154.0.1+linuxmint1+zena]
gir1.2-javascriptcoregtk-4.1/noble-updates,noble-security 2.52.6-0ubuntu0.24.04.1 amd64 [upgradable from: 2.52.3-0ubuntu0.24.04.1]
gir1.2-udisks-2.0/noble-updates,noble-security 2.10.1-6ubuntu1.5 amd64 [upgradable from: 2.10.1-6ubuntu1.3]
gir1.2-webkit2-4.1/noble-updates,noble-security 2.52.6-0ubuntu0.24.04.1 amd64 [upgradable from: 2.52.3-0ubuntu0.24.04.1]
gnupg-utils/noble-updates,noble-security 2.4.4-2ubuntu17.6 amd64 [upgradable from: 2.4.4-2ubuntu17.4]
gnupg/noble-updates,noble-updates,noble-security,noble-security 2.4.4-2ubuntu17.6 all [upgradable from: 2.4.4-2ubuntu17.4]
gpg-agent/noble-updates,noble-security 2.4.4-2ubuntu17.6 amd64 [upgradable from: 2.4.4-2ubuntu17.4]
gpg/noble-updates,noble-security 2.4.4-2ubuntu17.6 amd64 [upgradable from: 2.4.4-2ubuntu17.4]
gpgconf/noble-updates,noble-security 2.4.4-2ubuntu17.6 amd64 [upgradable from: 2.4.4-2ubuntu17.4]
gpgsm/noble-updates,noble-security 2.4.4-2ubuntu17.6 amd64 [upgradable from: 2.4.4-2ubuntu17.4]
gpgv/noble-updates,noble-security 2.4.4-2ubuntu17.6 amd64 [upgradable from: 2.4.4-2ubuntu17.4]
keyboxd/noble-updates,noble-security 2.4.4-2ubuntu17.6 amd64 [upgradable from: 2.4.4-2ubuntu17.4]
libattr1/noble-updates,noble-security 1:2.5.2-1ubuntu0.1 amd64 [upgradable from: 1:2.5.2-1build1.1]
libblkid1/noble-updates,noble-security 2.39.3-9ubuntu6.6 amd64 [upgradable from: 2.39.3-9ubuntu6.5]
libevent-2.1-7t64/noble-updates,noble-security 2.1.12-stable-9ubuntu2.1 amd64 [upgradable from: 2.1.12-stable-9ubuntu2]
libfdisk1/noble-updates,noble-security 2.39.3-9ubuntu6.6 amd64 [upgradable from: 2.39.3-9ubuntu6.5]
libgcrypt20/noble-updates,noble-security 1.10.3-2ubuntu0.2 amd64 [upgradable from: 1.10.3-2ubuntu0.1]
libjavascriptcoregtk-4.1-0/noble-updates,noble-security 2.52.6-0ubuntu0.24.04.1 amd64 [upgradable from: 2.52.3-0ubuntu0.24.04.1]
libjavascriptcoregtk-6.0-1/noble-updates,noble-security 2.52.6-0ubuntu0.24.04.1 amd64 [upgradable from: 2.52.3-0ubuntu0.24.04.1]
libmount1/noble-updates,noble-security 2.39.3-9ubuntu6.6 amd64 [upgradable from: 2.39.3-9ubuntu6.5]
libncurses6/noble-updates,noble-security 6.4+20240113-1ubuntu2.2 amd64 [upgradable from: 6.4+20240113-1ubuntu2.1]
libncursesw6/noble-updates,noble-security 6.4+20240113-1ubuntu2.2 amd64 [upgradable from: 6.4+20240113-1ubuntu2.1]
librabbitmq4/noble-updates,noble-security 0.11.0-1ubuntu0.2 amd64 [upgradable from: 0.11.0-1ubuntu0.1]
libsmartcols1/noble-updates,noble-security 2.39.3-9ubuntu6.6 amd64 [upgradable from: 2.39.3-9ubuntu6.5]
libssh-4/noble-updates,noble-security 0.10.6-2ubuntu0.5 amd64 [upgradable from: 0.10.6-2ubuntu0.4]
libssh-gcrypt-4/noble-updates,noble-security 0.10.6-2ubuntu0.5 amd64 [upgradable from: 0.10.6-2ubuntu0.4]
libtinfo6/noble-updates,noble-security 6.4+20240113-1ubuntu2.2 amd64 [upgradable from: 6.4+20240113-1ubuntu2.1]
libudisks2-0/noble-updates,noble-security 2.10.1-6ubuntu1.5 amd64 [upgradable from: 2.10.1-6ubuntu1.3]
libuuid1/noble-updates,noble-security 2.39.3-9ubuntu6.6 amd64 [upgradable from: 2.39.3-9ubuntu6.5]
libwebkit2gtk-4.1-0/noble-updates,noble-security 2.52.6-0ubuntu0.24.04.1 amd64 [upgradable from: 2.52.3-0ubuntu0.24.04.1]
libwebkitgtk-6.0-4/noble-updates,noble-security 2.52.6-0ubuntu0.24.04.1 amd64 [upgradable from: 2.52.3-0ubuntu0.24.04.1]
linux-firmware/noble-updates,noble-updates 20240318.git3b128b60.0ubuntu3.1 amd64 [upgradable from: 20240318.git3b128b60-0ubuntu2.29]
linux-generic-hwe-24.04/noble-updates,noble-security 7.0.0-31.31~24.04.1 amd64 [upgradable from: 7.0.0-30.30~24.04.1]
linux-headers-generic-hwe-24.04/noble-updates,noble-security 7.0.0-31.31~24.04.1 amd64 [upgradable from: 7.0.0-30.30~24.04.1]
linux-image-generic-hwe-24.04/noble-updates,noble-security 7.0.0-31.31~24.04.1 amd64 [upgradable from: 7.0.0-30.30~24.04.1]
linux-libc-dev/noble-updates,noble-security 6.8.0-139.139 amd64 [upgradable from: 6.8.0-138.138]
linux-tools-common/noble-updates,noble-updates,noble-security,noble-security 6.8.0-139.139 all [upgradable from: 6.8.0-138.138]
mount/noble-updates,noble-security 2.39.3-9ubuntu6.6 amd64 [upgradable from: 2.39.3-9ubuntu6.5]
ncurses-base/noble-updates,noble-updates,noble-security,noble-security 6.4+20240113-1ubuntu2.2 all [upgradable from: 6.4+20240113-1ubuntu2.1]
ncurses-bin/noble-updates,noble-security 6.4+20240113-1ubuntu2.2 amd64 [upgradable from: 6.4+20240113-1ubuntu2.1]
openssh-client/noble-updates,noble-security 1:9.6p1-3ubuntu13.19 amd64 [upgradable from: 1:9.6p1-3ubuntu13.18]
python3-pil/noble-updates,noble-security 10.2.0-1ubuntu1.3 amd64 [upgradable from: 10.2.0-1ubuntu1.2]
rfkill/noble-updates,noble-security 2.39.3-9ubuntu6.6 amd64 [upgradable from: 2.39.3-9ubuntu6.5]
thunderbird-locale-en-us/zara,zara 1:153.2.0esr+linuxmint1+zena all [upgradable from: 1:153.1.1esr+linuxmint1+zena]
thunderbird-locale-en/zara,zara 1:153.2.0esr+linuxmint1+zena all [upgradable from: 1:153.1.1esr+linuxmint1+zena]
thunderbird/zara 1:153.2.0esr+linuxmint1+zena amd64 [upgradable from: 1:153.1.1esr+linuxmint1+zena]
udisks2/noble-updates,noble-security 2.10.1-6ubuntu1.5 amd64 [upgradable from: 2.10.1-6ubuntu1.3]
util-linux/noble-updates,noble-security 2.39.3-9ubuntu6.6 amd64 [upgradable from: 2.39.3-9ubuntu6.5]
uuid-runtime/noble-updates,noble-security 2.39.3-9ubuntu6.6 amd64 [upgradable from: 2.39.3-9ubuntu6.5]
zlib1g/noble-updates,noble-security 1:1.3.dfsg-3.1ubuntu2.2 amd64 [upgradable from: 1:1.3.dfsg-3.1ubuntu2.1]

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.
```

## `uname -a
`

```
Linux wra 7.0.0-30-generic #30~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Fri Aug  7 13:27:52 UTC 2 x86_64 x86_64 x86_64 GNU/Linux
```

## `
`

```

```

