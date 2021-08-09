#!/usr/bin/env python
# coding: utf-8

# In[ ]:



from admin import *
from user import *

class menu(admin):
    admin = admin()
    user = user()
    j = 1
    try:
        while j!=0:
            print('+----------+')
            print('|1.| Admin |')
            print('|2.| Users |')
            print('|3.| Exit  |')
            print('+----------+')
            request = int(input('Please select an option : '))
            if request==1:
                i=1
                try:
                    while i!=0:
                        print('+=========================+')
                        print('**   Select any option   **')
                        print('+=========================+')
                        print('| 1.) Admin Login         |')
                        print('| 2.) Add Food Items      |')
                        print('| 3.) View Food Items     |')
                        print('| 4.) Edit Food Items     |')
                        print('| 5.) Delete Food Items   |')
                        print('| 6.) Logout              |')
                        print('+=========================+')
                        user_input = int(input('Please select the field : '))
                        print('\n')
                        if user_input==1:
                            admin.login()
                        elif user_input==2:
                            admin.add_item()
                        elif user_input==3:
                            admin.see_menu()
                        elif user_input==4:
                            admin.edit_item_details()
                        elif user_input==5:
                            admin.remove_item()
                        elif user_input==6:
                            admin.logout()
                            i=0
                            break
                        else:
                            print('Invalid input')
                except:
                    print('No options selected!')
            elif request==2:
                i=1
                try:
                    while i!=0:
                        print('+=========================+')
                        print('**   Select any option   **')
                        print('+=========================+')
                        print('| 1.) Login               |')
                        print('| 2.) Register            |')
                        print('| 3.) Exit                |')
                        print('+=========================+')
                        user_input = int(input('Please select the field : '))
                        print('\n')
                        if user_input==1:
                            user.login()
                        elif user_input==2:
                            user.register()
                        elif user_input==3:
                            print('Thank you for choosing Us')
                            i=0
                            break
                        else:
                            print('Invalid input')

                except Exception as e:
                    print(e)
                         #print('No options selected!')
            elif request==3:
                j=0
                print('Logging out of portal')
                break

    except:
        print('No option selected! Program exiting Admin...........', end=" ")

