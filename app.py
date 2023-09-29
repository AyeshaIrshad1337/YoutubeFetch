import streamlit as st
import pytube as py
import base64
import os

# Set page configuration
st.set_page_config(
    page_title="YouTube Video Downloader",
    page_icon=":clapper:",
    layout="centered",
    initial_sidebar_state="expanded",
)

[theme]
primaryColor = "#f7f6f2"
backgroundColor = "#0f1201"
secondaryBackgroundColor = "#1d4c52"
textColor = "#2b87a4"
font = "sans-serif"

# Custom CSS
custom_css = f"""
<style>
body {{
background-color: {backgroundColor};
color: {textColor};
font-family: {font};
}}
.StreamlitApp .stButton > button {{
color: {textColor};
background-color: {secondaryBackgroundColor};
}}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# Get the YouTube link from the user
youtube_link = st.text_input("Youtube Video Link: ", key="youtubelink")

# Button to process the YouTube link
if st.button("Process Video"):
    if youtube_link:
        # Create a YouTube object
        video_instance = py.YouTube(youtube_link)

        # Get the highest resolution stream
        stream = video_instance.streams.get_highest_resolution()

        # Display the video
        st.video(youtube_link)

        # Download the video (this will download the video to the server running Streamlit)
        filename = stream.download()

        # Check if the file exists (download was successful)
        if os.path.isfile(filename):
            # Get the actual name of the file without OS path
            actual_filename = os.path.basename(filename)

            # Read file data
            with open(filename, "rb") as f:
                bytes = f.read()
                b64 = base64.b64encode(bytes).decode()

            # Provide a link for the user to download the video file
            href = f'<a href="data:file/mp4;base64,{b64}" download="{actual_filename}">Click here to download</a>'
            st.markdown(href, unsafe_allow_html=True)
