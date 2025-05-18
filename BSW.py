import streamlit as st

st.title("어떤 게임을 좋아하시나요?")
st.caption("1학년 5반 방신우")

selected_option = st.radio("게임을 선택하세요", ("롤", "발로란트", "오버워치", "블루 아카이브", "니케", "스타레일"))
st.write("선택된 게임: ",selected_option)

name = st.text_input("게임에서 사용하는 닉네임을 적어주세요.")
st.write("입력된 닉네임:", name)

rating = st.select_slider("당신의 게임 실력은 어느정도 인가요?", ["브실골", "다이아", "랭커"])

st.header("당신은 개쩌는 나의 플레이를 볼것만 같은 느낌이 들었다!")
st.video("Bs.mov")

rating = st.select_slider("나의 최고티어를 맞춰 보시지?", ["아이언", "브론즈", "실버", "골드", "플레", "다이아", "초월자", "불멸", "레디언트"])

with st.expander("정답은?"):
    st.write("다이아")