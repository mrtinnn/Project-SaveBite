import flet as ft
import requests

API_URL = "http://127.0.0.1:8000"

def main(page: ft.Page):
    page.title = "SaveBite"
    page.vertical_alignment = "center"

    donor_name = ft.TextField(label="Donor Name")
    food_type = ft.TextField(label="Food Type")
    quantity = ft.TextField(label="Quantity")
    pickup_time = ft.TextField(label="Pickup Time (e.g., 4:00 PM)")

    def submit_donation(e):
        data = {
            "donor_name": donor_name.value,
            "food_type": food_type.value,
            "quantity": quantity.value,
            "pickup_time": pickup_time.value,
        }
        requests.post(f"{API_URL}/donations", params=data)
        page.snack_bar = ft.SnackBar(ft.Text("Donation Added"))
        page.snack_bar.open = True
        page.update()

    page.add(
        ft.Text("SaveBite Donation Entry", size=25, weight="bold"),
        donor_name,
        food_type,
        quantity,
        pickup_time,
        ft.ElevatedButton("Submit Donation", on_click=submit_donation)
    )

ft.app(target=main)
