# Wyniki komend — 2026-09-06 00:55

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

## `ss -tulpn
`

```
Netid State  Recv-Q Send-Q                     Local Address:Port  Peer Address:PortProcess                             
udp   UNCONN 0      0                                0.0.0.0:51281      0.0.0.0:*    users:(("python3",pid=12571,fd=9)) 
udp   UNCONN 0      0                             127.0.0.54:53         0.0.0.0:*                                       
udp   UNCONN 0      0                          127.0.0.53%lo:53         0.0.0.0:*                                       
udp   UNCONN 0      0                              127.0.0.1:323        0.0.0.0:*                                       
udp   UNCONN 0      0                          192.168.0.102:3702       0.0.0.0:*    users:(("python3",pid=12571,fd=10))
udp   UNCONN 0      0                        239.255.255.250:3702       0.0.0.0:*    users:(("python3",pid=12571,fd=8)) 
udp   UNCONN 0      0                                0.0.0.0:5353       0.0.0.0:*                                       
udp   UNCONN 0      0                                      *:53331            *:*    users:(("python3",pid=12571,fd=12))
udp   UNCONN 0      0                                  [::1]:323           [::]:*                                       
udp   UNCONN 0      0      [fe80::a00:27ff:fee7:327a]%enp0s3:546           [::]:*                                       
udp   UNCONN 0      0      [fe80::a00:27ff:fee7:327a]%enp0s3:3702          [::]:*    users:(("python3",pid=12571,fd=13))
udp   UNCONN 0      0                       [ff02::c]%enp0s3:3702          [::]:*    users:(("python3",pid=12571,fd=11))
udp   UNCONN 0      0                                   [::]:5353          [::]:*                                       
tcp   LISTEN 0      4096                           127.0.0.1:11434      0.0.0.0:*                                       
tcp   LISTEN 0      4096                       127.0.0.53%lo:53         0.0.0.0:*                                       
tcp   LISTEN 0      4096                           127.0.0.1:631        0.0.0.0:*                                       
tcp   LISTEN 0      4096                          127.0.0.54:53         0.0.0.0:*                                       
tcp   LISTEN 0      4096                               [::1]:631           [::]:*
```

## `sudo ufw status verbose
`

```
Stan: nieaktywny
```

## `ip -br addr
`

```
lo               UNKNOWN        127.0.0.1/8 ::1/128 
enp0s3           UP             192.168.0.102/24 2a02:2a40:9fe:7800::caaf/128 2a02:2a40:9fe:7800:a00:27ff:fee7:327a/64 fe80::a00:27ff:fee7:327a/64
```

## `sudo iptables -L -n -v
`

```
Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         

Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         

Chain OUTPUT (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination
```

