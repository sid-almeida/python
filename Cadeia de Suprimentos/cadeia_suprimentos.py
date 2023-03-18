from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from ttkthemes import ThemedTk
from PIL import Image, ImageTk

# Inicialização da janela principal com tema escuro
root = ThemedTk(theme="equilux")
root.title("Gestão de Cadeia de Suprimentos")

# Definição de fontes personalizadas
header_font = Font(family="Helvetica", size=20, weight="bold")
title_font = Font(family="Helvetica", size=16, weight="bold")
regular_font = Font(family="Helvetica", size=12)

# Variáveis para armazenar os dados do produto
product_name = StringVar()
product_quantity = IntVar()

# Variáveis para armazenar os dados do fornecedor
supplier_name = StringVar()
supplier_phone = StringVar()

# Variáveis para armazenar os dados do cliente
customer_name = StringVar()
customer_address = StringVar()

# Funções para adicionar um novo produto, fornecedor ou cliente na lista correspondente
def add_product():
    name = product_name.get()
    quantity = product_quantity.get()
    product_list.insert(END, f"{name} | Quantidade: {quantity}")
    product_name.set("")
    product_quantity.set(0)

def add_supplier():
    name = supplier_name.get()
    phone = supplier_phone.get()
    supplier_list.insert(END, f"{name} | Telefone: {phone}")
    supplier_name.set("")
    supplier_phone.set("")

def add_customer():
    name = customer_name.get()
    address = customer_address.get()
    customer_list.insert(END, f"{name} | Endereço: {address}")
    customer_name.set("")
    customer_address.set("")

# Criação das abas
tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Produtos")

tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="Fornecedores")

tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text="Clientes")

# Definição de ícones para as abas
product_icon = ImageTk.PhotoImage(Image.open("product.png").resize((32, 32)))
supplier_icon = ImageTk.PhotoImage(Image.open("supplier.png").resize((32, 32)))
customer_icon = ImageTk.PhotoImage(Image.open("customer.png").resize((32, 32)))

tab_control.tab(0, image=product_icon, compound="left")
tab_control.tab(1, image=supplier_icon, compound="left")
tab_control.tab(2, image=customer_icon, compound="left")

# Criação da aba de produtos
product_label = Label(tab1, text="Nome do Produto", font=title_font)
product_label.grid(row=0, column=0, padx=20, pady=10)

product_entry = Entry(tab1, textvariable=product_name, font=regular_font)
product_entry.grid(row=0, column=1, padx=20, pady=10)

quantity_label = Label(tab1, text="Quantidade", font=title_font)
quantity_label.grid(row=1, column=0, padx=20, pady=10)

quantity_entry = Spinbox(tab1, from_=0, to=10000, increment=1, textvariable=product_quantity, font=regular_font)
quantity_entry.grid(row=1, column=1, padx=20, pady=10)

add_product_button = Button(tab1, text="Adicionar Produto", command=add_product, font=regular_font)
add_product_button.grid(row=2, column=1, padx=20, pady=10)

product_list = Listbox(tab1, font=regular_font)
product_list.grid(row=3, column=0, columnspan=2, padx=20, pady=10)

#Criação da aba de fornecedores
supplier_label = Label(tab2, text="Nome do Fornecedor", font=title_font)
supplier_label.grid(row=0, column=0, padx=20, pady=10)

supplier_entry = Entry(tab2, textvariable=supplier_name, font=regular_font)
supplier_entry.grid(row=0, column=1, padx=20, pady=10)

phone_label = Label(tab2, text="Telefone", font=title_font)
phone_label.grid(row=1, column=0, padx=20, pady=10)

phone_entry = Entry(tab2, textvariable=supplier_phone, font=regular_font)
phone_entry.grid(row=1, column=1, padx=20, pady=10)

add_supplier_button = Button(tab2, text="Adicionar Fornecedor", command=add_supplier, font=regular_font)
add_supplier_button.grid(row=2, column=1, padx=20, pady=10)

supplier_list = Listbox(tab2, font=regular_font)
supplier_list.grid(row=3, column=0, columnspan=2, padx=20, pady=10)

#Criação da aba de fornecedores
supplier_label = Label(tab2, text="Nome do Fornecedor", font=title_font)
supplier_label.grid(row=0, column=0, padx=20, pady=10)

supplier_entry = Entry(tab2, textvariable=supplier_name, font=regular_font)
supplier_entry.grid(row=0, column=1, padx=20, pady=10)

phone_label = Label(tab2, text="Telefone", font=title_font)
phone_label.grid(row=1, column=0, padx=20, pady=10)

phone_entry = Entry(tab2, textvariable=supplier_phone, font=regular_font)
phone_entry.grid(row=1, column=1, padx=20, pady=10)

add_supplier_button = Button(tab2, text="Adicionar Fornecedor", command=add_supplier, font=regular_font)
add_supplier_button.grid(row=2, column=1, padx=20, pady=10)

supplier_list = Listbox(tab2, font=regular_font)
supplier_list.grid(row=3, column=0, columnspan=2, padx=20, pady=10)

#Criação da aba de clientes
customer_label = Label(tab3, text="Nome do Cliente", font=title_font)
customer_label.grid(row=0, column=0, padx=20, pady=10)

customer_entry = Entry(tab3, textvariable=customer_name, font=regular_font)
customer_entry.grid(row=0, column=1, padx=20, pady=10)

address_label = Label(tab3, text="Endereço", font=title_font)
address_label.grid(row=1, column=0, padx=20, pady=10)

address_entry = Entry(tab3, textvariable=customer_address, font=regular_font)
address_entry.grid(row=1, column=1, padx=20, pady=10)

add_customer_button = Button(tab3, text="Adicionar Cliente", command=add_customer, font=regular_font)
add_customer_button.grid(row=2, column=1, padx=20, pady=10)

customer_list = Listbox(tab3, font=regular_font)
customer_list.grid(row=3, column=0, columnspan=2, padx=20, pady=10)

#Exibição das abas
tab_control.pack(expand=1, fill="both")

#Início da interface gráfica
root.mainloop()