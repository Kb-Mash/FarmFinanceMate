# FarmFinanceMate: Simple Money Management App for Small Farmers
This is a simple money management application designed specifically for small farmers in rural villages who traditionally record their income and expenses manually in books. The application aims to digitize this process, making it more efficient and accessible.

## Features
- User Authentication: Users can sign up and log in securely to access their personal financial records.
- Income and Expense Tracking: Farmers can easily record their daily income and expenses, categorizing them for better organization.
- Monthly Reports: The app generates monthly reports summarizing the financial activities, helping users to understand their financial trends.
- Data Visualization: Graphical representation of income and expenses over time, providing users with a clear overview of their financial status.
- Responsive Design: Built using Bootstrap, the frontend of the app is mobile-friendly, ensuring accessibility across devices.

## Technologies Used
- Django: A high-level Python web framework used for building the backend of the application.
- Bootstrap: A popular HTML, CSS, and JavaScript framework for developing responsive, mobile-first web projects.
- SQLite: A lightweight, self-contained SQL database engine used for storing user data.
- Version Control: Git for version control and collaboration.
- IDE: Visual Studio Code (VS Code) for code editing and development.

## Getting Started
To run this application locally, follow these steps:
- Clone this repository to your local machine.
- Install Python and Django if you haven't already.
- Navigate to the project directory in your terminal.
- Run the following command to install dependencies:
    pip install -r requirements.txt
- Apply migrations to set up the database:
    python manage.py migrate
- Start the development server:
    python manage.py runserver
- Open your web browser and go to http://localhost:8000 to access the application.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them.
- Push your changes to your fork.
- Submit a pull request detailing your changes.
