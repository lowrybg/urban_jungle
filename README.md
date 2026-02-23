# Urban Jungle 🌿

Urban Jungle is a Django web app I built to help keep track of houseplants. You can organize your plants by the rooms they live in, keep an eye on their watering needs, and save specific care instructions so you don't accidentally kill them.

This is my project for the SoftUni Django Basics exam.

## What's Inside

* **Plant Catalog:** You can add, edit, and delete plants, plus upload photos of them.
* **Rooms:** Plants are linked to specific rooms (like Living Room or Kitchen). I set up full CRUD for this model too.
* **Filtered Views:** You can click on a room to see only the plants that live there.
* **Care Tips:** There's a Many-to-Many setup for care instructions, so one tip can apply to multiple plants.
* **Validations & Errors:** Added custom form validations (so you can't say a plant needs 10,000ml of water) and a custom 404 page if you get lost.

## Tech Stack

* Python 3 & Django 6.0.2
* PostgreSQL (psycopg2)
* Pillow (for handling the image uploads)
* HTML/CSS & Django Templates for the frontend

## How to Run It Locally

If you want to spin this up on your own machine:

1. Clone the repo and navigate into the folder.
2. Create and activate a virtual environment:
   `python -m venv venv`
   `venv\Scripts\activate` (or `source venv/bin/activate` on Mac/Linux)
3. Install the required packages:
   `pip install -r requirements.txt`
4. Set up your PostgreSQL database and update the `DATABASES` dictionary in `settings.py` with your local credentials.
5. Run the migrations:
   `python manage.py makemigrations`
   `python manage.py migrate`
6. Start the server:
   `python manage.py runserver`

Open `http://127.0.0.1:8000/` in your browser and you're good to go!

