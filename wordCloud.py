from turtle import pd

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import  numpy as np
from wordcloud import STOPWORDS
import pandas as pd

type(STOPWORDS)
STOPWORDS.add('said')
print(STOPWORDS)
text = open('/Users/Administrator/AI_project/alice.txt').read()

alice_mask = np.array(Image.open('/Users/Administrator/AI_project/다운로드.jpg'))
alice_mask

wordcloud = WordCloud(max_words=100,
                      stopwords=STOPWORDS,
                      mask=alice_mask,
                      background_color='ivory').generate(text)
plt.figure(figsize=(15,10))
plt.imshow(wordcloud)
plt.axis('off')
# plt.show()


#

# # print(text)
#
# wordcloud = WordCloud().generate(text)
# wordcloud
#
# plt.figure(figsize=(15,10))
# plt.imshow(wordcloud)
# plt.axis('off')
# plt.show()


irisData = pd.read_csv("/Users/Administrator/AI_project/iris.csv")

irisData.columns
df = irisData.groupby('Species').mean()

plt.pie(df['SepalLength'], labels= df.index, autopct= '% .1 %%', startangle= 90)

plt.show()
