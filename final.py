import tkinter, os

"""FUNCIONES"""

def guardar(palabra_español, palabra_ingles):
        palabras_español = []
        palabras_ingles = []

        palabras_español.append(palabra_español)
        palabras_ingles.append(palabra_ingles)

        palabras_esp_ing = {palabras_español:palabras_ingles for (palabras_español, palabras_ingles) in zip(palabras_español, palabras_ingles)}
        *keys, = palabras_esp_ing
        *values, = palabras_esp_ing.values()

        
        try:
            with open("palabras.txt", "a") as file:
                for i in keys:
                    file.write(i) 
                    file.write(" ")
                for j in values:
                    file.write(j)
                    file.write("\n")

        except BaseException:
            tkinter.messagebox.showerror("ERROR","Error a la hora de escribir los datos")


def leer():
        try:
            with open("palabras.txt", "r") as file:
                if os.stat("palabras.txt").st_size == 0:
                    tkinter.messagebox.showerror("ERROR", "El archivo esta vacio")
                else:
                    for lineas in file:
                        listbox.insert(tkinter.END, f"{lineas}")
        except BaseException:
            tkinter.messagebox.showerror("ERROR","Error a la hora de leer los datos")


def filtrar():
        x = filtro_entry.get().lower()

        comparar = x.replace(" ", "")
        if x != comparar:
            tkinter.messagebox.showerror("ERROR","NO PUEDES INGRESAR ESPACIOS VACIOS, Y SOLO PUEDES INGRESAR UNA PALABRA")
        elif x.isalpha() == False:
            tkinter.messagebox.showerror("ERROR","Solo ingresa letras")
        elif x == comparar and x.isalpha() == True:
            try:
                with open("palabras.txt", "r") as file:
                    if os.stat("palabras.txt").st_size == 0:
                        tkinter.messagebox.showerror("ERROR", "El archivo esta vacio")
                    else:
                        for lineas in file:
                            y = lineas.split(" ")
                            for i in y:
                                i = i.replace("\n", "")
                                
                                if x == i[0]:
                                    listbox2.insert(tkinter.END, f"{y[0]} - {y[1]}")
                                    break
                                                            
            except BaseException:
                tkinter.messagebox.showerror("ERROR","Error a la hora de leer los datos")
        

def traducir():
        if not traducir_entry.get():
            tkinter.messagebox.showerror("Error", "No dejes espacios en blanco")
            return
        frase = traducir_entry.get().lower()
        palabras = frase.split(" ")
        palabras_español = []
        palabras_ingles = []
        resultado = ""
        palabras_traducidas = []
        with open("palabras.txt", "r") as file:
            if os.stat("palabras.txt").st_size == 0:
                tkinter.messagebox.showerror("ERROR","El archivo esta vacio")
            else:
                for lineas in file:
                    y = lineas.split(" ")
                    palabras_español.append(y[0])
                    palabras_ingles.append(y[1].strip("\n"))
                        
                d = dict(zip(palabras_español, palabras_ingles))
                for palabra in palabras:
                    if palabra in d:
                        palabras_traducidas.append(d[palabra])
                    else:
                        palabras_traducidas.append(palabra)
                for i in palabras_traducidas:
                    resultado += i+ " "
                listbox3.insert(tkinter.END, f"{resultado}")
                


def borrar_filtro():
    listbox2.delete(0, tkinter.END)
    filtro_entry.delete(0, tkinter.END)
def borrar():
    listbox.delete(0, tkinter.END)

def borrar_traduc():
    listbox3.delete(0, tkinter.END)
    traducir_entry.delete(0, tkinter.END)

def agregar():
    esp = p_esp_entry.get().lower()
    ing = p_ing_entry.get().lower()
     

    x = esp.replace(" ", "")
    y = ing.replace(" ", "")

    if x != esp or y!=ing:
        tkinter.messagebox.showerror('Error', 'No dejes espacios en blanco.')
        return
    elif esp.isalpha() == False or ing.isalpha() == False:
        tkinter.messagebox.showerror("ERROR", "SOLO SE ACEPTAN LETRAS")
    elif x == esp and esp.isalpha() == True and y == ing and ing.isalpha() == True:
        p_esp_entry.delete(0, tkinter.END)
        p_ing_entry.delete(0, tkinter.END)
        guardar(esp, ing)


window = tkinter.Tk()
window.resizable(0,0)
window.title("DICCIONARIO")

frame = tkinter.Frame(window)
frame.pack()

# AGREGAR PALABRAS
funciones_label =tkinter.LabelFrame(frame, text="FUNCIONES")
funciones_label.grid(row= 0, column=0, padx=20, pady=10)

p_esp_label = tkinter.Label(funciones_label, text="Agrega una palabra en español: ")
p_esp_label.grid(row=0, column=0)
p_ing_label = tkinter.Label(funciones_label, text="Agrega la palabra en ingles: ")
p_ing_label.grid(row=0, column=1)

p_esp_entry = tkinter.Entry(funciones_label)
p_ing_entry = tkinter.Entry(funciones_label)
p_esp_entry.grid(row=1, column=0)
p_ing_entry.grid(row=1, column=1)

btn = tkinter.Button(funciones_label, text="Agregar palabra", command=agregar)
btn.grid(row= 1, column=2)

for widget in funciones_label.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#DESPLEGAR Y FILTRO
#DESPLEGADO
desplegar_label = tkinter.LabelFrame(frame, text="DESPLEGADO Y FILTRO")
desplegar_label.grid(row=1, column=0, sticky="news", padx=20, pady=10)

btn_desplegar = tkinter.Button(desplegar_label, text="Desplegar Diccionario",command= leer)
btn_desplegar.grid(row= 0, column=0, padx=10, pady=5)

borrarD = tkinter.Button(desplegar_label, text="Borrar Desplegado", command=borrar)
borrarD.grid(row= 2, column=0, padx=10, pady=5)

listbox = tkinter.Listbox(desplegar_label, width=25)
listbox.grid(row=1,column=0)

#FILTRO
filtro_label = tkinter.Label(desplegar_label, text=" Filtrar palabra: ")
filtro_label.grid(row= 0, column=1,padx=10, pady=5)

filtro_entry = tkinter.Entry(desplegar_label)
filtro_entry.grid(row=0, column=2)

filtrar_btn = tkinter.Button(desplegar_label, text="FILTRAR", command=filtrar)
filtrar_btn.grid(row=0, column=3)

borrar_filtros = tkinter.Button(desplegar_label, text="BORRAR", command=borrar_filtro)
borrar_filtros.grid(row=2, column=2)


listbox2 = tkinter.Listbox(desplegar_label, width=25, height=5)
listbox2.grid(row=1,column=2)

#TRADUCIR
traducir_frame = tkinter.LabelFrame(frame, text="TRADUCIR")
traducir_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

traducir_label = tkinter.Label(traducir_frame, text="Escribe el texto a traducir: ")
traducir_label.grid(row=0, column=0)

traducir_entry = tkinter.Entry(traducir_frame)
traducir_entry.grid(row= 0, column=1,)

traducir_btn = tkinter.Button(traducir_frame, text="TRADUCIR", command=traducir)
traducir_btn.grid(row=0, column=2)

listbox3 = tkinter.Listbox(traducir_frame, width=30)
listbox3.grid(row=1, column=1)

borrar_traduccion = tkinter.Button(traducir_frame, text="BORRAR", command=borrar_traduc)
borrar_traduccion.grid(row=0, column=3)

window.mainloop()