# Program to collect system metrics

#import lib for os, sys, platform, socket, psutil (https://github.com/giampaolo/psutil)
import os
import sys
import platform
import socket
#import time
import datetime
import psutil

# get OS 
print "OS NAME: " + os.name

# get os platform
print "OS PLATFORM: " + platform.system()

#get platform release
print "PLATFORM VERSION: " + platform.release()

#get system type
print "SYSTEM TYPE: " + sys.platform

#get platform version
print "PLATFORM VERSION: " + platform.platform()

#get hostname
print "HOSTNAME: " + socket.gethostname()

#get time in UTC
print "TIME: " + datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

#get CPU here we have used comma as we cannot 2 diff datatypes
print "CPU: " , psutil.cpu_times()

#get virtual memory
print "VIRTUAL MEMORY: ", psutil.virtual_memory()

#get swap memory
print "SWAP MEMORY: ", psutil.swap_memory()

#get disk partitions
print "DISK PARTITIONS: ", psutil.disk_partitions()

#get disk usage
print "DISK USAGE: ", psutil.disk_usage('/')

#get disk IO
print "DISK IO: ", psutil.disk_io_counters(perdisk=True)

#Network IO
print "NETWORK IO: ", psutil.net_io_counters(pernic=True)

#get network addresses
print "NETWORK ADDRESSES: ", psutil.net_if_addrs()

#get network stats
print "NETWORK STATS: ", psutil.net_if_stats()

#get users
print "USERS: ", psutil.users()

#get boot time
print "BOOT TIME: ", psutil.boot_time()
