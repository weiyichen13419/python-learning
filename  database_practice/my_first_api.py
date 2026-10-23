from fastapi import FastAPI
from fastapi import HTTPException
app = FastAPI()
@app.get("/")
def home():
    return {"message": "我的第一个Python后端接口"}
@app.get("/students/{student_id}")
def get_student(student_id: int):
    students = {
        1: "张三",
        2: "李四"
    }
    if student_id not in students:
        raise HTTPException(status_code=404, detail="学生不存在")
    return {"student_id": student_id, "name": students.get(student_id)}

@app.get("/search")
def search_students(keyword:str):

    return{"keyword": keyword,"message":"搜索请求已收到"}

@app.post("/feedback")
def receive_feedback(message:str):
    return {"message":message,"status":"received"}


from pydantic import field_validator
from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    prompt: str = Field(min_length=1)
    @field_validator("prompt")
    @classmethod
    def check_prompt(cls,value):
        if not value.strip():
            raise ValueError("问题不能为空或只有空格")
        else:
            return value

class ChatResponse(BaseModel):
    prompt: str
    reply: str

@app.post("/ai/chat",response_model=ChatResponse)
def ai_chat(data:ChatRequest):
    return{"prompt":data.prompt,"reply":"已收到你的问题","internal_note":"仅供后端使用"}

import sqlite3
conn = sqlite3.connect("notes.db")
conn.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT,content TEXT NOT NULL)")
conn.close()
class NoteRequest(BaseModel):
    content:str=Field(min_length=1)
@app.post("/notes",status_code=201)
def create_note(note:NoteRequest):
    conn = sqlite3.connect("notes.db")
    conn.execute("INSERT INTO notes(content) VALUES(?)",(note.content,))
    conn.commit()
    conn.close()
    return {
  "content": note.content,
  "message": "笔记创建成功"
}

@app.get("/notes",response_model=list[str])
def get_notes():
    conn = sqlite3.connect("notes.db")
    result=[]
    for c in conn.execute("SELECT content FROM notes ORDER BY id ASC"):
         result.append(c[0])
    conn.close()
    return result

