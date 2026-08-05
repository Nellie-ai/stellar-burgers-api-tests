from os import getenv


DEFAULT_BASE_URL = "https://stellarburgers.education-services.ru"
DEFAULT_HTTP_TIMEOUT_SECONDS = 10.0


def _read_base_url():
    base_url = getenv("STELLAR_BURGERS_BASE_URL", DEFAULT_BASE_URL).strip().rstrip("/")

    if not base_url.startswith(("http://", "https://")):
        raise ValueError("STELLAR_BURGERS_BASE_URL must use http:// or https://")

    return base_url


def _read_http_timeout():
    raw_value = getenv(
        "STELLAR_BURGERS_HTTP_TIMEOUT_SECONDS",
        str(DEFAULT_HTTP_TIMEOUT_SECONDS),
    )

    try:
        timeout = float(raw_value)
    except ValueError as exc:
        raise ValueError(
            "STELLAR_BURGERS_HTTP_TIMEOUT_SECONDS must be a number",
        ) from exc

    if timeout <= 0:
        raise ValueError("STELLAR_BURGERS_HTTP_TIMEOUT_SECONDS must be greater than 0")

    return timeout


BASE_URL = _read_base_url()
HTTP_TIMEOUT_SECONDS = _read_http_timeout()
