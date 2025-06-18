# -*- coding: utf-8 -*-
from openai import OpenAI
# OpenAI API를 사용하여 챗봇을 구현하는 코드입니다.

client = OpenAI(api_key="")

with open("prompt.txt", "r", encoding="utf-8") as f:
    instructions = f.read()


# 챗봇 생성
class chatbot:
    chat_log_size = 0 # 채팅을 기억할 수 있는 크기
    gpt_standard_messages = []

    def __init__(self):
        self.chat_log_size = 10  # 채팅을 기억할 수 있는 크기
        self.gpt_standard_messages = [
            {
                "role": "developer",
                "content": instructions,
            }
        ] 

    def set_log_size(self, chat_log_size):
        self.chat_log_size = chat_log_size

    def gpt_send_message(self, question: str):  # 질문 및 답변
        self.gpt_standard_messages.append({"role": "user", "content": question})

        res = client.responses.create(
            model="o4-mini-2025-04-16", input=self.gpt_standard_messages
        )  # 모델 선택 및 질의응답

        answer = res.output_text
        
        self.gpt_standard_messages.append({"role": "assistant", "content": answer})
        if self.chat_log_size * 2 < len(self.gpt_standard_messages):
            self.gpt_standard_messages.pop(1)
            self.gpt_standard_messages.pop(1)

        return answer
