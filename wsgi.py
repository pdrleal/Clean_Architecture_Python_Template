import os

import src
from application.app import create_app
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

app = create_app(os.getenv("FLASK_CONFIG"), dependency_container_packages=[src])

if __name__ == '__main__':
    app.run(debug=False, port=5005)
