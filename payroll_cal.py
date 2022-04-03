
#Application which using the online payroll calculator, will print out the net amounts
#assigned to the given gross salary

from dataclasses import replace
from tkinter import *
import requests
from bs4 import BeautifulSoup
import matplotlib
import matplotlib.pyplot as plt


class Application(Frame): 
    """Application for pyroll"""

    def __init__(self, master, req, chart, data):
        """Frame initialization"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets(req, chart, data)


    def create_widgets(self, req, chart, data):
        """Widgets needed to retrieve infromation from the user"""

        Label(self,
                text= "Wybierz formę zatrudnienia: "
                ).grid(row= 1, column= 0, sticky= W)

        self.types= StringVar()
        self.types.set= None

        types= ["UMOWA_O_PRACE", "UMOWA_ZLECENIE", "UMOWA_O_DZIELO"]
        column= 1
        for type in types:
            Radiobutton(self,
                        text= type, 
                        variable= self.types,
                        value= type,
                        padx= 50, pady= 10
                        ).grid(row= 1, column= column, sticky= W)
            column+= 1

    
        gross= StringVar()

        Label(self,
                text= "Wprowadź kwotę brutto wynagrodzenia: "
                ).grid(row= 2, column= 0, sticky= W)

        self.gross_ent= Entry(self, textvariable= gross)
        self.gross_ent.grid(row= 2, column= 1, padx= 50, pady= 10, sticky= E)


        self.work_place = BooleanVar()
        Checkbutton(self,
                    text= "praca w miejscu zamieszkania",
                    padx= 50, pady= 10,
                    variable= self.work_place
                    ).grid(row= 3, column= 0, sticky= W)


        self.more26= BooleanVar()
        Checkbutton(self,
                    text= "ukończone 26 lat",
                    padx= 50, pady= 10,
                    variable= self.more26
                    ).grid(row= 4, column= 0, sticky= W)     


        self.fgsp= BooleanVar()
        Checkbutton(self,
                    text= "składka na FGŚP",
                    padx= 50, pady= 10,
                    variable= self.fgsp
                    ).grid(row= 5, column= 0, sticky= W) 


        self.ppk= BooleanVar()
        Checkbutton(self,
                    text= "uczestnictwo w PPK",
                    padx= 50, pady= 10,
                    variable= self.ppk
                    ).grid(row= 6, column= 0, sticky= W) 


        percent= IntVar()

        Label(self,
                text= "stopa procentowa składki na ubezpieczenie wypadkowe ** "
                ).grid(row= 7, column= 0, sticky= W)

        self.percent= Entry(self, textvariable= percent)
        self.percent.grid(row= 7, column= 1, sticky= E)


        Label(self, 
                text= "%",
                pady= 10
                ).grid(row= 7, column= 2, sticky= W)


        Button(self, 
                text= "OBLICZ", bd= 5, padx= 54, pady= 20,
                command = lambda: req.application_data(self, data)
                ).grid(row= 8, column= 1, sticky= W)

        self.text= Text(self, width= 75, height= 10, wrap= WORD)
        self.text.grid(row= 9, column= 0, columnspan= 4)


        Button(self,
                text= "RYSUJ WYKRES", bd= 5, padx= 30, pady=20,
                command= lambda:chart.chart(data)
                ).grid(row= 8, column= 2, sticky= W)


class Request(object):
    """Class for sending request"""
    # if app.type == 1: 

    def application_data(self, app, data):
      
        global user_data
                
        user_data= {
                    "types": app.types.get(),
                    "gross_ent" : str(app.gross_ent.get()),
                    "work_place" : str(int(app.work_place.get())),
                    "more26" : str(int(app.more26.get())), 
                    "fgsp" : str(int(app.fgsp.get())), 
                    "ppk" : str(int(app.ppk.get())),
                    "percent" : str(app.percent.get())
                    }

        self.request_send(app, data)


    def request_send(self, app, data):
        """Request sending to Webside"""
        
        url= "https://www.money.pl/podatki/kalkulatory/plac"

        params= {
                "rok_podatkowy":2022,
                "pensja":user_data["gross_ent"], 
                "typ_kalkulatora":0, 
                "typ_wynagrodzenia":0, 
                "poza_miejscem_zamieszkania":user_data["work_place"],
                "uwzglednij_kwote_wolna":1,      
                "ppk": user_data["ppk"],
                "ppk_pracownik":2,
                "ppk_pracodawca":1.5,
                "pit_26": user_data["more26"]
                }

        app.text.delete(0.0, END)

        #Api send request to url
        try:
            response = requests.post(url, params= params)
            response.raise_for_status()

             #take a html, use BS4 for take a net value
            try:
                soup= BeautifulSoup(response.content, 'html.parser')
                soup.prettify()
                lst= soup.find_all("span",{'class':"sc-1qjgijr-1 tvpvj"})
                net= lst[0].string

                #send net value to app window 
                app.text.insert(0.0, user_data["types"] +
                    "- zarobki miesięczne dla kwoty " + user_data["gross_ent"] + 
                    " zł brutto wynoszą netto: " + net)
                
                #raplace net to string types
                replace= str(net)
                net_for_chart= replace.replace("\xa0", "") #remove ascii (\xa0) character 

                data.set(int(user_data["gross_ent"]), int(net_for_chart)) #set gross, net value to class Data for preparing Chart
                    
            except:
                app.text.insert(0.0, "Wystąpił błąd podczas pobierania danych")
        except requests.exceptions.HTTPError as error:
            app.text.insert(0.0, "Wystąpił błąd: (" + str(error) + ")")
        except requests.exceptions.ConnectionError: 
            app.text.insert(0.0, "Błąd połączenia z serwerem")
        except requests.exceptions.RequestException:
            app.text.insert(0.0, "Wystąpił błąd, spróbuj ponownie")

        

class Data(object):
    """Class for storing data"""
    x= []
    y= []
   
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def set(self, x, y):
        self.x.append(x)
        self.y.append(y)


class Chart(object):
    """Class for preparing chart"""

    def chart(self, data):
        """Preparing data for chart"""
        axisx= data.get_x()
        axisy= data.get_y()

        plt.title("Zależność między kwotami brutto/netto")
        plt.xlabel("Wynagrodzenie brutto")
        plt.ylabel("Wynagrodzenie netto")
        plt.plot(axisx,axisy)
        plt.show()
        
       

# main
reque= Request()
dat= Data()
chart_drawing= Chart()
root= Tk()
root.title("KALKULATOR WYNAGRODZEŃ")
application= Application(root, reque, chart_drawing, dat)
root.mainloop()

