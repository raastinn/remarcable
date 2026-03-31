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

3. Migrate and load data

   ```bash
   python manage.py migrate
   python manage.py loaddata sample_data.json
   ```   

3. Run the development server:

   ```bash
   python manage.py runserver
   ```

4. Open the app:

   * http://127.0.0.1:8000/

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

## Uses of AI

* General Use: Mix of AI/YouTube to learn Django
* Specific Use: Improve functionality for retrieving products (using "select_related" and "prefetch_related" as opposed to "objects.all") in `views.py`
* Specific Use: Formatting the `README.md` file
