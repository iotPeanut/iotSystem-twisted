#coding:utf-8

from twisted.internet.protocol import Protocol,ClientCreator
from twisted.internet import reactor
from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import Factory,ClientFactory
import json
import struct
text_content = '''\
HTTP/1.1 200 OK
Content-type: application/json;charset=UTF-8
Access-Control-Allow-Origin: *

'''
class Transfer(Protocol):
        def __init__(self):
                pass
        def connectionMade(self):
                c = ClientCreator(reactor,Clienttransfer)
                c.connectTCP("120.76.210.158",5002).addCallback(self.set_protocol)
                self.transport.pauseProducing()   #防止self.server.transport.wirte()  还没有被初始化就开始写，这个self.server是35行的

        def set_protocol(self,p):  #这里这个P就是Clienttransfer的实例对象
                self.server = p
                p.set_protocol(self)

        def dataReceived(self,data):
            try:
                dataEnd = {}
                self.transport.write(text_content)
                self.transport.loseConnection()
                disData = data.split("\r\n")
                #  print(disData)
                dataSend = disData[0].split(" ")[1][2:].split("&")
                for datai in dataSend:
                    a, b = datai.split("=")
                    dataEnd[a] = b
                dataStr = json.dumps(dataEnd)
                print dataStr
                dataData = struct.pack("bb", 1, dataStr.__len__())
                self.server.transport.write(dataData+dataStr)   #server就是一个client实例，所以这里就是转发给3389的，这里的server就是tcp客户端
            except:
                pass

        def connectionLost(self,reason):
                self.transport.loseConnection()
                self.server.transport.loseConnection()

class Clienttransfer(Protocol):
        def __init__(self):
                pass

        def set_protocol(self,p):
                self.server = p
                self.server.transport.resumeProducing()
                pass
        def dataReceived(self,data):
                self.server.transport.write(data)    #这里就是如果有数据，就转发到下边的，这里的server就是上边的transfer实例，
                pass

factory = Factory()
factory.protocol = Transfer
reactor.listenTCP(5005,factory)  #服务端
reactor.run()