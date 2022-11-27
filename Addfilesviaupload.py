class USER():
    def app_register(self):
        self.full_name=input("Enter your full name : ")
        self.phone_number=input("Enter your phone number : ")
        self.email = input("What is your email address? ")
        while "@" not in self.email:
            self.email= input("Your email address must have '@' in it\nPlease write your email address again: ")
        if len(self.email) <= 6 :
            self.email = input("Your email address is too short\nPlease write your email address again: ")
        if "." not in self.email:
            self.email = input("Your email address must have '.' in it\nPlease write your email address again: ")
        while "." not in self.email:
            self.email = input("Your email address must have '.' in it\nPlease write your email address again: ")
        if len(self.email) <= 6 :
            self.email = input("Your email address is too short\nPlease write your email address again: ")
        if "@" not in self.email:
            self.email = input("Your email address must have '@' in it\nPlease write your email address again: ")
        else:
            print("Emil verified successfully")

        self.address = input("Enter your adderess : ")
        self.user_name = input("enter user_name : ")
        self.password = input("enter your new password : ")

        self.user_information = {"Full name ":self.full_name,"Phone number": self.phone_number,"Email id":self.email,
                "Adderess":self.address,"User name":self.user_name,"Password":self.password}


        print(self.user_information)
        print("congratulation! your account is registered successfully ")


    def login(self):
        print("welcome to your login page ")
        while True:
            user_id = input("enter your user name : ")
            password = input("enter your password : ")
            if user_id == self.user_name:
                if password == self.password:
                    print("you are successfully logged in ")
                    break
                else:
                    print("incorrect information please try again ")
            else:
                print("incorrect information please try again ")


    def place_order(self):
        list_of_foods = [{"name":"Tandoori Chicken","quantity":"4 pieces","price":"INR 240"},
                        {"name":"Vegan Burger","quantity":"1 Piece" ,"price":"INR 320"},
                        {"name":"Truffle Cake","quantity":"500gm" ,"price":"INR 900"}]
        self.ordered_item = []
        print("here is the menu : ")
        for i in list_of_foods:
            print(f"{list_of_foods.index(i)+1}. {i['name']} [{i['quantity']}] (INR{i['price']})")
        user_order=int(input("select the items you want to order \n1. Tandoori Chicken\n2. Vegan Burger\n3. Truffle Cake\n "))
        if user_order ==1:
            self.ordered_item.append(list_of_foods[0])
            print(list_of_foods[0])
        elif user_order ==2:
            self.ordered_item.append(list_of_foods[1])
            print(list_of_foods[1])
        elif user_order ==3:
            self.ordered_item.append(list_of_foods[2])
            print(list_of_foods[2])
        else:
            print("choose the item from the menu")
        order = int(input("Do your order ?\n1. Yes\n2. No\n"))
        if order==1:
            print("order placed successfully")
        else:
            print("order cancelled")


    def order_history(self):
        for i in self.ordered_item:
            print("previous order\n ",i)
    def edit_personal_info(self):
        for i in self.user_information:
            self.user_information[i] = input(f"enter the {i} you want to update : ")
        print("personal details updated successfully \n ",self.user_information)

x=USER()
x.app_register()
x.login()
x.place_order()
x.order_history()
x.edit_personal_info()
