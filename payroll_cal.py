
#aplication which using the online payroll calculator, will print out the net amounts
#assigned to the given gross salary

from tkinter import *
from urllib import request, response


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

        types= ["UMOWA_O_PRACE", "UMOWA_ZLECENIE", "UMOWA_O_DZIELO"]
        column= 1
        for type in types:
            Radiobutton(self,
                        text= type, 
                        variable= self.types,
                        value= type,
                        padx= 50, pady= 10
                        ).grid(row= 1, column = column, sticky= W)
            column+= 1

    
        gross = StringVar()

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


class Request(object):
    """Class for sending request"""
    
    def check(self):
       # if app.text == 1: 
        global expression
                
        expression = {
                    "types": app.types.get(),
                    "gross_ent" : str(app.gross_ent.get()),
                    "work_place" : str(int(app.work_place.get())),
                    "cons_salary" : str(int(app.cons_salary.get())),
                    "more26" : str(int(app.more26.get())), 
                    "fgsp" : str(int(app.fgsp.get())), 
                    "ppk" : str(int(app.ppk.get())),
                    "percent" : str(app.percent.get())
                    }


        import requests
        from bs4 import BeautifulSoup

        url= "https://www.money.pl/podatki/kalkulatory/plac"

        header= { "query": "query sg_money_gielda_kalulator_wynagrodzen($rok_podatkowy: Int!, $typ_kalkulatora: Podatki_CalculatorTypesEnum!, $typ_wynagrodzenia: Podatki_SalaryTypesEnum!, $pensja: Float!, $pensja_miesiace: [Float], $koszty_autorskie: Int, $koszty_autorskie_procent: Int, $ppk: Int, $ppk_pracownik: Float, $ppk_pracodawca: Float, $pit_26: Int, $zwiekszone_koszty_uzyskania: Int, $poza_miejscem_zamieszkania: Int, $uwzglednij_kwote_wolna: Int, $wspolne_rozliczanie: Int) { calculated: salary_calc(rok_podatkowy: $rok_podatkowy, typ_kalkulatora: $typ_kalkulatora, typ_wynagrodzenia: $typ_wynagrodzenia, pensja: $pensja, pensja_miesiace: $pensja_miesiace, koszty_autorskie: $koszty_autorskie, koszty_autorskie_procent: $koszty_autorskie_procent, ppk: $ppk, ppk_pracownik: $ppk_pracownik, ppk_pracodawca: $ppk_pracodawca, pit_26: $pit_26, zwiekszone_koszty_uzyskania: $zwiekszone_koszty_uzyskania, poza_miejscem_zamieszkania: $poza_miejscem_zamieszkania, uwzglednij_kwote_wolna: $uwzglednij_kwote_wolna, wspolne_rozliczanie: $wspolne_rozliczanie) { miesiace { miesiac koszt_uzyskania zaliczka zdrowotne chorobowe rentowe emerytalne rentowe_pracodawca emerytalne_pracodawca brutto netto stawka zaliczka koszt_pracodawcy wypadkowe_pracodawca fundusz_pracy_pracodawca fgsp_pracodawca __typename } koszt_uzyskania zaliczka zdrowotne chorobowe rentowe emerytalne rentowe_pracodawca emerytalne_pracodawca zaliczka netto brutto niedoplata koszt_pracodawcy fgsp_pracodawca wypadkowe_pracodawca fundusz_pracy_pracodawca zlecenie_netto_miesiac zlecenie_brutto_miesiac zlecenie_pracodawca_miesiac dzielo_netto_miesiac dzielo_brutto_miesiac dzielo_pracodawca_miesiac praca_netto_miesiac praca_brutto_miesiac praca_pracodawca_miesiac __typename } } ",
                "operationName": "sg_money_gielda_kalulator_wynagrodzen",
                "variables": '\'{"rok_podatkowy":2022,"pensja":"' + str(expression["gross_ent"]) + '","typ_kalkulatora":"' + str(expression["types"]) + '","typ_wynagrodzenia":"brutto","koszty_autorskie":0,"koszty_autorskie_procent":0,"poza_miejscem_zamieszkania":' + str(expression["work_place"]) + ',"wspolne_rozliczanie":0,"uwzglednij_kwote_wolna":1,"ppk":' + str(expression["ppk"]) + ',"ppk_pracownik":2,"ppk_pracodawca":1.5,"pit_26":' + str(expression["more26"])+ ',"zus":"STANDARD"}\'}' }
        
        params = {"rok_podatkowy":2022,
                "pensja":expression["gross_ent"], 
                "typ_kalkulatora":0, 
                "typ_wynagrodzenia":0, 
                "koszty_autorskie":0,
                "koszty_autorskie_procent":0,
                "poza_miejscem_zamieszkania":expression["work_place"],
                "wspolne_rozliczanie":0,
                "uwzglednij_bowe":0,
                "zwiekszone_koszty_uzyskania":0,
                "uwzglednij_kwote_wolna":1,      
                "ppk": expression["ppk"],
                "ppk_pracownik":2,
                "ppk_pracodawca":1.5,
                "pit_26": expression["more26"],
                "zus":0,
                "dobrowolne_chorobowe":0,
                "zwiekszone_koszty_uzyskania":0
                }

        app.text.delete(0.0, END)

        #Api send request to url
        try:
            response = requests.post(url, headers= header, params= params)
            response.raise_for_status()

             #take a html, use BS4 for take a net value
            try:
                soup= BeautifulSoup(response.content, 'html.parser')
                soup.prettify()
                lst= soup.find_all("span",{'class':"sc-1qjgijr-1 tvpvj"})
                netto= lst[0].text
                #send net value to app window 
                app.text.insert(0.0, expression["types"] + "- zarobki miesięczne dla kwoty " + expression["gross_ent"] +" zł brutto wynoszą netto: " + netto)
            except: 
                app.text.insert(0.0, "Wystąpił błąd podczas pobierania danych")
        except requests.exceptions.HTTPError as error:
            app.text.insert(0.0, "Wystąpił błąd: (" + str(error) + ")")
        except requests.exceptions.ConnectionError: 
            app.text.insert(0.0, "Błąd połączenia z serwerem")
        except requests.exceptions.RequestException:
            app.text.insert(0.0, "Wystąpił błąd, spróbuj ponownie")
      

       

# main
req= Request()
root= Tk()
root.title("KALKULATOR WYNAGRODZEŃ")
app= Aplication(root, req)
root.mainloop()

