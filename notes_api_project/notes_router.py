from fastapi import APIRouter,HTTPException
import sqlite3
from pydantic import field_validator,BaseModel, Field
import os
BASE_DIR = os.path.dirname(__file__)
db_name = os.getenv("NOTES_DB_NAME","notes.db")
db_path = os.path.join(BASE_DIR,db_name)
router = APIRouter(prefix="/notes",tags=["笔记管理"])

conn = sqlite3.connect(db_path)
conn.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT,content TEXT NOT NULL)")
conn.close()
class NoteRequest(BaseModel):
    content:str=Field(min_length=1)

    @field_validator("content")
    @classmethod
    def check_content(cls,value):
        if not value.strip():
            raise ValueError("笔记内容不能为空或只有空格")
        return value.strip()

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
    try:
        conn.row_factory=sqlite3.Row
        cursor=conn.execute("SELECT id,content FROM notes WHERE id=?",(note_id,))
        row=cursor.fetchone()
    finally:
        conn.close()
    if row:
        return {"id":row["id"],"content":row["content"]}
    else:
        raise HTTPException(status_code=404, detail="id不存在")

@router.put("/{note_id}")
def update_note(note_id:int,note:NoteRequest):
   conn = sqlite3.connect(db_path)
   cursor=conn.execute("UPDATE notes SET content=? WHERE id=?",(note.content,note_id))
   affected=cursor.rowcount
   conn.commit()
   conn.close()
   if affected == 0:
       raise HTTPException(status_code=404, detail="id不存在")
   else:
       return {"id": note_id,"affected": affected,"content":note.content,"信息":"成功" }