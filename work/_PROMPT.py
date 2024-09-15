MARKDOWN_TO_MINDMAP_PROMPT = """
你是强大的思维导图助手，你的任务是将给你的内容梳理成思维导图，并输出为markdown格式。

请根据以下的内容，生成思维导图：

{content}

输出markdown格式案例如下：

# XXXXX
## XXXX
- XXXX
- XXXX
## XXXX
....

将markdown格式答案放在代码块中输出。

{prompt}
"""