from os import path
from scipy.misc import imread
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud

f=open('comment_iphone8_2.txt','r')
text = f.read()

cut_text = ' '.join(jieba.lcut(text))
#print(cut_text)
color_mask = imread("iphone8pro.jpg")
cloud = WordCloud(
    font_path='FZMWFont.ttf',
    background_color='white',
    mask=color_mask,
    max_words=200,
    max_font_size=5000
)
word_cloud = cloud.generate(cut_text)
plt.imshow(word_cloud)
plt.axis('off')
plt.show()
plt.savefig('iphone8cloud_2.png')
