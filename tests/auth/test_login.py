from lib.auth import Auth
from config import APP_URL,LOG

def test_login():
    LOG.info("test login")
    res= Auth().login(APP_URL, "admin", "admin")
    LOG.debug(res.json())
    assert res.ok