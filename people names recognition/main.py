
import csv
import subprocess
import sys

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from nltk.corpus import stopwords


csv.field_size_limit(sys.maxsize)

def get_similar_names(word):
    matches_bytes = subprocess.check_output(['/home/chrysogonus/Keyword-Hero/people names recognition/heise first names/gender.out', '-find_similar_name_utf8', word])
    return get_matches(matches_bytes)

def get_matches(matches_bytes):
    return matches_bytes.decode('iso8859-1').split("'")[1].split(';')

def is_name(word):
    gender = subprocess.check_output(['/home/chrysogonus/Keyword-Hero/people names recognition/heise first names/gender.out', '-get_gender', word])
    if 'name not found' in gender.decode('utf8'):
        print(word + ' ; '+ gender.decode('utf8'))
        return None
    else:
        print(word + ' ; '+ gender.decode('utf8'))
        return True

file = open('/usr/share/dict/words', 'r')
file_data = file.readlines()
no_names = [no_name.replace('\n', '') for no_name in file_data if no_name[0].isupper() ==False ]
stopwords = stopwords.words('german') + stopwords.words('english')

all_names_dict = {}

def fill_dict_with_names(names_dict, names_txt, coding):

    file = open(names_txt)
    file_data = file.readlines()
    names = [name.lower().replace('\n', '') for name in file_data if len(name) > 1 and len(name.split()) ==1]
    for name in names:
        all_names_dict[name] = None

fill_dict_with_names(all_names_dict, 'names_data_base/popular_first_names.txt', 'iso-8859-1')
all_names_list = all_names_dict.keys()


def add_person_labels(csvfile, coding):
# gets:

# does:

    names_found = 0

    new_csfile = 'person_labels_included_'+csvfile
    with open(new_csfile, 'w', newline='') as csvf2:
        writer = csv.writer(csvf2, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        with open(csvfile, newline='', encoding=coding) as csvf:
                reader = csv.reader(csvf, delimiter=' ', quotechar='|')
                for row in reader:
                    new_keyword = ' '.join(row).split(',')[1]
                    filtered_keyword = [word for word in (new_keyword.replace('"', '').split()) if word not in stopwords ]

                    person_label = "false"
                    person = "None"
                    for word in filtered_keyword:
                        if word in all_names_dict:
                            person_label = "true"
                            names_found += 1
                            person = word
                    row.append(';'+person_label)
                    row.append(';'+person)
                    writer.writerow(row)
    print(names_found)


add_person_labels('keywordset_klein.csv', 'iso-8859-1')
#add_person_labels('keywords_123makler.csv', 'iso-8859-1')
