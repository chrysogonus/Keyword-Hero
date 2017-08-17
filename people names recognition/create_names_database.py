import codecs

new_names_file = open('./names_data_base/popular_first_names.txt', 'w')
f = codecs.open('./heise first names/nam_dict.txt', 'r', 'iso-8859-1')
lines = f.readlines()

name_rows = lines[362:]
popular_enough = 4

for name_row in name_rows:
    split = name_row.split(' ')
    filtered = [entry for entry in split if entry != '']
    name = filtered[1]
    popularity = []
    for entry in filtered[2:]:
        for character in entry:
            if character.isdigit() or character in 'ABCD':
                popularity.append(character)

    popular_flag = False
    highest_score = 0
    for score in popularity:
        if score.isdigit() and int(score) >= popular_enough:
                popular_flag = True
                if int(score) > highest_score:
                    highest_score = int(score)

        elif score in 'ABCD':
            highest_score = 10

    if popular_flag:
        new_names_file.write(name+'\n')#+';'+str(highest_score)+'\n')
        #print(name)
        #print(highest_score)

new_names_file.close()
