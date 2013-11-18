#coding=utf-8
#author:u'王健'
#Date: 13-6-1
#Time: 下午9:21
import json
import os
from tools.util import getImagesUrl

__author__ = u'王健'

from google.appengine.ext import db


#记录最新的用户名
class UserAddress(db.Model):
    '''
    model 的 key_name 由tel的密文构成
    '''
    username = db.StringProperty()#用户名
    #address = db.StringProperty()#单点登录sessionid



