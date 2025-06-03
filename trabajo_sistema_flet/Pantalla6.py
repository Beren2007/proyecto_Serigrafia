import flet as ft

def main(page: ft.Page):
    page.title = "Printers Serigrafía"
    page.window_width = 600
    page.window_height = 700
    page.window_resizable = False
    page.window_max_width = 600
    page.window_min_width = 600
    page.window_max_height = 700
    page.window_min_height = 700
    page.bgcolor = "blue600"


    logo = ft.Image(
        src="IMG/logo.png",  # ruta relativa
        width=100,
        height=50,
        fit=ft.ImageFit.CONTAIN
    )

    btn_clientes = ft.ElevatedButton("Clientes", bgcolor="white")
    btn_crear = ft.ElevatedButton("Crear", bgcolor="white")
    avatar = ft.Icon(name="account_circle", size=40, color="black")


    header = ft.Row(
        controls=[
            logo,
            ft.Container(expand=True),
            btn_clientes,
            btn_crear,
            avatar
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    datos_pliego = ft.Column([
        ft.Text("Datos de pliego", weight="bold", italic=True, color="white"),
        ft.Row([
            ft.Text("Unidades:", color="white"),
            ft.TextField(width=100),
            ft.Text("Cinta CM:", color="white"),
            ft.TextField(width=100),
        ]),
        ft.Row([
            ft.Text("Ancho (cm):", color="white"),
            ft.TextField(width=100),
            ft.Text("Largo (cm):", color="white"),
            ft.TextField(width=100),
            ft.Text("Espesor:", color="white"),
            ft.TextField(width=100),
        ]),
        ft.Row([
            ft.Text("Posturas:", color="white"),
            ft.TextField(width=100),
            ft.Text("Superficie:", color="white"),
            ft.TextField(width=100, hint_text="(Automático)"),
            ft.Text("Volumen:", color="white"),
            ft.TextField(width=100, hint_text="Automático"),
        ])
    ])

    impresion = ft.Column([
        ft.Text("Impresión", weight="bold", italic=True, color="white"),
        ft.Row([
            ft.Text("Cant. Colores:", color="white"),
            ft.TextField(width=100),
            ft.Text("Colores:", color="white"),
            ft.TextField(width=200),
        ]),
        ft.Row([
            ft.Text("Pliegos:", color="white"),
            ft.Dropdown(width=100, options=[]),
            ft.Text("Pasadas:", color="white"),
            ft.TextField(width=100),
            ft.Text("Barniz:", color="white"),
            ft.Dropdown(width=100, options=[]),
        ])
    ])

    btn_siguiente = ft.ElevatedButton("Siguiente", bgcolor="white")

    page.add(
        header,
        ft.Divider(color="white"),
        datos_pliego,
        ft.Divider(color="white"),
        impresion,
        ft.Container(padding=10),
        btn_siguiente
    )

ft.app(target=main, assets_dir=".")


