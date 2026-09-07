# Wyniki komend — 2026-09-07 23:22

## `ps aux
`

```
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.0  28016 18000 ?        Ss   16:08   0:02 /usr/lib/systemd/systemd --switched-root --system --deserialize=52 splash
root           2  0.0  0.0      0     0 ?        S    16:08   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        S    16:08   0:00 [pool_workqueue_release]
root           4  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-rcu_gp]
root           5  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-sync_wq]
root           6  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-kvfree_rcu_reclaim]
root           7  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-slub_flushwq]
root           8  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-netns]
root          10  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/0:0H-kblockd]
root          13  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-mm_percpu_wq]
root          14  0.0  0.0      0     0 ?        S    16:08   0:00 [ksoftirqd/0]
root          15  0.0  0.0      0     0 ?        I    16:08   0:03 [rcu_preempt]
root          16  0.0  0.0      0     0 ?        S    16:08   0:00 [rcu_exp_par_gp_kthread_worker/0]
root          17  0.0  0.0      0     0 ?        S    16:08   0:00 [rcu_exp_gp_kthread_worker]
root          18  0.0  0.0      0     0 ?        S    16:08   0:00 [migration/0]
root          19  0.0  0.0      0     0 ?        S    16:08   0:00 [kprobe-optimizer]
root          20  0.0  0.0      0     0 ?        S    16:08   0:00 [idle_inject/0]
root          21  0.0  0.0      0     0 ?        S    16:08   0:00 [cpuhp/0]
root          22  0.0  0.0      0     0 ?        S    16:08   0:00 [cpuhp/1]
root          23  0.0  0.0      0     0 ?        S    16:08   0:00 [idle_inject/1]
root          24  0.0  0.0      0     0 ?        S    16:08   0:00 [migration/1]
root          25  0.0  0.0      0     0 ?        S    16:08   0:00 [ksoftirqd/1]
root          27  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/1:0H-kblockd]
root          28  0.0  0.0      0     0 ?        S    16:08   0:00 [cpuhp/2]
root          29  0.0  0.0      0     0 ?        S    16:08   0:00 [idle_inject/2]
root          30  0.0  0.0      0     0 ?        S    16:08   0:00 [migration/2]
root          31  0.0  0.0      0     0 ?        S    16:08   0:00 [ksoftirqd/2]
root          33  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/2:0H-kblockd]
root          34  0.0  0.0      0     0 ?        S    16:08   0:00 [cpuhp/3]
root          35  0.0  0.0      0     0 ?        S    16:08   0:00 [idle_inject/3]
root          36  0.0  0.0      0     0 ?        S    16:08   0:00 [migration/3]
root          37  0.0  0.0      0     0 ?        S    16:08   0:00 [ksoftirqd/3]
root          39  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/3:0H-kblockd]
root          40  0.0  0.0      0     0 ?        S    16:08   0:00 [cpuhp/4]
root          41  0.0  0.0      0     0 ?        S    16:08   0:00 [idle_inject/4]
root          42  0.0  0.0      0     0 ?        S    16:08   0:00 [migration/4]
root          43  0.0  0.0      0     0 ?        S    16:08   0:00 [ksoftirqd/4]
root          45  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/4:0H-kblockd]
root          46  0.0  0.0      0     0 ?        S    16:08   0:00 [cpuhp/5]
root          47  0.0  0.0      0     0 ?        S    16:08   0:00 [idle_inject/5]
root          48  0.0  0.0      0     0 ?        S    16:08   0:00 [migration/5]
root          49  0.0  0.0      0     0 ?        S    16:08   0:00 [ksoftirqd/5]
root          51  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/5:0H-kblockd]
root          52  0.0  0.0      0     0 ?        S    16:08   0:00 [kdevtmpfs]
root          53  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-inet_frag_wq]
root          54  0.0  0.0      0     0 ?        I    16:08   0:00 [rcu_tasks_kthread]
root          55  0.0  0.0      0     0 ?        I    16:08   0:00 [rcu_tasks_rude_kthread]
root          56  0.0  0.0      0     0 ?        S    16:08   0:00 [kauditd]
root          57  0.0  0.0      0     0 ?        S    16:08   0:00 [khungtaskd]
root          58  0.0  0.0      0     0 ?        S    16:08   0:00 [oom_reaper]
root          61  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-writeback]
root          62  0.0  0.0      0     0 ?        S    16:08   0:00 [kcompactd0]
root          63  0.0  0.0      0     0 ?        SN   16:08   0:00 [ksmd]
root          64  0.0  0.0      0     0 ?        SN   16:08   0:00 [khugepaged]
root          65  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-kblockd]
root          66  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-blkcg_punt_bio]
root          67  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-kintegrityd]
root          68  0.0  0.0      0     0 ?        S    16:08   0:00 [irq/9-acpi]
root          72  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-tpm_dev_wq]
root          73  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-ata_sff]
root          74  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-md_bitmap]
root          75  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-md_llbitmap_io]
root          76  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-md_llbitmap_unplug]
root          77  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-edac-poller]
root          78  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-devfreq_wq]
root          79  0.0  0.0      0     0 ?        S    16:08   0:00 [watchdogd]
root          81  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-quota_events_unbound]
root          82  0.0  0.0      0     0 ?        S    16:08   0:00 [kswapd0]
root          83  0.0  0.0      0     0 ?        S    16:08   0:00 [ecryptfs-kthread]
root          84  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-kthrotld]
root          85  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-acpi_thermal_pm]
root          86  0.0  0.0      0     0 ?        S    16:08   0:00 [scsi_eh_0]
root          87  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-scsi_tmf_0]
root          88  0.0  0.0      0     0 ?        S    16:08   0:00 [scsi_eh_1]
root          89  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-scsi_tmf_1]
root          94  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-mld]
root          95  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-ipv6_addrconf]
root          96  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-kstrp]
root          98  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/u25:0-ttm]
root         109  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-charger_manager]
root         191  0.0  0.0      0     0 ?        S    16:08   0:00 [irq/18-vmwgfx]
root         194  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-ttm]
root         317  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-iprt-VBoxWQueue]
root         318  0.0  0.0      0     0 ?        S    16:08   0:00 [scsi_eh_2]
root         319  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-scsi_tmf_2]
root         332  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/2:1H-kblockd]
root         333  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/4:1H-kblockd]
root         340  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/5:1H-kblockd]
root         344  0.0  0.0      0     0 ?        S    16:08   0:00 [jbd2/sda2-8]
root         345  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/R-ext4-rsv-conversion]
root         398  0.0  0.0  68032 32924 ?        S<s  16:08   0:01 /usr/lib/systemd/systemd-journald
root         440  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/0:1H-kblockd]
root         443  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/1:1H-kblockd]
systemd+     445  0.0  0.0  16808  7664 ?        Ss   16:08   0:04 /usr/lib/systemd/systemd-oomd
root         447  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/3:1H-kblockd]
root         448  0.0  0.0  41480 15124 ?        Ss   16:08   0:00 /usr/lib/systemd/systemd-udevd
systemd+     453  0.0  0.0  22908 15356 ?        Ss   16:08   0:00 /usr/lib/systemd/systemd-resolved
root         459  0.0  0.0      0     0 ?        S    16:08   0:00 [psimon]
avahi       1244  0.0  0.0   6884  5016 ?        Ss   16:08   0:01 avahi-daemon: running [mimson-VirtualBox.local]
root        1245  0.0  0.0   2888  1936 ?        Ss   16:08   0:00 /bin/sh /usr/lib/systemd/scripts/chronyd-starter.sh -n -F 1
message+    1246  0.0  0.0  11992  8912 ?        Ss   16:08   0:03 @dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
root        1262  0.0  0.0  46828 30180 ?        Ss   16:08   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
polkitd     1266  0.0  0.0 387196 13112 ?        Ssl  16:08   0:00 /usr/lib/polkit-1/polkitd --no-debug --log-level=notice
root        1275  0.0  0.1 2543168 47332 ?       Ssl  16:08   0:02 /usr/lib/snapd/snapd
root        1276  0.0  0.0 309960  9004 ?        Ssl  16:08   0:00 /usr/libexec/accounts-daemon
root        1278  0.0  0.0   7060  3356 ?        Ss   16:08   0:00 /usr/sbin/cron -f -P
root        1279  0.0  0.0 308132  8028 ?        Ssl  16:08   0:00 /usr/libexec/switcheroo-control
root        1281  0.0  0.0  18736  9732 ?        Ss   16:08   0:00 /usr/lib/systemd/systemd-logind
root        1282  0.0  0.0 544220 16380 ?        Ssl  16:08   0:00 /usr/libexec/udisks2/udisksd
avahi       1291  0.0  0.0   6560  1664 ?        S    16:08   0:00 avahi-daemon: chroot helper
_chrony     1345  0.0  0.0  24004 11352 ?        S    16:08   0:00 /usr/sbin/chronyd -n -F 1
_chrony     1367  0.0  0.0  12120  3356 ?        S    16:08   0:00 /usr/sbin/chronyd -n -F 1
syslog      1393  0.0  0.0 220604  6496 ?        Ssl  16:08   0:00 /usr/sbin/rsyslogd -n -iNONE
root        1455  0.0  0.0 337032 22552 ?        Ssl  16:08   0:03 /usr/sbin/NetworkManager --no-daemon
root        1457  0.0  0.0  17960  6964 ?        Ss   16:08   0:00 /usr/sbin/wpa_supplicant -u -s -O DIR=/run/wpa_supplicant GROUP=netdev
root        1493  0.0  0.0 391608 14016 ?        Ssl  16:08   0:00 /usr/sbin/ModemManager
root        1531  0.0  0.0   2900  1764 ?        Ss   16:08   0:00 /bin/sh /snap/cups/1238/scripts/run-cups-browsed
root        1535  0.0  0.0   2900  1736 ?        Ss   16:08   0:00 /bin/sh /snap/cups/1238/scripts/run-cupsd
root        1546  0.0  0.0 126044 32876 ?        Ssl  16:08   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
root        1799  0.0  0.0 353148  2980 ?        Sl   16:08   0:06 /usr/bin/VBoxDRMClient
root        1801  0.0  0.0 292080  3860 ?        Sl   16:08   0:01 /usr/sbin/VBoxService --pidfile /var/run/vboxadd-service.sh
root        1819  0.0  0.0 384912 11072 ?        Ssl  16:08   0:00 /usr/sbin/gdm3
root        1923  0.0  0.0      0     0 ?        S    16:08   0:00 [psimon]
root        1995  0.0  0.0  61280 12800 ?        S    16:08   0:00 cupsd -f -s /var/snap/cups/common/etc/cups/cups-files.conf -c /var/snap/cups/common/etc/cups/cupsd.conf
root        1996  0.0  0.0 241608 10224 ?        Sl   16:08   0:00 cups-proxyd /var/snap/cups/common/run/cups.sock /run/cups/cups.sock -l --logdir /var/snap/cups/1238/var/log
rtkit       2035  0.0  0.0  21872  3612 ?        SNsl 16:08   0:00 /usr/libexec/rtkit-daemon
root        2144  0.0  0.0   2900   912 ?        S    16:08   0:00 /bin/sh /snap/cups/1238/scripts/run-cups-browsed
ollama      2199  0.8  0.1 2258720 42292 ?       Ssl  16:08   3:31 /usr/local/bin/ollama serve
colord      2240  0.0  0.0 317868 16952 ?        Ssl  16:08   0:00 /usr/libexec/colord
root        2321  0.0  0.0 318976 11764 ?        Ssl  16:08   0:00 /usr/libexec/upowerd
root        2775  0.0  0.0      0     0 ?        I<   16:08   0:00 [kworker/u25:1]
root        2776  0.0  0.0 309516  8080 ?        Ssl  16:08   0:00 /usr/libexec/power-profiles-daemon
root        2969  0.0  0.0 174760 12724 ?        Sl   16:08   0:00 gdm-session-worker [pam/gdm-password]
mimson      3079  0.0  0.0  24040 15340 ?        Ss   16:08   0:00 /usr/lib/systemd/systemd --user
mimson      3081  0.0  0.0  25000  4244 ?        S    16:08   0:00 (sd-pam)
mimson      3116  0.0  0.0  10232  7184 ?        Ss   16:08   0:01 /usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
mimson      3117  0.0  0.0 125668 13964 ?        S<sl 16:08   0:00 /usr/bin/pipewire
mimson      3121  0.0  0.0 183744 11916 ?        SLsl 16:08   0:00 /usr/bin/gnome-keyring-daemon --foreground --components=pkcs11,secrets --control-directory=/run/user/1000/keyring
mimson      3133  0.0  0.0   7560  3980 ?        Ss   16:08   0:00 /usr/bin/mpris-proxy
mimson      3136  0.0  0.0 488948 23528 ?        S<sl 16:08   0:00 /usr/bin/wireplumber
mimson      3138  0.0  0.0  84812  5764 ?        Ssl  16:08   0:00 /usr/bin/pipewire -c filter-chain.conf
mimson      3143  0.0  0.0 183852 13888 ?        S<sl 16:08   0:00 /usr/bin/pipewire-pulse
mimson      3179  0.0  0.0 168540  7088 tty2     Ssl+ 16:08   0:00 /usr/libexec/gdm-wayland-session /usr/bin/gnome-session --session=ubuntu
mimson      3210  0.0  0.0 175204  9232 tty2     Sl+  16:08   0:00 /usr/libexec/gnome-session-init-worker ubuntu
mimson      3240  0.0  0.0 688048  9564 ?        Ssl  16:08   0:00 /usr/libexec/xdg-document-portal
mimson      3288  0.0  0.0 307688  7260 ?        Ssl  16:08   0:00 /usr/libexec/xdg-permission-store
root        3310  0.0  0.0   2792  2232 ?        Ss   16:08   0:00 fusermount3 -o rw,nosuid,nodev,fsname=portal,auto_unmount,subtype=portal -- /run/user/1000/doc
mimson      3379  0.0  0.0 310560  8508 ?        Ssl  16:08   0:00 /usr/libexec/gcr-ssh-agent --base-dir /run/user/1000/gcr
mimson      3380  0.0  0.0  87208  5800 ?        Ssl  16:08   0:00 /usr/libexec/gnome-session-ctl --monitor
mimson      3381  0.0  0.0  10484  6708 ?        Ss   16:08   0:00 /usr/bin/ssh-agent -D
mimson      3393  0.0  0.0 313420  9536 ?        Ssl  16:08   0:00 /usr/libexec/gvfsd
mimson      3399  0.0  0.0 324816  8124 ?        Sl   16:08   0:00 /usr/libexec/gvfsd-fuse /run/user/1000/gvfs -f
mimson      3403  0.0  0.0 613848 11952 ?        Ssl  16:08   0:00 /usr/libexec/gnome-session-service --session=ubuntu
mimson      3421  3.6  1.8 6527776 738504 ?      Ssl  16:08  15:58 /usr/bin/gnome-shell --mode=ubuntu
mimson      3523  0.0  0.0 381068  8164 ?        Ssl  16:08   0:00 /usr/libexec/at-spi-bus-launcher
mimson      3530  0.0  0.0   8744  5436 ?        S    16:08   0:00 /usr/bin/dbus-daemon --config-file=/usr/share/defaults/at-spi2/accessibility.conf --nofork --print-address 11 --address=unix:path=/run/user/1000/at-spi/bus
mimson      3532  0.0  0.0 168688  7884 ?        Sl   16:08   0:00 /usr/libexec/at-spi2-registryd --use-gnome-session
mimson      3550  0.0  0.0 659668 23712 ?        Sl   16:08   0:00 /usr/libexec/gnome-shell-calendar-server
mimson      3558  0.0  0.1 1288392 47196 ?       Ssl  16:08   0:00 /usr/libexec/evolution-source-registry
mimson      3562  0.0  0.0 2797324 33604 ?       Sl   16:08   0:00 /usr/bin/gjs -m /usr/share/gnome-shell/org.gnome.Shell.Notifications
mimson      3590  0.0  0.0 385864 12112 ?        Ssl  16:08   0:11 /usr/bin/ibus-daemon --panel disable
mimson      3591  0.0  0.0 254136 11084 ?        Ssl  16:08   0:00 /usr/libexec/gsd-a11y-settings
mimson      3592  0.0  0.0 252144 10996 ?        Ssl  16:08   0:00 /usr/libexec/gsd-color
mimson      3595  0.0  0.0 260500 13052 ?        Ssl  16:08   0:00 /usr/libexec/gsd-datetime
mimson      3596  0.0  0.0 391508 11592 ?        Ssl  16:08   0:00 /usr/libexec/gsd-housekeeping
mimson      3599  0.0  0.0 383476  8748 ?        Ssl  16:08   0:00 /usr/libexec/gsd-keyboard
mimson      3602  0.0  0.0 625872 15428 ?        Ssl  16:08   0:00 /usr/libexec/gsd-media-keys
mimson      3604  0.0  0.0 393808 12120 ?        Ssl  16:08   0:00 /usr/libexec/gsd-power
mimson      3605  0.0  0.0 327944 15008 ?        Ssl  16:08   0:00 /usr/libexec/gsd-print-notifications
mimson      3606  0.0  0.0 457320  8572 ?        Ssl  16:08   0:00 /usr/libexec/gsd-rfkill
mimson      3607  0.0  0.0 170228  8076 ?        Ssl  16:08   0:00 /usr/libexec/gsd-screensaver-proxy
mimson      3609  0.0  0.0 467740 13668 ?        Ssl  16:08   0:00 /usr/libexec/gsd-sharing
mimson      3613  0.0  0.0 386052 10288 ?        Ssl  16:08   0:00 /usr/libexec/gsd-smartcard
mimson      3617  0.0  0.0 255288 11232 ?        Ssl  16:08   0:00 /usr/libexec/gsd-sound
mimson      3622  0.0  0.0 312168  9692 ?        Sl   16:08   0:00 /usr/libexec/gsd-disk-utility-notify
mimson      3626  0.0  0.0 644024 35456 ?        Sl   16:08   0:00 /usr/bin/update-notifier
mimson      3627  0.0  0.0 480744 10592 ?        Ssl  16:08   0:00 /usr/libexec/gsd-usb-protection
mimson      3633  0.0  0.1 841648 69652 ?        Sl   16:08   0:00 /usr/libexec/evolution-data-server/evolution-alarm-notify
mimson      3634  0.0  0.0 390760 11276 ?        Ssl  16:08   0:00 /usr/libexec/gsd-wwan
mimson      3760  0.0  0.0 2732816 33572 ?       Sl   16:08   0:00 /usr/bin/gjs -m /usr/share/gnome-shell/org.gnome.ScreenSaver
mimson      3762  0.0  0.0 466964 32344 ?        Sl   16:08   0:00 /usr/libexec/goa-daemon
mimson      3764  0.0  0.0 243180  8492 ?        Sl   16:08   0:00 /usr/libexec/ibus-dconf
mimson      3765  0.0  0.0 500724 37864 ?        Sl   16:08   0:04 /usr/libexec/ibus-extension-gtk3
mimson      3778  0.0  0.0 308676  8268 ?        Sl   16:08   0:00 /usr/libexec/ibus-portal
mimson      3824  0.0  0.1 212528 71204 ?        S    16:08   0:00 /usr/bin/Xwayland :0 -rootless -noreset -accessx -core -auth /run/user/1000/.mutter-Xwaylandauth.NG4YU3 -listenfd 4 -listenfd 5 -displayfd 6 -initfd 7 -byteswappedclients -enable-ei-portal
mimson      3827  0.0  0.0 388120 10752 ?        Sl   16:08   0:00 /usr/libexec/goa-identity-service
mimson      3829  0.0  0.0 877072 26136 ?        SNsl 16:08   0:00 /usr/libexec/localsearch-3
mimson      3835  0.0  0.0 629532 21972 ?        Ssl  16:08   0:00 /usr/libexec/xdg-desktop-portal
mimson      3839  0.0  0.0 893696 27600 ?        Ssl  16:08   0:00 /usr/libexec/evolution-calendar-factory
mimson      3852  0.0  0.1 614924 46508 ?        Ssl  16:08   0:01 /usr/libexec/xdg-desktop-portal-gnome
mimson      3858  0.0  0.0 399656 12528 ?        Sl   16:08   0:00 /usr/libexec/gsd-printer
mimson      3888  0.0  0.0 461136 12948 ?        Ssl  16:08   0:00 /usr/libexec/gvfs-udisks2-volume-monitor
mimson      3925  0.0  0.0 826344 32188 ?        Ssl  16:08   0:00 /usr/libexec/evolution-addressbook-factory
mimson      3930  0.0  0.0 309000  8144 ?        Ssl  16:08   0:00 /usr/libexec/gvfs-gphoto2-volume-monitor
mimson      3940  0.0  0.0 308032  7652 ?        Ssl  16:08   0:00 /usr/libexec/gvfs-mtp-volume-monitor
mimson      3950  0.0  0.0 390052  9764 ?        Ssl  16:08   0:00 /usr/libexec/gvfs-afc-volume-monitor
mimson      3962  0.0  0.0 308012  7476 ?        Ssl  16:08   0:00 /usr/libexec/gvfs-goa-volume-monitor
mimson      3979  0.0  0.0 169484  8412 ?        Sl   16:08   0:04 /usr/libexec/ibus-engine-simple
mimson      3989  0.0  0.2 3289556 86484 ?       Sl   16:08   0:03 gjs /usr/share/gnome-shell/extensions/ding@rastersoft.com/app/ding.js -E -P /usr/share/gnome-shell/extensions/ding@rastersoft.com/app
mimson      4060  0.0  0.0 169180  7640 ?        Ssl  16:08   0:00 /usr/libexec/gvfsd-metadata
mimson      4099  0.0  0.0 165352  6764 ?        Ssl  16:08   0:00 /usr/libexec/dconf-service
mimson      4164  0.0  0.0 251636 14160 ?        Ssl  16:08   0:00 /usr/libexec/gsd-xsettings
mimson      4175  0.0  0.3 1717684 118928 ?      Sl   16:08   0:00 /usr/libexec/mutter-x11-frames
mimson      4177  0.0  0.0  16864  1820 ?        S    16:08   0:00 /usr/bin/VBoxClient --clipboard
mimson      4179  0.0  0.0 284000 16364 ?        Sl   16:08   0:00 /usr/bin/VBoxClient --clipboard
mimson      4210  0.0  0.0  16864  1824 ?        S    16:08   0:00 /usr/bin/VBoxClient --vmsvga-session
mimson      4214  0.0  0.0 148968  2392 ?        Sl   16:08   0:01 /usr/bin/VBoxClient --vmsvga-session
mimson      4226  0.0  0.0 608604 10644 ?        Sl   16:08   0:00 /usr/libexec/gvfsd-trash --spawner :1.21 /org/gtk/gvfs/exec_spaw/0
mimson      4259  0.0  0.1 374012 72648 ?        Sl   16:08   0:00 /usr/libexec/ibus-x11
mimson      4351  0.0  0.0 493076 30020 ?        Ssl  16:08   0:00 /usr/libexec/xdg-desktop-portal-gtk
mimson      4424  0.0  0.0 303928  6528 ?        Ssl  16:08   0:00 /snap/snapd-desktop-integration/391/usr/bin/user-session-helper /snap/snapd-desktop-integration/391/usr/bin/snapd-desktop-integration
mimson      4484  0.0  0.0 440272 36348 ?        Sl   16:08   0:00 /snap/snapd-desktop-integration/391/usr/bin/snapd-desktop-integration
mimson      4537  0.3  1.6 4314224 635460 ?      Sl   16:08   1:33 /usr/bin/nautilus --gapplication-service
mimson      4591  0.0  0.0 387584 10288 ?        Sl   16:08   0:00 /usr/libexec/gvfsd-recent --spawner :1.21 /org/gtk/gvfs/exec_spaw/1
mimson      4593  0.0  0.0 387636 10348 ?        Sl   16:08   0:00 /usr/libexec/gvfsd-network --spawner :1.21 /org/gtk/gvfs/exec_spaw/2
mimson      4604  0.0  0.0 388648 10256 ?        Sl   16:08   0:00 /usr/libexec/gvfsd-dnssd --spawner :1.21 /org/gtk/gvfs/exec_spaw/3
mimson      4610  0.0  0.0 387064  9956 ?        Sl   16:08   0:00 /usr/libexec/gvfsd-wsdd --spawner :1.21 /org/gtk/gvfs/exec_spaw/4
mimson      4615  0.0  0.0  44808 33800 ?        S    16:08   0:01 python3 /usr/bin/wsdd --no-host --discovery --listen /run/user/1000/gvfsd/wsdd
uuidd       4640  0.0  0.0   8104  3404 ?        Ss   16:08   0:00 /usr/sbin/uuidd --socket-activation --cont-clock
mimson      4724  0.0  0.0  10500  7056 ?        S    16:09   0:00 /usr/bin/ssh-agent -D -a /run/user/1000/gcr/.ssh
mimson      5004  1.5  1.2 3707208 475528 ?      Sl   16:12   6:40 /usr/bin/ptyxis --gapplication-service
mimson      5011  0.0  0.0 239948  8096 ?        Ssl  16:12   0:05 /usr/libexec/ptyxis-agent --socket-fd=3 --rlimit-nofile=1024
mimson      5052  0.0  0.0   9016  5936 pts/0    Ss+  16:12   0:00 /usr/bin/bash
mimson      7329  0.0  0.0   9016  5956 pts/1    Ss   16:15   0:00 /usr/bin/bash
mimson      7339  1.1  1.0 5578920 415812 pts/1  Sl+  16:15   4:57 claude -r
mimson     31686  0.0  0.0   9016  5960 pts/2    Ss+  16:30   0:00 /usr/bin/bash
root       31895  0.0  0.1 498456 48460 ?        Ssl  16:34   0:01 /usr/libexec/fwupd/fwupd
mimson     32058  0.0  0.0   9016  6028 pts/3    Ss+  16:41   0:00 /usr/bin/bash
root       32103  0.0  0.0  28908 12776 ?        Ss   16:42   0:00 /usr/sbin/cupsd -l
lp         32107  0.0  0.0  15436  7356 ?        S    16:42   0:00 /usr/lib/cups/notifier/dbus dbus://
cups-br+   32108  0.0  0.0 207540 22736 ?        Ssl  16:42   0:00 /usr/sbin/cups-browsed
mimson     58455  0.0  0.6 1518784368 241680 ?   SLl  17:56   0:03 /opt/Obsidian/obsidian
mimson     58461  0.0  0.1 54819184 58732 ?      S    17:56   0:00 /opt/Obsidian/obsidian --type=zygote --no-zygote-sandbox
mimson     58462  0.0  0.1 54819168 58260 ?      S    17:56   0:00 /opt/Obsidian/obsidian --type=zygote
mimson     58464  0.0  0.0 54819168 11728 ?      S    17:56   0:00 /opt/Obsidian/obsidian --type=zygote
mimson     58494  0.0  0.4 55212936 161384 ?     Sl   17:56   0:02 /opt/Obsidian/obsidian --type=gpu-process --ozone-platform=wayland --enable-crash-reporter=adab1108-20f4-4fc9-baa8-40bf031e7b11,no_channel --user-data-dir=/home/mimson/.config/obsidian --gpu-preferences=WAAAAAAAAAAgAQAEAAAAAAAAAAAAAGAAQAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAACAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAACAAAAAAAAAAIAAAAAAAAAA== --shared-files --field-trial-handle=3,i,12345914373214284705,2196888147369399576,262144 --enable-features=GlobalShortcutsPortalPreferredTrigger,PdfUseShowSaveFilePicker,SharedArrayBuffer --disable-features=DropInputEventsWhilePaintHolding,LocalNetworkAccessChecks,ScreenAIOCREnabled,SpareRendererForSitePerProcess,TraceSiteInstanceGetProcessCreation --variations-seed-version --pseudonymization-salt-handle=7,i,164869931763731753,14235819406639371567,4 --trace-process-track-uuid=3190708988185955192 --log-level=3
mimson     58497  0.0  0.2 54893416 84836 ?      Sl   17:56   0:00 /opt/Obsidian/obsidian --type=utility --utility-sub-type=network.mojom.NetworkService --lang=pl --service-sandbox-type=none --enable-crash-reporter=adab1108-20f4-4fc9-baa8-40bf031e7b11,no_channel --user-data-dir=/home/mimson/.config/obsidian --standard-schemes=app --secure-schemes=app --cors-schemes=app --fetch-schemes=app --streaming-schemes=app --code-cache-schemes=app --shared-files=v8_context_snapshot_data:100 --field-trial-handle=3,i,12345914373214284705,2196888147369399576,262144 --enable-features=GlobalShortcutsPortalPreferredTrigger,PdfUseShowSaveFilePicker,SharedArrayBuffer --disable-features=DropInputEventsWhilePaintHolding,LocalNetworkAccessChecks,ScreenAIOCREnabled,SpareRendererForSitePerProcess,TraceSiteInstanceGetProcessCreation --variations-seed-version --pseudonymization-salt-handle=7,i,164869931763731753,14235819406639371567,4 --trace-process-track-uuid=3190708989122997041 --log-level=3
mimson     58511  0.0  0.5 1522351948 231588 ?   Sl   17:56   0:04 /opt/Obsidian/obsidian --type=renderer --enable-crash-reporter=adab1108-20f4-4fc9-baa8-40bf031e7b11,no_channel --user-data-dir=/home/mimson/.config/obsidian --standard-schemes=app --secure-schemes=app --cors-schemes=app --fetch-schemes=app --streaming-schemes=app --code-cache-schemes=app --app-path=/opt/Obsidian/resources/app.asar --no-sandbox --no-zygote --ozone-platform=wayland --lang=pl --num-raster-threads=3 --enable-main-frame-before-activation --renderer-client-id=4 --time-ticks-at-unix-epoch=-1788790095379426 --launch-time-ticks=6523047921 --shared-files=v8_context_snapshot_data:100 --field-trial-handle=3,i,12345914373214284705,2196888147369399576,262144 --enable-features=GlobalShortcutsPortalPreferredTrigger,PdfUseShowSaveFilePicker,SharedArrayBuffer --disable-features=DropInputEventsWhilePaintHolding,LocalNetworkAccessChecks,ScreenAIOCREnabled,SpareRendererForSitePerProcess,TraceSiteInstanceGetProcessCreation --variations-seed-version --pseudonymization-salt-handle=7,i,164869931763731753,14235819406639371567,4 --trace-process-track-uuid=3190708990060038890 --log-level=3
mimson     58685  0.0  0.0   3768  2252 ?        S    17:57   0:00 bwrap --unshare-all --die-with-parent --chdir / --ro-bind /usr /usr --dev /dev --ro-bind-try /etc/ld.so.cache /etc/ld.so.cache --ro-bind-try /nix/store /nix/store --tmpfs /tmp-home --tmpfs /tmp-run --clearenv --setenv HOME /tmp-home --setenv XDG_RUNTIME_DIR /tmp-run --setenv XDG_RUNTIME_DIR /run/user/1000 --symlink /usr/lib /lib --symlink /usr/lib64 /lib64 --seccomp 98 /usr/libexec/glycin-loaders/2+/glycin-image-rs --dbus-fd 96
mimson     58686  0.0  0.0   3768  1416 ?        S    17:57   0:00 bwrap --unshare-all --die-with-parent --chdir / --ro-bind /usr /usr --dev /dev --ro-bind-try /etc/ld.so.cache /etc/ld.so.cache --ro-bind-try /nix/store /nix/store --tmpfs /tmp-home --tmpfs /tmp-run --clearenv --setenv HOME /tmp-home --setenv XDG_RUNTIME_DIR /tmp-run --setenv XDG_RUNTIME_DIR /run/user/1000 --symlink /usr/lib /lib --symlink /usr/lib64 /lib64 --seccomp 98 /usr/libexec/glycin-loaders/2+/glycin-image-rs --dbus-fd 96
mimson     58687  0.0  0.0 145332  6656 ?        Sl   17:57   0:00 /usr/libexec/glycin-loaders/2+/glycin-image-rs --dbus-fd 96
mimson     58857  0.0  0.0   3768  2228 ?        S    17:57   0:00 bwrap --unshare-all --die-with-parent --chdir / --ro-bind /usr /usr --dev /dev --ro-bind-try /etc/ld.so.cache /etc/ld.so.cache --ro-bind-try /nix/store /nix/store --tmpfs /tmp-home --tmpfs /tmp-run --clearenv --setenv HOME /tmp-home --setenv XDG_RUNTIME_DIR /tmp-run --setenv XDG_RUNTIME_DIR /run/user/1000 --symlink /usr/lib /lib --symlink /usr/lib64 /lib64 --seccomp 116 /usr/libexec/glycin-loaders/2+/glycin-image-rs --dbus-fd 115
mimson     58859  0.0  0.0   3768  1392 ?        S    17:57   0:00 bwrap --unshare-all --die-with-parent --chdir / --ro-bind /usr /usr --dev /dev --ro-bind-try /etc/ld.so.cache /etc/ld.so.cache --ro-bind-try /nix/store /nix/store --tmpfs /tmp-home --tmpfs /tmp-run --clearenv --setenv HOME /tmp-home --setenv XDG_RUNTIME_DIR /tmp-run --setenv XDG_RUNTIME_DIR /run/user/1000 --symlink /usr/lib /lib --symlink /usr/lib64 /lib64 --seccomp 116 /usr/libexec/glycin-loaders/2+/glycin-image-rs --dbus-fd 115
mimson     58860  0.0  0.0 145332 11004 ?        Sl   17:57   0:00 /usr/libexec/glycin-loaders/2+/glycin-image-rs --dbus-fd 115
root       89492  0.0  0.0      0     0 ?        I    19:50   0:00 [kworker/5:0-ata_sff]
root       90313  0.0  0.0      0     0 ?        I    22:17   0:00 [kworker/0:0-events]
root       91384  0.0  0.0      0     0 ?        I    22:30   0:00 [kworker/1:2-events]
root      146042  0.3  0.0      0     0 ?        I    22:40   0:08 [kworker/u24:0-flush-8:0]
root      146749  0.0  0.0      0     0 ?        I    22:50   0:00 [kworker/2:1-events]
mimson    153405  0.8  1.4 3610572 563604 ?      Sl   22:54   0:14 /usr/bin/baobab --gapplication-service
mimson    154640  0.0  0.0 2024884 28508 ?       Sl   22:55   0:00 /usr/bin/snap userd
root      154860  0.0  0.0      0     0 ?        I    22:55   0:00 [kworker/4:2-events]
root      156647  0.0  0.0      0     0 ?        I    22:57   0:00 [kworker/3:2-inet_frag_wq]
root      157120  0.0  0.0      0     0 ?        I    23:02   0:00 [kworker/3:0-events]
root      164616  0.0  0.0      0     0 ?        I    23:04   0:00 [kworker/2:2-mm_percpu_wq]
root      165537  0.0  0.0      0     0 ?        I    23:05   0:00 [kworker/1:0]
root      165676  0.0  0.0      0     0 ?        I    23:07   0:00 [kworker/4:0-events]
root      165696  0.0  0.0      0     0 ?        I    23:07   0:00 [kworker/0:2-cgroup_release]
root      165700  0.0  0.0   3220  1996 ?        S    23:08   0:00 sleep 3600
root      165707  0.0  0.0      0     0 ?        I    23:10   0:00 [kworker/5:1-cgroup_release]
mimson    165722  0.7  1.1 3632252 444812 ?      Sl   23:11   0:05 /usr/bin/gnome-text-editor --gapplication-service
root      165776  0.6  0.0      0     0 ?        I    23:11   0:04 [kworker/u24:3-ipv6_addrconf]
mimson    165777  5.4  1.7 3945964 681484 ?      Sl   23:11   0:36 /snap/firefox/8863/usr/lib/firefox/firefox
mimson    165844  0.0  0.0 149412  3048 ?        Sl   23:11   0:00 /snap/firefox/8863/usr/lib/firefox/crashhelper 165777 9 /tmp/ 11 20260904071051
mimson    165944  0.0  0.0 463396 34896 ?        S    23:11   0:00 /snap/firefox/8863/usr/lib/firefox/firefox -contentproc -ipcHandle 0 -signalPipe 1 -initialChannelId {52780bd9-1ced-4611-bec4-bbfacf05a7d0} -parentPid 165777 -greomni /snap/firefox/8863/usr/lib/firefox/omni.ja -appomni /snap/firefox/8863/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8863/usr/lib/firefox/browser 1 forkserver
mimson    165947  0.0  0.1 475528 39576 ?        Sl   23:11   0:00 /snap/firefox/8863/usr/lib/firefox/firefox -contentproc -parentBuildID 20260904071051 -prefsHandle 0:36687 -prefMapHandle 1:294310 -sandboxReporter 2 -chrootClient 3 -ipcHandle 4 -initialChannelId {c675bdc5-550c-4c58-bfc2-d8ffb2a28994} -parentPid 165777 -crashHelperPid 165844 -crashHelper 5 -crashReporter 6 -appDir /snap/firefox/8863/usr/lib/firefox/browser 2 socket
mimson    165963  0.2  0.4 2720200 184636 ?      Sl   23:11   0:01 /snap/firefox/8863/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:36839 -prefMapHandle 1:294310 -jsInitHandle 2:160936 -parentBuildID 20260904071051 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {64221d88-1fe3-48ed-b21b-8372f84a6ffb} -parentPid 165777 -crashHelperPid 165844 -crashHelper 6 -crashReporter 7 -greomni /snap/firefox/8863/usr/lib/firefox/omni.ja -appomni /snap/firefox/8863/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8863/usr/lib/firefox/browser 3 tab
mimson    165972  0.0  0.1 635184 48148 ?        Sl   23:11   0:00 /snap/firefox/8863/usr/lib/firefox/firefox -contentproc -parentBuildID 20260904071051 -prefsHandle 0:36839 -prefMapHandle 1:294310 -sandboxReporter 2 -chrootClient 3 -ipcHandle 4 -initialChannelId {8f989415-6b12-46fc-b473-a4db420c5b8f} -parentPid 165777 -crashHelperPid 165844 -crashHelper 5 -crashReporter 6 -appDir /snap/firefox/8863/usr/lib/firefox/browser 4 rdd
mimson    166170  0.0  0.3 2649476 119180 ?      Sl   23:11   0:00 /snap/firefox/8863/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:36951 -prefMapHandle 1:294310 -jsInitHandle 2:160936 -parentBuildID 20260904071051 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {c9b629e1-8902-4404-a6f6-d0837b4d2db3} -parentPid 165777 -crashHelperPid 165844 -crashHelper 6 -crashReporter 7 -greomni /snap/firefox/8863/usr/lib/firefox/omni.ja -appomni /snap/firefox/8863/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8863/usr/lib/firefox/browser 5 tab
mimson    166480  0.0  0.1 637232 51796 ?        Sl   23:11   0:00 /snap/firefox/8863/usr/lib/firefox/firefox -contentproc -parentBuildID 20260904071051 -sandboxingKind 0 -prefsHandle 0:54423 -prefMapHandle 1:294310 -sandboxReporter 2 -chrootClient 3 -ipcHandle 4 -initialChannelId {ae18f3c2-0f9a-46ea-b73a-76f00cb3aa66} -parentPid 165777 -crashHelperPid 165844 -crashHelper 5 -crashReporter 6 -appDir /snap/firefox/8863/usr/lib/firefox/browser 6 utility
mimson    166623  4.8  1.2 3258656 502416 ?      Sl   23:11   0:32 /snap/firefox/8863/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:50604 -prefMapHandle 1:294310 -jsInitHandle 2:160936 -parentBuildID 20260904071051 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {10ea9276-f668-4515-abd0-9ccd22f23184} -parentPid 165777 -crashHelperPid 165844 -crashHelper 6 -crashReporter 7 -greomni /snap/firefox/8863/usr/lib/firefox/omni.ja -appomni /snap/firefox/8863/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8863/usr/lib/firefox/browser 7 tab
mimson    166636  1.7  1.4 3261288 553848 ?      Sl   23:11   0:11 /snap/firefox/8863/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:50604 -prefMapHandle 1:294310 -jsInitHandle 2:160936 -parentBuildID 20260904071051 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {1a1c93c6-cf8d-4501-8c52-b39030c930ef} -parentPid 165777 -crashHelperPid 165844 -crashHelper 6 -crashReporter 7 -greomni /snap/firefox/8863/usr/lib/firefox/omni.ja -appomni /snap/firefox/8863/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8863/usr/lib/firefox/browser 9 tab
root      166718  0.4  0.0      0     0 ?        I    23:11   0:03 [kworker/u24:4-events_power_efficient]
root      167001  1.4  0.0      0     0 ?        I    23:17   0:04 [kworker/u24:1-events_unbound]
mimson    167054  0.0  0.2 2614676 90244 ?       Sl   23:17   0:00 /snap/firefox/8863/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:50656 -prefMapHandle 1:294310 -jsInitHandle 2:160936 -parentBuildID 20260904071051 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {62dbb049-f829-4156-b570-2578e0e2fec9} -parentPid 165777 -crashHelperPid 165844 -crashHelper 6 -crashReporter 7 -greomni /snap/firefox/8863/usr/lib/firefox/omni.ja -appomni /snap/firefox/8863/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8863/usr/lib/firefox/browser 11 tab
mimson    167060  0.0  0.1 2603288 76076 ?       Sl   23:17   0:00 /snap/firefox/8863/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:50656 -prefMapHandle 1:294310 -jsInitHandle 2:160936 -parentBuildID 20260904071051 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {e83ee359-ff25-4b37-87e5-3159c10d92cc} -parentPid 165777 -crashHelperPid 165844 -crashHelper 6 -crashReporter 7 -greomni /snap/firefox/8863/usr/lib/firefox/omni.ja -appomni /snap/firefox/8863/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8863/usr/lib/firefox/browser 12 tab
root      167208  0.0  0.0      0     0 ?        I    23:17   0:00 [kworker/3:1-events]
root      167245  0.0  0.0      0     0 ?        I    23:18   0:00 [kworker/2:0]
root      167250  0.0  0.0      0     0 ?        I    23:18   0:00 [kworker/0:1-events]
root      167415  0.0  0.0      0     0 ?        I    23:20   0:00 [kworker/5:2]
root      167416  0.0  0.0      0     0 ?        I    23:20   0:00 [kworker/5:3-cgroup_free]
mimson    167429  0.0  0.1 2603304 76288 ?       Sl   23:20   0:00 /snap/firefox/8863/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:50656 -prefMapHandle 1:294310 -jsInitHandle 2:160936 -parentBuildID 20260904071051 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {826109be-ceda-4185-80e5-2bc2e8112ced} -parentPid 165777 -crashHelperPid 165844 -crashHelper 6 -crashReporter 7 -greomni /snap/firefox/8863/usr/lib/firefox/omni.ja -appomni /snap/firefox/8863/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8863/usr/lib/firefox/browser 14 tab
root      167708  3.3  0.0      0     0 ?        I    23:22   0:00 [kworker/u24:2-events_unbound]
mimson    167719  0.2  0.1 2603304 75548 ?       Sl   23:22   0:00 /snap/firefox/8863/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:50656 -prefMapHandle 1:294310 -jsInitHandle 2:160936 -parentBuildID 20260904071051 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {afdd4b75-38fb-4da3-824c-272ac5fca390} -parentPid 165777 -crashHelperPid 165844 -crashHelper 6 -crashReporter 7 -greomni /snap/firefox/8863/usr/lib/firefox/omni.ja -appomni /snap/firefox/8863/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8863/usr/lib/firefox/browser 15 tab
mimson    167768  0.3  0.0   9016  5964 pts/4    Ss   23:22   0:00 /usr/bin/bash
mimson    167781 50.0  0.0  20564 12888 pts/4    S+   23:22   0:00 python3 commands.py
mimson    167785  0.0  0.0   2888  1924 pts/4    S+   23:22   0:00 /bin/sh -c ps aux 
mimson    167786  0.0  0.0  10296  5040 pts/4    R+   23:22   0:00 ps aux
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

## `getent group sudo
`

```
sudo:x:27:mimson
```

