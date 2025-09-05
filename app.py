import streamlit as st
from moviepy.editor import ImageSequenceClip
import tempfile
import os

st.title("🖼️➡️🎬 JPG a MP4")

# Subir varias imágenes
imagenes = st.file_uploader(
    "Sube tus imágenes JPG",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

fps = st.slider("Fotogramas por segundo (FPS)", 1, 60, 24)

if st.button("Crear video"):
    if not imagenes:
        st.warning("⚠️ Sube al menos una imagen primero.")
    else:
        # Guardar las imágenes temporalmente
        temp_dir = tempfile.mkdtemp()
        rutas = []
        for i, img in enumerate(imagenes):
            ruta = os.path.join(temp_dir, f"frame_{i:03d}.jpg")
            with open(ruta, "wb") as f:
                f.write(img.read())
            rutas.append(ruta)

        # Crear el video
        clip = ImageSequenceClip(rutas, fps=fps)
        video_path = os.path.join(temp_dir, "output.mp4")
        clip.write_videofile(video_path, codec="libx264")

        # Mostrar el video en la app
        st.video(video_path)

        # Botón de descarga
        with open(video_path, "rb") as f:
            st.download_button("📥 Descargar MP4", f, file_name="video.mp4")
