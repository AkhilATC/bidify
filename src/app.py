import streamlit as st
from bid_parser import parse


def submit_data(proto,str_):
    print(f"protocol is {proto}")
    print(str_)
    resp = parse(proto,str_)
    if resp:
        st.success(resp)
    else:
        st.error(f"Failed to fetch...:) error = {resp[1]}")


st.title("bidify 🛩️")
st.subheader("Bid simulator")
st.write("Generate bid request in google/openrtb protocol :)")

protocol = st.radio("Protocol:", ['Google', 'Openrtb'])
code_string = st.text_area(label="Request string") or None
st.button(label="Generate", on_click=submit_data(protocol, code_string))
