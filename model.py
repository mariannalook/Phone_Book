from Info import all_information


# com

class Edit_information:
    # Add new contact
    def add(self):
        # input new contacts date
        name = input('Input name,please!')
        sername = input('Input sername,please!')
        phone = input('Input phone number,please!')

        for n in range(len(all_information)):
            if all_information[n]['Phone'] == phone:
                print('Sorry,this number already exist.Please,try again')
                Edit_information().add()
            else:

                tmp = {}
                tmp['Name'] = name
                tmp['Sername'] = sername
                tmp['Phone'] = phone
        all_information.append(tmp)

    def sort(self):
        all_information.sort(key=lambda x: len(x["Sername"]))

    def delete_record(self):
        choose = input('''If you want delete for name - input 1
            If you want delete for sername - input 2
            If you want delete for number - input 3''')
        ed = input(('Input,please'))
        Edit_information().tmp_del(choose, ed)
        #print(all_information)

    def tmp_del(self, ch, ed):
        if ch == '1':
            k = 'Name'
        if ch == '2':
            k = 'Sername'
        if ch == '3':
            k = 'Phone'
        ind_del = []
        for n in range(len(all_information)):
            if all_information[n][k] == ed:
                ind_del.append(n)
        if len(ind_del) == 0:
            print('Sorry,this contact not found. Please, try again!')
            Edit_information().delete_record()
        if len(ind_del) == 1:
            all_information.remove(all_information[int(ind_del[0])])
        if len(ind_del) > 1:
            for i in range(len(ind_del)):
                print(all_information[i], ' - delete this contact input', i)
            ch = int(input())
            # print(ind_del[ch])
            all_information.pop(ind_del[ch])

    def edit_record(self):
        choose = input('''If you want edit for name - input 1
If you want edit for sername - input 2
If you want edit for number - input 3''')

        ed = input('Input,please:')
        Edit_information().tmp_edit_2(choose, ed)
        print(all_information)

    def tmp_edit(self, new_name, new_sername, new_phone, n):
        if new_name != '':
            all_information[n]['Name'] = new_name
        if new_sername != '':
            all_information[n]['Sername'] = new_sername
        if new_phone != '':
            all_information[n]['Phone'] = new_phone

    def tmp_edit_2(self, choose, ed):
        flag = []
        if choose == '1':
            k = 'Name'
        if choose == '2':
            k = 'Sername'
        if choose == '3':
            k = 'Phone'
        for n in range(len(all_information)):
            if all_information[n][k] == ed:
                flag.append(n)
        if len(flag) == 0:
            print('Sorry,this contact not found,try again')
            Edit_information().edit_record()
        if len(flag) == 1:
            new_name = input('Input new name')
            new_sername = input('Input new sername')
            new_phone = input('Input new phone')
            Edit_information().tmp_edit(new_name, new_sername, new_phone, flag[0])
        if len(flag) > 1:
            for i in range(len(flag)):
                print(all_information[i], ' - edit this contact input', i)
            ch = int(input())
            new_name = input('Input new name')
            new_sername = input('Input new sername')
            new_phone = input('Input new phone')
            Edit_information().tmp_edit(new_name, new_sername, new_phone, flag[ch])

    def see_all(self):
        for i in all_information:
            print('Name: ', i['Name'], 'Sername: ', i['Sername'], 'Phone: ', i['Phone'])

    def see_contact(self):
        de = input('Input name,sername or number')
        for i in all_information:
            if de == i['Name']:
                print('Name: ', i['Name'], 'Sername: ', i['Sername'], 'Phone: ', i['Phone'])
            if de == i['Sername']:
                print('Name: ', i['Name'], 'Sername: ', i['Sername'], 'Phone: ', i['Phone'])
            if de == i['Phone']:
                print('Name: ', i['Name'], 'Sername: ', i['Sername'], 'Phone: ', i['Phone'])
