# Personal-Notes App

The Personal-Notes App is a web application built with Django that allows users to create, manage, and organize their personal notes. It provides a user-friendly interface to create new notes, edit existing ones, and categorize them for easy retrieval. This app is ideal for anyone looking to keep track of their thoughts, ideas, and important information in one centralized location.

## Features

- User Authentication: Users can sign up, log in, and reset their passwords securely.
- Create Notes: Users can create new notes with a title and content.
- Edit and Delete Notes: Users can edit and delete their existing notes.
- Categories: Users can assign categories to their notes for better organization.
- Search Functionality: Users can search for specific notes based on keywords.
- Responsive Design: The app is designed to work smoothly across various devices.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Chatelo/Personal-Notes.git
cd Personal-Notes
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS and Linux
source venv/bin/activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Run database migrations:

```bash
python manage.py migrate
```

5. Create a superuser account:

```bash
python manage.py createsuperuser
```

6. Start the development server:

```bash
python manage.py runserver
```

7. Access the app in your web browser at `http://127.0.0.1:8000/`.

## Configuration

The Personal-Notes App uses a few environment variables for configuration. You can either set them in your environment or create a `.env` file in the project's root directory and set the values there.

Example `.env` file:

```plaintext
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

**Note**: In a production environment, make sure to set `DEBUG=False` and update `ALLOWED_HOSTS` accordingly for security.

## Contributing

Contributions to the Personal-Notes App are welcome and encouraged! If you have any bug fixes, improvements, or new features to add, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature/your-feature-name`.
3. Commit your changes: `git commit -m "Add your feature description"`.
4. Push the branch to your forked repository: `git push origin feature/your-feature-name`.
5. Submit a pull request to the `main` branch of the original repository.

## License

The Personal-Notes App is open-source software released under the [MIT License](LICENSE).

## Acknowledgments

- Thanks to the Django community for providing a robust and powerful web framework.
