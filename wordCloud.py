from wordcloud import WordCloud
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/spam.csv&quot")
text = " ".join(i for i in data)
stopword= set(STOPWORDS)
wordcloud = WordCloud(stopwords = stopword, background_color='white').generate(text)
plt.figure( figsize=(15,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

