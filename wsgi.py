import os
import os.path
import src
from application.app import create_app
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

if os.path.isfile(".env") is False:
    raise FileNotFoundError("No .env file found")
if "FLASK_CONFIG" not in os.environ:
    raise ValueError("No FLASK_CONFIG environment variable found")
app = create_app(os.getenv("FLASK_CONFIG"), dependency_container_packages=[src])

if __name__ == '__main__':
    app.run(debug=False, port=5005)
