#coding:utf-8
from twisted.internet import defer
import traceback
import json
class myFiler(object):
    def __init__(self,myHandler):
        self.handler = myHandler

    def checkData(self,body,socket):
        d=defer.Deferred()
        d.addCallback(self.returnData,self.noData)
        try:
            if socket.transport.getPeer().type=="TCP":
                #加入Mycontainter中
                data=json.loads(body)
                self.handler.dataHandler(data,d,socket)
            else:
                d.errback("无法辨认的请求类型：from[%s] Message[%s]"%(socket.transport.getPeer().type,body))
        except Exception,msg:
                print msg
    def returnData(self,parm):
        #返回类型数据过滤
        pass

    def noData(self,reason):
        
        print reason,traceback.print_exc()