from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as tex_and_scroll

############"interfaz grafica"################################################################################
root=Tk()
root.title("BBDD")
root.config(bg="black")
root.resizable(0,0)
root.config(cursor="pirate")
#####Barra Menu################################################################################################

menu_bar=Menu(root)
root.config(menu=menu_bar)


sub_BBDD=Menu(menu_bar, tearoff=0)
sub_BBDD.add_command(label="Conectar")
sub_BBDD.add_command(label="Insertar")
sub_BBDD.add_separator()
sub_BBDD.add_command(label="Salir")

sub_delete=Menu(menu_bar, tearoff=0)
sub_delete.add_command(label="Borrar Campos")


sub_CRUD=Menu(menu_bar, tearoff=0)
sub_CRUD.add_command(label="Crear")
sub_CRUD.add_command(label="Leer")
sub_CRUD.add_command(label="Actualizar")
sub_CRUD.add_command(label="Borrar")

sub_help=Menu(menu_bar, tearoff=0)
sub_help.add_command(label="Licencia")
sub_help.add_command(label="Información")


menu_bar.add_cascade(label="BBDD", menu=sub_BBDD)
menu_bar.add_cascade(label="Borrar", menu=sub_delete)
menu_bar.add_cascade(label="CRUD", menu=sub_CRUD)
menu_bar.add_cascade(label="Ayuda", menu=sub_help)



################################################################################################################
##frame y cuadros con sus textos##################################################################################

my_frame=Frame(root)
my_frame.pack()
my_frame.config(bg="orange")
my_frame.config(cursor="arrow")


label_ID=Label(my_frame, text="ID:",font=("Time New Roman",15))
label_ID.config(bg="orange")
label_ID.grid(row=0, column=0, sticky="e", padx=0, pady=10)

label_name=Label(my_frame, text="Nombre:",font=("Time New Roman",15))
label_name.config(bg="orange")
label_name.grid(row=1, column=0, sticky="e", padx=0, pady=10)

label_surname=Label(my_frame, text="Apellido:",font=("Time New Roman",15))
label_surname.config(bg="orange")
label_surname.grid(row=2, column=0, sticky="e", padx=0, pady=10)


label_address=Label(my_frame, text="Dirección:",font=("Time New Roman",15))
label_address.config(bg="orange")
label_address.grid(row=3, column=0, sticky="e", padx=0, pady=10)

etiqueta_password=Label(my_frame, text="Password:",font=("Time New Roman",15))
etiqueta_password.config(bg="orange")
etiqueta_password.grid(row=4, column=0, sticky="e", padx=0, pady=10)

label_comments=Label(my_frame, text="Comentarios:",font=("Time New Roman",15))
label_comments.config(bg="orange")
label_comments.grid(row=5, column=0, sticky="e", padx=0, pady=10)

ID_username=StringVar()
fields_ID=Entry(my_frame, width=25, textvariable=ID_username)
fields_ID.grid(row=0, column=1, padx=0, pady=10)
fields_ID.config(bd=5)

name_username=StringVar()
fields_name=Entry(my_frame, width=25, textvariable=name_username)
fields_name.grid(row=1, column=1, padx=0, pady=10)
fields_name.config(bd=5)

surname_username=StringVar()
fields_surname=Entry(my_frame, width=25, textvariable=surname_username)
fields_surname.grid(row=2, column=1, padx=0, pady=10)
fields_surname.config(bd=5)

username_address=StringVar()
fields_address=Entry(my_frame, width=25, textvariable=username_address)
fields_address.grid(row=3, column=1, padx=0, pady=10)
fields_address.config(bd=5)

password_username=StringVar()
field_password=Entry(my_frame, width=25, textvariable=password_username)
field_password.grid(row=4, column=1, padx=0, pady=10)
field_password.config(show= "*", bd=5)

field_comments=tex_and_scroll.ScrolledText(my_frame, width=20, height=5, padx=0, pady=10)
field_comments.grid(row=5, column=1)


########################################################################################################
#############botones@@@@@@@@@@@@@@@@@@@"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
my_frame2=Frame(root)
my_frame2.pack()
my_frame2.config(cursor="hand2")
my_frame2.config(bg="brown")

first_button=Button(my_frame2, text="Create")
first_button.config(bd=10,bg="green", fg="white")
first_button.config(relief="groove")
first_button.grid(row=0, column=0, padx=5, pady=10)

second_button=Button(my_frame2, text="Read")
second_button.config(bd=10,bg="green", fg="white")
second_button.config(relief="groove")
second_button.grid(row=0, column=1, padx=5, pady=10)

third_button=Button(my_frame2, text="Update")
third_button.config(bd=10,bg="green", fg="white")
third_button.config(relief="groove")
third_button.grid(row=0, column=2, padx=5, pady=10)

fourth_button=Button(my_frame2, text="Delete")
fourth_button.config(bd=10,bg="green", fg="white")
fourth_button.config(relief="groove")
fourth_button.grid(row=0, column=3, padx=5, pady=10)

fifth_button=Button(my_frame2, text="Insert")
fifth_button.config(bd=10,bg="green", fg="white")
fifth_button.config(relief="groove")
fifth_button.grid(row=0, column=4, padx=5, pady=10)









root.mainloop()
