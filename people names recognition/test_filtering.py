import csv
from nltk.corpus import stopwords

file = open('/usr/share/dict/words', 'r')
file_data = file.readlines()
no_names = [no_name.replace('\n', '') for no_name in file_data if no_name[0].isupper() ==False ]
stopwords = stopwords.words('german')

f = open('stopwords_german.txt', 'w+')

for word in stopwords:
    f.write(word+'\n')

f.close()


with open('keywords_123makler.csv', newline='', encoding='iso-8859-1') as csvf:
        reader = csv.reader(csvf, delimiter=' ', quotechar='|')
        for row in reader:

            new_keyword = ' '.join(row).split(';')[1]
            print(new_keyword.replace('"', '').split())

            filtered_text = [word for word in (new_keyword.replace('"', '').split()) if word not in stopwords ]

            print(' '.join(filtered_text))
