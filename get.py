import urllib2
from lxml import etree
import os

header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
            , "Connection": "keep-alive"
         }

def get_pic():
    url_list = []
    with open('/Users/zhangzhiliang/zzl/aijiu.txt') as f:
        for x in f.readlines():
            url_list.append(x[0:-1])

    for url in url_list:
        req = urllib2.Request(url, headers=header)
        html = urllib2.urlopen(req)
        htmldata = html.read()
        htmlpath = etree.HTML(htmldata)
        pic_url = htmlpath.xpath('//div[@id="js_content"]/p')[0].xpath('//img')[0].xpath('//@data-src')[0]
        pic_name = '%s.jpeg'%(htmlpath.xpath('//h2/text()')[0].strip())

        # save img
        req = urllib2.Request(pic_url, headers=header)
        urlhtml=urllib2.urlopen(req)
        resp=urlhtml.read()


        save_path = os.path.join('/Users/zhangzhiliang/zzl/aijiu', pic_name)
        binfile = open(save_path, 'wb')
        binfile.write(resp)
        binfile.close()
        
        
if __name__ == '__main__':
    get_pic()
