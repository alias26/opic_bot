import sys, os
import argparse
import streamlit as st
import streamlit.components.v1 as components
from gpt import chatbot

chatbot = chatbot()

st.header("OPIc Script Generator")  # 헤더 생성

# 답변 리스트 생성
if "generated" not in st.session_state:
    st.session_state["generated"] = []

# 질문 리스트 생성
if "past" not in st.session_state:
    st.session_state["past"] = []

# 유저 질문 입력 및 버튼 생성
with st.form("form", clear_on_submit=True):
    # user_input = st.text_input(label="Question", placeholder="Question", key="input")
    user_input = st.text_area(label="Question", placeholder="Question & Story", key="input", height=200)

    submitted = st.form_submit_button("Send")

# 질문 전송 및 질의응답 저장
if submitted and user_input:
    output = chatbot.gpt_send_message(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state["generated"]:
    index = st.selectbox(
        "Questions",
        range(len(st.session_state["past"])),
        format_func=lambda x: st.session_state["past"][x],
        index=len(st.session_state["past"]) - 1,
        placeholder="Select Questions",
    )  # 질문 선택상자 생성 및 인덱스 반환

    st.text(
        st.session_state["generated"][index]
    )
