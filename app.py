import streamlit as st
from streamlit_markmap import markmap
from work.work import FileLoad, ChatServer
import re

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "你好，我是你的AI助手。有什么我可以帮助你的吗？"},
    ]
if "content" not in st.session_state:
    st.session_state.content = ""
if "mindmapdata" not in st.session_state:
    st.session_state.mindmapdata = ""

def extract_code_blocks(text):

    pattern = r'```(?:markdown)?\s*([\s\S]*?)\s*```'
    

    matches = re.findall(pattern, text, re.MULTILINE)
    

    result = "\n\n".join(matches)
    

    return result.strip() if result else text

st.title(":blue[听微-mindmap 测试 🤖]")
st.divider()
st.set_page_config(page_title="markmap")

uploaded_file = st.file_uploader(label = "上传文件", type=["txt","doc","docx","pdf"])

prompt = st.chat_input("Say something")

for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("assistant").write(message["content"])

if uploaded_file is not None:
    file_load = FileLoad()
    st.session_state.content = file_load.read_file(uploaded_file)

model = ChatServer(model_name = "ERNIE-Speed-128K")
if prompt:
    with st.spinner("正在生成答案..."):
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = model.run(prompt=prompt,content=st.session_state.content)
        answer_content = ""
        placeholder = st.empty()
        for mes in response:
            if mes:
                answer_content += mes["body"]["result"]
                placeholder.write(answer_content)   
        placeholder.write(answer_content)
    st.session_state.mindmapdata = answer_content
    st.session_state.messages.append({"role": "assistant", "content": answer_content})






if st.session_state.mindmapdata:
    
    markmap(extract_code_blocks(st.session_state.mindmapdata))