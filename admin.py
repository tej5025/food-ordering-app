#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from data import *
import re
class admin(db):
    
    def __inint__(self, ):
        self.admin_session = admin_session
        self.admin_list = db.admin_list
        self.user_list = db.users_list

    
    def add_item(self):
        if self.admin_session :
            self.food_list = db.food_list
            self.food = {}
            self.name = input("Enter Name for Food item : " )
            self.quantity = input("Enter Quantity include in 1 order with unit : " )
            self.stock = int(input("Enter orders u could take with your ramaining stock : " ))
            self.price = int(input("Enter price per order : " ))
            self.discount = int(input("Enter discount offered on this item : " ))      
            self.foodid = db.food_id

            for j in self.food_list:
                if j['name'] == self.name:
                    print("Food item with same name already Exist, \nfurther procces will only add quanity of book")
                    ip = input('Do you want to continue and add stock , \nchoose y / n : ')
                    if ip == 'y':
                        j['stock'] += self.stock
                        break
                    


            if self.stock <= 0:
                print('stocks can not be less than one , pls enter valid amount of stocks')
            
            else:
                discount = int(self.price)-((int(self.discount)*int(self.price))/100)
                self.food['food_id'] = self.food_id
                self.food['name'] = self.name
                self.food['quantity'] = self.quantity
                self.food['price'] = self.price
                self.food['stock'] = self.stock
                self.food['discount'] = self.discount
                self.food['discounted_price'] = discount
                print("New Book has been created As")
                print(self.food)
                db.food_list.append(self.food)
                db.food_id += 1
                print("Now new book has been added to Food_list")
                
            #print(db.food_list)
        else:
            print('Please login first')
        
    def edit_item_details(self):
        if self.admin_session :
            bkid = int(input("enter food_id to edit food details"))
            for book in db.food_list:
                if book['food_id'] == bkid:
                    print(book)
        
                    print ('\n1.name \n2.quantity, \n3.price \n4.stock ,\n5.discount')
                    entry = int(input("Enter number among above to change "))
                    for keys in book:
                        if entry == 1:
                            val = input("Enter new name to food_id : ")
                            book['name'] = val
                            print('Name of food item coresponding to id has been changed to', val)
                            print(book)
                            break
                        elif entry == 2:
                            val = input("Enter new value to quantity of food per order : ")
                            book['quantity'] = val
                            print('quantity of food coresponding to id has been changed to', val)
                            print(book)
                            break
                        elif entry == 3:
                            val = int(input("Enter new price value to food item : "))
                            book['pages'] = val
                            print('New price value of food coresponding to id has been changed to', val)
                            print(book)
                            break
                        elif entry == 4:
                            val = int(input("Eneter the stock amount in orders to replace existing value"))
                            book['stock'] = val
                            print('value of stocks coresponding to id has been changed to', val)
                            print(book)
                            break
                        elif entry == 5:
                            val = int(input("Enter new Discount on food item : "))
                            book['discount'] = val
                            print('Discount for food item coresponding to id has been changed to', val)
                            print(book)
                            break
                else :
                    print('food id is not found please enter correct book_id')
        else:
            print('Please Log in for doing this operation')
        
        
    def remove_item(self):
        if self.admin_session :
            bkid = int(input("enter food id to remove the food item from menue"))
            for book in db.food_list:
                if book['food_id'] == bkid:
                    print(book)
                    print("Do you really want to remove this food item from menu")
                    option = input("please say yes or no, \n yes will remove the book and no ")
                    if option == "yes":
                        db.food_list.remove(book)
                        print("Food item has been rmoved successfully")
                        break
                    else:
                        print("Please enter valid yes ")
                        break
            else:
                print("Food not item present in database")
        else:
            print('Please Login to perform this task')
    
    def see_menu(self):
        if self.admin_session :
            for food in db.food_list:
                print('This is admin side view only')
                print(food)
        else:
            print('Login Please')
            
            
    def login(self):
        username = input("Enter username : ")
        password = input("Enter password : ")
        for admin in self.admin_list:
            if admin['username'] == username and admin['password'] == password:
                self.admin_session = True
                print('login success, welcome')

            else:
                print('Usename or Passeord is incorrect ,\nPlease check your username and password')

    def logout(self):
        if self.admin_session == True:
            self.admin_session = False
            print("logged out successfully")
        else:
            print("You are not logged in as admin")
        

