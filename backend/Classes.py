from mailsetup import lowInvMail
#import datetime
import pickle
import os
import random
# conda install -c conda-forge webdrivermanager
# conda install -c conda-forge selenium
# http://chromedriver.chromium.org/
ROOT_DIR = os.path.abspath(os.getcwd()) + "\\backend\\data\\"
print(ROOT_DIR)

l = 0
brugerList = []

class bruger:
    def __init__(self, admin, brugernavn, bruger_ID, mail):
        self.admin = admin
        self.brugernavn = brugernavn
        self.bruger_ID = bruger_ID
        self.mail = mail

    def write2file(self):
        with open(ROOT_DIR + "BrugerList.pkl", "wb") as pklBruger:
            pickle.dump(brugerList, pklBruger)

#Unpickle Brugerlisten
with open(ROOT_DIR + "BrugerList.pkl", "rb") as unpklBruger:
    brugerList = pickle.load(unpklBruger)

def nyBruger():
    global brugerList
    navn = input("Navn:")
    admin = input("True eller False:")
    mail = input("Mail:")
    bruger_ID = random.randint(1000000000000,9999999999999)
    brugerList.append(bruger(admin,navn,bruger_ID,mail))

loginNavn = ""
loginID = 0
loginAdmin = False
loginEmail = ""

def login(bruger_ID):
    global loginAdmin, loginEmail, loginID, loginNavn
    for i in brugerList:
        if i.bruger_ID == bruger_ID:
            loginNavn = i.brugernavn
            loginID = i.bruger_ID
            loginEmail = i.mail
            loginAdmin = i.admin
            break
        else:
            print("Brugernavnet findes ikke")
    pass

class vare:
    def __init__(self, varenummer, varenavn, antal):
        self.varenummer = varenummer
        self.varenavn = varenavn
        self.antal = antal

        def formindskAntal(self,n):
            self.antal -= n

        def foroegAntal(self,n):
            self.antal += n

class lager:
    def __init__(self):
        self.vareliste = []
        self.ordrehistorik = []
#        self.dato_for_sidste_optaelling = dato_for_sidste_optaelling
#        self.dato_for_naeste_optaelling = dato_for_naeste_optaelling
#        self.dato = dato

    def tilfoejNyVare(self, varenummer):
        for i in self.vareliste:
            if i.varenummer == varenummer:
                print("Varen eksisterer allerede i systemet")
                return None
        try:
            varenavn = input("Varenavn: ")
            antal = int(input("Antal: "))
            self.vareliste.append(vare(varenummer, varenavn, antal))
        except:
            print("Fejl")

    def fjernEksVare(self, varenummer):
        for i in self.vareliste:
            if i.varenummer == varenummer:
                print("Fjernede " + i.varenavn + " " + str(i.varenummer))
                self.vareliste.remove(i)
                break

    def write2file(self):
        global l
        with open(ROOT_DIR + "Lager.pkl", "wb") as pklLager:
            pickle.dump(l, pklLager)

    def nyOrdre(self):
        o = ordre()
        run = True

        while run:
            input = input('Indtast varenummer eller indtast exit for at afslutte eller indtast fjern for ændre ordre: ')
            if input == 'exit':
                run = False
                self.ordrehistorik.append(o.vareliste)
            elif input == "fjern":
                index = int(input("Indtast index af varen i varelisten: "))
                o.fjernVare(index)
            elif input == "ændre":
                index = int(input("Indtast index af varen i varelisten: "))
                antal = int(input("Indtast det nye antal: "))
                o.aendreAntal(index,antal)
            else:
                antal = int(input('Antal af varen: '))
                o.tilfoejVare(int(input),antal)


# Unpickle Lager
with open(ROOT_DIR + "Lager.pkl", "rb") as unpklLager:
    l = pickle.load(unpklLager)

class ordre:
    global l

    def __init__(self):
        self.vareliste = []
        self.brugernavn = None
        self.bruger_ID = None
        self.tidspunkt = datetime.datetime.now

    def tilfoejVare(self, varenummer, antal):
        for i in l.vareliste:
            if varenummer == i.varenummer:
                i.formindskAntal(antal)
                self.vareliste.append([i.varenummer,i.varenavn,antal])
            else:
                print('Varen findes ikke')

    def fjernVare(index):
        for i in l.vareliste:
            if self.vareliste[index][0] == i.varenummer:
                i.foroegAntal(self.vareliste[index][2])
        self.vareliste.pop(index)

    def aendreAntal(index, antal):
        exAntal = self.vareliste[index][2]
        self.vareliste[index][2] = antal
        for i in l.vareliste:
            if self.vareliste[index][0] == i.varenummer:
                i.foroegAntal(exAntal-antal)


    lowInvMail("arkivHTX@gmail.com","Belgisk/Vaffel55","nichlasost@gmail.com","kage")
