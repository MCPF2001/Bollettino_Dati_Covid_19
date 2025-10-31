from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from configparser import ConfigParser

####Configuazione finestra e temi####
finestra = Tk()
finestra.title("Bollettino Covid-19 (AGGIORNATO IL 13-12-2021) ")
finestra.geometry("1280x720")
finestra.iconbitmap('/home/christian28/Scrivania/Appunti Materie Universitá/Appunti Triennale/I ANNO/Materiale Fondamenti I/Progetto Fondamenti 1/bacterium.ico')

stile = ttk.Style()
stile.theme_use("default")

stile.configure("Treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3")

stile.map('Treeview',
        background=[('selected',"#347083")])



######Configuazione Tabella e barra dello scorrimento dei dati#######

tabella_frame = Frame(finestra)
tabella_frame.pack(pady=10)


tabella_scroll = Scrollbar(tabella_frame)
tabella_scroll.pack(side=RIGHT, fill=Y)

tabella_dati = ttk.Treeview(tabella_frame, yscrollcommand=tabella_scroll.set, selectmode="extended")
tabella_dati.pack()

tabella_scroll.config(command=tabella_dati.yview)


tabella_dati['columns'] = ("Data","Stato","Regione","Ricoverati con Sintomi","Terapia Intensiva","Totale Ospedalizzati","Guariti","Deceduti")

###Configurazione colonne dati Covid 19#####
tabella_dati.column("#0",width=0,stretch=NO)
tabella_dati.column("Data",anchor=CENTER,width=140)
tabella_dati.column("Stato",anchor=CENTER,width=140)
tabella_dati.column("Regione",anchor=CENTER,width=140)
tabella_dati.column("Ricoverati con Sintomi",anchor=CENTER,width=140)
tabella_dati.column("Terapia Intensiva",anchor=CENTER,width=140)
tabella_dati.column("Totale Ospedalizzati",anchor=CENTER,width=140)
tabella_dati.column("Guariti",anchor=CENTER,width=140)
tabella_dati.column("Deceduti",anchor=CENTER,width=140)

#####Configurazione intestazione dati Covid 19####

tabella_dati.heading("#0",text="",anchor=CENTER)
tabella_dati.heading("Data",text="Data",anchor=CENTER)
tabella_dati.heading("Stato",text="Stato",anchor=CENTER)
tabella_dati.heading("Regione",text="Regione",anchor=CENTER)
tabella_dati.heading("Ricoverati con Sintomi",text="Ricoverati con Sintomi",anchor=CENTER)
tabella_dati.heading("Terapia Intensiva",text="Terapia Intensiva",anchor=CENTER)
tabella_dati.heading("Totale Ospedalizzati",text="Totale Ospedalizzati",anchor=CENTER)
tabella_dati.heading("Guariti",text="Guariti",anchor=CENTER)
tabella_dati.heading("Deceduti",text="Deceduti",anchor=CENTER)


#####Aggiunta Dati Covid 19#####
dati =[["2021-12-12","ITA","Abruzzo",123,12,135,82495,2609],
       ["2021-12-12","ITA","Basilicata",20,1,21,30283,627],
       ["2021-12-12","ITA","Calabria",163,20,183,88891,1527],
       ["2021-12-12","ITA","Campania",365,29,394,475432,8291],
       ["2021-12-12","ITA","Emilia-Romagna",946,85,1031,428413,13907],
       ["2021-12-12","ITA","Friuli-Venezia-Giulia",294,27,321,126664,4070],
       ["2021-12-12","ITA","Lazio",782,112,894,404311,9073],
       ["2021-12-12","ITA","Liguria",274,27,301,117537,4494],
       ["2021-12-12","ITA","Lombardia",1108,143,1251,881680,34576],
       ["2021-12-12","ITA","Marche",118,34,152,119675,3171],
       ["2021-12-12","ITA","Molise",9,2,11,14635,507],
       ["2021-12-12","ITA","Prov. Aut. Bolzano",92,19,111,85999,1269],
       ["2021-12-12","ITA","Prov. Aut. Trento",81,18,99,50563,1400],
       ["2021-12-12","ITA","Piemonte",548,48,596,383709,11916],
       ["2021-12-12","ITA","Puglia",129,17,146,271128,6914],
       ["2021-12-12","ITA","Sardegna",96,6,102,75681,1710],
       ["2021-12-12","ITA","Sicilia",387,48,435,310526,7282],
       ["2021-12-12","ITA","Toscana",295,47,342,289481,7454],
       ["2021-12-12","ITA","Umbria",45,7,52,65358,1496],
       ["2021-12-12","ITA","Valle d´Aosta",19,2,21,12623,483],
       ["2021-12-12","ITA","Veneto",803,125,928,490725,12055]



]


######Aggiunta Dati Covid 19 nello schermo#####
global addcovid
addcovid = 0

for covidsel in dati:
    if addcovid % 2 == 0:
        tabella_dati.insert(parent='', index='end', iid=addcovid, text='', values=(covidsel[0],covidsel[1],covidsel[2],covidsel[3],covidsel[4],covidsel[5],covidsel[6],covidsel[7]),tags=('evenrow'))
    else:
        tabella_dati.insert(parent='', index='end', iid=addcovid, text='', values=(covidsel[0],covidsel[1],covidsel[2],covidsel[3],covidsel[4],covidsel[5],covidsel[6],covidsel[7]),tags=('oddrow'))

    addcovid += 1
    
    


###Creazione Tag di riga a strisce####
tabella_dati.tag_configure('oddrow', background="CadetBlue1")
tabella_dati.tag_configure('evenrow', background="brown1")


###Aggiungi Dato selezionato#####
dati_frame = LabelFrame(finestra, text="Dato Selezionato")
dati_frame.pack(fill="x",expand="yes",padx=20)

Data_label = Label(dati_frame, text="Data")
Data_label.grid(row=0,column=0,padx=10,pady=10)
Data_entry = Entry(dati_frame)
Data_entry.grid(row=0,column=1,padx=10,pady=10)

Stato_label = Label(dati_frame, text="Stato")
Stato_label.grid(row=0,column=2,padx=10,pady=10)
Stato_entry = Entry(dati_frame)
Stato_entry.grid(row=0,column=3,padx=10,pady=10)

Regione_label = Label(dati_frame, text="Regione")
Regione_label.grid(row=0,column=4,padx=10,pady=10)
Regione_entry = Entry(dati_frame)
Regione_entry.grid(row=0,column=5,padx=10,pady=10)

Ricoverati_con_Sintomi_label = Label(dati_frame, text="Ricoverati con Sintomi")
Ricoverati_con_Sintomi_label.grid(row=0,column=6,padx=10,pady=10)
Ricoverati_con_Sintomi_entry = Entry(dati_frame)
Ricoverati_con_Sintomi_entry.grid(row=0,column=7,padx=10,pady=10)

Terapia_Intensiva_label = Label(dati_frame, text="Terapia Intensiva")
Terapia_Intensiva_label.grid(row=1,column=0,padx=10,pady=10)
Terapia_Intensiva_entry = Entry(dati_frame)
Terapia_Intensiva_entry.grid(row=1,column=1,padx=10,pady=10)

Totale_Ospedalizzati_label = Label(dati_frame, text="Totale Ospedalizzati")
Totale_Ospedalizzati_label.grid(row=1,column=2,padx=10,pady=10)
Totale_Ospedalizzati_entry = Entry(dati_frame)
Totale_Ospedalizzati_entry.grid(row=1,column=3,padx=10,pady=10)

Guariti_label = Label(dati_frame, text="Guariti")
Guariti_label.grid(row=1,column=4,padx=10,pady=10)
Guariti_entry = Entry(dati_frame)
Guariti_entry.grid(row=1,column=5,padx=10,pady=10)

Deceduti_label = Label(dati_frame, text="Deceduti")
Deceduti_label.grid(row=1,column=6,padx=10,pady=10)
Deceduti_entry = Entry(dati_frame)
Deceduti_entry.grid(row=1,column=7,padx=10,pady=10)



#####Creazione funzioni tasto "Seleziona Dato"#######


def seldat():
    Data_entry.delete(0,END)
    Stato_entry.delete(0,END)
    Regione_entry.delete(0,END)
    Ricoverati_con_Sintomi_entry.delete(0,END)
    Terapia_Intensiva_entry.delete(0,END)
    Totale_Ospedalizzati_entry.delete(0,END)
    Guariti_entry.delete(0,END)
    Deceduti_entry.delete(0,END)

    dato_selez =tabella_dati.focus()
    valoridatiinseriti = tabella_dati.item(dato_selez,'values')

    Data_entry.insert(0,valoridatiinseriti[0])
    Stato_entry.insert(0,valoridatiinseriti[1])
    Regione_entry.insert(0,valoridatiinseriti[2])
    Ricoverati_con_Sintomi_entry.insert(0,valoridatiinseriti[3])
    Terapia_Intensiva_entry.insert(0,valoridatiinseriti[4])
    Totale_Ospedalizzati_entry.insert(0,valoridatiinseriti[5])
    Guariti_entry.insert(0,valoridatiinseriti[6])
    Deceduti_entry.insert(0,valoridatiinseriti[7])


def seldat_mouse(Entry):
    Data_entry.delete(0,END)
    Stato_entry.delete(0,END)
    Regione_entry.delete(0,END)
    Ricoverati_con_Sintomi_entry.delete(0,END)
    Terapia_Intensiva_entry.delete(0,END)
    Totale_Ospedalizzati_entry.delete(0,END)
    Guariti_entry.delete(0,END)
    Deceduti_entry.delete(0,END)

    dato_selez =tabella_dati.focus()
    valoridatiinseriti = tabella_dati.item(dato_selez,'values')

    Data_entry.insert(0,valoridatiinseriti[0])
    Stato_entry.insert(0,valoridatiinseriti[1])
    Regione_entry.insert(0,valoridatiinseriti[2])
    Ricoverati_con_Sintomi_entry.insert(0,valoridatiinseriti[3])
    Terapia_Intensiva_entry.insert(0,valoridatiinseriti[4])
    Totale_Ospedalizzati_entry.insert(0,valoridatiinseriti[5])
    Guariti_entry.insert(0,valoridatiinseriti[6])
    Deceduti_entry.insert(0,valoridatiinseriti[7])
    
#####Creazione GUI Tasto "Seleziona Dato"######
tasto_frame = LabelFrame(finestra, text="Tasti")
tasto_frame.pack(fill="x", expand="yes", padx=20)

seldat_button = Button(tasto_frame, text="Seleziona Dato", command=seldat)
seldat_button.grid(row=0,column=0,padx=10,pady=10)

tabella_dati.bind("<ButtonRelease-1>",seldat_mouse)


finestra.mainloop()






