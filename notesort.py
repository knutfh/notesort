import os
import sys

folder = os.path.abspath(sys.argv[1])

mapping = {}

# populate dictionary with instrument names
with open('Instruments.txt') as mapping_file:
    for line in mapping_file:
        prefix, body = line.split()
        mapping[prefix] = body

for filename in os.listdir(folder):
    prefix, extension = os.path.splitext(filename)
    # only rename PDF files
    if not extension.endswith('.pdf'):
        continue
    if prefix in mapping:
        newFileName = ''.join(prefix + '_' + mapping[prefix] + extension)
        oldPath = os.path.join(folder, filename)
        newPath = os.path.join(folder, newFileName)
        os.rename(oldPath, newPath)
        print 'Renamed', filename, '-->', newFileName
