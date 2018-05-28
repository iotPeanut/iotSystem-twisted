#coding:utf-8

class checkID(object):
    def __init__(self,db):
        self.db=db


    @staticmethod
    def idVerify(func):
        def wrapper(*args,**kwargs):
            db=args[0].db
            #检测是否数据库中有对应的ID
            db.sel_run("select ")




            return func(*args,**kwargs)

        return wrapper