import os
import streamlit as st
from pytube import YouTube

def download_video(url, itag):
    video = YouTube(url)

    st.write("Title:", video.title)
    st.write("Author:", video.author)

    itag = int(itag)
    stream = video.streams.get_by_itag(itag)

    if stream is not None:
        st.write("\nDownloading video...")
        download_path = os.path.join(os.path.expanduser("~"), "Downloads")
        filename = f"{video.title}.mp4"
        file_path = os.path.join(download_path, filename)
        stream.download(output_path=download_path, filename=filename)
        st.write("Video downloaded successfully!")
        st.write("File saved at:", file_path)
    else:
        st.write("Invalid itag.")

# Create the web-based interface using Streamlit
def main():
    st.title("Nkuku Down-loader")

    # URL input
    url = st.text_input("YouTube URL")

    # Available quality input
    itag = st.text_input("Video Quality (itag)")

    # Download button
    if st.button("Download"):
        if url and itag:
            download_video(url, itag)
        else:
            st.write("Please provide URL and Video Quality (itag).")

# Run the web-based interface
if __name__ == "__main__":
    main()
