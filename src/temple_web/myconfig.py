# Temple Web Settings

# one single place to find all the settings/config/constants for the temple web project

from urllib.parse import urljoin
from decouple import config
from importlib import metadata

DEPLOYMENT_VERSION = config(
    "DEPLOYMENT_VERSION", default="TestingLocal-ubuntu23-aahnik"
)


class PaymentGatewayConfig:
    BASE_URL = "https://merchant.upigateway.com/api/"

    CREATE_ORDER = BASE_URL + "create_order"
    CHECK_ORDER_STATUS = BASE_URL + "check_order_status"

    REQUEST_HEADERS = {"Content-Type": "application/json"}

    API_KEY = config("PAYMENT_GATEWAY_API_KEY")

    USER_DEFINED_FIELDS = {"udf1": DEPLOYMENT_VERSION}

    CALLBACK_SLUG = "payment-status"


class MyDjangoSettings:
    DEBUG = config("DEBUG", default=False, cast=bool)


# print(metadata())
# TODO: get project version from pyproject.toml

