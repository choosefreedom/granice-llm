# Wyniki komend — 2026-09-07 23:26

## `pwd
`

```
/home/mimson/Pulpit/projekt/granice-llm/room16
```

## `ls -la
`

```
total 104
drwxrwxr-x  3 mimson mimson  4096 Sep  7 23:26 .
drwxrwxr-x 34 mimson mimson  4096 Sep  7 23:20 ..
-rw-rw-r--  1 mimson mimson  1794 Sep  6 02:01 Modelfile
-rw-rw-r--  1 mimson mimson   410 Sep  6 00:05 Todo.md
-rw-rw-r--  1 mimson mimson  8062 Sep  7 22:42 ai_results_v1.md
-rw-rw-r--  1 mimson mimson  4047 Sep  7 23:04 ai_results_v1_check.md
-rw-rw-r--  1 mimson mimson  7031 Sep  7 22:36 ai_results_v2.md
-rw-rw-r--  1 mimson mimson  4861 Sep  7 22:56 ai_results_v2_check.md
-rw-rw-r--  1 mimson mimson 10813 Sep  7 22:40 ai_results_v3.md
-rw-rw-r--  1 mimson mimson  2433 Sep  7 22:29 attacks
-rw-rw-r--  1 mimson mimson  1220 Sep  7 22:52 attacks_check
drwxrwxr-x  2 mimson mimson  4096 Sep  7 23:25 bash
-rw-rw-r--  1 mimson mimson   105 Sep  7 23:26 cmd_results.md
-rw-rw-r--  1 mimson mimson    68 Sep  7 23:22 commands
-rwxrwxr-x  1 mimson mimson  1193 Sep  6 00:05 commands.py
-rw-rw-r--  1 mimson mimson    31 Sep  6 00:05 final_question
-rw-rw-r--  1 mimson mimson   147 Sep  7 22:28 modelfile_v1
-rw-rw-r--  1 mimson mimson   316 Sep  7 22:28 modelfile_v2
-rw-rw-r--  1 mimson mimson  1794 Sep  7 22:28 modelfile_v3
-rw-rw-r--  1 mimson mimson   125 Sep  7 16:18 questions
-rwxrwxr-x  1 mimson mimson   137 Sep  5 23:40 runcmd
```

## `sudo ss -tulpn
`

```
Netid State  Recv-Q Send-Q                     Local Address:Port  Peer Address:PortProcess                                   
udp   UNCONN 0      0                                0.0.0.0:5353       0.0.0.0:*    users:(("avahi-daemon",pid=1244,fd=12))  
udp   UNCONN 0      0                                0.0.0.0:51197      0.0.0.0:*    users:(("python3",pid=4615,fd=9))        
udp   UNCONN 0      0                             127.0.0.54:53         0.0.0.0:*    users:(("systemd-resolve",pid=453,fd=18))
udp   UNCONN 0      0                          127.0.0.53%lo:53         0.0.0.0:*    users:(("systemd-resolve",pid=453,fd=16))
udp   UNCONN 0      0                              127.0.0.1:323        0.0.0.0:*    users:(("chronyd",pid=1345,fd=4))        
udp   UNCONN 0      0                          192.168.0.102:3702       0.0.0.0:*    users:(("python3",pid=4615,fd=10))       
udp   UNCONN 0      0                        239.255.255.250:3702       0.0.0.0:*    users:(("python3",pid=4615,fd=8))        
udp   UNCONN 0      0                                      *:37116            *:*    users:(("firefox",pid=165777,fd=174))    
udp   UNCONN 0      0                                   [::]:5353          [::]:*    users:(("avahi-daemon",pid=1244,fd=13))  
udp   UNCONN 0      0                                      *:53063            *:*    users:(("firefox",pid=165777,fd=54))     
udp   UNCONN 0      0                                      *:32937            *:*    users:(("python3",pid=4615,fd=12))       
udp   UNCONN 0      0                                  [::1]:323           [::]:*    users:(("chronyd",pid=1345,fd=5))        
udp   UNCONN 0      0      [fe80::a00:27ff:fee7:327a]%enp0s3:546           [::]:*    users:(("NetworkManager",pid=1455,fd=28))
udp   UNCONN 0      0      [fe80::a00:27ff:fee7:327a]%enp0s3:3702          [::]:*    users:(("python3",pid=4615,fd=13))       
udp   UNCONN 0      0                       [ff02::c]%enp0s3:3702          [::]:*    users:(("python3",pid=4615,fd=11))       
tcp   LISTEN 0      4096                          127.0.0.54:53         0.0.0.0:*    users:(("systemd-resolve",pid=453,fd=19))
tcp   LISTEN 0      4096                           127.0.0.1:11434      0.0.0.0:*    users:(("ollama",pid=2199,fd=3))         
tcp   LISTEN 0      4096                           127.0.0.1:631        0.0.0.0:*    users:(("cupsd",pid=32103,fd=7))         
tcp   LISTEN 0      4096                       127.0.0.53%lo:53         0.0.0.0:*    users:(("systemd-resolve",pid=453,fd=17))
tcp   LISTEN 0      10                             127.0.0.1:53742      0.0.0.0:*    users:(("VBoxClient",pid=4179,fd=11))    
tcp   LISTEN 0      4096                               [::1]:631           [::]:*    users:(("cupsd",pid=32103,fd=6))
```

## `systemctl list-unit-files --state=enabled
`

```
UNIT FILE                                           STATE   PRESET
run-vmblock\x2dfuse.mount                           enabled enabled
snap-bare-5.mount                                   enabled enabled
snap-core18-2999.mount                              enabled enabled
snap-core20-2866.mount                              enabled enabled
snap-core22-2437.mount                              enabled enabled
snap-core24-1587.mount                              enabled enabled
snap-core24-1643.mount                              enabled enabled
snap-core26-462.mount                               enabled enabled
snap-cups-1238.mount                                enabled enabled
snap-desktop\x2dsecurity\x2dcenter-150.mount        enabled enabled
snap-desktop\x2dsecurity\x2dcenter-151.mount        enabled enabled
snap-firefox-8803.mount                             enabled enabled
snap-firefox-8863.mount                             enabled enabled
snap-firmware\x2dupdater-226.mount                  enabled enabled
snap-gnome\x2d3\x2d28\x2d1804-198.mount             enabled enabled
snap-gnome\x2d46\x2d2404-153.mount                  enabled enabled
snap-gnome\x2d46\x2d2404-164.mount                  enabled enabled
snap-gtk\x2dcommon\x2dthemes-1535.mount             enabled enabled
snap-mesa\x2d2404-1165.mount                        enabled enabled
snap-mesa\x2d2404-1839.mount                        enabled enabled
snap-prompting\x2dclient-204.mount                  enabled enabled
snap-prompting\x2dclient-222.mount                  enabled enabled
snap-snap\x2dstore-1367.mount                       enabled enabled
snap-snap\x2dstore-1390.mount                       enabled enabled
snap-snapd-26865.mount                              enabled enabled
snap-snapd-27710.mount                              enabled enabled
snap-snapd\x2ddesktop\x2dintegration-361.mount      enabled enabled
snap-snapd\x2ddesktop\x2dintegration-391.mount      enabled enabled
snap-wine\x2dplatform-154.mount                     enabled enabled
snap-wine\x2dplatform\x2druntime\x2dcore24-23.mount enabled enabled
apport-autoreport.path                              enabled enabled
cups.path                                           enabled enabled
tpm-udev.path                                       enabled enabled
accounts-daemon.service                             enabled enabled
anacron.service                                     enabled enabled
apparmor.service                                    enabled enabled
apport.service                                      enabled enabled
avahi-daemon.service                                enabled enabled
bluetooth.service                                   enabled enabled
chrony.service                                      enabled enabled
cloud-config.service                                enabled enabled
cloud-final.service                                 enabled enabled
cloud-init-local.service                            enabled enabled
cloud-init-main.service                             enabled enabled
cloud-init-network.service                          enabled enabled
console-setup.service                               enabled enabled
cron.service                                        enabled enabled
cups-browsed.service                                enabled enabled
cups.service                                        enabled enabled
dmesg.service                                       enabled enabled
e2scrub_reap.service                                enabled enabled
getty@.service                                      enabled enabled
gpu-manager.service                                 enabled enabled
grub-initrd-fallback.service                        enabled enabled
grub2-common.service                                enabled enabled
kdump-tools.service                                 enabled enabled
keyboard-setup.service                              enabled enabled
ModemManager.service                                enabled enabled
netplan-configure.service                           enabled enabled
networkd-dispatcher.service                         enabled enabled
NetworkManager-dispatcher.service                   enabled enabled
NetworkManager-wait-online.service                  enabled enabled
NetworkManager.service                              enabled enabled
ollama.service                                      enabled enabled
open-vm-tools.service                               enabled enabled
openvpn.service                                     enabled enabled
power-profiles-daemon.service                       enabled enabled
rsyslog.service                                     enabled enabled
secureboot-db.service                               enabled enabled
setvtrgb.service                                    enabled enabled
snap.cups.cups-browsed.service                      enabled enabled
snap.cups.cupsd.service                             enabled enabled
snapd.apparmor.service                              enabled enabled
snapd.autoimport.service                            enabled enabled
snapd.core-fixup.service                            enabled enabled
snapd.recovery-chooser-trigger.service              enabled enabled
snapd.seeded.service                                enabled enabled
snapd.service                                       enabled enabled
snapd.system-shutdown.service                       enabled enabled
ssl-cert.service                                    enabled enabled
sssd.service                                        enabled enabled
switcheroo-control.service                          enabled enabled
sysstat.service                                     enabled enabled
systemd-oomd.service                                enabled enabled
systemd-pstore.service                              enabled enabled
systemd-resolved.service                            enabled enabled
thermald.service                                    enabled enabled
ua-reboot-cmds.service                              enabled enabled
ubuntu-advantage.service                            enabled enabled
udisks2.service                                     enabled enabled
ufw.service                                         enabled enabled
unattended-upgrades.service                         enabled enabled
vboxadd-service.service                             enabled enabled
vboxadd.service                                     enabled enabled
vgauth.service                                      enabled enabled
wpa_supplicant.service                              enabled enabled
wtmpdb-update-boot.service                          enabled enabled
apport-forward.socket                               enabled enabled
avahi-daemon.socket                                 enabled enabled
cloud-init-hotplugd.socket                          enabled enabled
cups.socket                                         enabled enabled
polkit-agent-helper.socket                          enabled enabled
snapd.socket                                        enabled enabled
sssd-autofs.socket                                  enabled enabled
sssd-nss.socket                                     enabled enabled
sssd-pac.socket                                     enabled enabled
sssd-pam.socket                                     enabled enabled
sssd-ssh.socket                                     enabled enabled
sssd-sudo.socket                                    enabled enabled
systemd-oomd.socket                                 enabled enabled
systemd-resolved-monitor.socket                     enabled enabled
systemd-resolved-varlink.socket                     enabled enabled
uuidd.socket                                        enabled enabled
remote-fs.target                                    enabled enabled
anacron.timer                                       enabled enabled
apport-autoreport.timer                             enabled enabled
apt-daily-upgrade.timer                             enabled enabled
apt-daily.timer                                     enabled enabled
dpkg-db-backup.timer                                enabled enabled
e2scrub_all.timer                                   enabled enabled
fstrim.timer                                        enabled enabled
fwupd-refresh.timer                                 enabled enabled
logrotate.timer                                     enabled enabled
man-db.timer                                        enabled enabled
motd-news.timer                                     enabled enabled
snapd.snap-repair.timer                             enabled enabled
sysstat-collect.timer                               enabled enabled
sysstat-rotate.timer                                enabled enabled
sysstat-summary.timer                               enabled enabled
ua-timer.timer                                      enabled enabled
update-notifier-download.timer                      enabled enabled
update-notifier-motd.timer                          enabled enabled

132 unit files listed.
```

