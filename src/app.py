import streamlit as st


def submit_data(proto,str_):
    print(f"protocol is {proto}")
    print(str_)
    if proto == None or str_ == None:
        st.error("---------")

st.title("bidify 🛩️")
st.subheader("Bid simulator")
st.write("Generate bid request in google/openrtb protocol :)")

protocol = st.radio("Protocol:", ['Google', 'Openrtb'])
code_string = st.text_area(label="Request string") or None
st.button(label="Generate", on_click=submit_data(protocol, code_string))