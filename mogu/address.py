#coding=utf-8
#Date: 11-12-8
#Time: 下午10:28
from google.appengine.api import memcache
from models.model import UserAddress
from tools.page import Page
from tools.util import getResult

__author__ = u'王健'


keystr = 'address%s'
def getAddress(address):
    key = keystr % address
    p = memcache.get(key)
    if not p:
        p = UserAddress.get_by_key_name(key)
        if p:
            memcache.set(key, p, 3600 * 24 * 7)
            return p
        else:
            return None
    else:
        return p


def setAddress(address, username):
    key = keystr % address
    p = getAddress(address)
    if not p:
        p = UserAddress(key_name=key)
        p.username = username
        p.put()

    memcache.set(key, p, 3600 * 24 * 7)
    return p


class UserAddressUpdate(Page):
    def post(self):
        try:
            username = self.request.get('UserName')
            game = self.request.get('address')

            p=setAddress(game, username)
            self.flush(getResult(True))
        except:
            self.flush(getResult(False, False, u'保存失败。'))




class UserNameQuery(Page):
    '''
    用来查询，用来查询游戏的积分，并且排序。
    '''
    def post(self):
        '''
        查询并输出而且排序
        '''
        result = {'list':[]}
        try:
            addresslist = self.request.get('address', '').split(',')
            for address in addresslist:
                if address:
                    p = getAddress(address)
                    if p:
                        result['list'].append({'username':p.username, 'address':address})
            self.flush(getResult(result,message=u'查询成功'))
        except:
            self.flush(getResult(False, False, u'查询失败。'))

