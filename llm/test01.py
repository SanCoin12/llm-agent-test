from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="deepseek-flash", # 选择模型
    messages=[ # 发送对话
        {
            "role": "system",
            "content": "回复内容不超过10个字"
        },
        {
            "role": "user",
            "content": "请介绍你自己" # 用户的问题
        }
    ],
    temperature=2 # 温度参数，默认1，0保守，2发散
)

print(completion.choices[0].message.content) # 输出结果

