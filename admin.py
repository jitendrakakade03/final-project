import json
class Restaurant:
    def __init__(self):
        self.foods={}
        self.food_id=len(self.foods)+1
    
    def add_food_items(self):
        self.Name =input("enter the food name :")
        self.Quantity =int(input("enter quantity of food :"))
        self.Price = int(input("enter the price of food :"))
        self.Discount =int(input("enter the discount of food :"))
        self.Stock =int(input("enter the stock in the restuarant :"))
        self.Items ={"name":self.Name,"Quantity":self.Quantity,"Price":self.Price,"Discount":self.Discount,"Stock":self.Stock}
        self.food_id=len(self.foods)+1
        self.foods[self.food_id] = self.Items
        print(self.Items)
        print(self.foods)
        with open("food_data.json","w") as f:
            json.dump(self.foods,f)
        print("item added successfully")


    
    def remove_items(self):
        x = int(input("enter the food id which you want to delete : "))
        del self.foods[x] 
        print("remaining items available",self.foods)

    def edit_food_items(self):
        f_id=int(input("Enter the food id you wanat to update : "))
        for i in self.foods[f_id]:
            self.foods[f_id][i]=input(f"enter the {i} you want to update : ")
        print("Food details updated successfully \n ",self.foods)

    def all_food_items(self):
        print("list of all food items are")
        for i in self.foods:
            print("food id : ",i,"\n    ")
            for n in self.foods[i]:
                print(n,":",self.foods[i][n])


x=Restaurant()
x.add_food_items()
x.add_food_items()
x.remove_items()
x.edit_food_items()
x.all_food_items()
