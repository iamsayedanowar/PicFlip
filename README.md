![PicFlip](https://raw.githubusercontent.com/iamsayedanowar/PicFlip/refs/heads/main/GRP.png)

# PicFlip

A Django project for converting images. Users can upload an image, choose the desired output format and download the converted image instantly.

## Setup Instructions

1. Clone the repository:

   ```bash
   https://github.com/iamsayedanowar/PicFlip.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Create a superuser (admin):

   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

## Tech Stack

**Front-End :** HTML, CSS, JavaScript

**Back-End :** Django

## Deployment

- For deployment, ensure to set `DEBUG = False` in your `settings.py` and configure a production-ready database (e.g., PostgreSQL).
- Use a service like Heroku, AWS, DigitalOcean, or Vercel to deploy your Django application.
