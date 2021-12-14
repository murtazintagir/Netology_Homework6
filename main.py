documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }


def catalogue():
  '''
    Список доступных команд:
      p - вывод владельца по номеру документа
      s - вывод номера полки по номеру документа
      l - вывод списка документов в формате: тип "номер" "владелец"
      a - добавить документ (потребуется ввод типа, номера, владельца и номера полки для хранения документа
      d - удалить документ (функция в разработке)
      m - переместить документ
      as - добавить полку для хранения документов
      doc - список документов
      dir - список полок с документами
      exit - выход из программы
      help - справка
  '''
  print("Добро пожаловать в информационный каталог")
  print("Для вызова справки введите команду help")
  com = ''
  doc_exist = False # наличие документа в каталоге
  dir_exist = False # наличие полки
  while com != 'exit':
    com = str(input("Введите команду: "))
    if com == 'p':
      number_doc = input("Введите номер документа: ")
      doc_exist = check_docs(number_doc) # проверка наличия документа
      if doc_exist:
        print_doc(number_doc)
    elif com == 's':
      number_doc = input("Введите номер документа: ")
      doc_exist = check_docs(number_doc) # проверка наличия документа
      if doc_exist:
        print_dir(number_doc)
    elif com == 'd':
      number_doc = input("Введите номер документа: ")
      doc_exist = check_docs(number_doc) # проверка наличия документа
      if doc_exist:
        del_doc(number_doc)
    elif com == 'm':
      number_doc = input("Введите номер документа: ")
      doc_exist = check_docs(number_doc) # проверка наличия документа
      if doc_exist:
        number_dir = input("Введите номер полки: ")
        dir_exist = check_dir(number_dir) # проверка наличия полки
      if doc_exist and dir_exist:
        move_doc(number_doc, number_dir)
    elif com == 'as':
        number_dir = input("Введите номер полки: ")
        create_dir(number_dir)
    elif com == 'l':
      list_doc()
    elif com == 'a':
      type_doc = input("Введите тип документа: ")
      number_doc = input("Введите номер документа: ")
      name = input("Введите владельца документа: ")
      number_dir = input("Введите номер полки для хранения документа: ")
      if type_doc == '' or number_doc == '' or name == '' or number_dir == '':
        print("Пожалуйста, заполните все поля!")
      else: add_doc(type_doc, number_doc, name, number_dir)
    elif com == 'doc':
      print(documents)
    elif com == 'dir':
      print(directories)
    elif com == 'help':
      print(catalogue.__doc__)
    elif com == 'exit':
      continue
    else:
      print("Неизвестная команда!")
      print("Для вызова справки введите команду help")
  print("До свидания!")

def check_docs(number_doc):
  i = 0
  for k, v in directories.items():
    if number_doc in v:
      return True
    elif i == len(directories) - 1:  # если достигли конца списка и не нашли указанный номер документа, выводим сообщение
      print(f"Документ \"{number_doc}\" не найден!")
      print(f"Для создания документа \"{number_doc}\" введите команду \"a\"")
    i += 1

def check_dir(number_dir):
  i = 0
  for k, v in directories.items():
    if number_dir in k:
      return True
    elif i == len(directories) - 1:  # если достигли конца списка и не нашли указанный номер документа, выводим сообщение
      print(f"Полка \"{number_dir}\" не найдена!")
      print(f"Для создания полки \"{number_dir}\" введите команду \"as\"")
    i += 1

def print_doc(number_doc):
  i = 0
  while i < len(documents):
    f = documents[i]
    if number_doc == (f['number']): # если есть указанный номер документа
      print(f"Владельцем документа \"{number_doc}\" является {f['name']}")  # выводим имя владельца
      break                         # завершаем просмотр если документ найден
    i += 1

def print_dir(number_doc):
  i = 0
  for k,v in directories.items():
    if number_doc in v:
      print(f"Документ \"{number_doc}\" расположен на полке {k}")
      break
    i += 1

def list_doc():
  i = 0
  while i < len(documents):
    f = documents[i]
    print(f"{f['type']} \"{f['number']}\" \"{f['name']}\"")
    i += 1

def add_doc(type_doc, number_doc, name, number_dir):
  len1 = len(documents)
  f1 = {}
  f2 = {}
  l1 = []
  l2 = []
  f1['type'] = type_doc
  f1['number'] = number_doc
  f1['name'] = name
  documents.append(f1)
  len2 = len(documents)
  if len2 > len1:
    print("Список документов обновлен.")
  else: print("Список документов не обновлен!")
  for k in directories.keys():
    l1.append(k)
  if number_dir in l1:
    value = directories[number_dir]
    value.append(number_doc)
    print(f"Документ {number_doc} добавлен на полку {number_dir}.")
  else:
    print(f"Полка {number_dir} не существует")
    com = str(input("Хотите создать полку? y/n "))
    if com == 'y':
      l2.append(number_doc)
      f2[number_dir] = l2
      directories.update(f2)
      print(f"Документ {number_doc} добавлен на полку {number_dir}.")
    else: print(f"Документ {number_doc} не добавлен на полку {number_dir}.")

def del_doc(number_doc):
  i1 = 0
  i2 = 0
  for k,v in directories.items():
    if number_doc in v:
      v.remove(number_doc)
    i1 += 1

  while i2 < len(documents):
    f = documents[i2]
    if number_doc == (f['number']): # если есть указанный номер документа
      f.clear()                     # удаляем запись из каталога
    i2 += 1

  print(f"Документ \"{number_doc}\" удален")

def move_doc(number_doc, number_dir):
  i = 0
  for k,v in directories.items():
    if number_doc in v:
      v.remove(number_doc)
      v1 = directories[number_dir]
      v1.append(number_doc)
      print(f"Документ \"{number_doc}\" перемещен на полку {number_dir}")
      break

def create_dir(number_dir):
  l1 = []
  l2 = []
  f = {}
  for k in directories.keys():
    l1.append(k)
  if number_dir in l1:
    print(f"Полка {number_dir} существует")
  else:
    print(f"Полка {number_dir} не существует")
    com = str(input("Хотите создать полку? y/n "))
    if com == 'y':
      f[number_dir] = l2
      directories.update(f)
      print(f"Полка {number_dir} создана.")
    else: print(f"Полка {number_dir} не создана.")

catalogue() # вызов управляющей программы