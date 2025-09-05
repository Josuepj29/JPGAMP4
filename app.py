import streamlit as st
from moviepy.editor import ImageClip

st.title("🖼️ JPG → 🎬 MP4 Converter")

uploaded_file = st.file_uploader("Sube una imagen JPG", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("🎬 Generando tu video... espera un momento..."):
        clip = ImageClip("temp.jpg", duration=60)
        clip = clip.set_fps(24)

        output_file = "output.mp4"
        clip.write_videofile(output_file, codec="libx264", audio=False)

    with open(output_file, "rb") as f:
        st.download_button(
            label="⬇️ Descargar MP4",
            data=f,
            file_name="video.mp4",
            mime="video/mp4"
        )
