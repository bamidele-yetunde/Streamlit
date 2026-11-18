import streamlit as st


contact = st.Page(page='pages/contact.py', title='Contact')
about = st.Page(page='pages/about.py', title='About')
home = st.Page(page='pages/home.py', title='Home')


pg = st.navigation({
    'Home' : [home],
    'pages' : [contact, about]
})


pg.run()    



