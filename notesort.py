import os
import sys

mapping = {}
folder = os.path.abspath(sys.argv[1])

with open('Instruments.txt') as mapping_file:
    for line in mapping_file:
        prefix, body = line.split()
        mapping[prefix] = body

for filename in os.listdir(folder):
    prefix, extension = os.path.splitext(filename)
    # print prefix, extension
    if not extension.endswith('.pdf'):
        continue
    if prefix in mapping:
        newFileName = ''.join(prefix + '_' + mapping[prefix] + extension)
        oldPath = os.path.join(folder, filename)
        newPath = os.path.join(folder, newFileName)
        # print ''.join("Renaming " + filename + " --> " + newFileName)
        os.rename(oldPath, newPath)
        print 'Renamed', filename, '-->', newFileName
