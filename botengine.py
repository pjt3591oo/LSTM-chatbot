import codecs
from bs4 import BeautifulSoup
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
from keras.models import load_model
import numpy as np
import random, sys

model = load_model('mnist_mlp_model.h5')

fp = codecs.open("./converted.txt", "r", encoding="utf-8")
content = fp.readlines()
text = ''.join(content)

chars = sorted(list(set(text)))


char_indices = dict((c, i) for i, c in enumerate(chars)) # 문자 → ID
indices_char = dict((i, c) for i, c in enumerate(chars)) # ID → 문자

# 텍스트를 maxlen개의 문자로 자르고 다음에 오는 문자 등록하기
maxlen = 20
step = 3
sentences = []
next_chars = []

for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i + maxlen])
    next_chars.append(text[i + maxlen])


# 후보를 배열에서 꺼내기
def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

# model.fit(X, y, batch_size=128, nb_epoch=1)
# model.save('mnist_mlp_model.h5')

# 학습시키고 텍스트 생성하기 반복


# 임의의 시작 텍스트 선택하기
start_index = random.randint(0, len(text) - maxlen - 1)

def make_reply(sentence):
    generated = ''
    # sentence = t
    # generated += sentence
    # print('--- 시드 = "' + sentence + '"')
    # sys.stdout.write(generated)

    # 시드를 기반으로 텍스트 자동 생성
    for i in range(40):
        x = np.zeros((1, maxlen, len(chars)))
        for t, char in enumerate(sentence):
            x[0, t, char_indices[char]] = 1.

        # 다음에 올 문자를 예측하기
        preds = model.predict(x, verbose=0)[0]
        next_index = sample(preds, 0.8)
        next_char = indices_char[next_index]

        # 출력하기
        generated += next_char
        sentence = sentence[1:] + next_char
        # sys.stdout.write(next_char)
        # sys.stdout.flush()

    return generated

if __name__ == '__main__':
    make_reply('운동')
    make_reply('치킨먹고싶다')
    make_reply('운동해야하는데')
    make_reply('학교가고싶다')