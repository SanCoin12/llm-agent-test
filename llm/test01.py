import os

from openai import OpenAI

os.environ['OPENAI_BASE_URL'] = "https://api.deepseek.com" # 接口地址
os.environ['OPENAI_API_KEY'] = "" # 接口密钥

client = OpenAI()

completion = client.chat.completions.create(
    model="deepseek-v3", # 选择模型
    messages=[ # 发送对话
        {
            "role": "user",
            "content": "请介绍你自己" # 用户的问题
        }
    ]
)

print(completion.choices[0].message.content) # 输出结果