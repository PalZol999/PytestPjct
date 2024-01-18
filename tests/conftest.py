import pytest # to be installed
import requests # to be installed
from config import SESSION, APP_URL, ADMIN_PW, ADMIN_USER, LOG #generic variables


@pytest.fixture(scope="session")
def login_as_admin():
    LOG.info("login_as_admin")
    # Step 1: Auth
    payload={"username":ADMIN_USER, "password":ADMIN_PW}
    LOG.debug(payload)
    res= SESSION.post(f"{APP_URL}/auth/login", data=payload)
    assert res.ok

    # Step 2: Get comments  
    access_token= res.json()["access_token"]
    yield access_token #it's gonna use the token then areased it after it (memo)

