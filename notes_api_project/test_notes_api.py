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


def test_fixture_content(note_content):
    assert note_content =="今天学习fixture"

@pytest.fixture
def created_note():
    new_id = None
    try:
        response = client.post("/notes",json={"content":"fixture自动创建"})
        assert response.status_code==201
        new_id=response.json()["id"]
        yield {
            "id":new_id,
            "content":response.json()["content"]
        }
    finally:
        if new_id is not None:
            dele=client.delete(f"/notes/{new_id}")
            response = dele.status_code
            assert response in(200,404)

def test_created_note(created_note):
    note_id = created_note["id"]
    response = client.get(f"/notes/{note_id}")
    assert response.status_code==200

def test_update_note(created_note):
    note_id = created_note["id"]
    response = client.put(f"/notes/{note_id}",json={"content":"fixture更新成功"})
    assert response.status_code==200
    response=client.get(f"/notes/{note_id}")
    assert response.status_code==200
    assert response.json()["content"]=="fixture更新成功"

def test_delete_note(created_note):
    note_id = created_note["id"]
    delete_note = client.delete(f"/notes/{note_id}")
    assert delete_note.status_code == 200
    get_note = client.get(f"/notes/{note_id}")
    assert get_note.status_code==404
    assert get_note.json()["detail"]=="id不存在"

def test_delete_twice(created_note):
    new_id = created_note["id"]
    response = client.delete(f"/notes/{new_id}")
    assert response.status_code==200
    response = client.delete(f"/notes/{new_id}")
    assert response.status_code==404
    response = client.get(f"/notes/{new_id}")
    assert response.status_code==404