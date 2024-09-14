import pymupdf
from .baidu_model import BaiduModel
from typing import List, Dict, Any, Union, Optional
from streamlit_markmap import markmap
import io
import fitz  # PyMuPDF
import docx
from PIL import Image
from ._PROMPT import *


class FileLoad:
    def __init__(self):
        pass

    def read_file(self, uploaded_file):
        file_type = uploaded_file.name.split('.')[-1].lower()
        
        if file_type == 'txt':
            return self.read_txt(uploaded_file)
        elif file_type in ['doc', 'docx']:
            return self.doc_docx_to_txt(uploaded_file)
        elif file_type == 'pdf':
            return self.pdf_to_txt(uploaded_file)
        else:
            raise ValueError("Unsupported file type")

    def read_txt(self, file):
        return file.getvalue().decode('utf-8')

    def pdf_to_txt(self, file):
        text = ""
        with fitz.open(stream=file.read(), filetype="pdf") as pdf:
            for page in pdf:
                text += page.get_text()
        return text

    def doc_docx_to_txt(self, file):
        if file.name.endswith('.docx'):
            doc = docx.Document(file)
            return "\n".join([para.text for para in doc.paragraphs])
        else:  # .doc file
            # 注意: 直接处理 .doc 文件较为复杂，这里仅作为示例
            # 实际使用时可能需要其他库如 antiword 或转换为 .docx
            raise NotImplementedError("Direct .doc file processing is not implemented")

class ChatServer():

    def __init__(self, model_name: Optional[str] = None):
        self.model = BaiduModel(model=model_name)


    def run(self,prompt: Optional[str] = None, content: Optional[str] = None):
        if prompt is None:
            prompt = ""
        if content is None:
            content = ""
        content = MARKDOWN_TO_MINDMAP_PROMPT.format(prompt=prompt, content=content)
        messages = [{"role": "user", "content": content}]
        response = self.model.chat(messages=messages, stream=True)
        return response