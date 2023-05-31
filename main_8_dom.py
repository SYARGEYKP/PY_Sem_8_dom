#Дополнить телефонный справочник возможностью изменения
# и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.
import csv
def readfile(filename):
    data = [i.split() for i in open (filename,'r',encoding='utf-8')]
    return data
def printinfo(data):
    for i in data:
        print(i)
def export (data):
    with open('data.csv', mode='w', encoding ='utf-8') as file:
        writer = csv.writer(file)        
        # Запись данных
        for i in data:
            writer.writerow(i)
def exit_program(my_choice):    
    if my_choice == '0':
       return  
def add_contact(name, phone_number):    
        with open("tel.txt", "a",encoding='utf-8') as file:
            file.write(f"{name}: {phone_number}\n")
        return print(f"Контакт {name} с телефонным номером {phone_number} добавлен в файл")                         

def delete_contact(name):
    with open("tel.txt", "r",encoding='utf-8') as file:
        lines = file.readlines()
    with open("tel.txt", "w",encoding='utf-8') as file:
        for line in lines:
            if line.startswith(name):
                print(f"Контакт {name} удален из файла")
                continue
            file.write(line)  
def main():
    my_choice = -1
    data = readfile('tel.txt')
    print('выберите одно из действий: ') 
    print('1 - вывести на экран инфо') 
    print('2 - произвести экспорт данных')
    print('3 - ввести новую запись в файл')
    print('4 - удалить запись из файла')
    print('0 -  выход из программы')
    my_choice = int(input())
    if my_choice == 1 or my_choice == 2 or my_choice == 0:                        
        operations ={1:printinfo(data),2: export(data), 0:exit_program}
    elif my_choice == 3:
        operations1 ={3: add_contact(input('введите имя для добавления'), input('введите тел для добавления'))}
    elif my_choice == 4:
        operations2 ={4: delete_contact(input('введите имя для удаления '))}
    #operations [my_choice](data) 
if __name__=='__main__':
    main()
    

    

