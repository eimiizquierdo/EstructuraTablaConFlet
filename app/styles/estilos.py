import flet as ft

class Colors:
    BG = "#A9CBE1"
    CARD = "#B3A3DA"
    BORDER = "#483C6A"
    TEXT = "#FFFFFF"
    PRIMARY = "#5A4386"
    SUCCESS = "#7C719C"
    INFO = "#7B5BB3"
    DANGER = "#932929"
    WHITE = "#FFFFFF"
    BLACK = "#000000"
    FONDOINPUT = "#FFFCF8"

class Textos:
    H1 = ft.TextStyle(
        size=30, 
        height=1.2, 
        weight=ft.FontWeight.W_600, 
        font_family="Comic Sans MS",
        color=Colors.TEXT
    )
    
    H2 = ft.TextStyle(
        size=26, 
        height=1.2, 
        weight=ft.FontWeight.W_500, 
        font_family="Comic Sans MS",
        color=Colors.TEXT
    )
    
    H3 = ft.TextStyle(
        size=22, 
        height=1.2, 
        weight=ft.FontWeight.W_400, 
        font_family="Comic Sans MS",
        color=Colors.TEXT
    )
    
    text = ft.TextStyle(
        size=18, 
        height=1.2, 
        weight=ft.FontWeight.W_400, 
        font_family="Comic Sans MS",
        color=Colors.BORDER
    )

class Inputs:
    INPUT_PRIMARY = {
        "border_color": Colors.BORDER,
        "focused_border_color": Colors.PRIMARY,
        "cursor_color": Colors.PRIMARY,
        "width": 500,
        "text_style": Textos.text,
        "label_style": Textos.text,
        "bgcolor": Colors.FONDOINPUT,
    }

class Buttons:
    BUTTON_PRIMARY = ft.ButtonStyle (
            bgcolor=Colors.PRIMARY,
            color=Colors.WHITE,
            padding=10,
            shape=ft.RoundedRectangleBorder(radius=8),
            text_style=ft.TextStyle(
            size=16,
            weight=ft.FontWeight.BOLD,
            font_family="Comic Sans MS",
        )
    )
    BUTTON_SUCCESS = ft.ButtonStyle(
            bgcolor=Colors.SUCCESS,
            color=Colors.WHITE,
            padding=ft.Padding.all(10),
            shape=ft.RoundedRectangleBorder(radius=8),
            text_style=ft.TextStyle(
            size=16,
            weight=ft.FontWeight.BOLD,
            font_family="Comic Sans MS",
        )
            
    )
    BUTTON_DANGER = ft.ButtonStyle(
            bgcolor=Colors.DANGER,
            color=Colors.WHITE,
            padding=ft.Padding.all(10),
            shape=ft.RoundedRectangleBorder(radius=8),
            text_style=ft.TextStyle(
            size=16,
            weight=ft.FontWeight.BOLD,
            font_family="Comic Sans MS",
        )
    )

class Card:
    TARJETA = {
        "width": 600,
        "padding": 16,
        "border_radius": 12,
        "bgcolor": Colors.CARD,
        "border": ft.Border.all(2, Colors.BORDER),
    }
