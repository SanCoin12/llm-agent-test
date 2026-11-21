# 使用tools
import json
from test02_封装LLM import get_completion
from test02_工具 import get_weather

message = get_completion({"role": "user", "content": "今天北京天气如何"})
print(message)  # LLM返回工具调用信息

func_call_id = message['tool_calls'][0].id
func_kwargs = json.loads(message['tool_calls'][0].function.arguments)
func_result = get_weather(**func_kwargs) # 调用函数

print("")
message = get_completion({"role": "tool", "tool_call_id": func_call_id, "content": str(func_result)})
print(message)