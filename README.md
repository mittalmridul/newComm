# Project Setup Instructions

This document provides instructions on how to set up and run this project on a new machine.

## Initial Setup

Follow these steps to get the project running:

1.  **Clone the Repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-project-directory>
    ```

2.  **Create a Virtual Environment:**
    It's highly recommended to use a virtual environment to manage project dependencies.
    ```bash
    python -m venv venv
    ```
    *(You can replace `venv` with your preferred environment name)*

3.  **Activate the Virtual Environment:**
    *   **macOS/Linux (bash/zsh):**
        ```bash
        source venv/bin/activate
        ```
    *   **Windows (Command Prompt):**
        ```bash
        venv\Scripts\activate.bat
        ```
    *   **Windows (PowerShell):**
        ```powershell
        venv\Scripts\Activate.ps1
        ```
    Your terminal prompt should change to indicate the active environment.

4.  **Install Dependencies:**
    Install all the required packages listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

5.  **Database Migrations (if applicable for Django):**
    Apply any pending database migrations.
    ```bash
    python manage.py migrate
    ```

6.  **Run the Development Server (if applicable for Django):**
    Start the local development server.
    ```bash
    python manage.py runserver
    ```
    The application should now be accessible in your browser (usually at `http://127.0.0.1:8000/`).

## Managing Dependencies (`requirements.txt`)

The `requirements.txt` file lists all the Python packages required for this project.

**Important:** Installing new packages (e.g., using `pip install new-package`) does **NOT** automatically update the `requirements.txt` file.

**How to Update `requirements.txt`:**

Whenever you add, remove, or update packages in your activated virtual environment, you need to regenerate the `requirements.txt` file:

1.  Make sure your virtual environment is active.
2.  Run the following command in your project's root directory:
    ```bash
    pip freeze > requirements.txt
    ```
3.  Add the updated `requirements.txt` file to your Git commits:
    ```bash
    git add requirements.txt
    git commit -m "Update project dependencies"
    ```

Keeping `requirements.txt` up-to-date ensures that anyone setting up the project will install the correct versions of all necessary packages.