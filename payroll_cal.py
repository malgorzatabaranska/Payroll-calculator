
#aplication which using the online payroll calculator, will print out the net amounts
#assigned to the given gross salary

import tkinter as tk
from tkinter import *


class Aplication(Frame): 
    """Aplication for pyroll"""

    def __init__(self, master):
        """Frame initialization"""
        super(Aplication, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
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
                        value= type
                        ).grid(row= 1, column = column, sticky= W)
            column+= 1
    
        Label(self,
                text= "Wprowadź kwotę brutto wynagrodzenia: "
                ).grid(row= 2, column= 0, sticky= W)

        self.gross_ent = Entry(self)
        self.gross_ent.grid(row= 2, column = 1, sticky= W)

        self.work_place = BooleanVar()
        Checkbutton(self,
                    text= "praca w miejscu zamieszkania",
                    variable= self.work_place
                    ).grid(row= 3, column= 0, sticky= W)

        self.cons_salary = BooleanVar()
        Checkbutton(self,
                    text= "stałe wynagrodzenie w każdym miesiącu",
                    variable= self.cons_salary
                    ).grid(row= 4, column= 0, sticky= W) 

        self.more26= BooleanVar()
        Checkbutton(self,
                    text= "ukończone 26 lat",
                    variable= self.more26
                    ).grid(row= 5, column= 0, sticky= W)     

        self.middle_class= BooleanVar()
        Checkbutton(self,
                    text= "miesięczna ulga dla klasy średniej",
                    variable= self.middle_class
                    ).grid(row= 6, column= 0, sticky= W)  

        self.fgsp= BooleanVar()
        Checkbutton(self,
                    text= "składka na FGŚP",
                    variable= self.fgsp
                    ).grid(row= 7, column= 0, sticky= W) 

        self.ppk= BooleanVar()
        Checkbutton(self,
                    text= "uczestnictwo w PPK",
                    variable= self.ppk
                    ).grid(row= 8, column= 0, sticky= W) 

        Label(self,
                text= "stopa procentowa składki na ubezpieczenie wypadkowe ** "
                ).grid(row= 9, column= 0, sticky= W)

        self.gross_ent = Entry(self)
        self.gross_ent.grid(row= 10, column = 1, sticky= W)
        
        Label(self,
                text= "%"
                ).grid(row= 11, column= 2, sticky= W)

        Button(self, 
                text= "OBLICZ",
                #command= self.check
                ).grid(row= 12, column= 2, sticky= W)

        self.text= Text(self, width= 75, height= 10, wrap= WORD)
        self.text.grid(row= 13, column= 0, columnspan=4)

        



    
root= Tk()
root.title("KALKULATOR WYNAGRODZEŃ")
app= Aplication(root)
root.mainloop()



