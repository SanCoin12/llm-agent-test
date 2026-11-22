from deepseek_tokenizer import ds_token

# text = "你是谁？"
# result = ds_token.encode(text)

# print(result)
# print(f"Token数：{len(result)}")

# # 输出结果
# # [122294, 1148]
# # Token数：2

# 针对message对象，可以使用下面函数进行统计
def tokens_by_messages(message_history:list):
    tokens = 0
    for msg in message_history:
        text = msg['content']
        tokens += len(ds_token.encode(text))

    return tokens

