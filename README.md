# Remarcable Product Browse

## Overview

This is a simple Django web application that allows users to browse, search, and filter products by description, category, and tags.

---

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/raastinn/remarcable.git
   cd remarcable
   ```

2. Install dependencies:

   ```bash
   pip install django
   ```

3. Apply migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. (Optional) Create a superuser for admin access:

   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Open the app:

   * Main app: http://127.0.0.1:8000/
   * Admin panel: http://127.0.0.1:8000/admin/

---

## Features

* Search products by description
* Filter products by category
* Filter products by tags
* Combine search and filters
* Admin interface for managing data

---

## Assumptions

* Python and Django are installed
* SQLite is used as the default database
