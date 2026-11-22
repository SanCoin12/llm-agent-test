# 对message_history进行裁剪，仅保留system提示和最新的k个user提示

def context_sliding_window(message_list: list, k=2):
    new_message_list: list = message_list[-1*k:]

    # 如果丢失了系统提示，则手动补上
    if new_message_list[0]['role'] != "system": # 检查现在有没有系统提示
        if message_list[0]['role'] == "system": # 检查之前有没有系统提示
            new_message_list.insert(0,message_list[0])

    return new_message_list
