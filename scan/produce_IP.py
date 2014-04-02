import os
import threading
import time
import commands
import random

import subprocess
import re
 
def func():
    i = -1
    str1 = ["0","0","0","0","0"]
    str3 = ["0","0","0","0","0"]
    #tt = []
    while 1:
        getIPV6_process = subprocess.Popen("ifconfig", stdout = subprocess.PIPE)#get ipv6 address of the host  
        output = (getIPV6_process.stdout.read())
        ipv6_pattern='(([a-f0-9]{1,4}:){7}[a-f0-9]{1,4})'
        m = re.findall(ipv6_pattern, str(output))
        tt = []
        for l in range (0,len(m)):
            tt.append(m[l][0])
        tt = list(set(tt))
        num = tt.index('2402:f000:1:4414:21f:d0ff:fe0f:4c1a')
        tt.pop(num)
        tmp = set(tt)-set(str3)  #judge the ipv6 address whether produce by computer or by ourself
        tmp = list(tmp)
        if len(tmp) > 0:
            for k in range(0,len(tmp)):#if produce by compuyer ,then del it
                print tmp[k]
                str2 = "sudo /sbin/ip -6 addr del " + str(tmp[k]) + "/64 dev eth0"
                commands.getoutput(str2)
        s1 = hex(random.randint(0x0,0xffff))
        s2 = hex(random.randint(0x0,0xffff))
        s3 = hex(random.randint(0x0,0xffff))
        s4 = hex(random.randint(0x1,0xffff))
        s1 = s1.lstrip("0x")
        s2 = s2.lstrip("0x")
        s3 = s3.lstrip("0x")
        s4 = s4.lstrip("0x")

        #print s1
        i = i + 1
        j = i % 5
        print i
        str3[j] = "2402:f000:1:4414:"+s1+":"+s2+":"+s3+":"+s4 #produce a random address
        print str3[j]
        str1[j]="sudo /sbin/ip -6 addr add 2402:f000:1:4414:" + s1 + ":" + s2 + ":" + s3 + ":" + s4 + "/64 dev eth0"
        commands.getoutput(str1[j])
        time.sleep(60)
        if i >= 4:
            if j == 0:
                print commands.getoutput(str1[1].replace('addr add','addr del'))
            elif j ==1:
                commands.getoutput(str1[2].replace('addr add','addr del'))
            elif j ==2:
                commands.getoutput(str1[3].replace('addr add','addr del'))
            elif j ==3:
                commands.getoutput(str1[4].replace('addr add','addr del'))
            else:
                commands.getoutput(str1[0].replace('addr add','addr del'))
timer = threading.Timer(60, func)#wait a certain time ,then call func
timer.start()
