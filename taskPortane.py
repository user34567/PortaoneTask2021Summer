def get_file(input_text):
    path = str(input(input_text))
    try:
        return open(path, 'r')
    except:
        return None


def get_files():
    file1 = get_file("Enter path to file1test: ")
    file2 = get_file("Enter path to file2test: ")
    while file1 is None or file2 is None:
        if file1 is None:
            file1 = get_file("File 1 not found\n Enter path to file1 again: ")
        if file2 is None:
            file2 = get_file("File 2 not found\n Enter path to file1 again: ")
    return [file1, file2]


def get_names_from_file(file):
    names = set()
    name = None
    line = file.readline()[:-1]  
    while line != '':
        split_arr = line.split("user: ")
        for i in range(1, len(split_arr)):
            name = split_arr[i].split(",")[0]
            names.add(name)
        line = file.readline()[:-1]
    file.close()
    if name is not None:
        if name[-1] == '"':
            names.remove(name)
            names.add(name[:-1])
    return names


def get_unique_names(file, unique_names):
    line = file.readline()[:-1]
    name = None
    while line != '':
        split_arr = line.split("user: ")
        for i in range(1, len(split_arr)):
            name = split_arr[i].split(",")[0]
            unique_names.discard(name)
        line = file.readline()[:-1]
    file.close()
    if name is not None:
        if name[-1] == '"':
            unique_names.discard(name)
    return unique_names


def print_names(names):
    for name in names:
        print(name)


def main():
    files = get_files()
    names_in_first_file = get_names_from_file(files[0])
    names = get_unique_names(files[1], names_in_first_file)
    print_names(names)


main()
