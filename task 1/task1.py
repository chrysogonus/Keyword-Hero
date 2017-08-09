#Author: Christopher Filsinger

import tldextract
import csv
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from fuzzyset import FuzzySet as fuzzs

matching_cutoff = 50

'''
brand - recommended cutoff

simple - 50
123makler - 50
mandmdirect - 40
'''


def get_brand_from_url(url):
    return tldextract.extract(url).domain

#Tests
'''
print(get_brand_from_url('www.mandmdirect.com'))
print(get_brand_from_url('http://www.123makler.de'))
print(get_brand_from_url('https://www.simple.com'))
'''

# concept: we use approximate string matching also known as
# fuzzy string matching # for the calculation of our labels
# true (brand name recognized) # and false (brandname was not recognized)

# link to python library: https://pypi.python.org/pypi/fuzzywuzzy

def get_keyword_matches(brand, csvfile, coding):
# gets:
# the name of the brand we want to match in the corresponding keyword set,
# the name of the csvfile containing the keyword set,
# the coding for the csvfile

# does:
# creates a new file named 'matches_included_'+ former csvfile name which stores
# additionally to the former csvfile the labels true or false
# concerning the recognition of the brand name and the corresponding ratio values

    new_csfile = 'matches_included_'+csvfile
    with open(new_csfile, 'w', newline='') as csvf2:
        writer = csv.writer(csvf2, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        with open(csvfile, newline='', encoding=coding) as csvf:
                reader = csv.reader(csvf, delimiter=' ', quotechar='|')
                for row in reader:

                    new_keyword = ' '.join(row).split(';')[1]
                    ratio = fuzz.token_sort_ratio(brand, new_keyword)
                    #alternative version for approximate string matching
                    #_, ratio = process.extractOne(brand, new_keyword)
                    if ratio >= matching_cutoff:
                        match = '"true"'
                        print(' '.join(row).split(';')[0]+' : '+new_keyword+' : '+ str(ratio))
                    else:
                        match = '"false"'
                    row.append(';'+match)
                    row.append(';'+str(ratio))
                    writer.writerow(row)

#Tests

get_keyword_matches('mandmdirect', 'keywords_mandmdirect.csv', 'windows-1252')
#get_keyword_matches('123makler', 'keywords_123makler.csv', 'iso-8859-7')

# for the test case 'simple' you need to change the 1 to 0 (different format)
# in line: new_keyword = ' '.join(row).split(';')[1]
#get_keyword_matches('simple', 'keywords-simple.com.csv', 'utf-8')
