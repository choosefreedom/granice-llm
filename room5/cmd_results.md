# Wyniki komend — 2026-09-06 01:17

## `ps aux
`

```
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.0  26032 16992 ?        Ss   wrz05   0:02 /usr/lib/systemd/systemd --switched-root --system --deserialize=52 splash
root           2  0.0  0.0      0     0 ?        S    wrz05   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        S    wrz05   0:00 [pool_workqueue_release]
root           4  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-rcu_gp]
root           5  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-sync_wq]
root           6  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-kvfree_rcu_reclaim]
root           7  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-slub_flushwq]
root           8  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-netns]
root          10  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/0:0H-kblockd]
root          13  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-mm_percpu_wq]
root          14  0.0  0.0      0     0 ?        S    wrz05   0:00 [ksoftirqd/0]
root          15  0.0  0.0      0     0 ?        I    wrz05   0:01 [rcu_preempt]
root          16  0.0  0.0      0     0 ?        S    wrz05   0:00 [rcu_exp_par_gp_kthread_worker/0]
root          17  0.0  0.0      0     0 ?        S    wrz05   0:00 [rcu_exp_gp_kthread_worker]
root          18  0.0  0.0      0     0 ?        S    wrz05   0:00 [migration/0]
root          19  0.0  0.0      0     0 ?        S    wrz05   0:00 [kprobe-optimizer]
root          20  0.0  0.0      0     0 ?        S    wrz05   0:00 [idle_inject/0]
root          21  0.0  0.0      0     0 ?        S    wrz05   0:00 [cpuhp/0]
root          22  0.0  0.0      0     0 ?        S    wrz05   0:00 [cpuhp/1]
root          23  0.0  0.0      0     0 ?        S    wrz05   0:00 [idle_inject/1]
root          24  0.0  0.0      0     0 ?        S    wrz05   0:00 [migration/1]
root          25  0.0  0.0      0     0 ?        S    wrz05   0:00 [ksoftirqd/1]
root          27  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/1:0H-kblockd]
root          28  0.0  0.0      0     0 ?        S    wrz05   0:00 [cpuhp/2]
root          29  0.0  0.0      0     0 ?        S    wrz05   0:00 [idle_inject/2]
root          30  0.0  0.0      0     0 ?        S    wrz05   0:00 [migration/2]
root          31  0.0  0.0      0     0 ?        S    wrz05   0:00 [ksoftirqd/2]
root          33  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/2:0H-kblockd]
root          34  0.0  0.0      0     0 ?        S    wrz05   0:00 [cpuhp/3]
root          35  0.0  0.0      0     0 ?        S    wrz05   0:00 [idle_inject/3]
root          36  0.0  0.0      0     0 ?        S    wrz05   0:00 [migration/3]
root          37  0.0  0.0      0     0 ?        S    wrz05   0:00 [ksoftirqd/3]
root          39  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/3:0H-kblockd]
root          40  0.0  0.0      0     0 ?        S    wrz05   0:00 [cpuhp/4]
root          41  0.0  0.0      0     0 ?        S    wrz05   0:00 [idle_inject/4]
root          42  0.0  0.0      0     0 ?        S    wrz05   0:00 [migration/4]
root          43  0.0  0.0      0     0 ?        S    wrz05   0:00 [ksoftirqd/4]
root          45  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/4:0H-kblockd]
root          46  0.0  0.0      0     0 ?        S    wrz05   0:00 [cpuhp/5]
root          47  0.0  0.0      0     0 ?        S    wrz05   0:00 [idle_inject/5]
root          48  0.0  0.0      0     0 ?        S    wrz05   0:00 [migration/5]
root          49  0.0  0.0      0     0 ?        S    wrz05   0:00 [ksoftirqd/5]
root          51  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/5:0H-kblockd]
root          52  0.0  0.0      0     0 ?        S    wrz05   0:00 [kdevtmpfs]
root          53  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-inet_frag_wq]
root          54  0.0  0.0      0     0 ?        I    wrz05   0:00 [rcu_tasks_kthread]
root          55  0.0  0.0      0     0 ?        I    wrz05   0:00 [rcu_tasks_rude_kthread]
root          56  0.0  0.0      0     0 ?        S    wrz05   0:00 [kauditd]
root          57  0.0  0.0      0     0 ?        S    wrz05   0:00 [khungtaskd]
root          58  0.0  0.0      0     0 ?        S    wrz05   0:00 [oom_reaper]
root          61  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-writeback]
root          62  0.0  0.0      0     0 ?        S    wrz05   0:00 [kcompactd0]
root          63  0.0  0.0      0     0 ?        SN   wrz05   0:00 [ksmd]
root          64  0.0  0.0      0     0 ?        SN   wrz05   0:00 [khugepaged]
root          65  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-kblockd]
root          66  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-blkcg_punt_bio]
root          67  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-kintegrityd]
root          68  0.0  0.0      0     0 ?        S    wrz05   0:00 [irq/9-acpi]
root          70  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-tpm_dev_wq]
root          71  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-ata_sff]
root          72  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-md_bitmap]
root          73  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-md_llbitmap_io]
root          74  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-md_llbitmap_unplug]
root          75  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-edac-poller]
root          76  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-devfreq_wq]
root          77  0.0  0.0      0     0 ?        S    wrz05   0:00 [watchdogd]
root          79  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-quota_events_unbound]
root          80  0.0  0.0      0     0 ?        S    wrz05   0:00 [kswapd0]
root          81  0.0  0.0      0     0 ?        S    wrz05   0:00 [ecryptfs-kthread]
root          83  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-kthrotld]
root          84  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-acpi_thermal_pm]
root          85  0.0  0.0      0     0 ?        S    wrz05   0:00 [scsi_eh_0]
root          86  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-scsi_tmf_0]
root          87  0.0  0.0      0     0 ?        S    wrz05   0:00 [scsi_eh_1]
root          88  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-scsi_tmf_1]
root          93  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-mld]
root          94  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-ipv6_addrconf]
root          95  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-kstrp]
root          98  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/u25:0-ttm]
root         110  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-charger_manager]
root         199  0.0  0.0      0     0 ?        S    wrz05   0:00 [irq/18-vmwgfx]
root         200  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-ttm]
root         313  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-iprt-VBoxWQueue]
root         314  0.0  0.0      0     0 ?        S    wrz05   0:00 [scsi_eh_2]
root         315  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-scsi_tmf_2]
root         329  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/0:1H-kblockd]
root         333  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/4:1H-kblockd]
root         340  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/1:1H-kblockd]
root         341  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/2:1H-kblockd]
root         344  0.0  0.0      0     0 ?        S    wrz05   0:00 [jbd2/sda2-8]
root         345  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/R-ext4-rsv-conversion]
root         355  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/3:1H-kblockd]
root         388  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/5:1H-kblockd]
root         399  0.0  0.0  50928 21528 ?        S<s  wrz05   0:00 /usr/lib/systemd/systemd-journald
systemd+     448  0.0  0.0  16808  7628 ?        Ss   wrz05   0:01 /usr/lib/systemd/systemd-oomd
systemd+     452  0.0  0.0  22544 14960 ?        Ss   wrz05   0:00 /usr/lib/systemd/systemd-resolved
root         454  0.0  0.0  41464 15132 ?        Ss   wrz05   0:00 /usr/lib/systemd/systemd-udevd
root         459  0.0  0.0      0     0 ?        S    wrz05   0:00 [psimon]
avahi       1245  0.0  0.0   6744  4912 ?        Ss   wrz05   0:00 avahi-daemon: running [mimson-VirtualBox.local]
root        1246  0.0  0.0   2888  1944 ?        Ss   wrz05   0:00 /bin/sh /usr/lib/systemd/scripts/chronyd-starter.sh -n -F 1
message+    1247  0.0  0.0  12176  9072 ?        Ss   wrz05   0:02 @dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
root        1258  0.0  0.0  46828 30256 ?        Ss   wrz05   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
polkitd     1261  0.0  0.0 383248 11728 ?        Ssl  wrz05   0:00 /usr/lib/polkit-1/polkitd --no-debug --log-level=notice
root        1266  0.0  0.1 2182120 45532 ?       Ssl  wrz05   0:01 /usr/lib/snapd/snapd
root        1271  0.0  0.0 309960  9048 ?        Ssl  wrz05   0:00 /usr/libexec/accounts-daemon
root        1273  0.0  0.0   7060  3368 ?        Ss   wrz05   0:00 /usr/sbin/cron -f -P
root        1274  0.0  0.0 308132  8040 ?        Ssl  wrz05   0:00 /usr/libexec/switcheroo-control
root        1276  0.0  0.0  18612  9772 ?        Ss   wrz05   0:00 /usr/lib/systemd/systemd-logind
root        1277  0.0  0.0 544220 16608 ?        Ssl  wrz05   0:00 /usr/libexec/udisks2/udisksd
avahi       1291  0.0  0.0   6560  1620 ?        S    wrz05   0:00 avahi-daemon: chroot helper
_chrony     1355  0.0  0.0  23744 11328 ?        S    wrz05   0:00 /usr/sbin/chronyd -n -F 1
syslog      1357  0.0  0.0 220604  6464 ?        Ssl  wrz05   0:00 /usr/sbin/rsyslogd -n -iNONE
_chrony     1408  0.0  0.0  12120  3396 ?        S    wrz05   0:00 /usr/sbin/chronyd -n -F 1
root        1453  0.0  0.0 337084 22612 ?        Ssl  wrz05   0:01 /usr/sbin/NetworkManager --no-daemon
root        1457  0.0  0.0  17960  7076 ?        Ss   wrz05   0:00 /usr/sbin/wpa_supplicant -u -s -O DIR=/run/wpa_supplicant GROUP=netdev
root        1492  0.0  0.0 391608 14208 ?        Ssl  wrz05   0:00 /usr/sbin/ModemManager
root        1584  0.0  0.0   2900  1748 ?        Ss   wrz05   0:00 /bin/sh /snap/cups/1238/scripts/run-cups-browsed
root        1585  0.0  0.0   2900  1780 ?        Ss   wrz05   0:00 /bin/sh /snap/cups/1238/scripts/run-cupsd
root        1589  0.0  0.0 126044 32920 ?        Ssl  wrz05   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
root        1785  0.0  0.0 353148  2976 ?        Sl   wrz05   0:03 /usr/bin/VBoxDRMClient
root        1787  0.0  0.0 357616  3808 ?        Sl   wrz05   0:00 /usr/sbin/VBoxService --pidfile /var/run/vboxadd-service.sh
root        1813  0.0  0.0 384912 11124 ?        Ssl  wrz05   0:00 /usr/sbin/gdm3
root        1878  0.0  0.0      0     0 ?        S    wrz05   0:00 [psimon]
root        1990  0.0  0.0  61284 12856 ?        S    wrz05   0:00 cupsd -f -s /var/snap/cups/common/etc/cups/cups-files.conf -c /var/snap/cups/common/etc/cups/cupsd.conf
root        1991  0.0  0.0 241608 10196 ?        Sl   wrz05   0:00 cups-proxyd /var/snap/cups/common/run/cups.sock /run/cups/cups.sock -l --logdir /var/snap/cups/1238/var/log
rtkit       2026  0.0  0.0  87408  3664 ?        SNsl wrz05   0:00 /usr/libexec/rtkit-daemon
root        2154  0.0  0.0   2900   912 ?        S    wrz05   0:00 /bin/sh /snap/cups/1238/scripts/run-cups-browsed
colord      2187  0.0  0.0 317872 16788 ?        Ssl  wrz05   0:00 /usr/libexec/colord
ollama      2204  0.6  0.1 2332068 44216 ?       Ssl  wrz05   1:07 /usr/local/bin/ollama serve
root        2320  0.0  0.0 318976 11880 ?        Ssl  wrz05   0:00 /usr/libexec/upowerd
root        2771  0.0  0.0      0     0 ?        I<   wrz05   0:00 [kworker/u25:2]
root        2772  0.0  0.0 309516  8136 ?        Ssl  wrz05   0:00 /usr/libexec/power-profiles-daemon
root        2983  0.0  0.0 174760 12904 ?        Sl   wrz05   0:00 gdm-session-worker [pam/gdm-password]
mimson      3089  0.0  0.0  24404 15504 ?        Ss   wrz05   0:00 /usr/lib/systemd/systemd --user
mimson      3091  0.0  0.0  25000  4292 ?        S    wrz05   0:00 (sd-pam)
mimson      3126  0.0  0.0  10192  6968 ?        Ss   wrz05   0:01 /usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
mimson      3127  0.0  0.0 119996 13672 ?        Ssl  wrz05   0:00 /usr/bin/pipewire
mimson      3131  0.0  0.0 183612 11636 ?        SLsl wrz05   0:00 /usr/bin/gnome-keyring-daemon --foreground --components=pkcs11,secrets --control-directory=/run/user/1000/keyring
mimson      3144  0.0  0.0   7560  3908 ?        Ss   wrz05   0:00 /usr/bin/mpris-proxy
mimson      3147  0.0  0.0 488692 23188 ?        Ssl  wrz05   0:00 /usr/bin/wireplumber
mimson      3148  0.0  0.0  84812  5788 ?        Ssl  wrz05   0:00 /usr/bin/pipewire -c filter-chain.conf
mimson      3150  0.0  0.0 181348 13068 ?        Ssl  wrz05   0:00 /usr/bin/pipewire-pulse
mimson      3176  0.0  0.0 168540  7148 tty2     Ssl+ wrz05   0:00 /usr/libexec/gdm-wayland-session /usr/bin/gnome-session --session=ubuntu
mimson      3198  0.0  0.0 175204  9520 tty2     Sl+  wrz05   0:00 /usr/libexec/gnome-session-init-worker ubuntu
mimson      3227  0.0  0.0 762188  8260 ?        Ssl  wrz05   0:00 /usr/libexec/xdg-document-portal
mimson      3295  0.0  0.0 307688  7356 ?        Ssl  wrz05   0:00 /usr/libexec/xdg-permission-store
root        3322  0.0  0.0   2792  2236 ?        Ss   wrz05   0:00 fusermount3 -o rw,nosuid,nodev,fsname=portal,auto_unmount,subtype=portal -- /run/user/1000/doc
mimson      3393  0.0  0.0 310560  8508 ?        Ssl  wrz05   0:00 /usr/libexec/gcr-ssh-agent --base-dir /run/user/1000/gcr
mimson      3394  0.0  0.0  87208  5812 ?        Ssl  wrz05   0:00 /usr/libexec/gnome-session-ctl --monitor
mimson      3395  0.0  0.0  10484  6768 ?        Ss   wrz05   0:00 /usr/bin/ssh-agent -D
mimson      3407  0.0  0.0 313424  9444 ?        Ssl  wrz05   0:00 /usr/libexec/gvfsd
mimson      3413  0.0  0.0 324816  8092 ?        Sl   wrz05   0:00 /usr/libexec/gvfsd-fuse /run/user/1000/gvfs -f
mimson      3416  0.0  0.0 540120 12000 ?        Ssl  wrz05   0:00 /usr/libexec/gnome-session-service --session=ubuntu
mimson      3436  2.9  1.0 6212784 420932 ?      Ssl  wrz05   5:08 /usr/bin/gnome-shell --mode=ubuntu
mimson      3537  0.0  0.0 381068  8084 ?        Ssl  wrz05   0:00 /usr/libexec/at-spi-bus-launcher
mimson      3544  0.0  0.0   8740  5300 ?        S    wrz05   0:00 /usr/bin/dbus-daemon --config-file=/usr/share/defaults/at-spi2/accessibility.conf --nofork --print-address 11 --address=unix:path=/run/user/1000/at-spi/bus
mimson      3546  0.0  0.0 168688  7892 ?        Sl   wrz05   0:00 /usr/libexec/at-spi2-registryd --use-gnome-session
mimson      3566  0.0  0.0 659704 23688 ?        Sl   wrz05   0:00 /usr/libexec/gnome-shell-calendar-server
mimson      3573  0.0  0.1 1222856 46992 ?       Ssl  wrz05   0:00 /usr/libexec/evolution-source-registry
mimson      3583  0.0  0.0 2732788 33160 ?       Sl   wrz05   0:00 /usr/bin/gjs -m /usr/share/gnome-shell/org.gnome.Shell.Notifications
mimson      3596  0.0  0.0 459540 12156 ?        Ssl  wrz05   0:05 /usr/bin/ibus-daemon --panel disable
mimson      3597  0.0  0.0 254136 11092 ?        Ssl  wrz05   0:00 /usr/libexec/gsd-a11y-settings
mimson      3598  0.0  0.0 252148 10972 ?        Ssl  wrz05   0:00 /usr/libexec/gsd-color
mimson      3606  0.0  0.0 260500 13096 ?        Ssl  wrz05   0:00 /usr/libexec/gsd-datetime
mimson      3610  0.0  0.0 391344 11428 ?        Ssl  wrz05   0:00 /usr/libexec/gsd-housekeeping
mimson      3611  0.0  0.0 383476  8712 ?        Ssl  wrz05   0:00 /usr/libexec/gsd-keyboard
mimson      3615  0.0  0.0 625872 15332 ?        Ssl  wrz05   0:00 /usr/libexec/gsd-media-keys
mimson      3616  0.0  0.0 541272 12212 ?        Ssl  wrz05   0:00 /usr/libexec/gsd-power
mimson      3617  0.0  0.0 327976 14652 ?        Ssl  wrz05   0:00 /usr/libexec/gsd-print-notifications
mimson      3622  0.0  0.0 457320  8780 ?        Ssl  wrz05   0:00 /usr/libexec/gsd-rfkill
mimson      3625  0.0  0.0 170228  8080 ?        Ssl  wrz05   0:00 /usr/libexec/gsd-screensaver-proxy
mimson      3626  0.0  0.0 467740 13404 ?        Ssl  wrz05   0:00 /usr/libexec/gsd-sharing
mimson      3639  0.0  0.0 386052 10304 ?        Ssl  wrz05   0:00 /usr/libexec/gsd-smartcard
mimson      3641  0.0  0.0 312168  9760 ?        Sl   wrz05   0:00 /usr/libexec/gsd-disk-utility-notify
mimson      3643  0.0  0.0 255288 11260 ?        Ssl  wrz05   0:00 /usr/libexec/gsd-sound
mimson      3650  0.0  0.0 644024 35260 ?        Sl   wrz05   0:00 /usr/bin/update-notifier
mimson      3651  0.0  0.0 472548 10520 ?        Ssl  wrz05   0:00 /usr/libexec/gsd-usb-protection
mimson      3653  0.0  0.1 841904 69716 ?        Sl   wrz05   0:00 /usr/libexec/evolution-data-server/evolution-alarm-notify
mimson      3661  0.0  0.0 390760 11276 ?        Ssl  wrz05   0:00 /usr/libexec/gsd-wwan
mimson      3763  0.0  0.0 2730708 33112 ?       Sl   wrz05   0:00 /usr/bin/gjs -m /usr/share/gnome-shell/org.gnome.ScreenSaver
mimson      3766  0.0  0.0 473388 12800 ?        Sl   wrz05   0:00 /usr/libexec/gsd-printer
mimson      3768  0.0  0.0 243180  8392 ?        Sl   wrz05   0:00 /usr/libexec/ibus-dconf
mimson      3773  0.0  0.0 500712 37904 ?        Sl   wrz05   0:03 /usr/libexec/ibus-extension-gtk3
mimson      3785  0.0  0.0 308676  8392 ?        Sl   wrz05   0:00 /usr/libexec/ibus-portal
mimson      3791  0.0  0.0 466964 32508 ?        Sl   wrz05   0:00 /usr/libexec/goa-daemon
mimson      3812  0.0  0.1 212408 71100 ?        S    wrz05   0:00 /usr/bin/Xwayland :0 -rootless -noreset -accessx -core -auth /run/user/1000/.mutter-Xwaylandauth.PZ3WU3 -listenfd 4 -listenfd 5 -displayfd 6 -initfd 7 -byteswappedclients -enable-ei-portal
mimson      3814  0.0  0.0 803348 26032 ?        SNsl wrz05   0:01 /usr/libexec/localsearch-3
mimson      3817  0.0  0.0 629268 21376 ?        Ssl  wrz05   0:00 /usr/libexec/xdg-desktop-portal
mimson      3839  0.0  0.0 388120 10596 ?        Sl   wrz05   0:00 /usr/libexec/goa-identity-service
mimson      3866  0.0  0.1 688496 46508 ?        Ssl  wrz05   0:00 /usr/libexec/xdg-desktop-portal-gnome
mimson      3877  0.0  0.0 893568 27852 ?        Ssl  wrz05   0:00 /usr/libexec/evolution-calendar-factory
mimson      3888  0.0  0.0 169484  8344 ?        Sl   wrz05   0:01 /usr/libexec/ibus-engine-simple
mimson      3903  0.0  0.0 534868 12888 ?        Ssl  wrz05   0:00 /usr/libexec/gvfs-udisks2-volume-monitor
mimson      3952  0.0  0.0 826348 32340 ?        Ssl  wrz05   0:00 /usr/libexec/evolution-addressbook-factory
mimson      3956  0.0  0.0 309000  8108 ?        Ssl  wrz05   0:00 /usr/libexec/gvfs-gphoto2-volume-monitor
mimson      3967  0.0  0.0 308032  7604 ?        Ssl  wrz05   0:00 /usr/libexec/gvfs-mtp-volume-monitor
mimson      3977  0.0  0.0 390052  9736 ?        Ssl  wrz05   0:00 /usr/libexec/gvfs-afc-volume-monitor
mimson      3988  0.0  0.0 308012  7508 ?        Ssl  wrz05   0:00 /usr/libexec/gvfs-goa-volume-monitor
mimson      4020  0.0  0.2 3824644 84308 ?       Sl   wrz05   0:02 gjs /usr/share/gnome-shell/extensions/ding@rastersoft.com/app/ding.js -E -P /usr/share/gnome-shell/extensions/ding@rastersoft.com/app
mimson      4073  0.0  0.0 169120  7724 ?        Ssl  wrz05   0:00 /usr/libexec/gvfsd-metadata
mimson      4116  0.0  0.0 165352  6796 ?        Ssl  wrz05   0:00 /usr/libexec/dconf-service
mimson      4163  0.0  0.0 608604 10548 ?        Sl   wrz05   0:00 /usr/libexec/gvfsd-trash --spawner :1.21 /org/gtk/gvfs/exec_spaw/0
mimson      4291  0.0  0.0 251668 14036 ?        Ssl  wrz05   0:00 /usr/libexec/gsd-xsettings
mimson      4310  0.0  0.0  16864  1832 ?        S    wrz05   0:00 /usr/bin/VBoxClient --clipboard
mimson      4314  0.0  0.0 216768  9024 ?        Sl   wrz05   0:00 /usr/bin/VBoxClient --clipboard
mimson      4315  0.0  0.3 1718192 119412 ?      Sl   wrz05   0:00 /usr/libexec/mutter-x11-frames
mimson      4340  0.0  0.0  16864  1740 ?        S    wrz05   0:00 /usr/bin/VBoxClient --vmsvga-session
mimson      4341  0.0  0.0 148968  2300 ?        Sl   wrz05   0:00 /usr/bin/VBoxClient --vmsvga-session
mimson      4372  0.0  0.1 374012 72492 ?        Sl   wrz05   0:00 /usr/libexec/ibus-x11
mimson      4380  0.0  0.0 493064 29956 ?        Ssl  wrz05   0:00 /usr/libexec/xdg-desktop-portal-gtk
mimson      4516  0.0  0.0 303928  6520 ?        Ssl  wrz05   0:00 /snap/snapd-desktop-integration/391/usr/bin/user-session-helper /snap/snapd-desktop-integration/391/usr/bin/snapd-desktop-integration
mimson      4577  0.0  0.0 440260 36624 ?        Sl   wrz05   0:00 /snap/snapd-desktop-integration/391/usr/bin/snapd-desktop-integration
root        5866  0.1  0.0      0     0 ?        I    wrz05   0:15 [kworker/u24:0-events_unbound]
root       10065  0.0  0.0      0     0 ?        I    wrz05   0:00 [kworker/5:1-mm_percpu_wq]
root       10089  0.0  0.1 365956 46116 ?        Ssl  wrz05   0:00 /usr/libexec/fwupd/fwupd
root       10102  0.0  0.0      0     0 ?        I    wrz05   0:00 [kworker/1:2-events]
mimson     12163  0.0  0.0  10500  7052 ?        S    wrz05   0:00 /usr/bin/ssh-agent -D -a /run/user/1000/gcr/.ssh
root       12226  0.0  0.0      0     0 ?        I    wrz05   0:00 [kworker/3:0-events]
root       12287  0.0  0.0      0     0 ?        I    00:00   0:00 [kworker/0:0-events]
mimson     12544  0.0  0.0 387392 10064 ?        Sl   00:08   0:00 /usr/libexec/gvfsd-recent --spawner :1.21 /org/gtk/gvfs/exec_spaw/1
mimson     12546  0.0  0.0 387636 10352 ?        Sl   00:08   0:00 /usr/libexec/gvfsd-network --spawner :1.21 /org/gtk/gvfs/exec_spaw/2
mimson     12558  0.0  0.0 388648 10308 ?        Sl   00:08   0:00 /usr/libexec/gvfsd-dnssd --spawner :1.21 /org/gtk/gvfs/exec_spaw/3
mimson     12566  0.0  0.0 387064  9916 ?        Sl   00:08   0:00 /usr/libexec/gvfsd-wsdd --spawner :1.21 /org/gtk/gvfs/exec_spaw/4
mimson     12571  0.0  0.0  44808 33844 ?        S    00:08   0:00 python3 /usr/bin/wsdd --no-host --discovery --listen /run/user/1000/gvfsd/wsdd
uuidd      12577  0.0  0.0   8104  3380 ?        Ss   00:08   0:00 /usr/sbin/uuidd --socket-activation --cont-clock
mimson     13178  0.5  0.8 3640424 333396 ?      Sl   00:10   0:22 /usr/bin/nautilus --gapplication-service
root       21522  0.0  0.0   3220  1964 ?        S    00:20   0:00 sleep 3600
root       31280  0.0  0.0      0     0 ?        I    00:39   0:00 [kworker/2:0-cgroup_free]
root       31300  0.0  0.0      0     0 ?        I    00:40   0:00 [kworker/0:2]
root       31317  0.0  0.0      0     0 ?        I    00:40   0:00 [kworker/5:0]
root       38057  0.0  0.0      0     0 ?        I    00:50   0:00 [kworker/2:1-mm_percpu_wq]
root       39429  0.0  0.0      0     0 ?        I    00:54   0:00 [kworker/4:1-events]
root       39432  0.0  0.0      0     0 ?        I    00:54   0:00 [kworker/1:1-events]
root       42241  0.0  0.0  28932 12728 ?        Ss   01:00   0:00 /usr/sbin/cupsd -l
lp         42243  0.0  0.0  15436  7136 ?        S    01:00   0:00 /usr/lib/cups/notifier/dbus dbus://
lp         42244  0.0  0.0  15436  7100 ?        S    01:00   0:00 /usr/lib/cups/notifier/dbus dbus://
lp         42245  0.0  0.0  15436  7352 ?        S    01:00   0:00 /usr/lib/cups/notifier/dbus dbus://
lp         42246  0.0  0.0  15436  7232 ?        S    01:00   0:00 /usr/lib/cups/notifier/dbus dbus://
lp         42247  0.0  0.0  15436  7308 ?        S    01:00   0:00 /usr/lib/cups/notifier/dbus dbus://
lp         42248  0.0  0.0  15436  7192 ?        S    01:00   0:00 /usr/lib/cups/notifier/dbus dbus://
lp         42249  0.0  0.0  15436  7316 ?        S    01:00   0:00 /usr/lib/cups/notifier/dbus dbus://
lp         42250  0.0  0.0  15436  7192 ?        S    01:00   0:00 /usr/lib/cups/notifier/dbus dbus://
lp         42251  0.0  0.0  15436  7300 ?        S    01:00   0:00 /usr/lib/cups/notifier/dbus dbus://
lp         42252  0.0  0.0  15436  7260 ?        S    01:00   0:00 /usr/lib/cups/notifier/dbus dbus://
lp         42253  0.0  0.0  15436  7320 ?        S    01:00   0:00 /usr/lib/cups/notifier/dbus dbus://
lp         42254  0.0  0.0  15436  7196 ?        S    01:00   0:00 /usr/lib/cups/notifier/dbus dbus://
lp         42255  0.0  0.0  15436  7296 ?        S    01:00   0:00 /usr/lib/cups/notifier/dbus dbus://
lp         42256  0.0  0.0  15436  7280 ?        S    01:00   0:00 /usr/lib/cups/notifier/dbus dbus://
lp         42257  0.0  0.0  15436  7304 ?        S    01:00   0:00 /usr/lib/cups/notifier/dbus dbus://
lp         42258  0.0  0.0  15436  7356 ?        S    01:00   0:00 /usr/lib/cups/notifier/dbus dbus://
lp         42259  0.0  0.0  15436  7352 ?        S    01:00   0:00 /usr/lib/cups/notifier/dbus dbus://
lp         42260  0.0  0.0  15436  7380 ?        S    01:00   0:00 /usr/lib/cups/notifier/dbus dbus://
lp         42261  0.0  0.0  15436  7260 ?        S    01:00   0:00 /usr/lib/cups/notifier/dbus dbus://
cups-br+   42262  0.0  0.0 207540 22800 ?        Ssl  01:00   0:00 /usr/sbin/cups-browsed
root       42311  0.3  0.0      0     0 ?        I    01:00   0:03 [kworker/u24:4-flush-8:0]
root       44516  0.0  0.0      0     0 ?        I    01:08   0:00 [kworker/u24:2-events_power_efficient]
root       44529  0.0  0.0      0     0 ?        I    01:08   0:00 [kworker/3:1]
root       46407  0.0  0.0      0     0 ?        I    01:09   0:00 [kworker/1:0-events]
root       46423  0.0  0.0      0     0 ?        I    01:10   0:00 [kworker/4:3-cgroup_free]
root       46582  0.2  0.0      0     0 ?        I    01:14   0:00 [kworker/u24:1-events_unbound]
mimson     46619  5.4  1.1 3629860 444512 ?      Sl   01:15   0:06 /usr/bin/gnome-text-editor --gapplication-service
mimson     46803 17.0  0.6 3274888 257588 ?      Rl   01:17   0:00 ptyxis --new-window --working-directory /home/mimson/Pulpit/projekt/granice-llm/room5
mimson     46817  0.0  0.0 239948  7976 ?        Ssl  01:17   0:00 /usr/libexec/ptyxis-agent --socket-fd=3 --rlimit-nofile=1024
mimson     46858  0.2  0.0   9016  5952 pts/0    Ss+  01:17   0:00 /usr/bin/bash
mimson     46859  0.2  0.0   9016  6004 pts/1    Ss   01:17   0:00 /usr/bin/bash
mimson     46878 33.3  0.0  20564 12908 pts/1    S+   01:17   0:00 python3 commands.py
mimson     46881  0.0  0.0   2888  1924 pts/1    S+   01:17   0:00 /bin/sh -c ps aux 
mimson     46882  100  0.0  10164  4896 pts/1    R+   01:17   0:00 ps aux
```

