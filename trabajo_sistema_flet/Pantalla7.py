import flet as ft

def main(page: ft.Page):
    page.title = "Costo Producción"
    page.scroll = "auto"
    page.window_width = 800
    page.window_height = 700
    page.window_resizable = False
    page.window_max_width = 800
    page.window_min_width = 800
    page.window_max_height = 700
    page.window_min_height = 700
    page.bgcolor = "blue600"

    # Secciones agrupadas
    contenido = ft.Column([
        ft.Text("Costo Material", size=30, weight="bold"),

        ft.Row([
            ft.Text("Tipo Cambio:"),
            ft.TextField(value="120,00", width=100, text_align="right")
        ], spacing=20),

        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Material")),
                ft.DataColumn(ft.Text("P.E")),
                ft.DataColumn(ft.Text("Kg ($)")),
                ft.DataColumn(ft.Text("Peso")),
                ft.DataColumn(ft.Text("Total Kg.")),
                ft.DataColumn(ft.Text("Costo final")),
            ],
            rows=[
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text("PVC")),
                    ft.DataCell(ft.Text("1,40")),
                    ft.DataCell(ft.Text("18,00")),
                    ft.DataCell(ft.Text("0,000")),
                    ft.DataCell(ft.Text("0,000")),
                    ft.DataCell(ft.Text("$0")),
                ]),
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text("PET")),
                    ft.DataCell(ft.Text("0,88")),
                    ft.DataCell(ft.Text("0,00")),
                    ft.DataCell(ft.Text("0,000")),
                    ft.DataCell(ft.Text("0,000")),
                    ft.DataCell(ft.Text("$0")),
                ]),
            ]
        ),

        ft.Divider(),

        ft.Text("Costo Película", size=24, weight="bold"),
        ft.Row([
            ft.Text("Superficie:"),
            ft.TextField(value="0", width=60),
            ft.Text("x $/m2:"),
            ft.TextField(value="7,00", width=60),
            ft.Text("= Costo x uni:"),
            ft.TextField(value="0,00", width=80),
        ], spacing=10),

        ft.Divider(),

        ft.Text("Costo Impresión", size=24, weight="bold"),
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Tipo Impresion")),
                ft.DataColumn(ft.Text("Cant. Color")),
                ft.DataColumn(ft.Text("Pliegos")),
                ft.DataColumn(ft.Text("$ x Pasada")),
                ft.DataColumn(ft.Text("Costo Min.")),
                ft.DataColumn(ft.Text("Costo final")),
            ],
            rows=[
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text("Convencional")),
                    ft.DataCell(ft.Text("0")),
                    ft.DataCell(ft.Text("0")),
                    ft.DataCell(ft.Text("15,00")),
                    ft.DataCell(ft.Text("40,00")),
                    ft.DataCell(ft.Text("$0")),
                ]),
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text("UV")),
                    ft.DataCell(ft.Text("0")),
                    ft.DataCell(ft.Text("0")),
                    ft.DataCell(ft.Text("20,00")),
                    ft.DataCell(ft.Text("60,00")),
                    ft.DataCell(ft.Text("$0")),
                ]),
            ]
        ),

        ft.Divider(),

        ft.Text("Costo Tinta", size=24, weight="bold"),
        ft.Row([
            ft.Text("Sup. Total:"),
            ft.TextField(value="70", width=60),
            ft.Text("Tinta Rinde:"),
            ft.TextField(value="60%", width=60),
            ft.Text("Caras:"),
            ft.TextField(value="2", width=40),
        ], spacing=10),

        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Impresión")),
                ft.DataColumn(ft.Text("$ x Lt.")),
                ft.DataColumn(ft.Text("Costo final")),
            ],
            rows=[
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text("Convencional")),
                    ft.DataCell(ft.Text("33000,00")),
                    ft.DataCell(ft.Text("$0")),
                ]),
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text("UV")),
                    ft.DataCell(ft.Text("60000,00")),
                    ft.DataCell(ft.Text("$0")),
                ]),
            ]
        ),

        ft.Divider(),

        ft.Text("Costo Barniz", size=24, weight="bold"),
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Impresión")),
                ft.DataColumn(ft.Text("u$S x Lt")),
                ft.DataColumn(ft.Text("$ x Lt")),
                ft.DataColumn(ft.Text("Costo final por cm")),
            ],
            rows=[
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text("Convencional")),
                    ft.DataCell(ft.Text("18")),
                    ft.DataCell(ft.Text("1800,00")),
                    ft.DataCell(ft.Text("$0")),
                ]),
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text("UV")),
                    ft.DataCell(ft.Text("45")),
                    ft.DataCell(ft.Text("4500,00")),
                    ft.DataCell(ft.Text("$0")),
                ]),
            ]
        ),

        ft.Row([
            ft.ElevatedButton("Atrás"),
            ft.ElevatedButton("Siguiente"),
        ], alignment=ft.MainAxisAlignment.END)
    ])

    page.add(contenido)

ft.app(target=main)
