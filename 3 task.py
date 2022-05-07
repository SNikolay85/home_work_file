import os

def read_write():
    #file_path = os.path.join(os.getcwd(), 'recipes.txt')
    with open('file_1.txt', 'r', encoding='utf-8') as file1:
        lines1 = file1.readlines()
    with open('file_2.txt', 'r', encoding='utf-8') as file2:
        lines2 = file2.readlines()
    with open('file_3.txt', 'r', encoding='utf-8') as file3:
        lines3 = file3.readlines()

    dict_file = {len(lines1): [lines1, file1.name], len(lines2): [lines2, file2.name], len(lines3): [lines3, file3.name]}
    sorted_tuple = sorted(dict_file.items(), key=lambda x: x[0])
    dict_file = dict(sorted_tuple)

    for j, k in dict_file.items():
        with open('new_file.txt', 'a', encoding='utf-8') as file:
            file.write('\nНазвание файла: ' + k[1] + '\n')
            file.write('Количество строк: ' + str(j) + '\n')
            file.writelines(k[0])


read_write()