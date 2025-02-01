import flet as ft
from flet import Page

def main(page: Page):
    page.title = "Routes Example"
    page.add(ft.Text(f"Initial route: {page.route}"))


    def route_change(e: ft.RouteChangeEvent):
        page.add(ft.Text(f"New route: {e.route}"))

    
    def go_store(e):
        page.route = "/store"
        page.update()


    page.on_route_change = route_change
    page.update()
    page.add(ft.ElevatedButton("Go to Store", on_click=go_store))
