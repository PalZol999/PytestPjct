from config import LOG
from config import HideSensitiveData

def build_request_headers(access_token, access_type="application/json", **kwargs):
    headers={
        "Authorization": f"Bearer {access_token}",
        "Accept": access_type
    }
    if "content_type" in kwargs:
        headers["Conent-type"]=kwargs["content_type"]

    LOG.debug(f"Request headers: {headers}")
    return headers