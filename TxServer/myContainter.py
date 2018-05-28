#coding:utf-8

class myContainter(object):

    def __init__(self):
        self.users={}

    def get(self,id):
        if id in self.users.keys():
            return self.users[id]
        return None

    def set(self,id,socket):
        if id in self.users.keys():
            if self.users[id]==socket:
                return
        self.users[id]=socket
        print self.users[id]

    def num(self):
        return len(self.users)

    def delete(self,id):
        if id in self.users.keys():
            del self.users[id]
            return True
        return False
