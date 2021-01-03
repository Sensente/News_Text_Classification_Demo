#2018217722 程文
#LSTM
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
#/Users/chengwen/Downloads/
#/Users/chengwen/Downloads/text-classification-master
VECTOR_DIR = 'vectors.bin'

MAX_SEQUENCE_LENGTH = 100 #每序列最大长度
EMBEDDING_DIM = 200       #词向量空间维度
VALIDATION_SPLIT = 0.16   #验证集的比例
TEST_SPLIT = 0.2          #测试集的比例


#加载读入文本
print ('(1) load texts...')
train_texts = open('/Users/chengwen/Downloads/train_contents.txt').read().split('\n')
train_labels = open('/Users/chengwen/Downloads/train_labels.txt').read().split('\n')
test_texts = open('/Users/chengwen/Downloads/test_contents.txt').read().split('\n')
test_labels = open('/Users/chengwen/Downloads/test_labels.txt').read().split('\n')
all_texts = train_texts + test_texts
all_labels = train_labels + test_labels

#转换为向量
print ('(2) doc to var...')
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
import numpy as np

tokenizer = Tokenizer()
tokenizer.fit_on_texts(all_texts)
sequences = tokenizer.texts_to_sequences(all_texts)
word_index = tokenizer.word_index
print('Found %s unique tokens.' % len(word_index))
data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)
labels = to_categorical(np.asarray(all_labels))
print('Shape of data tensor:', data.shape)
print('Shape of label tensor:', labels.shape)

#分割数据集/验证
print ('(3) split data set...')
p1 = int(len(data)*(1-VALIDATION_SPLIT-TEST_SPLIT))
p2 = int(len(data)*(1-TEST_SPLIT))
x_train = data[:p1]
y_train = labels[:p1]
x_val = data[p1:p2]
y_val = labels[p1:p2]
x_test = data[p2:]
y_test = labels[p2:]
print ('train docs: '+str(len(x_train)))
print ('val docs: '+str(len(x_val)))
print ('test docs: '+str(len(x_test)))


#训练模型 LSTM
print ('(4) training model...')
from keras.layers import Dense, Input, Flatten, Dropout
from keras.layers import LSTM, Embedding
from keras.models import Sequential

model = Sequential()
model.add(Embedding(len(word_index) + 1, EMBEDDING_DIM, input_length=MAX_SEQUENCE_LENGTH))
model.add(LSTM(200, dropout=0.2, recurrent_dropout=0.2))
model.add(Dropout(0.2))
model.add(Dense(labels.shape[1], activation='softmax'))
model.summary()


model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['acc'])
print (model.metrics_names)
model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=2, batch_size=128)
model.save('lstm.h5')

#测试模型
print ('(5) testing model...')
print (model.evaluate(x_test, y_test))