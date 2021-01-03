# 2018217745 林泓一
import sys


VECTOR_DIR = 'vectors.bin'

MAX_SEQUENCE_LENGTH = 100 # 每条新闻最大长度
EMBEDDING_DIM = 200 # 词向量空间维度
TEST_SPLIT = 0.2 # 测试集比例

#把训练集和测试集的数据读出
print('(1) load texts...')
train_texts = open('train_contents.txt', encoding="utf-8").read().split('\n')
train_labels = open('train_labels.txt', encoding="utf-8").read().split('\n')
test_texts = open('test_contents.txt', encoding="utf-8").read().split('\n')
test_labels = open('test_labels.txt', encoding="utf-8").read().split('\n')
all_text = train_texts + test_texts

print('(2) doc to var...')
#文档集用tf-idf值填充，让它集成为一个 17600 x 65604 的 tf-idf 矩阵。

#使用 sklearn里的 CountVectorizer 与 TfidfTransformer 函数
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

#只考虑每个单词出现的频率；然后构成一个特征矩阵，每一行表示一个训练文本的词频统计结果
count_v0 = CountVectorizer();
counts_all = count_v0.fit_transform(all_text);
count_v1 = CountVectorizer(vocabulary=count_v0.vocabulary_);
counts_train = count_v1.fit_transform(train_texts);
print("the shape of train is " + repr(counts_train.shape))
count_v2 = CountVectorizer(vocabulary=count_v0.vocabulary_);
counts_test = count_v2.fit_transform(test_texts);
print("the shape of test is " + repr(counts_test.shape))

#TfidfTransformer用于统计vectorizer中每个词语的TF-IDF值
tfidftransformer = TfidfTransformer();
train_data = tfidftransformer.fit(counts_train).transform(counts_train);
test_data = tfidftransformer.fit(counts_test).transform(counts_test);

x_train = train_data
y_train = train_labels
x_test = test_data
y_test = test_labels


#训练集和测试集如果分别提取特征的话会导致他们的特征空间不同，导致同一个词语的序号可能不相同或者完全不存在
#所以我们先用所有文档共同提取特征，然后得到一个词典，利用该词典分别给训练集和测试集提取特征
print('(3) Naive Bayes...')
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

clf = MultinomialNB(alpha=0.01)
clf.fit(x_train, y_train);
preds = clf.predict(x_test);
num = 0
preds = preds.tolist()
for i, pred in enumerate(preds):
    if int(pred) == int(y_test[i]):
        num += 1
print('precision_score:' + str(float(num) / len(preds)))










