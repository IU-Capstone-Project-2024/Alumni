# Alumni Project

This repository contains the codebase for the Innopolis Alumni project developed as part of the IU Capstone Project 2024.

## Project Description

The Alumni project aims to create a platform for connecting alumni between each other and with current students and faculty. The platform includes features such as user authentication, profile management, donation opportunities, alumni merchandise, AI chat, and event organization.

## Installation

1. **Clone the repository**:

    To clone a specific branch (for example, `main`), use the following command:

    ```bash
    git clone --branch main https://github.com/IU-Capstone-Project-2024/Alumni.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd Alumni
    ```

3. **Set up a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

2. **Open your browser and navigate to** `http://127.0.0.1:8000` to view the application.

## Changing Branches

To switch to a different branch (for example, `aichat`), use the following commands:

1. **Fetch all branches**:

    ```bash
    git fetch
    ```

2. **Switch to the desired branch**:

    ```bash
    git checkout aichat
    ```

3. **Pull the latest changes from the branch**:

    ```bash
    git pull origin aichat
    ```

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

To contribute:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

Feel free to modify this README to better suit your project's specifics and to provide additional information as needed.
