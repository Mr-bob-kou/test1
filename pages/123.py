import streamlit as st

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)

if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")

danger = st.radio("Is this Heritage in Danger?", ["Yes", "No"])

# 根據用戶的選擇顯示不同的文字
if danger == "Yes":
    st.write("Coco")
else:
    st.write("lol")


danger2=st.radio("Is this Heritage in Danger?",["Yes","No"],key="danger2")
if danger2 =="Yes":
    st.write("Coco")
else:
    st.write("lol")
          
modal = Modal(
    "Demo Modal", 
    key="demo-modal",
    
    # Optional
    padding=20,    # default value
    max_width=744  # default value
)

open_modal = st.button("Open")
if open_modal:
    modal.open()

if modal.is_open():
    with modal.container():
        st.write("Text goes here")

        st.write("Some fancy text")
        value = st.checkbox("Check me")
        st.write(f"Checkbox checked: {value}")
