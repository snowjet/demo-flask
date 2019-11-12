import os
import pathlib

from dotenv import load_dotenv

env_file = os.environ.get("env_file", ".env")
load_dotenv(env_file)

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()
PROJECT_NAME = os.getenv("PROJECT_NAME", "app")

IBM_IMAGE_NAME = os.getenv("IBM_IMAGE_NAME", "not_found.jpg")
REDHAT_IMAGE_NAME = os.getenv("REDHAT_IMAGE_NAME", "not_found.jpg")
SECRET_IMAGE_LOCATION = os.getenv("SECRET_IMAGE_LOCATION", "not_found.jpg")

if SECRET_IMAGE_LOCATION == "not_found.jpg":
    src_image_data = "static/images/not_found.jpg"
else:
    full_path = "/opt/app-root/src/static/images/" + SECRET_IMAGE_LOCATION
    img_data = Path(full_path).read_text()
    img_data = img_data.replace('\n', '')
    src_image_data = "data:image/jpeg;base64," + img_data

# Set or retrieve OpenShift Namespace for
namespace_filepath = "/run/secrets/kubernetes.io/serviceaccount/namespace"
ns_path = pathlib.Path(namespace_filepath)
if ns_path.is_file():
    file_namespace = open("/run/secrets/kubernetes.io/serviceaccount/namespace", "r")
    NAMESPACE = file_namespace.read()
else:
    NAMESPACE = os.getenv("NAMESPACE", "default")

