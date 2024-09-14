
import os
import qianfan
from typing import List, Dict, Any


# os.environ["QIANFAN_ACCESS_KEY"] = "995cbd07f1174a5490176fd02eace66a"
# os.environ["QIANFAN_SECRET_KEY"] = "3b5592144eee4239b3a5c0d93ca4aad9"


class BaiduModel():
    def __init__(self, model:str = "ERNIE-Speed-128K"):
        self.model = model
    def chat(self, messages:List[Dict[str, Any]], stream:bool = False, **kwargs) -> Any:

        chat_comp = qianfan.ChatCompletion()
        resp = chat_comp.do(model=self.model, messages=messages, stream=stream, **kwargs)

        return resp
