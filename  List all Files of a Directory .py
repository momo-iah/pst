from os import listdir
from os.path import isfile , join

file_list = [f for f in listdir('/home') if isfile(join('/home', f))]

from os import walk

f = []
for (dirpath, dirnames, filenames) in walk('/home'):
    f.extend(filenames)
    break

import glob
print(glob.glob("/usr/bin/*.txt"))