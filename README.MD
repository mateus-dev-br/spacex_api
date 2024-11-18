# SpaceX Launches Viewer

This project is a web application developed with Django that displays information about **SpaceX launches**, including successful, failed, and upcoming launches. The application consumes the public SpaceX API and organizes the data for better visualization.

## Features

- Displays **successful SpaceX launches.**
- Displays **failed SpaceX launches.**
- Displays **upcoming SpaceX launches.**
- Provides an **interactive interface** to navigate between different launch sections.

## Technologies Used

- **Django**: Web framework used to develop the application.
- **Requests**: Library to perform HTTP requests to the SpaceX API.
- **HTML/CSS**: Used to structure and style the user interface.

## Requirements

Make sure the following dependencies are installed:

- **Python 3.8+**
- **Django 5.1.3**
- **Requests**

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/seu-usuario/spaceX-launches-viewer.git
   cd spaceX-launches-viewer

2. Create a virtual environment (recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  #  On Windows, use `venv\Scripts\activate`

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt

4. Run the development server:

    ```bash
    python manage.py runserver

5. Access the application in your browser:

    ```arduino
    http://127.0.0.1:8000