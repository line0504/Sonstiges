
#Fachklasse Hund
class Hund():
     #in der def _init_ Methode wird festgelegt welche Attribute ein Objekt dieser Klasse haben soll, in den Klammern werden parameter übergeben
    def __init__(self,name,farbe,rasse):
       self.name=name
       self.farbe=farbe
       self.rasse=rasse 
       
    def bellen(self, anzahl):
        beller=""
        for i in range(0,anzahl):
            beller=beller +"Wau "  
        ausgabe=self.name+" sagt "+beller
        return ausgabe
            
    def anzeigen(self):
        return self.name         
            

#Liste erstellen
bello=Hund("Bello","braun","Chihuahua")    
fritzi=Hund("Fritzi","weiß","Beagle")    
hunde=[bello,fritzi]
       
#GUI
import tkinter as tk
root=tk.Tk()

label1 = tk.Label(root, text="Hunde")
label1.pack()

lbox = tk.Listbox(root)
lbox["selectmode"] = "single"
lbox.pack()

eingabefeld=tk.Entry(root)
eingabefeld.pack()

schaltf1 = tk.Button(root, text="Anzahl")
schaltf1.bind("<Button-1>",on_select)
schaltf1.pack()


# Funktion zum Laden der Liste 
def reload_list():
    lbox.delete(0, "end")
    for h in hunde:
        lbox.insert("end", h.anzeigen())

# Hunde-Objekt auswählen und zurückgeben
def on_select(event):
    s = lbox.curselection()
    if len(s) == 0:
      return
    index = int(s[0])
    h = hunde[index]
    menge = int(eingabefeld.get())
    ausgabe=h.bellen(menge)
    label2 = tk.Label(root, text=ausgabe)
    label2.pack()
    
    
 
#Programmstart
reload_list()
root.mainloop()