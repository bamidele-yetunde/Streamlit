import streamlit as st

new_chat = st.Page(page="Gemini/new_chat.py", title="New chat")
library = st.Page(page="Gemini/library.py", title="Library")
images = st.Page(page="Gemini/images.py", title="Images")
schedule = st.Page(page="Gemini/schedule.py", title="Schedule")
customize = st.Page(page="Gemini/customize.py", title="Customize")
video = st.Page(page="Gemini/video.py", title="Video")
new_notebook = st.Page(page="Gemini/new_notebook.py", title="New notebook")
all_page = st.Page(page="Gemini/all.py", title="All chats")

pg = st.navigation(
    [
        new_chat,
        library,
        images,
        schedule,
        customize,
        video,
        new_notebook,
        all_page,
    ],
    position="hidden",
)

with st.sidebar:
    st.page_link(new_chat)
    st.page_link(library)
    st.page_link(images)
    st.page_link(schedule)
    st.page_link(customize)
    st.page_link(video)

    with st.expander("Notebooks", expanded=False):
        st.page_link(new_notebook)

    with st.expander("All", expanded=False):
        st.page_link(all_page)

pg.run()


