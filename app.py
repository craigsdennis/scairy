import os
import glob

import streamlit as st
from elevenlabs import generate, save

from utils import answer_image_question, generate_greeting, generate_video


"""# scAIry

You think AI is scary? Wait till you see `scAIry` 👻
"""

@st.cache_resource
def get_image_list():
    return sorted(glob.glob(os.path.join("data", "photos", "*")))


images = get_image_list()

image_index = st.slider(
    "🎃 Choose your trick-or-treater", min_value=0, max_value=len(images) - 1
)
st.image(images[image_index])
with st.form("kiddos"):
    submitted = st.form_submit_button("Choose")
    if submitted:
        summary = answer_image_question(
            images[image_index], 
            "List each costume you can detect in the photo."
        )
        "## Summary of trick or treaters"
        st.write(summary)
        st.session_state["costume_summary"] = summary

if "costume_summary" in st.session_state:
    GREETERS = {
        "freddy_krueger": {
            "name": "Freddy Krueger",
            "voice_id": "0fTYMUuqMxZoSywLwS0b",
            "image": "freddy.jpg"
        },
        "chucky": {
            "name": "Chucky",
            "voice_id": "zJSt7YEaVvvPws74ziWG",
            "image": "chucky.jpg"
        }
    }

    def get_greeter_name(val):
        return GREETERS[val]["name"]

    with st.form("greeting"):
        greeter_key = st.selectbox(
            "Choose a scary greeter",
            options=GREETERS.keys(),
            format_func=get_greeter_name,
        )
        greeter = GREETERS[greeter_key]
        submitted = st.form_submit_button("Generate")
        if submitted:
            "## Scary Greeting"
            with st.spinner("Generating greeting..."):
                greeting = generate_greeting(
                    greeter["name"], st.session_state["costume_summary"]
                )
                st.write(greeting)

            with st.spinner("Generating audio..."):
                response = generate(greeting, voice=greeter["voice_id"])
                file_name = f"{greeter_key}-{image_index}.wav"
                file_path = os.path.join("data", "audio", file_name)
                save(response, file_path)
                st.audio(file_path)
                st.session_state["generated_audio"] = file_path

if "generated_audio" in st.session_state:
    greeter_image = os.path.join("data", "greeters", greeter["image"])
    st.image(greeter_image, greeter["name"])
    # This takes a bit
    with st.spinner("Generating video..."):
        output = generate_video(
            greeter_image, 
            st.session_state["generated_audio"]
        )
        print(output)
        st.video(output)

