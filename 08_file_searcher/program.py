import os
import pathlib


def print_header():
    print("----------------------------------")
    print("        FILE SEARCH APP")
    print("----------------------------------")
    print()

def get_folder_from_user():
    folder = input('What folder do you want to search? ')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None
    
    return os.path.abspath(folder)
    # return pathlib.Path(folder).absolute()

def get_search_text_from_user():
    text = input('What are you searching for [single phrases only]? ')
    return text.lower()

def search_folders(folder, text):
    print(f'Would search for {folder} for [{text}]')

    all_matches  = []
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            continue
    
        matches = search_file(full_item, text)
        all_matches.extend(matches)

    return all_matches

def search_file(filename, search_text):
    matches = []
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            if line.lower().find(search_text) >= 0:
                matches.append(line)
        
        return matches

def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print('Sorry we cant search that location.')
        return 

    text = get_search_text_from_user()
    if not text:
        print('Sorry we cant search for nothing.')
        return 

    matches = search_folders(folder, text)
    for match in matches:
        print(match)

if __name__ == "__main__":
    main()