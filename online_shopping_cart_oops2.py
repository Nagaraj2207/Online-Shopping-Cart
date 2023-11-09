#Here we import shopping_oops_validation for validation.

import shopping_oops_validation as my_validation

#Here we import random,tabulate and time module.

import random
import tabulate
import time

#Here we create Shopping class as the Base class (or) parent class.

class Shopping:
    # Here we create constructor and instance variable.
    
    def __init__(self):
        self.__customer_id = "" # Here we create private variable for customer id, it connot access outside the class.
        self._customer_name = ""
        self.__phone_number = "" # Here we create private variable for phone number, it connot access outside the class.
        self.user_information ={}
        self.cart = []
        self.total_price = 0
        self.item_list_key = []
        self.users_total_information = {}

    # Here we create user_input() function to get name and phone number.
         
    def user_input(self):
        name = 1
        while name:
            try:
                self._customer_name = input("\nEnter Your Name:").upper()
                my_validation.cus_name_validation(self._customer_name)
                self.user_detials["Name"] = self._customer_name
                name = 0
            except Exception as er:
                print(er)
        ph_num = 1
        check_value = 0
        while ph_num:
            try:
                self.__phone_number = input("\nEnter Employee Phone Number:")
                my_validation.cus_phone_number_validation(self.__phone_number)
                if self.user_information != {}:
                    for x,my_dict in self.user_information.items():
                        if my_dict["Phone Number"] == self.__phone_number:
                            check_value = 0
                            break
                        
                        else:
                            check_value = 1

                    if check_value > 0:
                        self.user_detials["Phone Number"] = self.__phone_number
                        ph_num = 0
                    else:
                        print("\nYou already entered this phone number.")
                        ph_num = 1

                else:
                    self.user_detials["Phone Number"] = self.__phone_number
                    ph_num = 0
            except Exception as er:
                print(er)

    # Here we create extract_word() function for get supermarket name.

    def extract_word(self):
        self.store_name = "*******Welcome to the FRIENDS online Supermarket*******"
        text1= self.store_name.find("online")
        text2= self.store_name.find("the")
        if text1 > text2:
            self.store_name1= self.store_name[text2+4:text1-1]
            self.store_name1 = self.store_name1.lower()

    # Here create random_num() function for get 4 random number.

    def random_num(self):
        random_num = random.randrange(1000,10000)
        self.random_num1 = str(random_num)

    # Here we create register() function for user sign up process.

    def register(self):
        self.items_list = {"1.Milk":150,"2.Bread":99,"3.Eggs":150}
        self.user_detials = {}
        self.extract_word()
        self.random_num()
        short_place = ""
        self.place = ["adayar","besantnagar","indiranagar","t-nagar"]
        self.places = ["Ad","Bn","In","Tn"]
        print("\n{:<18}(".format(" ")+("*"*11)+"Please Enter the following details"+("*"*11)+")")
        print("\n"+("="*35))
        print("\nThe Available Location are:")
        print("\n"+("="*35))
        print("\n{:<15}Adayar".format(" "))
        print("\n{:<15}Besant nagar".format(" "))
        print("\n{:<15}Indira nagar".format(" "))
        print("\n{:<15}T-nagar".format(" "))
        place = 1
        while place:
            try:
                location = input("\nPlease Choose Location:").lower()
                location = location.replace(" ","")
                my_validation.location_validation(location)
                self.user_detials["Location"] = location
                if location not in self.place:
                    print("\nEntered Location not available.Please enter nearest location")
                else:
                    for x in range(len(self.place)):
                        if location == self.place[x]:
                            short_place = self.places[x]
                            place = 0

            except Exception as er:
                print(er)
        self.__customer_id = self.store_name1+self.random_num1+short_place   
        print("\nYour customer id is:",self.__customer_id)
        self.user_detials["customer_id"] = self.__customer_id 
        self.user_input()
        self.user_information[self.__customer_id ] = self.user_detials
        print("\nHELLO",self._customer_name)
        print("\n{:<21}".format(" "),("~"*45))
        print("\n{:<18}{}".format(" ",self.store_name))
        print("\n{:<21}".format(" "),("~"*45))

    # Here we create list_key() function for append the dictionary keys.    

    def list_key(self,item_list):
        for x in item_list:
            self.item_list_key.append(x)

    # Here we cart_calculation() function for calculating the total for each product.

    def cart_calculation(self,item_dict,item_list1):
        quand = 1
        while quand:
            try:
                user_quantity = input("\nEnter quantity:")
                my_validation.user_quant_validation(user_quantity)
                for x in range(1,len(item_list1)+1):
                    if x == int(self.user_cart):
                        total= int(user_quantity) * item_dict[item_list1[x-1]]
                        self.total_price += total
                        item_exists = False
                        for x in self.users_total_information:
                            for item in x:
                                if item[0] == item_list1[x - 1]:
                                    item[1] += total
                                    item_exists = True
                                    break
                        if not item_exists:
                            self.cart.append([item_list1[x - 1], total])
                        print("\n{} added to the cart.Total price Rs.{}".format(item_list1[x-1],self.total_price))
                        quand = 0
            except Exception as er:
                print(er)

    # Here we create sign_in() function for user sign in process.

    def sign_in(self):
        self.headers = ["Items","Price"]
        self.list_key(self.items_list)
        cus_id = 1
        while cus_id:
            try:
                self.user_cus_id = input("\nEnter customer's id:")
                if len(self.user_cus_id) == 0:
                    raise Exception ("\nCustomer id should not be empty.")
                elif self.user_cus_id in self.user_information:
                    cus_id = 0
                else:
                    raise Exception ("\nEntered customer's id is not registered.")
            except Exception as er:
                print(er)
        print("\nAdd Products to the cart!")
        cart = 1
        while cart:
            try:
                print("\nList of available items for shopping")
                print("\n"+tabulate.tabulate(([x,y] for x,y in self.items_list.items()),headers = self.headers,tablefmt = 'grid'))
                self.user_cart = input("\nEnter item number to add to cart(prss 'q' to quit):")
                if self.user_cart == "1":
                    self.add_cart = self.items_list["1.Milk"]
                    self.cart_calculation(self.items_list,self.item_list_key)
                elif self.user_cart == "2":
                    self.add_cart = self.items_list["2.Bread"]
                    self.cart_calculation(self.items_list,self.item_list_key)
                elif self.user_cart == "3":
                    self.add_cart = self.items_list["3.Eggs"]
                    self.cart_calculation(self.items_list,self.item_list_key)
                elif self.user_cart == "q":
                    self.item_list_key = []
                    cart = 0
                else:
                    raise Exception ("\nEnter the correct given items in the cart.")
            except Exception as er:
                print(er)

    # Here we generate_receipt() function for generate the bill for the user.
    
    def generate_receipt(self):
        delivery_charges = 40
        print("\nAvailable delivery location")
        print("\nAdayar")
        print("\nBesant nagar")
        print("\nIndira nagar")
        print("\nT-nagar")
        places = input("\nEnter delivery location:")
        print("\nSorry,online delivery is not available.")
        pick = 1
        while pick:
            try:
                user_pick = input("\nwould you like to pick it up from our nearest store(y/n)").lower()
                if user_pick == "n":
                    self.cart.append(["Delivery charges",delivery_charges])
                    self.total_price += delivery_charges
                    self.cart.append(["Total amount",self.total_price])
                    pick = 0
                elif user_pick == "y":
                    self.cart.append(["Total amount",self.total_price])
                    pick = 0
                else:
                    raise Exception ("\nPlease enter yes or no!!!")
            except Exception as er:
                print(er)
        self.users_total_information[self.user_cus_id] = self.cart
        print(self.users_total_information)
                
        print("\nDelivery charges will be applied.")
        for x,my_dict in self.user_information.items():
            if self.user_cus_id == x:
                print("\nCustomer Name:",my_dict["Name"])
                print("\nCustomer Id:",my_dict["customer_id"])
                print("\nCustomer Phone no:",my_dict["Phone Number"])
                print("\nCustomer Location:",my_dict["Location"])
        print(tabulate.tabulate(self.cart,headers = self.headers,tablefmt = 'grid'))

#Here we create Discount class as the child class for Shopping and parent class for Luckycart.

class Discount(Shopping): # Here we inherit the shopping class.

    # Here we create constructor for Discount class.
    
    def __init__(self):
        super().__init__() # Here we call Shopping class constructor by using super() function.
        self.discount_dict = {"1.Sugar":40,"2.Rice":50,"3.Atta":60}
        self.discount_amount = 0

    # Here we create apply_discount_calculation() function based on the product discount.

    def apply_discount_calculation(self,quantity,cart):
        if int(cart) == 1:
            if int(quantity) >= 1 and int(quantity) <=4:
                self.discount_amount = 5
            elif int(quantity) >= 5:
                self.discount_amount = 10
        elif int(cart) == 2:
            if int(quantity) >= 10 and int(quantity) <=24:
                self.discount_amount = 4
            elif int(quantity) >= 25:
                self.discount_amount = 8
            else:
                 self.discount_amount = 0
        elif int(cart) == 3:
            if int(quantity) >= 5 and int(quantity) <=9:
                self.discount_amount = 6
            elif int(quantity) >= 10:
                self.discount_amount = 12
            else:
                 self.discount_amount = 0

    # Here we crete cart_calculation1() function display the bill for discount products.
            
    def cart_calculation1(self,item_dict,item_list1):
        quand = 1
        while quand:
            try:
                self.user_quantity = input("\nEnter quantity:")
                my_validation.user_quant_validation(self.user_quantity)
                self.apply_discount_calculation(self.user_quantity,self.user_cart)
                for x in range(1,len(item_list1)+1):
                    if x == int(self.user_cart):
                        total= int(self.user_quantity) * (item_dict[item_list1[x-1]] - (item_dict[item_list1[x-1]]*(self.discount_amount/100)))
                        self.total_price += total
                        item_exists = False
                        for item in self.cart:
                            if item[0] == item_list1[x - 1]:
                                item[1] += total
                                item_exists = True
                                break
                        if not item_exists:
                            self.cart.append([item_list1[x - 1], total])
                        print("\n{} added to the cart.Total price Rs.{}".format(item_list1[x-1],self.total_price))
                        quand = 0
            except Exception as er:
                print(er)

    # Here we create discount() function to process the discount products. 

    def discount(self):
        self.list_key(self.discount_dict)
        self.discount_list = [["Item","Quantity","Discount"],
                              ["Sugar","1kg","5%"],
                              ["Sugar","5kg","10%"],
                              ["Rice","10kg","4%"],
                              ["Rice","25kg","8%"],
                              ["Atta","5kg","6%"],
                              ["Atta","10kg","12%"]]
        print("\nDiscount products available..")
        purc = 1
        while purc:
            try:
                user_purchase = input("\nDo you want to purchase(y/n):").lower()
                if user_purchase == "y":
                     print(tabulate.tabulate(self.discount_list,headers = 'firstrow',tablefmt = 'grid'))
                     cart1 = 1
                     while cart1:
                         try:
                             print("\nList of available items for shopping")
                             print("\n"+tabulate.tabulate(([x,y] for x,y in self.discount_dict.items()),headers = self.headers,tablefmt = 'grid'))
                             self.user_cart = input("\nEnter item number to add to cart(prss 'q' to quit):")
                             if self.user_cart == "1":
                                 self.add_cart = self.discount_dict["1.Sugar"]
                                 self.cart_calculation1(self.discount_dict,self.item_list_key)
                             elif self.user_cart == "2":
                                 self.add_cart = self.discount_dict["2.Rice"]
                                 self.cart_calculation1(self.discount_dict,self.item_list_key)
                             elif self.user_cart == "3":
                                 self.add_cart = self.discount_dict["3.Atta"]
                                 self.cart_calculation1(self.discount_dict,self.item_list_key)
                             elif self.user_cart == "q":
                                 self.item_list_key = []
                                 cart1 = 0
                                 purc = 0
                             else:
                                 raise Exception ("\nEnter the correct given items in the cart.")
                         except Exception as er:
                             print(er)
                elif user_purchase == "n":
                    self.item_list_key = []
                    purc = 0
                else:
                    raise Exception ("\nPlease enter yes or no!!!")
            except Exception as er:
                print(er)

#Here we create LuckyDraw class as the Grand child class for Shopping and child class for Discount.

class LuckyDraw(Discount):# Here we inherit the Discount class.

    # Here we create lucky_draw for process the lucky Draw.
    
    def lucky_draw(self):
        num = [5,4,3,2,1]
        luck_draw = ["New smartphone","New helmet","Cookware","Flat 200","Better Luck Next Time"]
        luck_draw1 = random.choice(luck_draw)
        print("\nWelcome to lucky draw.")
        for x,my_dict in self.user_information.items():
            if self.user_cus_id == x:
                print("\nCustomer Name:",my_dict["Name"])
        print("\nNow it's time to spin the board...")
        print("\nPlease wait:")
        num1 = [(time.sleep(1), print(n , end = "" )) for n in num]
        print("\n\nAnd the result is....")
        time.sleep(2)
        if luck_draw1 == "Better Luck Next Time":
            print("\nSorry, today's not your day. Better luck next time.")
        else:
            print("\nCongratulations! You have won a:",luck_draw1)
        print("\nThank you for shopping with us and participating in the Lucky Draw. Have a great day!")
        self.cart = []
        self.total_price = 0

    # Here we create the main_menu() function to call the all function by their choice.
        
    def main_menu(self):
        self.extract_word()
        print("\n"+("~"*45))
        print("\n{:<18}{}".format(" ",self.store_name))
        print("\n{:<21}".format(" "),("~"*45))
        choice = 1
        while choice:
            print("\n{:<15}1.Sign up(New user)".format(" "))
            print("\n{:<15}2.Sign in".format(" "))
            print("\n{:<15}3.Exit".format(" "))
            user_choice = input("\nEnter Your Choice:")
            if user_choice == "1":
                self.register()
            elif user_choice == "2":
                if self.user_information != {}: 
                    self.sign_in()
                    self.discount()
                    if self.cart != []:
                        self.generate_receipt()
                        self.lucky_draw()
                    else:
                        print(f"\nThanks for using {self.store_name1} Shopping Cart,we make sure next time we satisfied you to buy our products.")
                else:
                    print("\nThere is no users register in our data,please first register.")
            elif user_choice == "3":
                choice = 0
            else:
                print("\nPlease Enter correct choice(1-3)")

# Here we craete my_cart object for LuckyDraw class.

my_cart = LuckyDraw()

# Here we call the main_menu() by the object name.

my_cart.main_menu()
