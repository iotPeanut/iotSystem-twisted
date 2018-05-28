#coding:utf-8
#from .action import heart
import datetime
class myHandler(object):
    flag=1
    def __init__(self,db,containter):
        self.db=db
        self.containter=containter
        # self.actionFromClientToServer={
        #     "heart":heart,
        #     "register":
        #
        #
        #
        # }

    def dataHandler(self,data,d,socket):
        try:
            if data["command"]=="sendToServer":
                self.containter.set(data["id"], socket)
                #self.db.exclude_sel_run("insert into iotsystem_data (name,value,time) values ('%s',%f,'%s') "%(data["data"][1],data["data"][0],datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            elif data["command"]=="transmitOther":
                # if myHandler.flag == 1:
                #     self.containter.get(data["id"]).transport.write("1")
                #     myHandler.flag = 0
                # else:
                #     self.containter.get(data["id"]).transport.write("0")
                #     myHandler.flag = 1
                #.encode(encoding='UTF-8')
                print "dataindataindatain   ",data["data"],data["command"]
                self.containter.get(data["id"]).transport.write(data["data"])
            elif data["command"]=="hello":
                print"pengliang"
        except :
            raise