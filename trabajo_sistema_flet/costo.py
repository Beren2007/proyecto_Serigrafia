import flet as ft

def main(page: ft.Page):
    page.title = "Demostración de imágenes en Flet"
    page.bgcolor = "#1a75d0"
    page.scroll = "auto"
    page.padding = 0  # Elimina márgenes exteriores

    imagen = ft.Container(
        ft.Image(src="imagenes\Captura de pantalla 2025-05-28 211607.png",width=150,height=100,fit=ft.ImageFit.CONTAIN),
        # alignment=ft.alignment.top_right,
        width=150,height=100,margin=ft.margin.only(left=1100)
        # padding=ft.Padding(1000, 0, 0, 0),
        )

    # Encabezado rojo que cubre todo el ancho
    encabezado = ft.Container(
        expand=True,  # Asegura que se expanda a todo el ancho
        height=100,
        bgcolor="#0292f6",
        alignment=ft.alignment.center_left,
        padding=ft.Padding(20, 0, 0, 0), 
        content=ft.Text("Costos", color=ft.Colors.WHITE,font_family="Times New Roman", size=30),
    )

    encabezado_con_imagen = ft.Stack(
    controls=[
        encabezado,
        imagen
    ]
)


    # Función para generar una fila con campos de texto
    def fila(*campos):
        return ft.Row(
            [ft.Container(
                ft.TextField(label=campo),
                bgcolor=ft.Colors.WHITE,
                width=330
            ) for campo in campos],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            spacing=20
        )

    # Contenido del formulario
    contenido = ft.Container(  
    padding=20,
    content=ft.Column(
        controls=[
            fila("Varios", "Material", "Valor"),
            fila("Valor Peliculas", "Valor Tinta", "Shablón"),
            fila("Barniz", "Valor Corte", "Valor Troquel"),
            fila("Valor Armado", "Valor Troquelado", "Valor Doblado"),
            fila("Aplicacion Cinta", "Cant. horas", "Cant. Empleados"),
            ft.Row([
                ft.Container(ft.TextField(label="Valor total de mano de obra"), bgcolor=ft.Colors.WHITE, width=600)
            ], alignment=ft.MainAxisAlignment.CENTER)
        ],
        spacing=20
    )
)
    dato_total_1 =ft.Container(
        content=ft.TextField(label="Sub Total",bgcolor="#ffffff",),
        width=200,
    )
    dato_total_2 =ft.Container(
        content=ft.TextField(label="Margen",bgcolor="#ffffff"),
        width=200,
    )
    dato_total_3 =ft.Container(
        content=ft.TextField(label="Total ventas",bgcolor="#ffffff"),
        width=200,
    )

    boton1 = ft.Container(
        content=ft.ElevatedButton("Atras"),
        width=120,
        margin=ft.margin.only(top=40,bottom=40)
        )
    
    boton2 =ft.Container(
        content=ft.ElevatedButton("Orden Pedido"),
        width=120,
        margin=ft.margin.only(top=40,bottom=40),
        )

    datos_filas = ft.Row(
        controls=[dato_total_1,dato_total_2,dato_total_3],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=100,
    )

    boton_filas = ft.Row(
        controls=[boton1,boton2],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=100,
    )



    # Agregar todo a la página
    page.add(
        ft.Column(
            controls=[
                encabezado_con_imagen,
                contenido,
                ft.Divider(color=ft.Colors.WHITE),
                datos_filas,
                boton_filas
            ],
            scroll=ft.ScrollMode.ALWAYS
        )
    )

ft.app(target=main)