import os
import sys

FOLDER = os.path.abspath(sys.argv[1])


def create_instrument_map():
    """Create a dictionary mapping each prefix
    to the corresponding instrument name."""
    with open('Instruments.txt') as instrument_file:
        return {
            line.split()[0]: line.split()[1] for line in instrument_file
        }


def rename_files_with_instrument_name(instrument_map):
    """Rename PDF files in folder based on the root of
    the original file name."""
    for filename in os.listdir(FOLDER):
        root, extension = os.path.splitext(filename)
        if not extension.endswith('.pdf'):
            continue
        try:
            if root[2]:
                part_number = root[3]
                instrument_number = root[:2]
                if instrument_number in instrument_map:
                    new_file_name = '{prefix}_'\
                                    '{instrument_name}'\
                                    '{part_number}'\
                                    '{extension}'.format(
                                        prefix=root[:2],
                                        instrument_name=instrument_map[root[:2]],
                                        part_number=root[3],
                                        extension=extension)
        except:
            if root in instrument_map:
                new_file_name = '{prefix}_{instrument_name}{extension}'.format(
                                    prefix=root,
                                    instrument_name=instrument_map[root],
                                    extension=extension)
        old_path = os.path.join(FOLDER, filename)
        new_path = os.path.join(FOLDER, new_file_name)
        os.rename(old_path, new_path)
        print 'Renamed', filename, '-->', new_file_name

if __name__ == '__main__':
    instrument_map = create_instrument_map()
    rename_files_with_instrument_name(instrument_map)
