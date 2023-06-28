import tkinter.font

import requests
import json
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror



class CurrConverter:

    def __init__(self):
        # Api key from exchange rate API
        APIKEY = "5bf27c832d92ade5f974af21"
        APIURL = f'https://v6.exchangerate-api.com/v6/{APIKEY}/latest/USD'

        fresult = "000"
        # setting window using tkinter
        window = Tk()
        window.geometry('400x400')
        window.title('Example Converter using API and tkinter')
        window.resizable(height=FALSE, width=FALSE)

        # setting values from api into app (list of currencies)
        response = requests.get(f'{APIURL}').json()
        currencies = dict(response[
                              'conversion_rates'])  # dict is to create a dictionary (turn the data into keys), and "converseion_rates" is used because of the way the  API works

        # creation of header
        frame1 = Frame(window, width=400, height=100)
        frame1.grid(row=0, column=0)

        frameL1 = Label(frame1, text="Currency Converter", bg="#023020", pady=20, padx=80, fg='#FFFFFF',
                        justify="center", font=("Times", "25"))
        frameL1.grid(row=0, column=0)

        # creating half with buttons and labels needed for conversion

        frame2 = Frame(window, width=400, height=300)
        frame2.grid(row=1, column=0)

        fromLabel = Label(frame2, text='From: ', justify="left", font=("Times", "25"))
        fromLabel.grid(row=0, column=0, pady=5)
        fromCombo = ttk.Combobox(frame2, values=list(currencies.keys()), width=5, font=("Times", "25"))
        fromCombo.grid(row=0, column=1, pady=5)

        toLabel = Label(frame2, text='To: ', justify="left", font=("Times", "25"))
        toLabel.grid(row=1, column=0, pady=5)
        toCombo = ttk.Combobox(frame2, values=list(currencies.keys()), width=5, font=("Times", "25"))
        toCombo.grid(row=1, column=1, pady=5)

        totalLabel = Label(frame2, text="Amount: ", justify="left", font=("Times", "25"))
        totalLabel.grid(row=2, column=0, pady=5)
        totalEntry = Entry(frame2, width=10, font=("Times", "25"))
        totalEntry.grid(row=2, column=1, pady=5)

        self.resultLabel = Label(frame2, text="", justify="center", font=("Times", "15","bold"))
        self.resultLabel.grid(row=3, column=0, pady=5,columnspan=2)

        Button1 = Button(frame2, text="Convert", bg="#FFA500", fg="#FFFFFF", justify="center", font=("Times", "25"),
                         command=lambda : self.changeLabel(fromCombo.get(),toCombo.get(),totalEntry.get()))
        Button1.grid(row=4, column=0, columnspan=2)

        window.mainloop()  # to mantain window open until user closes it, must be at the end


    def convertCurrency(self,fromSource,toSource,totalSource):
        finalResult = requests.get( f'https://v6.exchangerate-api.com/v6/5bf27c832d92ade5f974af21/pair/{fromSource}/{toSource}/{totalSource}').json()
        convertedResult = finalResult['conversion_result']
        #formatResult = f'{totalSource} {fromSource} = {convertedResult} {toSource}'
        return (convertedResult)
        #self.totalLabel.config(text=formatResult)
    def changeLabel(self,fromSource,toSource,totalSource):
        try:
         num = self.convertCurrency(fromSource, toSource, totalSource)
         print(num);
         num = f'Conversion rate is {num}'
         self.resultLabel.config(text = num)
        except:
         showerror(title='Error', message='An error Ocurred! No letters or blank spaces')