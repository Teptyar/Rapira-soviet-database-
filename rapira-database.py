welcome_massage = '''
                              ******************************************************************       
                              * Добро пожаловать в стилизованную базу данных "РАПИРА-1981"!*
                              ******************************************************************  

                       Разработана Новосибирским Научно-Исследовательским Институтом АН СССР в 1981 году.
                                                 Все стандарты ГОСТ соблюдены.
    '''

main_menu = ''' 
 Пожалуйста, выберите Ваше дальнейшее действие:

 1 - добавить новый контакт

 2 - вывести все добавленные контакты

 3 - найти контакт

 4 - удалить существующий контакт

 5 - выйти
 '''

global_contacts = []
current_id = 0

print(welcome_massage)

t = True

while t:
    print(main_menu)

    x = input()
    if x == '1':
        full_name = str(input(" Имя контакта. Пожалуйста,введите ФИО полностью: "))
        contact_number = int(input(" Контактный номер. Пожалуйста, введите номер телефона : "))
        post_index = int(input(" Адрес по КЛАДР. Пожалуйста, введите почтовый индекс адреса: "))
        subject_of_rf = str(input(" Пожалуйста, введите название субъекта РФ в следующем формате ТВЕРСКАЯ ОБЛ: "))
        city = str(input(" Пожалуйста, введите наименование населенного пункта в следующем формате ГОР. МОСКВА: "))
        street = str(input(" Пожалуйста, введите название улицы в следующем формате УЛ. ЛЕНИНА: "))
        house = int(input(" Пожалуйста, введите номер дома:  "))
        apt = int(input(" Пожалуйста, введите номер квартиры: "))
        print("Пожалуйста, удостоверьтесть в корректном написании данных о контакте:")
        contact_info = [current_id, full_name, contact_number, post_index, subject_of_rf, city, street, house, apt]
        current_id += 1
        print(contact_info)
        global_contacts.append(contact_info)
    elif x == '2':
        for i in range(0, len(global_contacts)):
            citizen = global_contacts[i]
            identification = citizen[0]
            citizen_name = citizen[1]
            citizen_number = citizen[2]
            adress = citizen[3:7]+['Д.', citizen[7], 'КВ.', citizen[8]]

            print('Идентификатор контакта:', identification)
            print('Имя Контакта:', citizen_name)
            print('Номер контакта:', citizen_number)
            print('Адрес Контакта:', adress)
            print('--------------------------------------------------------------------')
    elif x == '3':
        print('Пожалуйста, введите ФИО контакта: ')
        search_name = input()
        not_found = True
        for i in range(0, len(global_contacts)):
            citizen = global_contacts[i]
            citizen_name = citizen[1]
            if search_name == citizen_name:
                print(citizen)
                not_found = False
        if not_found:
            print("Не найдено.")
    elif x == '4':
        print('Введите Идентификатор контакта, который хотите удалить: ')
        index_to_delete = None
        identification_to_delete = int(input())
        not_found = True
        for i in range(0, len(global_contacts)):
            citizen = global_contacts[i]
            identification = citizen[0]
            if identification_to_delete == identification:
                index_to_delete = i
                not_found = False
        if not_found:
            print("Не найдено.")
        else:
            global_contacts.pop(index_to_delete)
            print("Удалено")
    elif x == '5':
        print('Сеанс окончен, всего Вам доброго!')
        t = False
    else:
        print(" Ошибка. Пожалуйста, выберите один из предложенных вариантов.")

