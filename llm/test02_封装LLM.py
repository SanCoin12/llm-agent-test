from openai import OpenAI

client = OpenAI()

# 使用变量保存历史记录
message_history = []

# 描述函数
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "根据指定的坐标提供当地摄氏度",
        "parameters": {
            "type": "object",
            "properties": {
                "latitude": {"type": "number"},
                "longitude": {"type": "number"}
            },
            "required": ["latitude", "longitude"],
            "additionalProperties": False
        },
        "script": True
    }
}]

# 发送消息给大模型，并自动保存记录
def get_completion(message):
    message_history.append(message) # 用户提问加入记录
    response = client.chat.completions.create(
        model="deepseek-flash", # 选择模型
        messages=message_history,
        tools=tools
    )

    response_dict = dict(response.choices[0].message)
    message_history.append(response_dict) # 大模型回答加入记录
    return response_dict
