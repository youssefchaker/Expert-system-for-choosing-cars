from experta import *
from tkinter import Label,Tk
from PIL import ImageTk, Image
details_of_cars=[]
details_map={}


def preprocess():
    global details_of_cars,details_map
    list_cars=open("Cars.txt")
    cars_all = list_cars.read()
    cars=cars_all.split("\n")
    list_cars.close()
    for car in cars :
        car_file = open("info/"+car+".txt")
        a = car_file.read()
        detail_list=a.split("\n")
        details_of_cars.append(detail_list)
        details_map[str(detail_list)]= car
        car_file.close()     

def if_not_matching(car):
    main = Tk()
    main.title("Not quite perfect")
    lbl1=Label(main,text="There is no perfect car according to your choices but",font=("Arial", 25)).pack()
    lbl2=Label(main,text="The most suitable for you is a \""+car+"\"\n",font=("Arial", 25)).pack()
    img = ImageTk.PhotoImage(Image.open("images/"+car+".jpg"))
    lbl3 = Label(main, image = img).pack()
    main.mainloop()

class Welcome(KnowledgeEngine):
    @DefFacts()
    def initial(self):
        print("Welcome! We are going to help you with your car purchase \n")
        print("Please answer the upcoming questions with either yes or no\n")
        
        yield Fact(action="find_car")
        
    @Rule(Fact(action='find_car'),NOT(Fact(AL=W())),salience=5)
    def symptom_0(self):
        self.declare(Fact(AL=input("Do you want a German car? > ")))  
    
    @Rule(Fact(action='find_car'),NOT(Fact(AL=W())),OR((Fact(US="yes")),(Fact(IT="yes")),(Fact(FR="yes")),(Fact(JP="yes"))),salience=5)
    def symptom_12(self):
        self.declare(Fact(AL="no"))  
    
    @Rule(Fact(action='find_car'),NOT(Fact(US=W())),salience=5)
    def symptom_1(self):
        self.declare(Fact(US=input("Do you want an US car? > "))) 

    @Rule(Fact(action='find_car'),NOT(Fact(US=W())),OR((Fact(JP="yes")),(Fact(IT="yes")),(Fact(FR="yes")),(Fact(AL="yes"))),salience=5)
    def symptom_13(self):
        self.declare(Fact(US="no"))  
   
    @Rule(Fact(action='find_car'),NOT(Fact(FR=W())),salience=5)
    def symptom_2(self):
        self.declare(Fact(FR=input("Do you want a French car? > ")))  

    @Rule(Fact(action='find_car'),NOT(Fact(FR=W())),OR((Fact(US="yes")),(Fact(IT="yes")),(Fact(AL="yes")),(Fact(JP="yes"))),salience=5)
    def symptom_14(self):
        self.declare(Fact(FR="no"))  
   
    @Rule(Fact(action='find_car'),NOT(Fact(IT=W())),salience=5)
    def symptom_3(self):
        self.declare(Fact(IT=input("Do you want an Italien car? > "))) 

    @Rule(Fact(action='find_car'),NOT(Fact(IT=W())),OR((Fact(JP="yes")),(Fact(AL="yes")),(Fact(FR="yes")),(Fact(US="yes"))),salience=5)
    def symptom_15(self):
        self.declare(Fact(IT="no"))   
   
    @Rule(Fact(action='find_car'),NOT(Fact(JP=W())),salience=5)
    def symptom_4(self):
        self.declare(Fact(JP=input("Do you want a Japanese car? > ")))  

    @Rule(Fact(action='find_car'),NOT(Fact(JP=W())),OR((Fact(US="yes")),(Fact(IT="yes")),(Fact(FR="yes")),(Fact(AL="yes"))),salience=5)
    def symptom_16(self):
        self.declare(Fact(JP="no"))  

    @Rule(Fact(action='find_car'),NOT(Fact(budgethigh=W())),salience=6)
    def symptom_5(self):
        self.declare(Fact(budgethigh=input("High budget? > ")))  

    @Rule(Fact(action='find_car'),NOT(Fact(budgethigh=W())),OR((Fact(budgetlow="yes")),(Fact(budgetmoy="yes"))),salience=6)
    def symptom_17(self):
        self.declare(Fact(budgethigh="no"))  
   
    @Rule(Fact(action='find_car'),NOT(Fact(budgetmoy=W())),salience=6)
    def symptom_6(self):
        self.declare(Fact(budgetmoy=input("Medium budget? > ")))  

    @Rule(Fact(action='find_car'),NOT(Fact(budgetmoy=W())),OR((Fact(budgethigh="yes")),(Fact(budgetlow="yes"))),salience=6)
    def symptom_18(self):
        self.declare(Fact(budgetmoy="no")) 
   
    @Rule(Fact(action='find_car'),NOT(Fact(budgetlow=W())),salience=6)
    def symptom_7(self):
        self.declare(Fact(budgetlow=input("Low Budget? > ")))  

    @Rule(Fact(action='find_car'),NOT(Fact(budgetlow=W())),OR((Fact(budgetmoy="yes")),(Fact(budgethigh="yes"))),salience=6)
    def symptom_19(self):
        self.declare(Fact(budgetlow="no")) 
   
    @Rule(Fact(action='find_car'),NOT(Fact(speedhigh=W())),salience=4)
    def symptom_8(self):
        self.declare(Fact(speedhigh=input("Do you want a high speed car? > ")))  

    @Rule(Fact(action='find_car'),NOT(Fact(enginehigh=W())),salience=3)
    def symptom_9(self):
        self.declare(Fact(enginehigh=input("Do you want a high engine power car? > ")))  

    @Rule(Fact(action='find_car'),NOT(Fact(gasoline=W())),salience=2)
    def symptom_10(self):
        self.declare(Fact(gasoline=input("Do you want a gasoline powered car? > ")))   

    @Rule(Fact(action='find_car'),NOT(Fact(manual=W())),salience=1)
    def symptom_11(self):
        self.declare(Fact(manual=input("Do you want a manually controlled car? > ")))  

        

    @Rule(Fact(action='find_car'),Fact(AL='yes'),Fact(US='no'),
          Fact(FR='no'),Fact(IT='no'),Fact(JP='no'),
          Fact(budgetlow='no'),Fact(budgetmoy='no'),Fact(budgethigh='yes'),
          Fact(speedhigh='yes'),Fact(enginehigh='yes'),Fact(gasoline='yes'),
          Fact(manual='no'))
    def car_0(self):
          self.declare(Fact(car="BMWxm"))

    @Rule(Fact(action='find_car'),Fact(AL='no'),Fact(US='yes'),
          Fact(FR='no'),Fact(IT='no'),Fact(JP='no'),
          Fact(budgethigh='no'),Fact(budgetmoy='yes'),Fact(budgetlow='no'),
          Fact(speedhigh='no'),Fact(enginehigh='no'),Fact(gasoline='yes'),
          Fact(manual='no'))
    def car_1(self):
          self.declare(Fact(car="ChevroletSonic"))

    @Rule(Fact(action='find_car'),Fact(AL='no'),Fact(US='no'),
          Fact(FR='yes'),Fact(IT='no'),Fact(JP='no'),
          Fact(budgethigh='no'),Fact(budgetmoy='no'),Fact(budgetlow='yes'),
          Fact(speedhigh='no'),Fact(enginehigh='no'),Fact(gasoline='yes'),
          Fact(manual='yes'))
    def car_2(self):
          self.declare(Fact(car="CitroenC3"))

    @Rule(Fact(action='find_car'),Fact(AL='no'),Fact(US='no'),
          Fact(FR='no'),Fact(IT='yes'),Fact(JP='no'),
          Fact(budgethigh='yes'),Fact(budgetmoy='no'),Fact(budgetlow='no'),
          Fact(speedhigh='yes'),Fact(enginehigh='yes'),Fact(gasoline='yes'),
          Fact(manual='no'))
    def car_3(self):
          self.declare(Fact(car="Ferrari488VISTA"))

    @Rule(Fact(action='find_car'),Fact(AL='no'),Fact(US='no'),
          Fact(FR='no'),Fact(IT='yes'),Fact(JP='no'),
          Fact(budgethigh='no'),Fact(budgetmoy='yes'),Fact(budgetlow='no'),
          Fact(speedhigh='no'),Fact(enginehigh='no'),Fact(gasoline='yes'),
          Fact(manual='yes'))
    def car_4(self):
          self.declare(Fact(car="Fiat500"))

    @Rule(Fact(action='find_car'),Fact(AL='no'),Fact(US='yes'),
          Fact(FR='no'),Fact(IT='no'),Fact(JP='no'),
          Fact(budgethigh='no'),Fact(budgetmoy='yes'),Fact(budgetlow='no'),
          Fact(speedhigh='no'),Fact(enginehigh='yes'),Fact(gasoline='yes'),
          Fact(manual='no'))
    def car_5(self):
          self.declare(Fact(car="FORDFocus"))

    @Rule(Fact(action='find_car'),Fact(AL='no'),Fact(US='no'),
          Fact(FR='yes'),Fact(IT='no'),Fact(JP='no'),
          Fact(budgethigh='no'),Fact(budgetmoy='yes'),Fact(budgetlow='no'),
          Fact(speedhigh='no'),Fact(enginehigh='no'),Fact(gasoline='no'),
          Fact(manual='yes'))
    def car_6(self):
          self.declare(Fact(car="Renaultexpressvan"))

    @Rule(Fact(action='find_car'),Fact(AL='no'),Fact(US='no'),
          Fact(FR='no'),Fact(IT='no'),Fact(JP='yes'),
          Fact(budgethigh='no'),Fact(budgetmoy='no'),Fact(budgetlow='yes'),
          Fact(speedhigh='no'),Fact(enginehigh='no'),Fact(gasoline='yes'),
          Fact(manual='yes'))
    def car_7(self):
          self.declare(Fact(car="SuzukiCeleriopopulaire"))

    @Rule(Fact(action='find_car'),Fact(AL='no'),Fact(US='no'),
          Fact(FR='no'),Fact(IT='no'),Fact(JP='yes'),
          Fact(budgethigh='yes'),Fact(budgetmoy='no'),Fact(budgetlow='no'),
          Fact(speedhigh='yes'),Fact(enginehigh='yes'),Fact(gasoline='no'),
          Fact(manual='yes'))
    def car_8(self):
          self.declare(Fact(car="Toyotalandcruiser"))

    @Rule(Fact(action='find_car'),Fact(AL='yes'),Fact(US='no'),
          Fact(FR='no'),Fact(IT='no'),Fact(JP='no'),
          Fact(budgethigh='no'),Fact(budgetmoy='yes'),Fact(budgetlow='no'),
          Fact(speedhigh='no'),Fact(enginehigh='no'),Fact(gasoline='yes'),
          Fact(manual='yes'))
    def car_9(self):
          self.declare(Fact(car="Volkswagenpolosedan"))

    @Rule(Fact(action='find_car'),Fact(car=MATCH.car),salience=998)
    def car(self,car):
        main = Tk()
        main.title("We have found you the perfect car!!!")
        Label(main,text="The perfect car for you is a \""+car+"\"\n",font=("Arial", 25)).pack()
        img = ImageTk.PhotoImage(Image.open("images/"+car+".jpg"))
        Label(main, image = img).pack()
        main.mainloop()
        
    @Rule(Fact(action='find_car'),
         Fact(AL=MATCH.AL),
         Fact(US=MATCH.US),
         Fact(FR=MATCH.FR),
         Fact(IT=MATCH.IT),
         Fact(JP=MATCH.JP),
         Fact(budgethigh=MATCH.budgethigh),
         Fact(budgetmoy=MATCH.budgetmoy),
         Fact(budgetlow=MATCH.budgetlow),
         Fact(speedhigh=MATCH.speedhigh),
         Fact(enginehigh=MATCH.enginehigh),
         Fact(gasoline=MATCH.gasoline),
         Fact(manual=MATCH.manual),
         NOT(Fact(car=MATCH.car)),salience=-999)

        
    def not_matched(self,AL,US,FR,IT,JP,budgethigh,budgetmoy,budgetlow,speedhigh,enginehigh,gasoline,manual):
        listofsymp=[AL,US,FR,IT,JP,budgethigh,budgetmoy,budgetlow,speedhigh,enginehigh,gasoline,manual]
        max_count = 0
        max_car = ""
        for key,val in details_map.items():
            count = 0
            temp = eval(key)
            for i in range(0,len(listofsymp)):
                if(temp[i] == listofsymp[i]):
                    count = count + 1
            if count > max_count:
                max_count = count
                max_car = val
        if_not_matching(max_car)

    
          
if __name__=="__main__":
        preprocess()
        engine=Welcome()
        while(1):
            engine.reset()   
            engine.run()
            print("Do you want to go for another round?")
            if input()=='no':
                print("Come back for more car predictions!")
                break
            
