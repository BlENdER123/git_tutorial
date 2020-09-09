try:
    filename = input('Назовите путь к файлу : ')

    if filename == '-':
        raise ValueError
    else:
        file = open(filename, 'r')
        print('В данном файле : ' + str(len(file.read())) + ' символа(ов)!')
        file.close()
except ValueError:
    print('Пропуск')
except:
    print('Неверный путь к файлу')

try:
    filename_create = input('Назовите какой файл хотите создать/перезаписать? : ')

    if filename_create == '-':
        raise ValueError
    else:
        file_create = open(filename_create, 'w') 

        print('Файл "' + filename_create + '" успешно создан!')

        filetext = input('Что вы хотите записать в файл? : ')

        file_create.write(filetext)

        file_create.close()
except ValueError:
    print('Пропуск')
except:
    print('Произошла ошибка!')

try:
    filecopy_name = input('Какой файл копировать? : ')

    if filecopy_name == '-':
        raise ValueError
    else:
        filecopied = open('_copy_' + filecopy_name, 'w')
        filecopy = open(filecopy_name, 'r')

        filecopied.write(filecopy.read())

        filecopied.close()
        filecopy.close()
except ValueError:
    print('Пропуск')
except:
    print('Произошла ошибка!')


# r - чтение файла
# w - перезапись файла
# a - добавление в файла

# b - binary mode 

