#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8-*-
import re
import urllib2
from bs4 import BeautifulSoup
#002023海特高新2013年年度报告
url = 'http://quotes.money.163.com/f10/ggmx_002023_1311716.html'
def go():
    headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6"}
    req = urllib2.Request( url, headers = headers)
    content = urllib2.urlopen(req).read()
    g = re.findall('(?<=xe4xb8x80xe3x80x81xe6xa6x82xe8xbfxb0).*?(?=xe4xbax8cxe3x80x81xe4xb8xbbxe8x90xa5xe4xb8x9axe5x8axa1xe5x88x86xe6x9ex90)',content,re.S)
    g = g[0]
    a = re.findall('(?<=<br/><br/><br/><br/>&ensp;).*?(?=<br/><br/><br/><br/>)',g, re.S)
    for i in range(len(a)):
        b = re.compile("<br/><br/><br/><br/>&ensp;"+a[i]+"<br/><br/><br/>")
        g = b.sub('',g)
    print BeautifulSoup(g).prettify()

if __name__ == '__main__':
    go()
