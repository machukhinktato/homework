# import os
# import shutil

# EASY.PY DIFFICULTY
# Задача 1

# def create_dirs():
#     dirs = ['dir_1', 'dir_2', 'dir_3', 'dir_4', 'dir_5', 'dir_6', 'dir_7', 'dir_8', 'dir_9']
#     for i in dirs:
#         print(i)
#         os.mkdir(i)
#
#     print(os.listdir())
#
#
# def delete_dirs():
#     dirs = ['dir_1', 'dir_2', 'dir_3', 'dir_4', 'dir_5', 'dir_6', 'dir_7', 'dir_8', 'dir_9']
#     for k in dirs:
#         print(k)
#         os.removedirs(k)


# create_dirs()
# delete_dirs()


# Задача-2:

# def list_dir ():
#     buffer = os.listdir()
#     print('Список файлов:')
#     for index, element in enumerate(buffer, start=1):
#         if os.path.isdir(element):
#             print('{}. {}'.format(index, element))
#
#
# list_dir()

# Задача-3:

# def current_file_copy():
#     name_file = os.path.realpath(__file__)
#     new_file = name_file + '.copy'
#     if os.path.isfile(new_file) != True:
#         shutil.copy(name_file, new_file)
#         return new_file + ' - создан'
#     else:
#         return 'Файл уже скопирован'
#
#
# print(current_file_copy())
