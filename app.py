import streamlit as st

st.title('My Streamlit App',anchor= False) 

# Input element


name = st.text_input('What is your name?', placeholder='Type your name.....')
number = st.number_input('Enter a number: ', min_value=0, max_value= 100, step=1, disabled=True, help = 'please enter a number betweeen 0 and 100')
radio_option = st.radio('Choose an option:', options=['Option 1',  'Option 3', 'Option 3'], index = 0, horizontal = True)
date = st.date_input('Select a date:', help='Please select date from the calender')
time = st.time_input('Select a time', help='Please select time')
color = st.color_picker('Pick a color:', value= '#00f900', help = 'Please help pick a color.')
checkbox  = st.checkbox('Check this box iif you agree.', value= False, help= 'Please check the box if you agree')
char = st.text_area('Enter some text', placeholder='Type your text here...', help= 'Please enter some text')
chatbox = st.chat_input('Ask  me anything')
file =  st.file_uploader('Upload a file', type= ['jpg','png','pdf'], help="Please upload file in JPG,PNG, or PDF format")
video= st.video('https://www.youtube.com/watch?v=ikJqntMaMfs', format='video/mp4', start_time=0)
image = st.image('https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcRHjX58Mo3wTEVaFAlabYgfSOsWwquaLPe-EIZCoK5x9FHUWgXyxggi7o84wl5AaNiBuSERf_nA4YdLF63e5KRzy4BLQtNBM7mVU5CbFoM&usqp=CAc', caption='sample image',output_format='auto')





options = st.multiselect(
    "What are your favorite colors?",
    ["Green", "Yellow", "Red", "Blue"],
    default=["Yellow", "Red"],
)

st.link_button("Go to gallery", "https://streamlit.io/gallery")




sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"You selected: {sentiment_mapping[selected]}")




options = ["North", "East", "South", "West"]
selection = st.pills("Directions", options, selection_mode="multi")
st.markdown(f"Your selected options: {selection}.")





color = st.select_slider(
    "Select a color of the rainbow",
    options=[
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet",
    ],
)
st.write("My favorite color is", color)




option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

st.write("You selected:", option)





on = st.toggle("Activate feature")

if on:
    st.write("Feature activated!")




age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, "years old")





st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")




@st.fragment(key="charts")
def charts():
    st.line_chart({"data": [1, 2, 3]})

charts()
st.button(
    "Refresh charts",
    on_click=lambda: st.rerun("charts"),
)









