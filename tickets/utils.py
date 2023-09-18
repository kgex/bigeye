# Import necessary modules
import random
from django.db import transaction
from .models import Washroom  # Replace 'your_app' with the actual name of your Django app

# Define a function to create washrooms with the specified criteria
def create_washrooms():
    # Define the number of floors and conditions
    num_floors = 5
    conditions = ['Good', 'Bad']

    # Create a function to generate random 10-digit numbers
    def generate_random_number():
        return str(random.randint(10**9, 10**10 - 1))

    # Create washrooms
    washrooms = []
    with transaction.atomic():
        for floor in range(1, num_floors + 1):
            for condition in conditions:
                for gender in ['Male', 'Female']:
                    name = generate_random_number()
                    location = f'G{floor}_{gender[0]}'  # Generate meaningful location
                    washroom = Washroom(name=name, location=location, condition=condition)
                    washrooms.append(washroom)

        # Bulk insert the washrooms into the database for better performance
        Washroom.objects.bulk_create(washrooms)

    return len(washrooms)

# import qrcode
import qrcode

def generate_qrcodes():
    # Retrieve all washroom records from the database
    washrooms = Washroom.objects.all()

    for washroom in washrooms:
        # Define the data to encode in the QR code
        data = f"/{washroom.name}"

        # Create a filename based on location and condition
        filename = f"{washroom.location}_{washroom.condition}.png"  # You can choose the image format you prefer (e.g., 'png', 'jpg', 'jpeg', etc.)

        # Create a QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # Add data to the QR code
        qr.add_data(data)
        qr.make(fit=True)

        # Create a QR code image
        qr_img = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code image to the disk
        qr_img.save(filename)
