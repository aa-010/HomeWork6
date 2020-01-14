
class Goods:
    name = ""
    count = 0
    status = False

    def __init__(self, name = "", count = 0, status = False):
        self.name = name
        self.count = count
        self.status = status

    def display(self):
        print("Название товара ", self.name)
        print("Количество товара ", self.count)
        if (self.status):
            print("Товар куплен")
        else:
            print("Товар не куплен")
class Buy:
    buy = []

   # def __init__(self, good = Goods()):
    #    self.buy.append(good) 

    def add_goods(self, good = Goods()):
        if (len(self.buy) !=0):
            for i in range(0, len(self.buy)):
                if self.buy[i].name == good.name:
                    self.buy[i].count += good.count
                    #print("Совпадение")
                    break
                else:
                    self.buy.append(good)
        else:
            self.buy.append(good)
   
    def show(self):

         for i in range(0, len(self.buy)-1):
             if(self.buy[i].status == True):
                 self.buy[i].display()
                 print("\n")

         for i in range(0, len(self.buy)-1):
             if(self.buy[i].status == False):
                 self.buy[i].display()
                 print("\n")
         
    
    def buy_product(self, name_product):
          for i in range(0, len(self.buy)):
              if (self.buy[i].name == name_product):
                  self.buy[i].status = True





g1 = Goods("Good1", 5, True)
g2 = Goods("Good2", 3, True)
g3 = Goods("Good1", 2, True)
g4 = Goods("Good1", 5, True)
g5 = Goods("Good3", 5, False)

#g1.display()
#g2.display()
#g3.display()

Buy1 = Buy()

Buy1.add_goods(g1)
Buy1.add_goods(g2)
Buy1.add_goods(g3)
Buy1.add_goods(g4)
Buy1.add_goods(g5)


Buy1.show()

Buy1.buy_product("Good3")

Buy1.show()





    