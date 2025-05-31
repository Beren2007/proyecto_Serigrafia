import flet as ft

def main (page: ft.Page):
    page.title = "login"
    page.bgcolor = "#1a75d0"#88b5e3
    page.horizontal_alignment =ft.CrossAxisAlignment.CENTER

    texto = ft.Text(value="¡Bienvenido a nuestro sistema!",color="#ffffff",size=30)

    #Contenido para la pestaña Iniciar secion
    contenido_Secion = ft.Stack(controls=[
        ft.Container(ft.Image(src="imagenes\Captura de pantalla 2025-05-28 211607.png",width=400,height=400,fit=ft.ImageFit.CONTAIN),
            # bgcolor = "#ffffff",
            left=40,
            top=30,
            ),
        ft.Container(
            content=ft.Text(value="Ingrese su cuenta",color="#ffffff",size=30),
            left=600,
            top=60,
            ),
        ft.Container(
            content=ft.TextField(label="Usuario"),
            bgcolor=ft.Colors.WHITE,
            width=600,
            left=500,
            top=120,
            ),
        ft.Container(
            content=ft.TextField(label="Contraseña", bgcolor=ft.Colors.WHITE),
            width=600,
            left=500,
            top=220,
            ),
        ft.Container(
            content=ft.ElevatedButton("Continuar"),
            left=500,
            top=320,
            )
    ])

    #Contenido para la pestaña Registro
    contenido_Registro = ft.Stack(controls=[
        ft.Container(ft.Image(src="imagenes\Captura de pantalla 2025-05-28 211607.png",width=400,height=400,fit=ft.ImageFit.CONTAIN),
            # bgcolor = "#ffffff",
            left=750,
            top=30,
            ),
        ft.Container(
            content=ft.Text(value="Ingrese los datos Requeridos",color="#ffffff",size=30),
            left=40,
            top=20,
            ),
        ft.Container(
            content=ft.TextField(label="Usuario"),
            bgcolor=ft.Colors.WHITE,
            width=600,
            left=40,
            top=80,
            ),
        ft.Container(
            content=ft.TextField(label="Confirmar Usuario"),
            bgcolor=ft.Colors.WHITE,
            width=600,
            left=40,
            top=160,
            ),
        ft.Container(
            content=ft.TextField(label="Confirmar Contraseña"),
            bgcolor=ft.Colors.WHITE,
            width=600,
            left=40,
            top=240,
            ),
        ft.Container(
            content=ft.TextField(label="Contraseña"),
            bgcolor=ft.Colors.WHITE,
            width=600,
            left=40,
            top=320,
            ),
        ft.Container(
            content=ft.ElevatedButton("Continuar"),
            left=40,
            top=400,
            )
    ])

    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=200,
        tabs=[
            ft.Tab(text="Iniciar secion",icon=ft.Icons.LOGIN, content=contenido_Secion),
            ft.Tab(text="Registro",icon=ft.Icons.PERSON_ADD, content=contenido_Registro),
        ],
        expand=0
    )

    page.add(texto,tabs)

ft.app(target=main)