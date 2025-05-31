import flet as ft

def main (pedir: ft.Page):
    pedir.title="Orden de pedido"
    pedir.bgcolor = "#1a75d0"
    pedir.scroll = "auto"
    pedir.padding = 0

    contenedor = ft.Container(
        content=ft.Text(value="Orden pedido",color="#ffffff",font_family="Times New Roman",size=30),
        margin=0,
        padding=15,
        width=250,
        height=70,
        bgcolor="blue",
        border_radius=ft.BorderRadius(
            top_left=0,    # Solo esta esquina será redondeada
            top_right=0,
            bottom_left=0,
            bottom_right=60
        )
    )

    # texto1 = ft.Container(
        
    #     alignment=ft.alignment. center_left
    #     )
    texto2 = ft.Container(
        content=ft.Text(value="Cantidad de pedidos",color="#ffffff",size=19),
        margin=ft.margin.only(top=100),
        padding=ft.padding.only(left=14,top=10),
        width=200,
        height=50,
        bgcolor="blue",
        border_radius=ft.BorderRadius(
            top_left=30,    # Solo esta esquina será redondeada
            top_right=30,
            bottom_left=30,
            bottom_right=0
        ),
        )
    def solo_numeros(e):
        # Filtra los caracteres no numéricos
        e.control.value = ''.join(filter(str.isdigit, e.control.value))
        pedir.update()

    def solo_numeros_y_barra(e):
        # Permitir solo números y "/"
        campo = e.control
        texto = campo.value
        campo.value = "".join(c for c in texto if c.isdigit() or c == "/")
        pedir.update()

    dato = ft.TextField(bgcolor="#ffffff",on_change=solo_numeros,width=120)

    entry_fila = ft.Column(
        controls=[texto2,dato],
    )


    dato1 = ft.Container(
        content=ft.TextField(label="Cliente",bgcolor="#ffffff"),
        width=340,
        margin=ft.margin.only(left=30)
        )
    dato2 = ft.Container(
        content=ft.TextField(label="Publicidad",bgcolor="#ffffff"),
        width=340,
        margin=ft.margin.only(left=30)
        )
    dato3 = ft.Container(
        content=ft.TextField(label="Trabajo",bgcolor="#ffffff"),
        width=340,
        margin=ft.margin.only(left=30)
        )

    texto3 = ft.Container(
        content=ft.Text(value="Cantidad Unidad/es",color="#ffffff",size=19),
        padding=ft.padding.only(left=14,top=10),
        width=200,
        height=50,
        bgcolor="blue",
        border_radius=ft.BorderRadius(
            top_left=30,    # Solo esta esquina será redondeada
            top_right=30,
            bottom_left=30,
            bottom_right=0
        )
        )
    dato4 = ft.TextField(bgcolor="#ffffff",on_change=solo_numeros,width=120)

    Datos_columnas = ft.Column(
        controls=[contenedor,dato1,dato2,dato3],
        spacing=30,
        )

    entry_fila1 = ft.Column(
        controls=[texto3,dato4],
    )

    columna = ft.Column(
        controls=[entry_fila,entry_fila1],
        spacing=20
    )

    datos_fila = ft.Row(
        controls=[Datos_columnas,columna],
        spacing=100
    )

    texto5 = ft.Container(
        content=ft.Text("Cantidad de colores", size=18,color="#ffffff"),
        margin=ft.margin.only(left=20),
        padding=ft.padding.only(left=14,top=10),
        width=200,
        height=50,
        bgcolor="blue",
        border_radius=ft.BorderRadius(
            top_left=30,    # Solo esta esquina será redondeada
            top_right=30,
            bottom_left=30,
            bottom_right=0
        )
        )
    dato5 = ft.Container(ft.TextField(bgcolor="#ffffff",on_change=solo_numeros,width=120))

    entry_fila2 = ft.Row(
        controls=[texto5,dato5],
    )

    texto6 = ft.Container(
        ft.Text("Detalles:", size=18,color="#ffffff"),
        margin=ft.margin.only(left=20),
        padding=ft.padding.only(left=60,top=10),
        width=200,
        height=50,
        bgcolor="blue",
        border_radius=ft.BorderRadius(
            top_left=30,    # Solo esta esquina será redondeada
            top_right=0,
            bottom_left=30,
            bottom_right=30
        )
        )

    Dlista1 = ft.Container(
        content=ft.TextField(label="1-",bgcolor="#ffffff",width=450),
        margin=ft.margin.only(left=120)
        )
    Dlista2 = ft.Container(
        content=ft.TextField(label = "2-",bgcolor="#ffffff",width=450),
        margin=ft.margin.only(left=120)
        )
    Dlista3 = ft.Container(
        content=ft.TextField(label = "3-",bgcolor="#ffffff",width=450),
        margin=ft.margin.only(left=120)
        )
    Dlista4 = ft.Container(
        content=ft.TextField(label = "4-",bgcolor="#ffffff",width=450),
        margin=ft.margin.only(left=120)
        )
    Dlista5 = ft.Container(
        content=ft.TextField(label = "5-",bgcolor="#ffffff",width=450),
        margin=ft.margin.only(left=120)
        )
    Dlista6 = ft.Container(
        content=ft.TextField(label = "6-",bgcolor="#ffffff",width=450),
        margin=ft.margin.only(left=120)
        )

    lista2 = ft.Column(
        controls=[texto6,Dlista1,Dlista2,Dlista3,Dlista4,Dlista5,Dlista6],
        spacing=10,
    )

    dato6 = ft.Container(
        ft.TextField(bgcolor="#ffffff",width=320),
        )
    
    texto7 = ft.Container(
        ft.Text("Imprecion", size=18,color="#ffffff"),
        margin=ft.margin.only(left=20),
        padding=ft.padding.only(left=60,top=10),
        width=200,
        height=50,
        bgcolor="blue",
        border_radius=ft.BorderRadius(
            top_left=30,    # Solo esta esquina será redondeada
            top_right=0,
            bottom_left=30,
            bottom_right=0
        )
        )
    
    lista3 = ft.Row(
        controls=[texto7,dato6]
    )

    switch_opcion = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text("Termoformar/Doblar", size=18,color="#ffffff"),
                ft.Switch(value=False),
            ],
            alignment=ft.MainAxisAlignment.CENTER  # Centra el texto y el switch en la fila
        ),
        alignment=ft.alignment.center,  # Centra la fila en el contenedor
        padding=10
    )

    dropdown = ft.Dropdown(
        label="Selecciona una opción",
        width=200,
        options=[
            ft.dropdown.Option("Opción 1"),
            ft.dropdown.Option("Opción 2"),
            ft.dropdown.Option("Opción 3"),
        ]
    )

    texto8 = ft.Container(
        ft.Text("Material", size=18,color="#ffffff"),
        margin=ft.margin.only(left=20),
        padding=ft.padding.only(left=60,top=15),
        width=200,
        height=50,
        bgcolor="blue",
        border_radius=ft.BorderRadius(
            top_left=30,    # Solo esta esquina será redondeada
            top_right=0,
            bottom_left=30,
            bottom_right=0
        )
        )
    
    texto9 = ft.Container(
        ft.Text("Cant. Material", size=18,color="#ffffff"),
        margin=ft.margin.only(left=400),
        padding=ft.padding.only(left=40,top=15),
        width=200,
        height=50,
        bgcolor="blue",
        border_radius=ft.BorderRadius(
            top_left=30,    # Solo esta esquina será redondeada
            top_right=0,
            bottom_left=30,
            bottom_right=0
        )
        )

    dato7 = ft.Container(ft.TextField(bgcolor="#ffffff",on_change=solo_numeros,width=120))

    lista4 = ft.Row(
        controls=[texto8,dropdown,texto9,dato7]
    )

    texto10 = ft.Container(
        ft.Text("Med. pliego", size=18,color="#ffffff"),
        margin=ft.margin.only(left=20),
        padding=ft.padding.only(left=40,top=15),
        width=200,
        height=50,
        bgcolor="blue",
        border_radius=ft.BorderRadius(
            top_left=30,    # Solo esta esquina será redondeada
            top_right=0,
            bottom_left=30,
            bottom_right=0
        )
        )
    
    dato8 = ft.Container(ft.TextField(label="Ancho-cm",bgcolor="#ffffff",on_change=solo_numeros,width=120))

    dato9 = ft.Container(ft.TextField(label="Alto-cm",bgcolor="#ffffff",on_change=solo_numeros,width=120))

    texto11 = ft.Container(
        ft.Text("Espesor", size=18,color="#ffffff"),
        margin=ft.margin.only(left=350),
        padding=ft.padding.only(left=70,top=10),
        width=200,
        height=50,
        bgcolor="blue",
        border_radius=ft.BorderRadius(
            top_left=30,    # Solo esta esquina será redondeada
            top_right=0,
            bottom_left=30,
            bottom_right=0
        )
        )
    
    dato10 = ft.Container(ft.TextField(bgcolor="#ffffff",on_change=solo_numeros,width=120))

    lista5 = ft.Row(
        controls=[texto10,dato8,dato9,texto11,dato10]
    )

    switch_opcion1 = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text("Troquelado", size=18,color="#ffffff"),
                ft.Switch(value=False),
            ],
        ),
        margin=ft.margin.only(left=20),
        padding=10
    )

    texto12 = ft.Container(
        ft.Text("Cinta bifaz", size=18,color="#ffffff"),
        margin=ft.margin.only(left=20),
        padding=ft.padding.only(left=60,top=15),
        width=200,
        height=50,
        bgcolor="blue",
        border_radius=ft.BorderRadius(
            top_left=30,    # Solo esta esquina será redondeada
            top_right=0,
            bottom_left=30,
            bottom_right=0
        )
        )

    dropdown1 = ft.Dropdown(
        label="Selecciona una opción",
        width=200,
        options=[
            ft.dropdown.Option("Opción 1"),
            ft.dropdown.Option("Opción 2"),
            ft.dropdown.Option("Opción 3"),
        ]
    )


    switch_opcion2 = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text("Doblado", size=18,color="#ffffff"),
                ft.Switch(value=False),
            ],
        ),
        padding=10
    )

    switch_opcion3 = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text("Corte", size=18,color="#ffffff"),
                ft.Switch(value=False),
            ],
        ),
        padding=10
    )

    datos_fila1 = ft.Row(
        controls=[texto12,dropdown1]
    )

    lista6 = ft.Row(
        controls=[switch_opcion1,switch_opcion2,switch_opcion3,datos_fila1],
        spacing=80,
    )

    texto13 = ft.Container(
        ft.Text("Observaciones", size=18,color="#ffffff"),
        padding=ft.padding.only(left=40,top=12),
        width=200,
        height=50,
        bgcolor="blue",
        border_radius=ft.BorderRadius(
            top_left=30,    # Solo esta esquina será redondeada
            top_right=0,
            bottom_left=30,
            bottom_right=0
        )
        )

    texto_largo =ft.Container( ft.TextField(
        bgcolor="#ffffff",
        multiline=True,
        max_lines=4,
        hint_text="Escribe aquí todos los detalles...",
    ),width=600)

    datos_fila2 = ft.Row(
        controls=[texto13,texto_largo],
        alignment=ft.MainAxisAlignment.CENTER
    )


    texto14 = ft.Container(
        ft.Text("Fecha recepcion", size=18,color="#ffffff"),
        margin=ft.margin.only(left=20),
        padding=ft.padding.only(left=40,top=15),
        width=200,
        height=50,
        bgcolor="blue",
        border_radius=ft.BorderRadius(
            top_left=30,    # Solo esta esquina será redondeada
            top_right=0,
            bottom_left=30,
            bottom_right=0
        )
        )
    
    dato11 = ft.Container(ft.TextField(bgcolor="#ffffff",on_change=solo_numeros_y_barra,width=120))

    datos_fila3 = ft.Row(
        controls=[texto14,dato11]
    )

    texto15 = ft.Container(
        ft.Text("Fecha entrega", size=18,color="#ffffff"),
        margin=ft.margin.only(left=0),
        padding=ft.padding.only(left=50,top=15),
        width=200,
        height=50,
        bgcolor="blue",
        border_radius=ft.BorderRadius(
            top_left=30,    # Solo esta esquina será redondeada
            top_right=0,
            bottom_left=30,
            bottom_right=0
        )
        )
    
    dato12 = ft.Container(ft.TextField(bgcolor="#ffffff",on_change=solo_numeros_y_barra,width=120))

    datos_fila4 = ft.Row(
        controls=[texto15,dato12]
    )

    lista7 = ft.Row(
        controls=[datos_fila3,datos_fila4],
        spacing=500,
    )

    texto16 = ft.Container(
        ft.Text("Firma", size=18,color="#ffffff"),
        margin=ft.margin.only(left=20,bottom=40),
        padding=ft.padding.only(left=60,top=15),
        width=200,
        height=50,
        bgcolor="blue",
        border_radius=ft.BorderRadius(
            top_left=30,    # Solo esta esquina será redondeada
            top_right=0,
            bottom_left=30,
            bottom_right=0
        )
        )
    
    texto17 = ft.Container(
        ft.Text("Imprimio", size=18,color="#ffffff"),
        margin=ft.margin.only(left=140,bottom=40),
        padding=ft.padding.only(left=50,top=15),
        width=200,
        height=50,
        bgcolor="blue",
        border_radius=ft.BorderRadius(
            top_left=30,    # Solo esta esquina será redondeada
            top_right=0,
            bottom_left=30,
            bottom_right=0
        )
        )
    
    dato13 = ft.Container(
        ft.TextField(bgcolor="#ffffff",width=200),
        margin=ft.margin.only(bottom=40)
        )

    datos_fila5 = ft.Row(
        controls=[texto17,dato13]
    )

    texto18 = ft.Container(
        ft.Text("Cant. Impresa", size=18,color="#ffffff"),
        margin=ft.margin.only(left=60,bottom=40),
        padding=ft.padding.only(left=40,top=15),
        width=200,
        height=50,
        bgcolor="blue",
        border_radius=ft.BorderRadius(
            top_left=30,    # Solo esta esquina será redondeada
            top_right=0,
            bottom_left=30,
            bottom_right=0
        )
        )
    
    dato14 = ft.Container(
        ft.TextField(bgcolor="#ffffff",on_change=solo_numeros,width=120),
        margin=ft.margin.only(bottom=40)
        )

    datos_fila6 =ft.Row(
        controls=[texto18,dato14]
    )

    lista8 = ft.Row(
        controls=[texto16,datos_fila5,datos_fila6],
    )

    separador =ft.Divider(color=ft.Colors.BLUE_GREY_200)

    pedir.add(datos_fila,separador,entry_fila2,lista2,lista3,switch_opcion,separador,lista4,lista5,lista6,datos_fila2,separador,lista7,lista8)


ft.app(main)