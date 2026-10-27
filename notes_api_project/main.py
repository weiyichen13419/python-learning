from fastapi import FastAPI,HTTPException,Query,Header,Cookie,Response

from pydantic import field_validator,BaseModel, Field

# uvicorn main:app --reload
app = FastAPI()

@app.get("/")
def home():
    return {"message": "我的第一个Python后端接口"}
@app.get("/students/{student_id}",tags=["学生查询"])
def get_student(student_id: int):
    students = {
        1: "张三",
        2: "李四"
    }
    if student_id not in students:
        raise HTTPException(status_code=404, detail="学生不存在")
    return {"student_id": student_id, "name": students.get(student_id)}

@app.get("/search",tags=["搜索"])
def search_students(keyword:str = Query(min_length=2)):

    return{"keyword": keyword,"message":"搜索请求已收到"}

@app.post("/feedback",tags=["反馈"])
def receive_feedback(message:str):
    return {"message":message,"status":"received"}

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

@app.post("/ai/chat",tags=["AI聊天接口"],response_model=ChatResponse)
def ai_chat(data:ChatRequest):
    return{"prompt":data.prompt,"reply":"已收到你的问题","internal_note":"仅供后端使用"}

from notes_router import router
app.include_router(router)


@app.get("/header-test",tags=["测试请求头"])
def header_test(
    client_name: str = Header(alias="X-Client-Name")
):
    return {"client_name":client_name,"测试信息":"成功！"}

@app.get("/cookie-info",tags=["Cookie"])
def cookie_info(
        session_id: str = Cookie()
):
    return {"session_id":session_id , "信息":"成功！"}

@app.get("/set-session",tags=["Cookie"])
def cookie_set(response:Response):
    response.set_cookie(
        key="session_id",
        value="lesson70"
    )
    return {"message": "Cookie已设置"}

@app.get("/clear-session",tags=["Cookie"])
def cookie_clear(response:Response):
    response.delete_cookie(
        key="session_id"
    )
    return {"message": "Cookie已删除"}

@app.get("/set-http-only-session",tags=["Cookie"])
def set_http_only_session(response:Response):
    response.set_cookie(
        key="session_id",
        value="lesson72",
        httponly=True
    )
    return {"message": "httponlyCookie已设置"}

@app.get("/set-secure-session",tags=["Cookie"])
def set_secure_session(response:Response):
    response.set_cookie(
        key="session_id",
        value="lesson73",
        secure=True
    )
    return {"message": "secureCookie已设置"}

@app.get("/set-samesite-session",tags=["Cookie"])
def set_samesite_session(response:Response):
    response.set_cookie(
        key="session_id",
        value="lesson74",
        samesite="lax"
    )
    return {"message": "laxCookie已设置"}

@app.get("/set-expiring-session",tags=["Cookie"])
def set_expiring_session(response:Response):
    response.set_cookie(
        key="session_id",
        value="lesson75",
        max_age=3600
    )
    return {"message": "Cookie已设置,max_age=3600"}

@app.get("/set-notes-path-cookie",tags=["Cookie"])
def set_notes_path_cookie(response:Response):
    response.set_cookie(
        key="view_mode",
        value="dark",
        path="/notes"
    )
    return {"message": "指定notes_path_Cookie已设置"}


