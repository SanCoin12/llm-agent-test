from openai import OpenAI

client = OpenAI()

# 好像对于flash模型没差别
for t in [0, 0.5, 1, 1.5, 2]:
    completion = client.chat.completions.create(
        model="deepseek-flash", # 选择模型
        messages=[ # 发送对话
            {
                "role": "user",
                "content": "我爱你" # 用户的问题
            }
        ],
        temperature=t # 温度参数，默认1，0保守，2发散
    )

    print(completion.choices[0].message.content) # 输出结果

