import os
import pathlib

from dotenv import load_dotenv

from core.security import decrypt

env_file = os.environ.get("env_file", ".env")
load_dotenv(env_file)

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()
PROJECT_NAME = os.getenv("PROJECT_NAME", "app")

IBM_IMAGE_NAME = os.getenv("IBM_IMAGE_NAME", "not_found.jpg")
REDHAT_IMAGE_NAME = os.getenv("REDHAT_IMAGE_NAME", "not_found.jpg")
SECRET_IMAGE_LOCATION = os.getenv("SECRET_IMAGE_LOCATION", None)

SECRET_KEY = os.getenv("SECRET_KEY", None)

QUOTE_URL = os.getenv("QUOTE_URL", "http://quote:8080")

if SECRET_IMAGE_LOCATION is None or SECRET_KEY is None:
    src_image_data = "static/images/encrypted.png"
else:
    ROOT_DIR = str(pathlib.Path(__file__).parent.parent)
    full_path = ROOT_DIR + "/static/images/" + SECRET_IMAGE_LOCATION
    img_data = pathlib.Path(full_path).read_text()
    img_data = img_data.replace("\n", "")
    cleartext_string = decrypt(cipher_text_string=img_data, secret_key=SECRET_KEY)
    src_image_data = "data:image/jpeg;base64," + cleartext_string

# Set or retrieve OpenShift Namespace for
namespace_filepath = "/run/secrets/kubernetes.io/serviceaccount/namespace"
ns_path = pathlib.Path(namespace_filepath)
if ns_path.is_file():
    file_namespace = open("/run/secrets/kubernetes.io/serviceaccount/namespace", "r")
    NAMESPACE = file_namespace.read()
else:
    NAMESPACE = os.getenv("NAMESPACE", "default")
