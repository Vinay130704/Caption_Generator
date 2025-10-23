import streamlit as st

def info_page():
    st.title("How to Use the App")
    st.write("""
        This app generates a caption for an uploaded image.
        
        **Steps**:
        1. Navigate to the **Caption Generator** page via the sidebar.
        2. Upload an image using the **Browse files** button.
        3. Select the number of captions and the creativity of the captions using the sliders.
        4. The caption(s) will be generated and displayed below the image.
        5. The generation can take some time so your patience is appreciated.
             
        This Interactive Application Is Developed By Vinay Kumar
    """)

if __name__ == '__page__':
    info_page()
