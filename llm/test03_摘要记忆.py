import openai

client = openai.OpenAI()

def context_summary(message_list):
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[{
            "role": "user",
            "content": f"请对以下对话内容进行总结：{message_list}"
        }]
    )
    
    new_message_list = [{"role": "system", "content": f"此前对话内容的总结： {response.choices[0].message.content}"}]

    return new_message_list

