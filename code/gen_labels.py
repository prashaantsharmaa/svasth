import csv
import numpy as np


text_file = csv.reader(open('labels_init.txt'), delimiter=" ")

f = open('labels-three-categories.txt','w')

for row in text_file:
	if row[2] == 'NORM':
		f.write('0\n')
	elif row[3] == 'B' :
			f.write('1\n')
	else:
		f.write('2\n')

f.close()
