# -*- codding:utf8 -*-

import Tkinter

def envoyer():
    pass

def actualiser():
    pass

if __name__=="__main__":
    mainFen = Tkinter.Tk()
    mainFen.title("Chat")
    
    buttonActualiser = Tkinter.Button(mainFen, text = "Actualiser", command = actualiser)
    buttonActualiser.pack(side = "top")
    
    labelTexte = Tkinter.Label(mainFen)
    labelTexte.pack(side = "top")

    entryMessage = Tkinter.Entry(mainFen)
    entryMessage.pack(side = "left")

    buttonSubmit = Tkinter.Button(mainFen, text = "envoyer", command = envoyer)
    buttonSubmit.pack(side = "right")
    
    mainFen.mainloop()
