from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()


@app.post("/convert-to-uppercase/")
async def convert_to_uppercase(file: UploadFile = File(...)):
    # 确认文件扩展名为.txt
    if not file.filename.endswith('.txt'):
        return {"message": "Please upload a .txt file."}
    # 读取原始文件内容
    content = await file.read()
    # 转换内容为大写
    content_uppercase = content.decode('utf-8').upper()
    # 写入转换后的内容到一个新文件
    output_filename = 'output_uppercase.txt'
    with open(output_filename, 'w') as output_file:
        output_file.write(content_uppercase)
    # 返回转换后的文件
    return FileResponse(path=output_filename, filename=output_filename, media_type='txt')


@app.get("/")
def read_root():
    return {"message": "Welcome to the Document Wizard API!"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="127.0.0.1", log_level="info")
