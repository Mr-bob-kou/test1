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


danger2=st.radio("Is this Heritage in Danger?",["Yes","No"])
if danger2 =="Yes":
    st.write("Coco")
else:
    st.write("lol")
          
