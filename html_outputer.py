#coding:utf8
'''
Created on 2016

@author: Administrator
'''

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []


    def collect_data(self,data):
        if data is None:
            return 
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html','w')
        fout.write("<html>")
        fout.write('<meta charset="utf-8"></meta>')
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            #fout.write("<td>%s</td>"% data['url'])
            #fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td><a href='%s'>%s</a></td>" % (data["url"].encode("utf-8"),data["title"].encode("utf-8")))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        