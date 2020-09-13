# Задание 1
"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


with open('my_text.txt', 'w') as my_obj:
    while True:
        my_str = input('введите строку: ') + '\n'
        my_obj.writelines(my_str)
        if my_str == '\n':
            break


# Задание 2
"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, 
количества слов в каждой строке.
"""

with open('task_2_text.txt', 'r') as my_text:
    content = my_text.readlines()
    print(content)
    line_cnt = 0
    for el in content:
        line_cnt += 1
        print(f'Строка {line_cnt}, количество слов {len(el.split())}')

# Задание 3
"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, 
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.
"""

with open('employees.txt', 'r') as empl_sal:
    salary_calc = empl_sal.readlines()
    # print(salary_calc)
    person = {}
    for el in salary_calc:
        person_list = el.split()
        person.update({person_list[0]: int(person_list[1])})
    # print(person)
    min_salary = 1000000
    person_cnt = 0
    salary_sum = 0
    for key, val in person.items():
        if val < min_salary:
            min_salary = val
            person_name = key
        salary_sum = salary_sum + val
        person_cnt += 1
    print(f'person with the least salary - {person_name}, {min_salary}\n'
      f'average salary = {salary_sum / person_cnt}')

# Задание 4
"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
"""
rus_numb = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
with open('task_4_text.txt') as numb_text:
    numbers = numb_text.readlines()

    numb_en_dict = {}
    for el in numbers:
        numb_en = el.split()
        numb_en_dict.update({numb_en[0]: int(numb_en[2])})

result = {}
for key, val in numb_en_dict.items():
    result.update({val: rus_numb.get(val)})

result_list = []
result_str = ''
for key, val in result.items():
    result_str = f'{val} - {str(key)} \n'
    result_list.append(result_str)

with open('result_text.txt', 'w') as result_text_rus:
    result_text_rus.write(''.join(result_list))

# Задание 5
"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

my_numbers_text = open('task_5_text.txt', 'w')
my_numbers_text.write(input('введите числа через пробел: '))

my_numbers_text = open('task_5_text.txt', 'r')
numbers = my_numbers_text.read()

sum_num = 0
for el in numbers.split():
    sum_num = sum_num + int(el)
print(sum_num)
my_numbers_text.close()

# Задание 6
"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, 
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно 
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

with open('task_6_text.txt', 'r') as subj_text:
    content = subj_text.readlines()
    # print(content)
    content_list = []
    result_dict = {}
    for el in content:
        # print(el[:el.find(':')]) # Название предмета
        content_list = el.split()
        howers = 0
        content_list.pop(0)
        for item in content_list:
            item.split()
            if len(item) > 1:
                howers = howers + int(item[:item.find('(')])
        print(howers)
        result_dict.update({el[:el.find(':')]: howers})

    print(result_dict)





