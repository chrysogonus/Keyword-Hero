
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import csv
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import random

all_names_dict = {}

def fill_dict_with_names(names_dict, names_csv, coding):

    with open(names_csv, encoding=coding) as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            if len(row) == 1:
                #print(''.join(row))
                all_names_dict[''.join(row)] = None

fill_dict_with_names(all_names_dict, 'names_csvs/germany.csv', 'iso-8859-1')
#fill_dict_with_names(all_names_dict, 'names_csvs/all_names.csv', 'iso-8859-1')

all_names_list = all_names_dict.keys()
train1 = [(name.lower(), 'name') for name in all_names_list]

file = open('/usr/share/dict/words', 'r')
file_data = file.readlines()
train2 = [(no_name.replace('\n', ''), 'no_name') for no_name in file_data if no_name[0].isupper() ==False ]
random.shuffle(train1)
random.shuffle(train2)
train = train1+train2[:2000]
random.shuffle(train)
#print(train[:100])



c = NaiveBayesClassifier(train)

print('Training completed')


with open('keywords_123makler.csv', newline='', encoding='iso-8859-1') as csvf:
        reader = csv.reader(csvf, delimiter=' ', quotechar='|')
        for row in reader:

            new_keyword = ' '.join(row).split(';')[1]
            person_label = "false"
            person = "None"

            print(new_keyword)
            for word in (new_keyword.replace('"', '')).split():
                #word.replace('"', '')
                #if count < 1000:
                #    print(word.capitalize())
                print(c.classify(word))
