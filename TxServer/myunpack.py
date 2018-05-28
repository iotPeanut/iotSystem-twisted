#coding:utf-8
#防止黏包，毡包，在这里解析
import struct

class myUnpack(object):
    HEADER_SIZE=2
    def __init__(self,socket):
        self.sumData=""
        self.socket=socket     #记录这个socket，便于想下边传

    def unpackage(self,newData):
        self.sumData=self.sumData+newData
        while True:
            if len(self.sumData)<self.HEADER_SIZE:
                print("数据包(%s BYTE)小于包头"%len(self.sumData))
                break
                """如果发整形
            bodySize=self.sumData[1:self.HEADER_SIZE]
            bodySize=int(bodySize,16)
            """
            head=struct.unpack('!2b',self.sumData[:self.HEADER_SIZE])
            bodySize=head[1]
            if len(self.sumData)<(bodySize+self.HEADER_SIZE):
                print("数据包(%s BYTE)小于整个包的长度"%len(self.sumData))
                break
            body=self.sumData[self.HEADER_SIZE:self.HEADER_SIZE+bodySize]
            #处理拿到的数据
            self.socket.factory.filter.checkData(body,self.socket)
            self.sumData=self.sumData[self.HEADER_SIZE+bodySize:]