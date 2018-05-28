#coding:utf-8
from twisted.enterprise import adbapi

from MySQLdb.cursors import DictCursor
class myMysql(object):
    __dbpool=None
    def __init__(self,args=()):
        self.pool=self._getConn(args)

    def _getConn(self,args):
        if self._myMysql__dbpool is None:
            self._myMysql__dbpool=adbapi.ConnectionPool("MySQLdb",host=args[0],
                                              db=args[1],user=args[2],passwd=args[3],charset="utf8",
                                              cursorclass=DictCursor,
                                            use_unicode=True
                                            )
        return self._myMysql__dbpool

    def exclude_sel_run(self,sql):
        d=self.pool.runQuery(sql)
        d.addErrback(self.handle_error)

    def sel_run(self,sql):
        d = self.pool.runQuery(sql)
        d.addErrback(self.handle_error)
        return d

    def handle_error(self,reason):
        print reason