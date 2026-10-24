from fastapi import APIRouter,HTTPException
import sqlite3
from pydantic import field_validator,BaseModel, Field
import os
BASE_DIR = os.path.dirname(__file__)
db_path = os.path.join(BASE_DIR, "notes.db")

router = APIRouter(prefix="/notes",tags=["笔记管理"])

conn = sqlite3.connect(db_path)
conn.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT,content TEXT NOT NULL)")
conn.close()
class NoteRequest(BaseModel):
    content:str=Field(min_length=1)
@router.post("",status_code=201)
def create_note(note:NoteRequest):
    conn = sqlite3.connect(db_path)
    cursor=conn.execute("INSERT INTO notes(content) VALUES(?)",(note.content,))
    new_id=cursor.lastrowid
    conn.commit()
    conn.close()
    return {
        "id": new_id,
  "content": note.content,
  "message": "笔记创建成功"
}

@router.get("", response_model=list[str])
def get_notes():
    conn = sqlite3.connect(db_path)
    result=[]
    for c in conn.execute("SELECT content FROM notes ORDER BY id ASC"):
         result.append(c[0])
    conn.close()
    return result

@router.delete("/{note_id}")
def delete_note(note_id:int):
        conn = sqlite3.connect(db_path)
        cursor=conn.execute("DELETE FROM notes WHERE id=?",(note_id,))
        affected=cursor.rowcount
        conn.commit()
        conn.close()
        if affected == 0:
            raise HTTPException(status_code=404, detail="id不存在")
        else:
            return {"affected":affected,"id":note_id}

@router.get("/{note_id}")
def detail_note(note_id:int):
    conn = sqlite3.connect(db_path)
    conn.row_factory=sqlite3.Row
    cursor=conn.execute("SELECT id,content FROM notes WHERE id=?",(note_id,))
    row=cursor.fetchone()
    conn.close()
    if row:
        return {"id":row["id"],"content":row["content"]}
    else:
        raise HTTPException(status_code=404, detail="id不存在")
