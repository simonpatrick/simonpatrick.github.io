#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8-*-
# @Date    : 2014-05-20
# @Author  : Lifemaxer
# @Website : http://lifemaxer.com
# @Description1:  <span id="7_nwp" style="width: auto; height: auto; float: none;"><a id="7_nwl" href="http://cpro.baidu.com/cpro/ui/uijs.php?rs=1&u=http%3A%2F%2Flifemaxer%2Ecom%2Fpython%2D2%2Fpython%2Dget%2Dstock%2Dasset%2Dliability%2Dratio%2F&p=baidu&c=news&n=10&t=tpclicked3_hc&q=66004140_cpr&k=python&k0=python&k1=%CD%F8%D2%D7%B2%C6%BE%AD&k2=a%B9%C9&k3=%B9%C9%C6%B1&k4=%B4%B4%D2%B5%B0%E5&k5=%B9%C9%C6%B1%B4%FA%C2%EB&sid=d44a64652711cb8f&ch=0&tu=u1861886&jk=29f312ada2424c5e&cf=29&rb=0&fv=16&stid=9&urlid=0&luki=10&seller_id=1&di=128" target="_blank" mpid="7" style="text-decoration: none;"><span style="color:#0000ff;font-size:13px;width:auto;height:auto;float:none;">python</span></a></span>-大批量自动采集获取<span id="8_nwp" style="width: auto; height: auto; float: none;"><a id="8_nwl" href="http://cpro.baidu.com/cpro/ui/uijs.php?rs=1&u=http%3A%2F%2Flifemaxer%2Ecom%2Fpython%2D2%2Fpython%2Dget%2Dstock%2Dasset%2Dliability%2Dratio%2F&p=baidu&c=news&n=10&t=tpclicked3_hc&q=66004140_cpr&k=%CD%F8%D2%D7%B2%C6%BE%AD&k0=%CD%F8%D2%D7%B2%C6%BE%AD&k1=a%B9%C9&k2=%B9%C9%C6%B1&k3=%B4%B4%D2%B5%B0%E5&k4=%B9%C9%C6%B1%B4%FA%C2%EB&k5=excel&sid=d44a64652711cb8f&ch=0&tu=u1861886&jk=29f312ada2424c5e&cf=29&rb=0&fv=16&stid=9&urlid=0&luki=1&seller_id=1&di=128" target="_blank" mpid="8" style="text-decoration: none;"><span style="color:#0000ff;font-size:13px;width:auto;height:auto;float:none;">网易财经</span></a></span>所有A股上市公司<span id="9_nwp" style="width: auto; height: auto; float: none;"><a id="9_nwl" href="http://cpro.baidu.com/cpro/ui/uijs.php?rs=1&u=http%3A%2F%2Flifemaxer%2Ecom%2Fpython%2D2%2Fpython%2Dget%2Dstock%2Dasset%2Dliability%2Dratio%2F&p=baidu&c=news&n=10&t=tpclicked3_hc&q=66004140_cpr&k=%B9%C9%C6%B1&k0=%B9%C9%C6%B1&k1=%B4%B4%D2%B5%B0%E5&k2=%B9%C9%C6%B1%B4%FA%C2%EB&k3=excel&k4=%B2%C6%BE%AD&k5=%C9%CF%BD%BB%CB%F9&sid=d44a64652711cb8f&ch=0&tu=u1861886&jk=29f312ada2424c5e&cf=29&rb=0&fv=16&stid=9&urlid=0&luki=3&seller_id=1&di=128" target="_blank" mpid="9" style="text-decoration: none;"><span style="color:#0000ff;font-size:13px;width:auto;height:auto;float:none;">股票</span></a></span>资产负债率
# @Description2:  并导入<span id="10_nwp" style="width: auto; height: auto; float: none;"><a id="10_nwl" href="http://cpro.baidu.com/cpro/ui/uijs.php?rs=1&u=http%3A%2F%2Flifemaxer%2Ecom%2Fpython%2D2%2Fpython%2Dget%2Dstock%2Dasset%2Dliability%2Dratio%2F&p=baidu&c=news&n=10&t=tpclicked3_hc&q=66004140_cpr&k=excel&k0=excel&k1=%B2%C6%BE%AD&k2=%C9%CF%BD%BB%CB%F9&k3=%C9%CF%CA%D0%B9%AB%CB%BE&k4=python&k5=%CD%F8%D2%D7%B2%C6%BE%AD&sid=d44a64652711cb8f&ch=0&tu=u1861886&jk=29f312ada2424c5e&cf=29&rb=0&fv=16&stid=9&urlid=0&luki=6&seller_id=1&di=128" target="_blank" mpid="10" style="text-decoration: none;"><span style="color:#0000ff;font-size:13px;width:auto;height:auto;float:none;">excel</span></a></span>表格中
# @Description3:  替换下方中文可修改成获取任意财务数据
# @Tools-Required: BeautifulSoup, xlwt
import re,urllib2
import xlwt
from bs4 import BeautifulSoup
count = 1
class getstock:
    def __init__(self):
        pass

    def go(self):
        #定义网址，获取<span id="11_nwp" style="width: auto; height: auto; float: none;"><a id="11_nwl" href="http://cpro.baidu.com/cpro/ui/uijs.php?rs=1&u=http%3A%2F%2Flifemaxer%2Ecom%2Fpython%2D2%2Fpython%2Dget%2Dstock%2Dasset%2Dliability%2Dratio%2F&p=baidu&c=news&n=10&t=tpclicked3_hc&q=66004140_cpr&k=%C9%CF%BD%BB%CB%F9&k0=%C9%CF%BD%BB%CB%F9&k1=%C9%CF%CA%D0%B9%AB%CB%BE&k2=python&k3=%CD%F8%D2%D7%B2%C6%BE%AD&k4=a%B9%C9&k5=%B9%C9%C6%B1&sid=d44a64652711cb8f&ch=0&tu=u1861886&jk=29f312ada2424c5e&cf=29&rb=0&fv=16&stid=9&urlid=0&luki=8&seller_id=1&di=128" target="_blank" mpid="11" style="text-decoration: none;"><span style="color:#0000ff;font-size:13px;width:auto;height:auto;float:none;">上交所</span></a></span>创业板只需对应修改stock_num为6开头或3开头即可
        stock_num = str(count).zfill(6)
        url = 'http://quotes.money.163.com/f10/zycwzb_'+stock_num+',year.html'
        print(u"<span id="12_nwp" style="width: auto; height: auto; float: none;"><a id="12_nwl" href="http://cpro.baidu.com/cpro/ui/uijs.php?rs=1&u=http%3A%2F%2Flifemaxer%2Ecom%2Fpython%2D2%2Fpython%2Dget%2Dstock%2Dasset%2Dliability%2Dratio%2F&p=baidu&c=news&n=10&t=tpclicked3_hc&q=66004140_cpr&k=%B9%C9%C6%B1%B4%FA%C2%EB&k0=%B9%C9%C6%B1%B4%FA%C2%EB&k1=excel&k2=%B2%C6%BE%AD&k3=%C9%CF%BD%BB%CB%F9&k4=%C9%CF%CA%D0%B9%AB%CB%BE&k5=python&sid=d44a64652711cb8f&ch=0&tu=u1861886&jk=29f312ada2424c5e&cf=29&rb=0&fv=16&stid=9&urlid=0&luki=5&seller_id=1&di=128" target="_blank" mpid="12" style="text-decoration: none;"><span style="color:#0000ff;font-size:13px;width:auto;height:auto;float:none;">股票代码</span></a></span>:" + stock_num)
        headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6"}
        req = urllib2.Request( url, headers = headers)
        try:
            content = urllib2.urlopen(req).read()
        except:
            return
        soup = BeautifulSoup(content)
        #获取名称
        name = soup.find('h1',class_='name').contents[1].contents[0].encode('gb18030').decode('gb18030')
        print name
        ws.write(count, 0, stock_num)
        ws.write(count, 1, name)
        #获取负债率
        a = soup.find_all(class_='table_bg001 border_box fund_analys')
        for i in a:
            #此处替换中文可修改成获取任意财务数据
            if i.find('td',text=re.compile(u'资产负债率')):
               b = i.find('td',text=re.compile(u'资产负债率')).parent.contents
               #<span id="13_nwp" style="width: auto; height: auto; float: none;"><a id="13_nwl" href="http://cpro.baidu.com/cpro/ui/uijs.php?rs=1&u=http%3A%2F%2Flifemaxer%2Ecom%2Fpython%2D2%2Fpython%2Dget%2Dstock%2Dasset%2Dliability%2Dratio%2F&p=baidu&c=news&n=10&t=tpclicked3_hc&q=66004140_cpr&k=%CD%F8%D2%D7%B2%C6%BE%AD&k0=%CD%F8%D2%D7%B2%C6%BE%AD&k1=a%B9%C9&k2=%B9%C9%C6%B1&k3=%B4%B4%D2%B5%B0%E5&k4=%B9%C9%C6%B1%B4%FA%C2%EB&k5=excel&sid=d44a64652711cb8f&ch=0&tu=u1861886&jk=29f312ada2424c5e&cf=29&rb=0&fv=16&stid=9&urlid=0&luki=1&seller_id=1&di=128" target="_blank" mpid="13" style="text-decoration: none;"><span style="color:#0000ff;font-size:13px;width:auto;height:auto;float:none;">网易财经</span></a></span>默认一页最多显示2008-2013年年报共6年
               number = [3,4,5,6,7,8]
               for num in number:
                   if num < len(b):
                         data = b[num].contents[0].decode('unicode_escape')
                         ws.write(count, num-1, data)

if __name__ == '__main__':
    #定义<span id="14_nwp" style="width: auto; height: auto; float: none;"><a id="14_nwl" href="http://cpro.baidu.com/cpro/ui/uijs.php?rs=1&u=http%3A%2F%2Flifemaxer%2Ecom%2Fpython%2D2%2Fpython%2Dget%2Dstock%2Dasset%2Dliability%2Dratio%2F&p=baidu&c=news&n=10&t=tpclicked3_hc&q=66004140_cpr&k=excel&k0=excel&k1=%B2%C6%BE%AD&k2=%C9%CF%BD%BB%CB%F9&k3=%C9%CF%CA%D0%B9%AB%CB%BE&k4=python&k5=%CD%F8%D2%D7%B2%C6%BE%AD&sid=d44a64652711cb8f&ch=0&tu=u1861886&jk=29f312ada2424c5e&cf=29&rb=0&fv=16&stid=9&urlid=0&luki=6&seller_id=1&di=128" target="_blank" mpid="14" style="text-decoration: none;"><span style="color:#0000ff;font-size:13px;width:auto;height:auto;float:none;">excel</span></a></span>表格内容
    wb = xlwt.Workbook()
    ws = wb.add_sheet(u'资产负债表')
    ws.write(0, 0, u'<span id="15_nwp" style="width: auto; height: auto; float: none;"><a id="15_nwl" href="http://cpro.baidu.com/cpro/ui/uijs.php?rs=1&u=http%3A%2F%2Flifemaxer%2Ecom%2Fpython%2D2%2Fpython%2Dget%2Dstock%2Dasset%2Dliability%2Dratio%2F&p=baidu&c=news&n=10&t=tpclicked3_hc&q=66004140_cpr&k=%B9%C9%C6%B1%B4%FA%C2%EB&k0=%B9%C9%C6%B1%B4%FA%C2%EB&k1=excel&k2=%B2%C6%BE%AD&k3=%C9%CF%BD%BB%CB%F9&k4=%C9%CF%CA%D0%B9%AB%CB%BE&k5=python&sid=d44a64652711cb8f&ch=0&tu=u1861886&jk=29f312ada2424c5e&cf=29&rb=0&fv=16&stid=9&urlid=0&luki=5&seller_id=1&di=128" target="_blank" mpid="15" style="text-decoration: none;"><span style="color:#0000ff;font-size:13px;width:auto;height:auto;float:none;">股票代码</span></a></span>')
    ws.write(0, 1, u'<span id="16_nwp" style="width: auto; height: auto; float: none;"><a id="16_nwl" href="http://cpro.baidu.com/cpro/ui/uijs.php?rs=1&u=http%3A%2F%2Flifemaxer%2Ecom%2Fpython%2D2%2Fpython%2Dget%2Dstock%2Dasset%2Dliability%2Dratio%2F&p=baidu&c=news&n=10&t=tpclicked3_hc&q=66004140_cpr&k=%B9%C9%C6%B1&k0=%B9%C9%C6%B1&k1=%B4%B4%D2%B5%B0%E5&k2=%B9%C9%C6%B1%B4%FA%C2%EB&k3=excel&k4=%B2%C6%BE%AD&k5=%C9%CF%BD%BB%CB%F9&sid=d44a64652711cb8f&ch=0&tu=u1861886&jk=29f312ada2424c5e&cf=29&rb=0&fv=16&stid=9&urlid=0&luki=3&seller_id=1&di=128" target="_blank" mpid="16" style="text-decoration: none;"><span style="color:#0000ff;font-size:13px;width:auto;height:auto;float:none;">股票</span></a></span>名称')
    ws.write(0, 2, u'2013-12-31')
    ws.write(0, 3, u'2012-12-31')
    ws.write(0, 4, u'2011-12-31')
    ws.write(0, 5, u'2010-12-31')
    ws.write(0, 6, u'2009-12-31')
    ws.write(0, 7, u'2008-12-31')
    gs = getstock()
    #目前深证最大号为002725，获取<span id="17_nwp" style="width: auto; height: auto; float: none;"><a id="17_nwl" href="http://cpro.baidu.com/cpro/ui/uijs.php?rs=1&u=http%3A%2F%2Flifemaxer%2Ecom%2Fpython%2D2%2Fpython%2Dget%2Dstock%2Dasset%2Dliability%2Dratio%2F&p=baidu&c=news&n=10&t=tpclicked3_hc&q=66004140_cpr&k=%C9%CF%BD%BB%CB%F9&k0=%C9%CF%BD%BB%CB%F9&k1=%C9%CF%CA%D0%B9%AB%CB%BE&k2=python&k3=%CD%F8%D2%D7%B2%C6%BE%AD&k4=a%B9%C9&k5=%B9%C9%C6%B1&sid=d44a64652711cb8f&ch=0&tu=u1861886&jk=29f312ada2424c5e&cf=29&rb=0&fv=16&stid=9&urlid=0&luki=8&seller_id=1&di=128" target="_blank" mpid="17" style="text-decoration: none;"><span style="color:#0000ff;font-size:13px;width:auto;height:auto;float:none;">上交所</span></a></span>创业板请修改相应最大号码
    while count <=2725:
        gs.go()
        wb.save('stockdebt.xls')
        count += 1
