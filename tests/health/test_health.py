import pytest
import requests

def test_health():
    resp = requests.get("http://localhost:8080/health")
    assert resp.ok