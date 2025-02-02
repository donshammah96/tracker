# tracker

## Project Description
This project is a simple tracker application that allows users to track their expenses and income. It provides endpoints to list and create expenses and income, as well as generate a monthly summary of expenses and income.

## Setup Instructions
1. Clone the repository:
    ```sh
    git clone https://github.com/donshammah96/tracker.git
    ```
2. Navigate to the project directory:
    ```sh
    cd tracker
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Apply the migrations:
    ```sh
    python manage.py migrate
    ```
5. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage Examples
- List and create expenses:
    ```
    GET /expenses/
    POST /expenses/
    ```
- List and create income:
    ```
    GET /income/
    POST /income/
    ```
- Generate monthly summary:
    ```
    GET /summary/<year>/<month>/
    ```
