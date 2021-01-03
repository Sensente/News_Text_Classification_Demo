# 2018217722 程文
import sys
import json
#读取文件
docs = json.load(open('/Users/chengwen/Downloads/news_sohusite.json'))
label_maps = json.load(open('/Users/chengwen/Downloads/url_to_catagory_to_label.json'))
num_of_docs_of_label = [0]*15
docs_labeled = {}

#进行标签
num = 0
num_labeled = 0
for doc in docs:
    num += 1
    if num%10000 == 0:
        print (num)
    content = doc['title']+' '+doc['content']
    url = doc['url']
    label = None
    for label_map in label_maps:
        if label_map['url'] in url:
            label = label_map['label']
            break
    if label is None:
        continue
    num_labeled += 1
    if str(label) not in docs_labeled:
        docs_labeled[str(label)] = []
        docs_labeled[str(label)].append(content)
    else:
        docs_labeled[str(label)].append(content)

#查看标签结果
print ('all:'+str(len(docs)))
print ('labeled:'+str(num_labeled))

for i in range(1,16):
    if str(i) in docs_labeled:
        print ('label '+str(i)+':'+str(len(docs_labeled[str(i)])))

fout = open('/Users/chengwen/Downloads/news_sohusite_labeled.json','w')
fout.write(json.dumps(docs_labeled,ensure_ascii=False,indent=4))
fout.close()