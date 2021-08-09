#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from data import *
import re


class user(db):
    def __init__(self):
        self.session = []
        self.email = ''
    
    def register(self):
        isContact = False
        isEmail = False
        isExist = True
        emailReg = r'[\w\.-]+@[\w\.-]+(\.[\w]+)+'
        user = {} 
        name = input('Enter your full name : ')
        print("Be carefull you will not get a chance to update contact" )
        contact = input('Enter your contact number (10 digit only): ')
        if contact.isdigit():
            
            if len(contact)==10:
                isContact = True
        else:
            isContact = False
        print("Be carefull you will not get a chance to update email" )
        email = input('Enter your email : ')
        for i in range(len(db.user_list)):
            mail = db.users_list[i]['email']
            if mail==email:
                isExist=True
                break
        else:
            isExist=False
        if bool(re.search(emailReg, email)):
            isEmail = True
        address = input('Enter your Address: ')    
        password = input('Enter your password : ')
        if isContact==True and isEmail==True and isExist==False:
            contact = int(contact)
            user['name'] = name
            user['contact'] = contact
            user['email'] = email
            user['address'] = address
            user['password'] = password

            db.user_list.append(user)
            #print(db.users_list)
            if user:
                print(user)
                print('Your account has been created successfully')
            else:
                print('There is some error in creating user account')

        elif isContact == False:
            print('Contact can only be of 10 digits!' )

        elif isEmail==False:
            print('Please enter a valid email!')

        elif isExist==True:
            print('This email already exists')
            
    def login(self):
        users = db.user_list
        username = input('Enter your email : ')
        password = input('Enter your password : ')
        if len(users)>0:
            for i in range(len(users)):
                if users[i]['email']==username and users[i]['password']==password:
                    # breakpoint()
                    self.session = True
                    self.email = username
                    print('Login success, Welcome to Library', end=" ")
                    self.functions_of_users()
                    break
                else:
                    pass
            else:
                print('Password or username is incorrrect')
        else:
            print('No users')
            
    def functions_of_users(self):
        flag=1
        while flag!=0:
            print('+=========================+')
            print('**   Select any option   **')
            print('+=========================+')
            print('| 1.) Place new order     |')
            print('| 2.) Order History       |')
            print('| 3.) Update Profile      |')
            print('| 4.) Go back             |')
            print('+=========================+')
            option = int(input('Enter the option : '))
            print('\n')
            if option==1:
                self.place_order()
            elif option==2:
                self.order_history()
            elif option==3:
                self.update_profile()
            elif option==4:
                break
            else:
                print('Invalid input!')

    
    def place_order(self):
        if self.session:
            food = db.food_list
            cart = []
            for f in food:
                print(str(f['food_id']) + ". " + f['name'] + " (" + f['quantity'] + ") [INR " + str(f['price']) + "]" )

            food_order = list(map(int, input('Enter food ID : ').split(',')))
            cart = []
            food_id_to_order = []
            for i in food_order:
                for j in food:
                    if j['food_id']==i:
                        stock=j['stock']
                        if stock<1:
                            name = food[j]['name']
                            food_id = food[j]['food_id']
                            print(f'No stock is available for {name} ({food_id})')
                        else:
                            temp_list = []
                            food_id_to_order.append(j['food_id'])
                            temp_list.append(j['food_id'])
                            temp_list.append(j['name'])
                            temp_list.append(j['stock'])
                            temp_list.append(j['quantity'])
                            temp_list.append(j['price'])
                            temp_list.append(j['discount'])
                            temp_list.append(j['discounted_price'])
                            cart.append(temp_list)
                            #print(cart)
                        continue
    
                else:
                    print(f'{i} is not availabale, Please enter a valid food ID')
                self.cart(cart, food_id_to_order)

            else:
                print('There are no food items to view\n')
        else:
            print('PLease login')
            
    def cart(self, cart, food_id_to_order):
        if cart:
            order = db.order_history
            food = db.food_list
            table_list = []
            total_cost = 0
            for i in range(len(cart)):
                temp_list = []
                temp_list.append(cart[i][0])
                temp_list.append(cart[i][1])
                price = 'Rs. '+str(cart[i][6])
                total_cost+=cart[i][6]
                temp_list.append(price)
                table_list.append(temp_list)
                print(table_list)
            for i in table_list:
                print(i)
            
            print('  Confirm your order  ')
            print('------------------------')
            print('| 1.) Yes   | 2.) No   |')
            print('+===========+==========+')
            print('Total : Rs. '+str(total_cost))
            
            user_input = int(input('Enter your choice : '))
            if user_input==1:
                email = self.email
                for ids in food_id_to_order:       
                    for food_list in range(len(food)):
                        if food[food_list]['food_id']==ids:
                            stock = food[food_list]['stock']
                            food[food_list]['stock']=stock-1
                            temphis = {}
                            temphis['email'] = email
                            temphis['order'] = table_list
                            order.append(temphis)
                            print('Order Placed successfully')
                            #print(temphis)
                            
            elif user_input==2:
                del table_list
                print('Your order has been canceled\n')
            else:
                print('Invalid option')
        
        
    def update_profile(self):
        if self.session:
            email = self.email
            for user in db.user_list:
                if user['email'] == email:
                    print(user)
        
                    print ('1.name \n2.address \n3.password'  )
                    entry = int(input("Enter number among above to change "))
                    for keys in user:
                        if entry == 1:
                            val = input("Enter Name with changes : ")
                            user['name'] = val
                            print('Your Name has been changed to', val)
                            print(book)
                            break
                        elif entry == 2:
                            val = int(input("Enter new address : "))
                            user['address'] = val
                            print('Your address has been changed to', val)
                            print(book)
                            break
                        elif entry == 3:
                            val = int(input("Eneter New Password : "))
                            user['password'] = val
                            print('Your Password has been changed to', val)
                            print(book)
                            break
                    else :
                        print('Email not found')
      
    
    def order_history(self):
        if self.session:
            email = self.email
            food = db.order_history
            for i in food:
                if i['email'] == email:
                    print (i)
        else:
            print('login for order history')
                    
                
    def logout(self):
        if self.session:
            self.Session=False
            print('logout out sucess, Thank You')

