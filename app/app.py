import streamlit as st

def main():
    info = st.Page('info.py', title='Home', icon='🏠')
    generate = st.Page('generate.py', title='Caption Generator', icon='📃')
    pages = st.navigation([info, generate])
    pages.run()
    
if __name__ == '__main__':
    main()