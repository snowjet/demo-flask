import os
import pathlib

from dotenv import load_dotenv

from core.security import decrypt

env_file = os.environ.get("env_file", ".env")
load_dotenv(env_file)

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
PROJECT_NAME = os.getenv("PROJECT_NAME", "app")

MAIN_TITLE_NAME = os.getenv("MAIN_TITLE_NAME", "Basic Demo")
MAIN_IMAGE_NAME = os.getenv("MAIN_IMAGE_NAME", "not_found.jpg")
MAP_IMAGE_NAME = os.getenv("MAP_IMAGE_NAME", "not_found.jpg")
OPENSHIFT_IMAGE_NAME = os.getenv("OPENSHIFT_IMAGE_NAME", "not_found.jpg")
SECRET_IMAGE_LOCATION = os.getenv("SECRET_IMAGE_LOCATION", None)

SECRET_KEY = os.getenv("SECRET_KEY", None)

QUOTE_URL = os.getenv("QUOTE_URL", "http://quote:8080")

if SECRET_IMAGE_LOCATION is None or SECRET_KEY is None:
    src_image_data = "static/images/encrypted.jpg"
else:
    ROOT_DIR = str(pathlib.Path(__file__).parent.parent)
    full_path = ROOT_DIR + "/static/images/" + SECRET_IMAGE_LOCATION
    posix_full_path = pathlib.Path(full_path)
    if posix_full_path.is_file():
        img_data = posix_full_path.read_text()
        img_data = img_data.replace("\n", "")
        cleartext_string = decrypt(cipher_text_string=img_data, secret_key=SECRET_KEY)
        src_image_data = "data:image/jpeg;base64," + cleartext_string
    else:
        src_image_data = "static/images/encrypted.jpg"
