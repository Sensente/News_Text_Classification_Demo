#2018217722 程文
import json
import xml.dom.minidom

xml = open("/Users/chengwen/Downloads/news_sohusite_xml.txt").read() #打开源文件
docs_xml = xml.split('<doc>\n') #分割语义
print(len(docs_xml)) #用于数据校验
del docs_xml[0]
docs = []

# 进行分割转换为JSON格式
for doc_xml in docs_xml:
    if (len(doc_xml.split('<url>')) != 2) or (len(doc_xml.split('<docno>')) != 2) or (len(doc_xml.split('<contenttitle>')) != 2) or (len(doc_xml.split('<content>')) != 2):
        continue
    url = doc_xml.split('<url>')[1].split('</url>')[0]
    docno = doc_xml.split('<docno>')[1].split('</docno>')[0]
    title = doc_xml.split('<contenttitle>')[1].split('</contenttitle>')[0]
    content = doc_xml.split('<content>')[1].split('</content>')[0]
    doc = {'url':url, 'docno':docno, 'title':title, 'content':content}
    docs.append(doc)

#写入新的JSON文件
print (len(docs))
fout = open("/Users/chengwen/Downloads/news_sohusite.json",'w')
fout.write(json.dumps(docs,ensure_ascii=False))
fout.close()