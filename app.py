"""The main app behind the blog site it runs imports the create_app and runs it"""

from website import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
