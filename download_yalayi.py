import re
import os
import urllib.request



'''
下载https://www.yalayi.com里的图片
如果不能检索字符串，要用url_read.decode('utf-8)来重新编码（url_read可替换）
'''
def url(number):
	return f'https://www.yalayi.com/gallery/{number}.html'
#url_http = 'https://www.yalayi.com/gallery/251.html'
def url_yuan(number):
	return urllib.request.urlopen(url(number)).read()
#print(url_yuan(186))

def getpiclist(number):
	url_pattr = re.compile(r'https:\/\/yly\.hywly\.com\/img\/gallery\/%d\/.*?\.jpg' % number)
	return re.findall(url_pattr,url_yuan(number).decode('utf-8'))

def downloadmmpic(number):
	os.mkdir(f'{number}')
	os.chdir(f'./{number}/')
	n = 1
	for x in getpiclist(number):
		urllib.request.urlretrieve(x, f'{number}-{n}.jpg')
		n += 1
	print('Download is done.\n')
	return None

downloadmmpic(238)
