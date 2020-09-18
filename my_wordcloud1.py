import matplotlib.pyplot as pPlot
from wordcloud import WordCloud, STOPWORDS
import numpy as npy
from PIL import Image
import wikipedia 

def create_word_cloud(string):
   maskArray = npy.array(Image.open("cloud.jpg"))
   cloud = WordCloud(background_color = "white", max_words = 200, mask = maskArray, stopwords = set(STOPWORDS))
   cloud.generate(string)
   cloud.to_file("wordCloud.png")


page = wikipedia.page("Machine Learning")
dataset = page.content
dataset = dataset.lower()

create_word_cloud(dataset)