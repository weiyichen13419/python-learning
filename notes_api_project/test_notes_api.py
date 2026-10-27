import os
os.environ["NOTES_DB_NAME"] = "test_notes.db"
from fastapi.testclient import TestClient
from main import app
client = TestClient(app)
def test_get_existing_note():
    new_id = None
    try:
        response=client.post("/notes",json={"content":"测试"})
        new_id=response.json()["id"]
        response = client.get(f"/notes/{new_id}")
        assert response.status_code==200
    finally:
        if new_id is not None:
            status = client.delete(f"/notes/{new_id}")
            assert status.status_code == 200


    # response = client.get("/notes/19")
    # assert response.status_code==200
    # # 逗号并不能同时检查两个条件
    # # assert response.json()["id"]==19,response.json()["content"]=="更新"
    # assert response.json()["id"] == 19
    # assert response.json()["content"]=="更新"

def test_get_missing_note():
    response = client.get("/notes/999999")
    assert response.status_code==404
    assert response.json()["detail"]=="id不存在"

# def test_create_and_note():
#     response = client.post("/notes",json={"content":"pytest自动创建"})
#     assert response.status_code==201
#     note_id = response.json()["id"]
#     response = client.get(f"/notes/{note_id}")
#     assert response.status_code==200
#     assert response.json()["content"]=="pytest自动创建"

def test_create_and_note():

    note_id = None
    try:
        response = client.post("/notes", json={"content": "pytest自动创建"})
        assert response.status_code == 201
        note_id = response.json()["id"]
        note = client.get(f"/notes/{note_id}")

        assert note.status_code==200
        assert note.json()["content"] =="pytest自动创建"


    finally:

        if note_id is not None:
            status = client.delete(f"/notes/{note_id}")

            assert status.status_code == 200

import pytest
@pytest.mark.parametrize("content",[""," ","  "])
def test_invalid_note_content(content):
    response = client.post("/notes", json={"content":content})
    assert response.status_code==422
