import streamlit as st
from pytube import YouTube

def download_video(url, itag, output_path):
    video = YouTube(url)

    st.write("Title:", video.title)
    st.write("Author:", video.author)

    st.write("\nAvailable Streams:")
    for stream in video.streams:
        st.write(stream)

    itag = int(itag)
    stream = video.streams.get_by_itag(itag)

    if stream is not None:
        st.write("\nDownloading video...")
        stream.download(output_path=output_path)
        st.write("Video downloaded successfully!")
    else:
        st.write("Invalid itag.")

# Create the web-based interface using Streamlit
def main():
    st.title("Nkuku Down-loader")

    # URL input
    url = st.text_input("YouTube URL")

    # Available quality input
    itag = st.text_input("Video Quality (itag)")

    # Output directory input
    output_path = st.text_input("Output Directory")

    # Download button
    if st.button("Download"):
        if url and itag and output_path:
            download_video(url, itag, output_path)
        else:
            st.write("Please provide URL, Video Quality (itag), and Output Directory.")

# Run the web-based interface
if __name__ == "__main__":
    main()

