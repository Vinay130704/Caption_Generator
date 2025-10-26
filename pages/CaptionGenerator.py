# streamlit: page_title=Caption Generator, page_icon=📃
import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

processor = BlipProcessor.from_pretrained('Salesforce/blip-image-captioning-base')
model = BlipForConditionalGeneration.from_pretrained('Salesforce/blip-image-captioning-base')

st.title('Caption Generator')
img_path = st.file_uploader(label='Image', type=['png', 'jpg', 'jpeg'])

num_return_sequences = st.slider(
    "Number of Captions", min_value=1, max_value=5, value=1, step=1,
    help="Select how many captions you want to generate (1-5)"
)
temperature = st.slider(
    "Creativity (Temperature)", min_value=0.7, max_value=1.3, value=1.0, step=0.1,
    help="Select the creativity of the generated captions (0.7-1.3), higher the value, higher the creativity"
)

if img_path is not None:
    st.image(img_path, caption='Uploaded Image')
    image = Image.open(img_path).convert('RGB')

    inputs = processor(image, return_tensors='pt')
    outputs = model.generate(
        **inputs,
        num_return_sequences=num_return_sequences,
        temperature=temperature,
        do_sample=True,
        top_p=0.9,
        repetition_penalty=1.2
    )

    captions = [processor.decode(output, skip_special_tokens=True) for output in outputs]
    st.write('Generated Caption(s):')
    for idx, caption in enumerate(captions, 1):
        st.write(f'Caption {idx}: {caption}')
