import streamlit as st
from PIL import Image
import io
import base64

# Mock function to generate image variations (Replace with actual API/model)
def generate_variations(input_image=None, prompt=None):
    st.info("🔧 Generating image variations... (Mock output)")
    variations = []
    for i in range(3):
        if input_image:
            variations.append(input_image)  # Placeholder - return original image as dummy variation
        else:
            img = Image.new('RGB', (256, 256), (255 - 20*i, 200 + 10*i, 220 - 30*i))
            variations.append(img)
    return variations

# App UI
st.set_page_config(page_title="PenAI: Graphic Design Assistant", layout="wide")

st.title("🎨 PenAI - Design Variation Generator")
st.markdown("""
This tool allows you to upload a **vector/image** or enter a **text prompt**, and it will generate design variations using generative AI. Useful for logo design, UI components, icons, and more!
""")

# Input Options
tab1, tab2 = st.tabs(["📤 Upload Image", "✏️ Text Prompt"])

uploaded_image = None
prompt_text = None

with tab1:
    uploaded_file = st.file_uploader("Upload an image (PNG/SVG preferred)", type=["png", "jpg", "jpeg", "svg"])
    if uploaded_file:
        try:
            uploaded_image = Image.open(uploaded_file)
            st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
        except Exception as e:
            st.error(f"Could not process image: {e}")

with tab2:
    prompt_text = st.text_area("Describe the design or shape you want to vary (e.g., 'Minimalist flat icon of a moon')")
    if prompt_text:
        st.info(f"Prompt: **{prompt_text}**")

# Submit button
if st.button("🚀 Generate Variations"):
    if uploaded_image or prompt_text:
        results = generate_variations(input_image=uploaded_image, prompt=prompt_text)
        st.subheader("🖼️ Generated Variations")
        cols = st.columns(len(results))
        for col, img in zip(cols, results):
            col.image(img, use_column_width=True)
    else:
        st.warning("Please upload an image or enter a prompt to proceed.")

st.markdown("---")
st.caption("Built with ❤️ for the open-source design community using Penpot and Streamlit.")
