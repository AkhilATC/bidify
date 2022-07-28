import streamlit as st
from bid_parser import parse


def submit_data():
    # print("--submit--")
    vals = list(filter(None, [x for x in st.session_state.values()]))
    # print(len(vals))
    if len(vals) == 3:
        proto = st.session_state['protocol']
        exchange = st.session_state['exchange']
        stream = st.session_state['code_string']
        resp = parse(proto, stream)
        st.session_state['exp_1_message'] = resp
        # st.session_state.clear()
        pop_items = [st.session_state.pop(k) for k in ['protocol', 'exchange', 'code_string']]
        # print(st.session_state)


def init_app():
    st.title("bidify 🛩️")
    st.subheader("Bid simulator")
    st.write("Generate bid request in google/openrtb protocol :)")
    exp_1 = st.expander(label="Generate bidRequest")
    exp_1.radio("Protocol:", ['Google', 'Openrtb'], key="protocol")
    exp_1.selectbox('choose a exchange', ['GOOGLE', 'OPENX'], key="exchange")
    exp_1.text_area(label="Request string", key="code_string")
    exp_1.button(label="SEND", on_click=submit_data)
    exp_1.write(st.session_state.get("exp_1_message", "Set your bid to fly with bidify... 🎉🎉🎉"))
    exp_2 = st.expander(label="Construct your bidRequest")
    exp_2.write("Work in progress 🚧 (bidify:v.1)")


if __name__ == '__main__':
    st.set_page_config(
        page_title="bidify 🛩️"
    )
    init_app()

