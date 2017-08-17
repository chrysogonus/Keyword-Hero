import csv
import Levenshtein as ls

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

count = 0
with open('keywords_123makler.csv', newline='', encoding='iso-8859-1') as csvf:
        reader = csv.reader(csvf, delimiter=' ', quotechar='|')

        for row in reader:
            #if count > 1000:
            #    break
            count += 1
            new_keyword = ' '.join(row).split(';')[1]
            print("new keyword : "+' '.join(row))
            for word in (new_keyword.replace('"', '')).split():
                smallest_edit_distance = 100
                best_match = None
                for name in all_names_list:
                    edit_distance = ls.distance(name, word)
                    if edit_distance < smallest_edit_distance and edit_distance <= 2:
                        smallest_edit_distance = edit_distance
                        best_match = name
                if best_match != None:
                    print(word + ' ----Best Match---' + best_match + ' ---Edit Distance---: '+ str(smallest_edit_distance))
                else:
                    print('None')
