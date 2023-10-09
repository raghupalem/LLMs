import streamlit as st
import os

from dotenv import load_dotenv
 
 
 
def get_pdf_text(pdf_docs):
    
    
    
    
def main():
    load_dotenv()
    st.set_page_config(page_title='Chat with pdf files', page_icon=":books:")
    st.header('Chat with multiple pdfs')

    with st.sidebar:
        st.subheader('Your documnets')
        pdf_docs = st.file_uploader('Upload your pdf here', accept_multiple_files=True)
        if st.button('Process'):
            with st.spinner('Processing'):
                # get pdf text
                raw_text = get_pdf_text(pdf_docs)
            

if __name__ == '__main__':
    main()
