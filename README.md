![PicFlip](https://raw.githubusercontent.com/iamsayedanowar/PicFlip/refs/heads/main/GRP.png)

# PicFlip

This is a Django project for creating and managing resumes. Users can sign up, fill in their details, and generate a professional resume in PDF format.

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

## Project Structure

- The `app` directory contains the main Django application for managing resumes.
- Templates are stored in the `templates` directory for rendering HTML pages.
- Static files (CSS, JavaScript) are stored in the `static` directory.

## Tech Stack

**Front-End :** HTML, CSS, JavaScript

**Back-End :** Django

## Deployment

- For deployment, ensure to set `DEBUG = False` in your `settings.py` and configure a production-ready database (e.g., PostgreSQL).
- Use a service like Heroku, AWS, DigitalOcean, or Vercel to deploy your Django application.

## Contributing

Contributions are always welcome! Feel free to open an issue, fork the repository, and submit a pull request.