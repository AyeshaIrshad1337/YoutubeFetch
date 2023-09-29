import streamlit as st
import pytube as py
import os

# Set page configuration
st.set_page_config(
    page_title="YouTube Video Downloader",
    page_icon=":clapper:",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS
custom_css = """
<style>
[data-testid="stAppViewContainer"]{
background-color: #f7f6f2;
color: #2b87a4;
font-family: "sans-serif";
font-size:65px;
}
[data-testid="stButton"],[data-testid="stDownloadButton"] :active, :visited{

color: #2b87a4;
border-color: #2b87a4;
}

[data-testid="stButton"] :hover{
background-color: #1d4c52;
color: white;
border-color:white;
}
[data-testID="stHeader"]{
background-color:rgba(0,0,0,0);
}
[data-testid="stDownloadButton"] :hover{
background-color: #1d4c52;
color: white;
border-color:white;
}
[data-testid="stTextInput"] p{
color: #2b87a4;
font-family: "sans-serif";
font-size: 25px;
font-weight:bold;
}
[data-testid="stWidgetLabel"] p{
color: #2b87a4;
font-family: "sans-serif";
font-size: 25px;
font-weight:bold;
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)
st.image("logo.png")
# Get the YouTube link from the user
# st.text("Enter The Youtube Video link: ")
youtube_link = st.text_input("Enter The Youtube Video link:", key="youtubelink")

# Get the video resolution from the user
# st.text("Select Video Resolution: ")
video_resolution = st.selectbox("Select Video Resolution:", ["360p", "720p","1080"], key="resolution")

# Button to process the YouTube link
if st.button("Process Video"):
    if youtube_link:
        # Create a YouTube object
        video_instance = py.YouTube(youtube_link)

        # Get the stream with the selected resolution
        stream = video_instance.streams.filter(res=video_resolution).first()

        if stream is None:
            st.write(f"No video found with resolution {video_resolution}")
        else:
            # Download the video (this will download the video to the server running Streamlit)
            filename = stream.download()

            # Check if the file exists (download was successful)
            if os.path.isfile(filename):
                # Get the actual name of the file without OS path
                actual_filename = os.path.basename(filename)

                # Read file data
                with open(filename, "rb") as f:
                    bytes = f.read()

                # Provide a button for the user to download the video file
                st.download_button(
                    label="Download Video",
                    data=bytes,
                    file_name=actual_filename,
                    mime='video/mp4'
        
                )

            st.video(youtube_link)
