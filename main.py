import os

def rename_files(mapping_file, directory):
    # Load the mapping from the text file
    mappings = {}
    with open(mapping_file, 'r') as f:
        for line in f:
            parts = line.strip().split(' ', 1)
            if len(parts) == 2:
                number, filename = parts
                formatted_number = number.zfill(4)
                mappings[filename] = formatted_number
    
    # Process the files in the directory
    for filename in os.listdir(directory):
        if filename in mappings:
            new_filename = mappings[filename] + "_" + filename
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {old_file_path} -> {new_file_path}')

# Path to the mapping file and the directory with the files
mapping_file = './rename_file/mapping.txt'
directory = './rename_file'

rename_files(mapping_file, directory)
