import os
import struct
import array
import time
import socket
import IPy
import threading
import subprocess

ipPool = []               #build a global buffer to buffer ip adderss
f1=open("result1.txt","w")
class SendPingThr(threading.Thread):    # send thread
    def __init__(self,icmpPacket, icmpSocket):
        threading.Thread.__init__(self)
        self.sock = icmpSocket
        self.packet = icmpPacket

    def run(self):
        time.sleep(0.01)  #wait 0.01s for recv thread start
        i = -1
        while 1:
            i = i+1
            try:
                print i
                print ipPool[i]
                self.sock.sendto(self.packet,(ipPool[i],0))#sendto the specified  ipaddress ipPool[i]
                time.sleep(0.01)
            except:
                break

class Nscan:
    def __init__(self):
        self.__id = os.getpid()

    def __inCksum(self,packet):  #calculate checknum
        if len(packet) & 1:
            packet = packet + '\0'
        words = array.array('h', packet)
        sum = 0
        for word in words:
            sum += (word & 0xffff)
        sum = (sum >> 16) + (sum & 0xffff)
        sum = sum + (sum >> 16)
        return (~sum) & 0xffff

    def mPing(self, ipPool):
        recvFroms = []
        result = []
        result1 = []
        Sock = socket.socket(socket.AF_INET6, socket.SOCK_RAW, 58) 
        packet = struct.pack("BbHHh", 128, 0, 0, self.__id, 0)   #build the icmpv6 packet
        chksum = self.__inCksum(packet)
        packet = struct.pack("BbHHh", 128, 0, chksum, self.__id, 0)

        sendThr = SendPingThr(packet, Sock)     #send thread start
        sendThr.start()

        while True:
            try:
                recvFroms.append(Sock.recvfrom(1024)[1][0]) #receive the packet 
            except Exception:
                pass
            finally:
                if not sendThr.isAlive():
                    break
        #print recvFroms[0]
		#tmp = [val for val in ipPool if val in recvFroms]
        #result.append(tmp)
        recvFroms = set(recvFroms)  #convert the list (recvFroms)
        ipPool = set(ipPool)
        result = ipPool & recvFroms #check the result of receive  & with the ipPool
        result1 =[i for i in result]
        tt = -1 
        while 1:
            try:
                tt = tt+1
                print result1[tt]
                f1.write(result1[tt]+"\n")#write to f1
            except:
                break

if __name__=='__main__':
    s = Nscan()
    f = open("ip_prefix1.txt","r") #read the prefix to generate the whole ip address
    for i in f:
        tmp = i.split()
        l = 0
        for j in range(0x0,0x100):
            k = 1
            s1 = str(hex(j))
            s3 = s1.lstrip("0x")
            #print s1
            for k in range (0x1,0x100):
                s2 = str(hex(k))
                s4 = s2.lstrip("0x")
                if s1 == "0x0":
                    str1 = tmp[l]+"::"+s4  #the form of ip 
                else:
                    str1 = tmp[l]+"::"+s3+":"+s4 # the form of ip
                ipPool.append(str1)
                print str1
        l = l+1
    s.mPing(ipPool)
