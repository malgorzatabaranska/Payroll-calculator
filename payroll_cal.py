
#aplication which using the online payroll calculator, will print out the net amounts
#assigned to the given gross salary


from telnetlib import NOP
from tkinter import *
from click import command
import requests

url= "https://wynagrodzenia.pl/kalkulator-wynagrodzen"


class Aplication(Frame): 
    """Aplication for pyroll"""

    def __init__(self, master, req):
        """Frame initialization"""
        super(Aplication, self).__init__(master)
        self.grid()
        self.create_widgets(req)


    def create_widgets(self, req):
        """Widgets needed to retrieve infromation from the user"""

        Label(self,
                text= "Wybierz formę zatrudnienia: "
                ).grid(row= 1, column= 0, sticky= W)

        self.types= StringVar()
        self.types.set= None

        types= ["Umowa o pracę", "Umowa zlecenie", "Umowa o dzieło"]
        column= 1
        for type in types:
            Radiobutton(self,
                        text= type, 
                        variable= self.types,
                        value= type,
                        padx= 50, pady= 10
                        ).grid(row= 1, column = column, sticky= W)
            column+= 1

    
        gross = IntVar()

        Label(self,
                text= "Wprowadź kwotę brutto wynagrodzenia: "
                ).grid(row= 2, column= 0, sticky= W)

        self.gross_ent = Entry(self, textvariable= gross)
        self.gross_ent.grid(row= 2, column = 1, padx= 50, pady= 10, sticky= E)

        self.work_place = BooleanVar()
        Checkbutton(self,
                    text= "praca w miejscu zamieszkania",
                    padx= 50, pady= 10,
                    variable= self.work_place
                    ).grid(row= 3, column= 0, sticky= W)

        self.cons_salary = BooleanVar()
        Checkbutton(self,
                    text= "stałe wynagrodzenie w każdym miesiącu",
                    padx= 50, pady= 10,
                    variable= self.cons_salary
                    ).grid(row= 4, column= 0, sticky= W) 

        self.more26= BooleanVar()
        Checkbutton(self,
                    text= "ukończone 26 lat",
                    padx= 50, pady= 10,
                    variable= self.more26
                    ).grid(row= 5, column= 0, sticky= W)     

        self.middle_class= BooleanVar()
        Checkbutton(self,
                    text= "miesięczna ulga dla klasy średniej",
                    padx= 50, pady= 10,
                    variable= self.middle_class
                    ).grid(row= 6, column= 0, sticky= W)  

        self.fgsp= BooleanVar()
        Checkbutton(self,
                    text= "składka na FGŚP",
                    padx= 50, pady= 10,
                    variable= self.fgsp
                    ).grid(row= 7, column= 0, sticky= W) 

        self.ppk= BooleanVar()
        Checkbutton(self,
                    text= "uczestnictwo w PPK",
                    padx= 50, pady= 10,
                    variable= self.ppk
                    ).grid(row= 8, column= 0, sticky= W) 

        
        percent= IntVar()

        Label(self,
                text= "stopa procentowa składki na ubezpieczenie wypadkowe ** "
                ).grid(row= 9, column= 0, sticky= W)

        self.percent = Entry(self, textvariable= percent)
        self.percent.grid(row= 9, column = 1, sticky= E)

        Label(self, 
                text= "%",
                pady= 10
                ).grid(row= 9, column= 2, sticky= W)
        

        Button(self, 
                text= "OBLICZ", bd= 5, padx= 54, pady= 20,
                command = lambda: req.check()
                ).grid(row= 12, column= 1, sticky= W)

        self.text= Text(self, width= 75, height= 10, wrap= WORD)
        self.text.grid(row= 13, column= 0, columnspan= 4)

class Mockup(object):
    """Class for sending request"""
    
    def check(self):
       # if app.text == 1: 
        expression = {
                    "types": app.types.get(),
                    "gross_ent" : app.gross_ent.get(),
                    "work_place" : app.work_place.get(),
                    "cons_salary" : app.cons_salary.get(),
                    "more26" : app.more26.get(), 
                    "middle_class": app.middle_class.get(),
                    "fgsp" : app.fgsp.get(), 
                    "ppk" : app.ppk.get(),
                    "percent" : app.percent.get()
                    }

        
        


# main
req= Mockup()
root= Tk()
root.title("KALKULATOR WYNAGRODZEŃ")
app= Aplication(root, req)
root.mainloop()

