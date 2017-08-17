import subprocess

word = 'John'
output = subprocess.check_output(['ls', '-1'])
print(output)
gender = subprocess.check_output(['/home/chrysogonus/Keyword-Hero/people names recognition/heise first names/gender.out', '-get_gender', word])
print(gender.decode('iso8859-1'))
