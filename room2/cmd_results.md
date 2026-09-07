# Wyniki komend — 2026-09-06 00:45

## `ls
`

```
Modelfile
Todo.md
cmd_results.md
commands
commands.py
final_question
questions
run
runcmd
script.py
```

## `lsblk -f
`

```
NAME   FSTYPE   FSVER            LABEL          UUID                                 FSAVAIL FSUSE% MOUNTPOINTS
loop0  squashfs 4.0                                                                        0   100% /snap/core20/2866
loop1  squashfs 4.0                                                                        0   100% /snap/core18/2999
loop2  squashfs 4.0                                                                        0   100% /snap/core22/2437
loop3  squashfs 4.0                                                                        0   100% /snap/bare/5
loop4  squashfs 4.0                                                                        0   100% /snap/core24/1587
loop5  squashfs 4.0                                                                        0   100% /snap/core24/1643
loop6  squashfs 4.0                                                                        0   100% /snap/core26/462
loop7  squashfs 4.0                                                                        0   100% /snap/cups/1238
loop8  squashfs 4.0                                                                        0   100% /snap/desktop-security-center/150
loop9  squashfs 4.0                                                                        0   100% /snap/firefox/8803
loop10 squashfs 4.0                                                                        0   100% /snap/desktop-security-center/151
loop11 squashfs 4.0                                                                        0   100% /snap/firmware-updater/226
loop12 squashfs 4.0                                                                        0   100% /snap/firefox/8863
loop13 squashfs 4.0                                                                        0   100% /snap/gnome-3-28-1804/198
loop14 squashfs 4.0                                                                        0   100% /snap/gnome-46-2404/153
loop15 squashfs 4.0                                                                        0   100% /snap/gnome-46-2404/164
loop16 squashfs 4.0                                                                        0   100% /snap/mesa-2404/1165
loop17 squashfs 4.0                                                                        0   100% /snap/gtk-common-themes/1535
loop18 squashfs 4.0                                                                        0   100% /snap/mesa-2404/1839
loop19 squashfs 4.0                                                                        0   100% /snap/prompting-client/204
loop20 squashfs 4.0                                                                        0   100% /snap/prompting-client/222
loop21 squashfs 4.0                                                                        0   100% /snap/snap-store/1367
loop22 squashfs 4.0                                                                        0   100% /snap/snap-store/1390
loop23 squashfs 4.0                                                                        0   100% /snap/snapd/26865
loop24 squashfs 4.0                                                                        0   100% /snap/snapd/27710
loop25 squashfs 4.0                                                                        0   100% /snap/snapd-desktop-integration/361
loop26 squashfs 4.0                                                                        0   100% /snap/snapd-desktop-integration/391
loop27 squashfs 4.0                                                                        0   100% /snap/wine-platform/154
loop28 squashfs 4.0                                                                        0   100% /snap/wine-platform-runtime-core24/23
sda                                                                                                 
├─sda1                                                                                              
└─sda2 ext4     1.0                             1158c52b-c7cf-4c1b-9786-62e3210319a7    1,4G    92% /
sr0    iso9660  Joliet Extension VBox_GAs_7.2.8 2026-04-18-10-51-51-50                     0   100% /run/media/mimson/VBox_GAs_7.2.8
```

## `cat /etc/crypttab
`

```
cat: /etc/crypttab: No such file or directory
```

## `last -F
`

```
mimson   tty2                          Sat Sep  5 22:21:31 2026 - still logged in          
gdm-gree tty1                          Sat Sep  5 22:20:53 2026 - Sat Sep  5 22:21:34 2026  (00:00)
reboot   system boot  7.0.0-31-generic Sat Sep  5 22:20:47 2026 - still running            
rejestra pts/0                         Sat Sep  5 13:21:50 2026 - Sat Sep  5 13:24:04 2026  (00:02)
mimson   tty2                          Sat Sep  5 12:33:33 2026 - crash                    
gdm-gree tty1                          Sat Sep  5 12:33:25 2026 - Sat Sep  5 12:33:39 2026  (00:00)
reboot   system boot  7.0.0-31-generic Sat Sep  5 12:33:17 2026 - crash                    
mimson   tty2         local            Sat Sep  5 11:32:35 2026 - crash                    
mimson   tty2         local            Sat Sep  5 10:47:01 2026 - crash                    
mimson   tty2         local            Sat Sep  5 10:44:28 2026 - crash                    
mimson   tty2         local            Sat Sep  5 09:01:09 2026 - crash                    
mimson   tty2         local            Thu Sep  3 18:03:27 2026 - crash                    
mimson   tty2         local            Wed Sep  2 21:56:51 2026 - crash                    
mimson   tty2         local            Mon Aug 31 19:59:12 2026 - crash                    
mimson   tty2         local            Mon Aug 31 19:48:52 2026 - crash                    
mimson   tty2         local            Mon Aug 31 18:03:01 2026 - crash                    
mimson   tty2         local            Thu Aug 27 16:50:07 2026 - crash                    
mimson   tty2         local            Mon Aug 24 16:08:42 2026 - crash                    
mimson   tty2         local            Sun Aug 16 17:44:41 2026 - crash                    
mimson   tty2         local            Sun Aug 16 16:33:29 2026 - crash                    
mimson   tty2         local            Sat Aug 15 22:45:42 2026 - crash                    
mimson   tty2         local            Sat Aug 15 22:23:24 2026 - Sat Aug 15 22:44:20 2026  (00:20)
mimson   tty2         local            Sat Aug 15 22:19:29 2026 - Sat Aug 15 22:22:19 2026  (00:02)
mimson   tty2         local            Sat Aug 15 19:40:03 2026 - Sat Aug 15 22:18:00 2026  (02:37)

wtmpdb begins Sat Aug 15 19:40:03 2026
```

## `grep -Ei 'accepted|failed|session opened' /var/log/auth.log | tail -20
`

```
grep: /var/log/auth.log: plik binarny pasuje do wzorca
```

