import pytest # to be installed
import requests # to be installed
from lib.utils import build_request_headers
from lib.comments import Comments # .(for current lib)comments(for folder) import Comments (for Class)
from config import APP_URL, LOG


def test_get_all_comments(login_as_admin): #I've passed the conftest func
    LOG.info("test_get_all_comments")# to know what you test
    res = Comments().get_all_comments(APP_URL, login_as_admin)
    LOG.debug(res.json())
    assert res.ok

def test_cud_comment(login_as_admin):
    LOG.info("test_cud_comment") # to know what you test
    res= Comments().create_comments(APP_URL, login_as_admin, "first post")
    assert res.ok
    response_data = res.json()
    comment_id= response_data["id"]
    LOG.debug(response_data)
    assert response_data["comment_text"] == "first post"

    res = Comments().update_comment(APP_URL, login_as_admin, comment_id,
                                    message="updated to second part", likes= 3)
    assert res.ok #response 200
    response_data= res.json()
    LOG.debug(response_data)
    assert response_data["comment_text"] == "updated to second part"
    assert response_data["likes"] == 3

    res= Comments().deleted_comment(APP_URL, login_as_admin, comment_id)
    assert res.ok
    response_data = res.json()
    LOG.debug(response_data)
    assert response_data["detail"].strip() == f"Deleted comment {comment_id}".strip()



