import os
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

os.environ["CLASSPATH"]= '/home/chrysogonus/stanford-ner/stanford-ner.jar'


st = StanfordNERTagger('/home/chrysogonus/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz')

text = 'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'

tokenized_text = word_tokenize(text)
classified_text = st.tag(tokenized_text)

print(classified_text)
