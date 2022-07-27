import streamlit as st
from bid_parser import parse


def submit_data():
    print("--submit--")
    vals = list(filter(None, [x for x in st.session_state.values()]))
    print(len(vals))
    if len(vals) == 3:
        proto = st.session_state['protocol']
        exchange = st.session_state['exchange']
        stream = st.session_state['code_string']
        resp = parse(proto, stream)
        st.info(resp)
        st.session_state.clear()

st.title("bidify 🛩️")
st.subheader("Bid simulator")
st.write("Generate bid request in google/openrtb protocol :)")
protocol = st.radio("Protocol:", ['Google', 'Openrtb'], key="protocol")
exchange = st.selectbox('choose a exchange', ['GOOGLE', 'OPENX'], key="exchange")
code_string = st.text_area(label="Request string", key="code_string") or None
st.button(label="Generate", on_click=submit_data)




