import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 環境変数の読み込み
load_dotenv()

# アプリタイトル
st.title("LLM質問アプリ")

# LLM設定
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

# ユーザー入力
question = st.text_input("質問を入力してください")

# 実行ボタン
if st.button("送信"):
    if question:
        response = llm.invoke(question)
        st.write("### 回答")
        st.write(response.content)
    else:
        st.warning("質問を入力してください。")