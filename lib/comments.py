import requests
from lib.utils import build_request_headers
from config import SESSION, LOG

class Comments: # name it the same way you named you class
    def __init__(self): # constructor
        self.comment_url = "/comments"  #if this change, you can change it for all

    def get_all_comments(self, app_url, access_token):
        LOG.info("get_all_comments")
        request_headers = build_request_headers(access_token)
        res=SESSION.get(f"{app_url}{self.comment_url}", headers= request_headers)
        return res
    
    def create_comments(self, app_url, access_token, message):
        LOG.info("create_comments")
        request_headers = build_request_headers(access_token)
        payload= {"text": message}
        LOG.debug(f"Request payload: {payload}")
        res=SESSION.post(f"{app_url}{self.comment_url}/", headers= request_headers, params=payload)
        #params give the end of the address related to the comment's text
        #don't forget the / at the end of the url!
        return res
    
    def update_comment(self, app_url, access_token, comment_id, **kwargs):
        LOG.info("update_comment")
        request_headers = build_request_headers(access_token, content_type="application/json")
        payload= {}
        
        if "message" in kwargs:
            payload["comment_text"] = kwargs["message"]
        if "likes" in kwargs:
            payload["likes"] = kwargs["likes"]

        LOG.debug(f"Request payload: {payload}")
        res=SESSION.put(f"{app_url}{self.comment_url}/{comment_id}", headers= request_headers, json=payload)
        return res
    
    def deleted_comment(self, app_url, access_token, comment_id):
        LOG.info("deleted_comment")
        request_headers = build_request_headers(access_token)
        res=SESSION.delete(f"{app_url}{self.comment_url}/{comment_id}", headers=request_headers)
        return res
        
    