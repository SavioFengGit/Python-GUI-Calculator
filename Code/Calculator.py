# Python Calculator
from tkinter import *
# funzione: prende il parametro e lo aggiunge alla variabile globale, poi aggiorna quello che mostra nella GUI
def button_press(num):

    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text) #aggiornamento del label


# funzione per il caso con il ciclo for
def button_command(num):
    return lambda: button_press(num)

# funzione che valuta l'espressione contenuta nella variabile globale attraverso la funzione eval, che esegue il codice contenuto in una stringa. Se valida l'espressione
# lo inserisce sulla variabile globale, altrimenti cattura l'errore
def equals():

    global equation_text

    try:

        total = str(eval(equation_text)) #esegue l'operazione
        equation_label.set(total)
        equation_text = total

    except SyntaxError:

        equation_label.set("Syntax Error!")
        equation_text = ""

    except ZeroDivisionError:

        equation_label.set("Division Error!")
        equation_text = ""

    except ValueError:

        equation_label.set("Value Error!")
        equation_text = ""

    except NameError:

        equation_label.set("Name Error!")
        equation_text = ""

    except TypeError:

        equation_label.set("Type Error!")
        equation_text = ""

# La funzione clear() azzera sia equation_text che equation_label, cancellando l’espressione e il risultato dallo schermo.
def clear():

    global equation_text
    equation_label.set("Calculator") #setta il label sullo schermo a vuoto
    equation_text = "Calculator" #azzera la variabile globale

# La variabile window crea un oggetto di tipo Tk, che rappresenta la finestra principale del programma. Il metodo title imposta il titolo della finestra, 
# mentre il metodo geometry imposta le dimensioni della finestra.
window = Tk() #crea la finestra 
window.title("Calculator program") #titolo
window.geometry("430x550") #grandezza

# La variabile equation_text è una stringa vuota che verrà riempita con i numeri e gli operatori premuti dall’utente.
equation_text = ""
# La variabile equation_label è un oggetto di tipo StringVar, che è una classe speciale di tkinter che permette di creare variabili che si aggiornano automaticamente quando cambiano. Il metodo set imposta il valore della variabile, mentre il metodo get restituisce il valore della variabile.
equation_label = StringVar() #permette di utilizzato i metodi di StringVar
# Definizione di costanti utili
global BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_FONT
BUTTON_HEIGHT = 4 # altezza dei pulsanti in righe
BUTTON_WIDTH = 9 # larghezza dei pulsanti in caratteri
BUTTON_FONT = 35 # font dei pulsanti



# La variabile label crea un oggetto di tipo Label, che è una classe di tkinter che permette di creare etichette di testo. 
# Il parametro textvariable indica che il testo della label dipende dal valore di equation_label. 
# Il parametro font imposta il tipo e la dimensione del carattere. 
# Il parametro bg imposta il colore di sfondo. Il parametro width imposta la larghezza della label in caratteri. Il parametro height imposta l’altezza della label 
# in righe. Il metodo pack posiziona la label nella finestra.
label = Label(window, textvariable=equation_label, font=('Coldiac',20), bg="white", width=27, height=2)
label.pack()

# La variabile frame crea un oggetto di tipo Frame, che è una classe di tkinter che permette di creare contenitori per altri widget. 
# Il metodo pack posiziona il frame nella finestra.
frame = Frame(window)
frame.pack()



# # CREAZIONE DEI TASTI DA 0 A 9 SENZA CICLO FOR
# # Le variabili button1 fino a button9 e button0 creano degli oggetti di tipo Button, che sono classi di tkinter che permettono di creare pulsanti. 
# # Il parametro text imposta il testo del pulsante. 
# # Il parametro height imposta l’altezza del pulsante in righe. 
# # Il parametro width imposta la larghezza del pulsante in caratteri. 
# # Il parametro font imposta il tipo e la dimensione del carattere. 
# # Il parametro command imposta la funzione da eseguire quando il pulsante viene premuto. 
# # Il metodo grid posiziona il pulsante nel frame, usando il sistema a griglia. 
# # Il parametro row indica la riga della griglia, 
# # il parametro column indica la colonna della griglia.
# button1 = Button(frame, text=1, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT,
#                  command=lambda: button_press(1)) #passaggio di funzione come argomento
# button1.grid(row=0, column=0)

# button2 = Button(frame, text=2, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT,
#                  command=lambda: button_press(2))
# button2.grid(row=0, column=1)

# button3 = Button(frame, text=3, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT,
#                  command=lambda: button_press(3))
# button3.grid(row=0, column=2)

# button4 = Button(frame, text=4, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT,
#                  command=lambda: button_press(4))
# button4.grid(row=1, column=0)

# button5 = Button(frame, text=5, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT,
#                  command=lambda: button_press(5))
# button5.grid(row=1, column=1)

# button6 = Button(frame, text=6, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT,
#                  command=lambda: button_press(6))
# button6.grid(row=1, column=2)

# button7 = Button(frame, text=7, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT,
#                  command=lambda: button_press(7))
# button7.grid(row=2, column=0)

# button8 = Button(frame, text=8, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT,
#                  command=lambda: button_press(8))
# button8.grid(row=2, column=1)

# button9 = Button(frame, text=9, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT,
#                  command=lambda: button_press(9))
# button9.grid(row=2, column=2)

# button0 = Button(frame, text=0, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT,
#                  command=lambda: button_press(0))
# button0.grid(row=3, column=0)






# CREAZIONE DEI TASTI DA 0 A 9 CON CICLO FOR
# Creazione dei pulsanti dei numeri e degli operatori usando un ciclo for, useremo button_comman per passare il num, button press prende
# solamente l'ultimo valore in quanto c'è la lambda function, quindi non va bene
numeri = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # lista dei numeri
pulsanti = {} # creo il dizionario dei pulsanti
for num in numeri: # ciclo sui numeri
    pulsanti[num] = Button(frame, text=num, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT, command=button_command(num)) # creazione del pulsante
    pulsanti[num].grid(row=(num)//3, column=(num)%3) # posizionamento del pulsante nella griglia





# Le variabili plus, minus, multiply, divide, equal e decimal creano altri pulsanti per gli operatori aritmetici, il segno di uguale e il punto decimale. 
# Hanno gli stessi parametri e metodi dei pulsanti dei numeri, ma il parametro command passa una lambda funzione che chiama la funzione button_press con 
# l’operatore corrispondente come argomento.
plus = Button(frame, text='+', height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT,
                 command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT,
                 command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT,
                 command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT,
                 command=lambda: button_press('/'))
divide.grid(row=3, column=3)

equal = Button(frame, text='=', height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT,
                 command=equals)
equal.grid(row=3, column=2)

decimal = Button(frame, text='.', height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT,
                 command=lambda: button_press('.'))
decimal.grid(row=3, column=1)



# La variabile clear crea un pulsante per cancellare l’espressione e il risultato. Ha gli stessi parametri e metodi degli altri pulsanti, 
# ma il parametro command passa la funzione clear come argomento.
clear = Button(window, text='CLEAR ALL', height=BUTTON_HEIGHT, width=50, font=BUTTON_FONT,
                 command=clear)
clear.pack()

# Il metodo mainloop avvia il ciclo principale del programma, che gestisce gli eventi dell’interfaccia grafica.
window.mainloop()




# Author Xiao Li Savio Feng