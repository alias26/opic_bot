# OPIc Bot

## 설명
**AI Prompt를 통해 오픽 스크립트를 만들어주는 챗봇 생성**

## API 범위 및 상세
**ChatGPT** : 사용자 질문 입력에 따른 스크립트 생성  
**Streamlit** : UI 구성 및 답변 출력 
> Streamlit Text_Input -> ChatGPT 서버 -> Streamlit 질문, 캔버스, 코드 출력

## 파일
> **gpt.py** : ChatGPT API 기반 챗봇 Object  
> **main.py** : Streamlit으로 UI 구성

## 환경설정
```
pip install -r requirements.txt

gpt.py 내부에 ChatGPT API를 넣어주세요.
```
## 실행 방법
```
streamlit run main.py
or
streamlit run main.py --server.port [port_number]
```
