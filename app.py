# -*- coding: UTF-8 -*-
#  ______________________________________________________________
# |  __________________________________________________________  |
# | | Debut du système ;)                                      | |
# | |  → "Créé par YassiGame | Ici c'est le main de l'app"     | |
# | |__________________________________________________________| |
# |______________________________________________________________|

print(f'''
       ______                         ______                           __           
      / ____/___  _________ _____    / ____/___  ____ _   _____  _____/ /____  _____
     / /   / __ \/ ___/ __ `/ __ \  / /   / __ \/ __ \ | / / _ \/ ___/ __/ _ \/ ___/
    / /___/ /_/ / /  / /_/ / / / / / /___/ /_/ / / / / |/ /  __/ /  / /_/  __/ /    
    \____/\____/_/   \__,_/_/ /_/  \____/\____/_/ /_/|___/\___/_/   \__/\___/_/     
                                                          --- Created by YassiGame ---
''')

print("Checking for the modules...")


#  ___________________________________________________________________
# |  _______________________________________________________________  |
# | | Importations (Import des modules Python):                     | |
# | |  → "Pour evité des bugs en essaye de importé chaque module    | |
# | |        s'il n'est pas présent, on l'installe automatiquement" | |
# | |_______________________________________________________________| |
# |___________________________________________________________________|

### function created for install module if not exist:
def install(package):
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


### --- Import with no errors: --- (Pov: J'essaye un petit programme, je promet rien...)

## Import with try statement the module (tkinter):
try:
    from tkinter import *
    import tkinter
except ModuleNotFoundError:
    install('tkinter')
else:
    print(" ↪ Tkinter is installed")

## Import with try statement the module (pillow):
try:
    from PIL import ImageTk, Image
except ModuleNotFoundError:
    install('pillow')
else:
    print(" ↪ Pillow is installed")

## Import some other modules:
from scripts import configurer
import datetime

#  _________________________________________________
# |  _____________________________________________  |
# | | Variables (Des variables de tout le code):  | |
# | |  → "Une variable ('date' et 'time_format')" | |
# | |_____________________________________________| |
# |_________________________________________________|

date = datetime.datetime.now()
time_format = f"{date.hour}:{date.minute}"

#  ________________________________________________________________________________
# |  ____________________________________________________________________________  |
# | | Functions ans Class (Fonctions et class pour le code et actions de l'app): | |
# | |  → "Fonctions pour ('clear', 'Parse', 'calculate')"                        | |
# | |____________________________________________________________________________| |
# |________________________________________________________________________________|

### --- Function Clear (Clear le Text sous le nom de 'OutPut' dans l'app): ---

def clear():
    entre_output.delete('1.0', END)


### --- Function Parse (Print un text dans la section 'OutPut' dans l'app): ---

class Parse:
    def __init__(self):
        self.TextOutpout = entre_output

    def logo(self):
        self.TextOutpout.insert(tkinter.END, f'''
       ______                         ______                           __           
      / ____/___  _________ _____    / ____/___  ____ _   _____  _____/ /____  _____
     / /   / __ \/ ___/ __ `/ __ \  / /   / __ \/ __ \ | / / _ \/ ___/ __/ _ \/ ___/
    / /___/ /_/ / /  / /_/ / / / / / /___/ /_/ / / / / |/ /  __/ /  / /_/  __/ /    
    \____/\____/_/   \__,_/_/ /_/  \____/\____/_/ /_/|___/\___/_/   \__/\___/_/     
                                                          --- Created by YassiGame ---\n''')

    def info(self, str):
        self.TextOutpout.insert(tkinter.END, f" » [{time_format} | INFO] {str}\n")

    def succes(self, str):
        self.TextOutpout.insert(tkinter.END, f" » [{time_format} | SUCCES] {str}\n")

    def warn(self, str):
        self.TextOutpout.insert(tkinter.END, f" » [{time_format} | WARN] {str}\n")

    def error(self, str):
        self.TextOutpout.insert(tkinter.END, f" » [{time_format} | ERROR] {str}\n")


### --- Function calculate (calcul le Text dans la section 'input' pui le met dans la section 'OutPut' dans l'app): ---

def calculate():
    ## Principale Formatters:
    clear()  # clear cmd
    Parse().logo()  # print logo
    ## Variables:
    word = entre_input.get("1.0", END) # Take input
    word = word.replace(' ', '') # replace space with anything
    word = word.replace("'", '') # replace ' with anything
    word = word.replace("\n", '') # replace \n (Enter) with anything
    calcul = 0 # reset variable calcul
    word_len = len(word) # length of the variable word
    ## Code:
    for x in range(word_len):
        letter = word[int(x)]
        try:
            calcul = calcul + int(configurer.encoder[letter])
        except:
            Parse().error(f"The letter(s) '{letter}' in word '{word}'. Are not in the database.")
            break
        else:
            clear()  # clear cmd
            Parse().logo()  # print logo
    if calcul != 0:
        Parse().info(f'> The word or the sentence(s): {word}')
    if calcul == 0:
        Parse().warn(f'No calcul, the calcul is 0')
    else:
        Parse().succes(f'The calcul is: {str(calcul)}')




#  ______________________________________________________________
# |  __________________________________________________________  |
# | | Options for the App Tkinter (Nouvelle fenetre):          | |
# | |  → "Créé une fenêtre et la configure ('nom', 'taille')"  | |
# | |__________________________________________________________| |
# |______________________________________________________________|

## Créé une variable qui ouvre un nouveau projet Tkinter:
fenetre = Tk()

## Met un nom a l'application:
fenetre.title("Coran Converter | Created by YassiGame with ❤ !")

## Met une geometrie de base a la fenetre (a chaque ouverture):
fenetre.geometry("1405x495")

fenetre.iconbitmap('./data/img/logo.ico')

## Créé une limite de taille pour la fenettre:
fenetre.minsize(1405, 495)
fenetre.maxsize(1405, 495)

#  _______________________________________________________________
# |  ___________________________________________________________  |
# | | Cadres / Frames sans nom (Répartit l'app en 3):           | |
# | |  → "Un cadre A Droite, A Gauche et Au Coté Tout A Droite" | |
# | |___________________________________________________________| |
# |_______________________________________________________________|

### --- Section Fenetre: ---

## Cadre (Frame) pour 'A Gauche':
Cadre_LEFT = Frame(fenetre)
Cadre_LEFT.pack(side=LEFT)

## Cadre (Frame) pour 'A Droite':
Cadre_RIGHT = Frame(fenetre)
Cadre_RIGHT.pack(side=RIGHT)

## Cadre (Frame) pour 'Au Coté Tout A Droite':
Cadre_RIGHT_RIGHT = Frame(Cadre_RIGHT)
Cadre_RIGHT_RIGHT.pack(side=RIGHT)

#  _____________________________________________________________
# |  _________________________________________________________  |
# | | Labels Frame (Frame avec Nom):                          | |
# | |  → "Pour chaque section ('input', 'output', 'options')" | |
# | |_________________________________________________________| |
# |_____________________________________________________________|

### --- Section Cadre_RIGHT_RIGHT [Pour Cadre (Frame) pour 'Au Coté Tout A Droite']: ---

## LabelFrame pour la section 'Options':
label3 = LabelFrame(Cadre_RIGHT_RIGHT, text="Options", padx=25, pady=25)
label3.pack(fill="both", expand="yes", padx=5, pady=4)

### --- Section Cadre_RIGHT [Pour Cadre (Frame) pour 'A Droite']: ---

## LabelFrame pour la section 'Output':
label2 = LabelFrame(Cadre_RIGHT, text="Console Output", padx=20, pady=20)
label2.pack(fill="both", expand="yes", padx=5, pady=2)

### --- Section Cadre_LEFT [Pour Cadre (Frame) pour 'A Gauche']: ---

## LabelFrame pour la section 'Input':
label1 = LabelFrame(Cadre_LEFT, text="Text Input", padx=20, pady=20)
label1.pack(fill="both", expand="yes", padx=5, pady=2)

#  __________________________________________________________
# |  ______________________________________________________  |
# | | Texts / Big Input (Text with inputs):                | |
# | |  → "Inputs et aussi des Inputs qui sont des Outputs" | |
# | |______________________________________________________| |
# |__________________________________________________________|

### --- Section Label1 [LabelFrame pour la section 'Input']: ---

## Entrée (Text) pour le text 'Input':
entre_input = Text(label1, width=40)
entre_input.pack(side=TOP)

### --- Section Label2 [LabelFrame pour la section 'Output']: ---

## Entrée (Text) pour le text 'Output':
entre_output = Text(label2, width=90)
entre_output.pack(side=TOP)

# Evite une entré dans le text 'Output':
entre_output.bind("<Key>", lambda e: "break")

#  ______________________________________________________________________________
# |  __________________________________________________________________________  |
# | | Buttons (Boutons qui execute des taches):                                | |
# | |  → "Des butons avec nom ('Calculate', 'Reset Output', 'Config', etc...)" | |
# | |__________________________________________________________________________| |
# |______________________________________________________________________________|

### --- Section Cadre_LEFT [Pour Cadre (Frame) pour 'A Gauche']: ---

## Bouton pour action Calculate():
bouton1 = Button(Cadre_LEFT, text="Calculate", command=calculate, relief=RAISED, cursor="circle", width=25)
bouton1.pack()

### --- Section Cadre_RIGHT [Cadre (Frame) pour 'A Droite']: ---

## Bouton pour action clear() qui va clear le Output ('console'):
bouton2 = Button(Cadre_RIGHT, text="Reset Output", command=clear, relief=RAISED, cursor="circle", width=25)
bouton2.pack()

### --- Section label3 [LabelFrame pour la section 'Options']: ---

## Bouton pour lancé le menu config:
bouton_config = Button(label3, text="Config", command=calculate, relief=RAISED, cursor="plus", width=25).pack(pady=5)

## Bouton pour reset la config d'après la repo GitHub:
bouton_test = Button(label3, text="Reset Config", command=calculate, relief=RAISED, cursor="plus", width=25).pack(pady=35)

#  ____________________________________________________
# |  ________________________________________________  |
# | | Decorations (Section photo et label):          | |
# | |  → "Des photos pour decorer l'application"     | |
# | |________________________________________________| |
# |____________________________________________________|

## Create Variable 'logo' to the path of the file:
logo = Image.open("./data/img/logo.png")
logo = ImageTk.PhotoImage(logo)

### --- Section label3 [LabelFrame pour la section 'Options']: ---

## Create label 'label_logo' to put in the image:
label_logo = tkinter.Label(label3, image=logo)
label_logo.image = logo
label_logo.pack()

#  _________________________________________________
# |  _____________________________________________  |
# | | Function Launch():                          | |
# | |  → "Une des fonctions clé de l'application" | |
# | |_____________________________________________| |
# |_________________________________________________|

def launch():
    try:
        fenetre.mainloop()
    except Exception as e:
        print(f"ERROR: {e}")
    else:
        print("The application has been successfully exited.")

#  _________________________________________________
# |  _____________________________________________  |
# | | Main Launcher:                              | |
# | |  → "Une des fonctions clé de l'application" | |
# | |_____________________________________________| |
# |_________________________________________________|

if __name__ == '__main__':
    print('Launching The app...')
    launch()
