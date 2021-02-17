# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 19:52:41 2020

@author: faisa
"""

class Contact():
    def __init__(self, name=None, no_phone=None, email=None, address=None):
        self.name=name
        self.no_phone= no_phone
        self.email= email
        self.address= address
    
    def add_contact(self, other):
        if self.name== None:
            raise Exception('Name cannot empty')
        if self.no_phone== None:
            self.no_phone= 'empty'
        if self.email== None:
            self.email='empty'
        if self.address== None:
            self.address= 'empty'
        list_contact=[self.name.capitalize(), self.no_phone, self.email, self.address]
        other.append(list_contact)
        print ('Contact has been added')
    
    def del_contact(self, other, name=None):
        for i in other:
            if name.capitalize()== i[0]:
                other.remove(i)
                print('Contact has been deleted')
        if i[0] != name.capitalize():
                print ('Can not find the contact') 
            
    
    def search_contact(self, other, obj='name', value=None):
        if obj == 'name':
            for i in other:
                if value in i:
                    print ("Phone Number: {}\n".format(i[1]) +
                           "Email: {}\n".format(i[2]) +
                           "Address: {}\n".format(i[3]))
                    break
            if i[0] != value:
                print ('Can not find the contact')
                
        elif obj == 'no_phone':
            for i in other:
                if value in i:
                    print ("Name: {}\n".format(i[0]) +
                           "Email: {}\n".format(i[2]) +
                           "Address: {}\n".format(i[3]))
                    break
            if i[1] != value:
                print ('Can not find the contact')
                    
    def edit_contact(self, other, obj='name', value=None, new_value=None):
        if obj == 'name':
            for i in other:
                old_name=i[0]
                if value.capitalize() in i:
                    i[0]= new_value.capitalize()
                    print ('Successfully edited')
            if old_name != value.capitalize():
                print ('Can not find the contact')
                
        elif obj == 'no_phone':
            for i in other:
                old_name=i[0]
                if value.capitalize() in i:
                    i[1]= new_value
                    print ('Successfully edited')
            if old_name != value.capitalize():
                print ('Can not find the contact')
                
        elif obj == 'email':
            for i in other:
                old_name=i[0]
                if value.capitalize() in i:
                    i[2]= new_value
                    print ('Successfully edited')
            if old_name != value.capitalize():
                print ('Can not find the contact')
        
        elif obj == 'address':
            for i in other:
                old_name=i[0]
                if value.capitalize() in i:
                    i[3]= new_value
                    print ('Successfully edited')
            if old_name != value.capitalize():
                print ('Can not find the contact')
    
    def reset (self, other):
        other[:]=other[0]
        print ('All contact erased')
    
    def all_contact(self, other):
        import numpy as np
        other=np.array(other[1:])
        from astropy.table import Table
        if other.ndim > 1:
            arr={'name': other[:,0], 'Phone Number': other[:,1], 
                 'Email': other[:,2], 'Address': other[:,3]}
            print(Table(arr))
        else:
            print('There is no contact in your address book')
#%%
def UI():
    text='''
                    MAIN MENU
    
    =========================================
    
    [1] Add a new Contact
    
    [2] List all Contacts
    
    [3] Search for contact
    
    [4] Edit a Contact
    
    [5] Delete a Contact
    
    [6] Reset All
    
    [0] Exit
    
    =========================================='''
    print (text)
#%%
def main():
    import csv
    import os
    import numpy as np
    if os.path.isfile('./Contact.csv') ==  False:
            with open('Contact.csv', 'w', newline='') as csvfile:
                header=['Name', 'Phone Number', 'email', 'address']
                writer = csv.DictWriter(csvfile, fieldnames=header)
                writer.writeheader()
            with open('Contact.csv', newline='') as f:
                reader = csv.reader(f)
                data=list(reader)      
    else:
        with open('Contact.csv', newline='') as f:
            reader = csv.reader(f)
            data=list(reader)
    print('    ===Welcome to Contact Management System===')
    UI()
    choice=int(input('Enter the choice: '))
    while choice !=0:
        if choice== 1:
            name=input('Name: ')
            no_phone=input('Phone number: ')
            email=input('email: ')
            address=input('Address: ')
            new_contact=Contact(name, no_phone, email, address)
            new_contact.add_contact(data)
            UI()
            choice=int(input('Enter the choice: '))
        elif choice== 2:
            new_contact=Contact()
            new_contact.all_contact(data)
            UI()
            choice=int(input('Enter the choice: '))
        elif choice== 3:
            new_contact=Contact()
            menu='''
            [1] Search by Name
            [2] Search by Phone Number
            '''
            print(menu)
            choice2=int(input('Enter choice: '))
            if choice2== 1:
                name=input('Name: ')
                new_contact.search_contact(data, 'name', name.capitalize())
            elif choice2== 2:
                no_phone=input('Phone number: ')
                new_contact.search_contact(data, 'no_phone', no_phone)
            else:
                print('menu is wrong')
            UI()
            choice=int(input('Enter the choice: '))
        
        elif choice== 4:
            new_contact=Contact()
            menu='''
            [1] Edit Name
            [2] Edit Phone number
            [3] Edit Email
            [4] Edit Address
            '''
            print(menu)
            choice2=int(input('Enter choice: '))
            if choice2== 1:
                name=input('Name: ')
                new_name= input('New Name: ')
                new_contact.edit_contact(data, 'name', name, new_name)
            elif choice2== 2:
                name=input('Name: ')
                no_phone=input('New Phone number: ')
                new_contact.edit_contact(data, 'no_phone', name, no_phone)
            elif choice2== 3:
                name=input('Name: ')
                email=input('New email: ')
                new_contact.edit_contact(data, 'email', name, email)
            elif choice2== 4:
                name=input('Name: ')
                address=input('new Address: ')
                new_contact.edit_contact(data, 'address', name, address)
            else:
                print('menu is wrong')
            UI()
            choice=int(input('Enter the choice: '))
        
        elif choice==5:
            name=input('Name: ')
            new_contact=Contact()
            new_contact.del_contact(data, name)
            UI()
            choice=int(input('Enter the choice: '))
            
        elif choice==6:
            asking= input('Are you sure you want to delect all contact? (y/n) ')
            if asking.lower()== 'y':
                new_contact=Contact()
                new_contact.reset(data)
            elif asking.lower()== 'n':
                print('Reset cancelled')
            UI()
            choice=int(input('Enter the choice: '))
    os.remove('Contact.csv')
    with open('Contact.csv', 'w', newline='') as csvfile:
        new_data= np.array(data[1:])
        header=['Name', 'Phone Number', 'email', 'address']
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        if new_data.ndim >1:
            for i in range(len(new_data)):
                writer.writerow({header[0]:new_data[i][0],
                                 header[1]:new_data[i][1],
                                 header[2]:new_data[i][2],
                                 header[3]:new_data[i][3]})
        else:
            pass
if __name__ == '__main__':
    main()
