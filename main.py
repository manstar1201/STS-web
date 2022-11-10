import streamlit as st
import time
from predict import load_model, get_predict
import torch


st.set_page_config(page_title = "MANSTAR's Test Page", layout = "centered")

st.title("문장 의미 유사도 측정 데모")
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    s1 = st.text_input(
        "첫 번째 문장을 입력해주세요.",
        placeholder = "이곳에 작성해주세요."
    )

with col2:
    s2 = st.text_input(
        "두 번째 문장을 입력해주세요.",
        placeholder = "이곳에 작성해주세요."
    )
show = st.checkbox('점수 표시(0-5점)')
activate = st.button('계산')
st.markdown("---")
if activate:
    if s1 and s2:
        model= load_model()

        with st.spinner("계산 중..."):
            result = get_predict(model, s1, s2)

            if result < float(3):
                is_similiar = "유사하지 않습니다."

            if result >= float(3):
                is_similiar = "유사합니다."

        if show:
            st.success(f'{is_similiar}')
            st.success(f'유사도 점수는 {result} 입니다.')

        else:
            st.success(f'{is_similiar}')
    
    else:
        st.error("문장을 입력해주세요")