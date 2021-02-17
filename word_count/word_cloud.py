from os import path
import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, STOPWORDS
import pandas as pd


root_dir = r'F:\Edin\1_2\Design with Data\Project\word_count\per_subject_combined'



def draw_word_cloud(file, name):
    file = open(file, encoding='UTF-8').read()
    default_mode = jieba.cut(file)
    text = " ".join(default_mode)
    stopwords = set(STOPWORDS)
    stopwords.add("said")
    stopwords.add("Broadside")
    stopwords.add("broadside")
    stopwords.add("ballad")
    stopwords.add("published")
    wc = WordCloud(
        # set the font
        font_path=r'F:\Edin\1_2\Design with Data\Project\word_count\GIL.TTF',
        background_color="white",
        max_words=200,
        width=200,
        height=200,
        stopwords=stopwords)
    # generate word cloud
    wc.generate(text)

    # show
    plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis("off")
    plt.figure()
    plt.show()


    dirName = root_dir + "\\" + "word_cloud"
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    word_cloud_name = name + ".jpg"
    wc.to_file(path.join(dirName, word_cloud_name))



def read_file():
    path = os.listdir(root_dir + "\\" + "text")
    for file in path:
        name = file.split('.')[0]
        print(name)
        fp = root_dir + "\\" + "text" + '\\' + file
        f = open(fp, encoding='utf-8')
        print()
        print('filename: ', file)
        f.close()
        draw_word_cloud(fp, name)


read_file()