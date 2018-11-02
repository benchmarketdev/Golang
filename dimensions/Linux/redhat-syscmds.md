#### Check the CPU info:
- Any CPU with the same physical ID are threads or cores in the same physical socket.
- Any CPU with the same core ID are hyper-threads in the same core.
```
> cat /proc/cpuinfo |grep "physical id" |sore |uniq |wc -l
```

#### Check the mem info:
- Available Memory = free + buffers + cached
```
> free -m
```

#### Check the disk info:

```
> fdisk -l
> df -h

# check disk I/O performance
# iostat [ options ] [ <interval> [ <count> ] ]
# %util ~= 100%, %idle < 70%
# vmstat, 
# r(displays the total number of processes waiting for access to the processor), 
# b(displays the total number of processes in a “sleep” state),
# wa(the amount of time that the processor spends waiting for IO operations to complete)
> iostat -x 1 10
```

#### Check load average:
```
# system load averages for the past 1, 5, and 15 minutes
# vmstat, r > 3/4, id < 50%, busy
> uptime
> w
> top
```

#### Show the status of modules in the Linux Kernel
```
# formats the contents of the /proc/modules
> lsmod
```

#### List all PCI devices:
```
> lspci
```

#### Check network connections
```
> netstat -na | awk '/^tcp/ {++S[$NF]} END {for(a in S) print a, S[a]}'
```

#### View default gateway
```
> route -n
> netstat -r
> traceroute
```
#### List open files
```
> lsof -i:22
```

#### Add persistent routes
```
> route add -net 172.16.6.0 netmask 255.255.255.0 gw 172.16.2.25
> vim /etc/sysconfig/network-scripts/route-eth0
```

#### Check system log
```
> vim /var/log/messages
> vim /var/log/secure
# /var/log/wtmp
> last
# /var/log/lastlog
> lastlog
# system boot info /var/log/dmesg
> dmesg |grep error
```

#### Data real-time synchronization
```
inotify + rsync: suitable for small files synchronization.
inotify can be able to monitor file system events.

```

#### Check max open files
```
# one process
ulimit -a
# system limits
cat /proc/sys/fs/file-max
# current open files 
cat /proc/sys/fs/file-nr
# modify
/etc/sysctl.conf
/etc/security/limits.conf
/etc/rc.local  --> ulimit -SHn 65535
```
