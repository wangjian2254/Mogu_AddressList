#coding=utf-8
import os
import re
import string
from jinja2 import filters
from jinja2.filters import environmentfilter

# from mogu.models.model import User


__author__ = 'wangjian2254'


def getResult(result,success=True,message=u'',status=200):
    return {'result':result,'success':success,'message':message,'status':status}


def getImagesUrl(id):
    return "http://%s/download?image_id=%s" % (os.environ['HTTP_HOST'], id)

def datetimeformat(value, format='%Y-%m-%d %H:%M'):
    return value.strftime(format)


filters.FILTERS['datetimeformat'] = datetimeformat
