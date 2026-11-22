from test03_上下文长度计算 import tokens_by_messages
from test03_滑动窗口 import context_sliding_window
from test03_摘要记忆 import context_summary


message_history = []

system_prompt = """
你运行在一个和思考、行动、观察和回答的循环，在循环结束时，你输出最终的答案。
用“思考”来描述你对被问问题的想法。
用“操作”运行您可用的操作之一。
“观察”将是运行这些操作的结果。
“答案”将是分析观察结果的结果。
"""
message_history.append({"role": "system", "content": system_prompt})

query = "比赛场上，篮球队的球员人数乘以排球队的球员人数，结果是多少"
message_history.append({"role": "user", "content": query})
message_history.append({"role": "user", "content": query})
message_history.append({"role": "user", "content": "1*1=？"})
message_history.append({"role": "user", "content": "再加1呢？"})

# print(tokens_by_messages(message_history)) # 81
# print(len(system_prompt) + len(query)) # 131

# print(context_sliding_window(message_history))

print(context_summary(message_history))