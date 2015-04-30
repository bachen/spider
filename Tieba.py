#coding=utf-8
#---------------------------------------
#   程序：百度贴吧爬虫
#   版本：0.1
#   作者：baidu
#   日期：2015-03-18
#   语言：Python 2.7
#   操作：输入带分页的地址，去掉最后面的数字，设置一下起始页数和终点页数。
#   功能：下载对应页码内的所有页面并存储为html文件。
#---------------------------------------
 
import string, urllib2
 
#定义百度函数
def baidu_tieba(url,begin_page,end_page):   
    for i in range(begin_page, end_page+1):
        sName = string.zfill(i,5) + '.html'#自动填充成六位的文件名
        print 'download' + str(i) + 'page, save as ' + sName + '......'
        f = open(sName,'w+')
        m = urllib2.urlopen(url + str(i)).read()
        f.write(m)
        f.close()
 
if __name__=="__main__":
#-------- 在这里输入参数 ------------------
# 用 idle 运行
# 这个是 读书吧 中某一个帖子的地址
#bdurl = 'http://tieba.baidu.com/p/3639125570?pn='
#iPostBegin = 2
#iPostEnd = 10

	bdurl = str(raw_input(u'input url and delete the number behind pn=:\n'))
	begin_page = int(raw_input(u'input page to start \n'))
	end_page = int(raw_input(u'input page to end \n'))
	#-------- 在这里输入参数 ------------------

	#调用
	baidu_tieba(bdurl,begin_page,end_page)
