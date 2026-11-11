from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="deepseek-flash", # 选择模型
    messages=[ # 发送对话
        {
            "role": "user",
            "content": "你是谁？" # 用户的问题
        }
    ],
    stream=True # 流式
)

for chunk in completion:
    print(chunk.choices[0].delta.content, end="|")  # 逐个打印最新生成的内容

