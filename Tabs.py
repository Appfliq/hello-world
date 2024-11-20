import streamlit as st

# Create tabs
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

# Content for the first tab
with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

# Content for the second tab
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

# Content for the third tab
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
