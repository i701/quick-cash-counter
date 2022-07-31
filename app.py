import streamlit as st

st.set_page_config(
    page_title="QCC",
    page_icon="💸",
)
st.title("Cash Counter 💸+💸")


if "total_sum" not in st.session_state:
    st.session_state["total_sum"] = 0

st.caption("Select number of notes for each note.")
_500s = st.slider("500 MVR", 0, 100, 0) * 500
_100s = st.slider("100 MVR", 0, 100, 0) * 100
_50s = st.slider("50 MVR", 0, 100, 0) * 50
_20s = st.slider("20 MVR", 0, 100, 0) * 20
_10s = st.slider("10 MVR", 0, 100, 0) * 10
_5s = st.slider("5 MVR", 0, 100, 0) * 5


def accumulate(*notes) -> int:
    total = 0
    return sum(total + n for n in notes)


st.session_state.total_sum = accumulate(_500s, _100s, _50s, _20s, _10s, _5s)


st.header(f"{st.session_state.total_sum} MVR")
