#coding:utf-8
import os
#在linux下用epoll，程序在windows下调试
# if os.name!="nt":
#     from twisted.internet import epollreactor
#     epollreactor.install()
# else:
#     from twisted.internet import iocpreactor
#     iocpreactor.install()
from twisted.internet import reactor,defer
from twisted.internet.protocol import ServerFactory,Protocol
from twisted.python import log
import sys
from myunpack import myUnpack
from myFilter import myFiler
from myHandler import myHandler
from myContainter import myContainter
from myMysql import myMysql
class serverProtocol(Protocol):

    def __init__(self):
        pass

    def connectionMade(self):
        self.factory.num=self.factory.num+1
        log.msg("Connection %s count=%d"%(self.transport.getPeer(),self.factory.num))
        self.myUnpack=myUnpack(self)

    def connectionLost(self, reason):
        self.factory.num = self.factory.num - 1

    def dataReceived(self, data):
        log.msg(data)
        self.myUnpack.unpackage(data)

class myFactory(ServerFactory):
    protocol = serverProtocol
    #做一些全局变量,给所有的protocal用
    def __init__(self,myfilter):
        #记录连接的客户端总数
        self.num=0
        self.filter=myfilter
#完成单例模式
def makeInit(args):
    db=myMysql(args["mysqlDB"])
    #re=
    containter=myContainter()
  #  myhandler=myHandler(db,re,containter)
    myhandler = myHandler(db, containter)
    myfilter=myFiler(myhandler)
    factory=myFactory(myfilter)
    return factory

args={
    "tcpPort":5002,
    "mysqlDB":("127.0.0.1",'iot','root','root')
}
log.startLogging(sys.stdout)
reactor.listenTCP(args["tcpPort"],makeInit(args))
reactor.run()