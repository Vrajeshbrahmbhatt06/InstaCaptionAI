import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
# import os
# from dotenv import load_dotenv, find_dotenv

# load_dotenv(find_dotenv(), override=True)
api_key = st.secrets["GOOGLE_API_KEY"]
st.title('Instagram Caption Generator')

llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro', temperature=0, max_output_tokens=None, api_key= api_key)

lang = st.selectbox("Select Language:", ['english(default)', 'French'])

scene = st.text_input('Explain the scenario for which you want the caption: ')

captions = st.selectbox('Select Number of Alternatives you want: ', [1, 2, 3, 4, 5])

tone = st.selectbox("Select Tone:", ['Creative', 'Humorous', 'Funny', 'Humorous and funny', 'Conversational', 'genZ language'])

length = st.selectbox('Select caption Type:', ['Story caption (short)', 'Post caption (Short)', 'Story caption (long)', 'Post caption (long)'])


if st.button("Generate Captions"):
    if scene:
        template = PromptTemplate(
            input_variables=["language", "totalCaptions", "scenario", "captionTone", "captionLength"],
            template= "I want {totalCaptions} alternative caption(s) for the following scenario: \"{scenario}\" in {language} language, and the tone should be {captionTone} and the caption length should be Instagram {captionLength} size"
        )
        
        #format the prompt
        formatted_prompt = template.format(
            totalCaptions = captions,
            scenario=scene,
            language=lang,
            captionTone=tone,
            captionLength=length
        )
        
        message = [
            (
                'system',
                'You are a helpful assitant that helps people generate their instagram story and post captions'
            ),
            (
                'human', formatted_prompt
            )
        ]
        genCaption = llm.invoke(message)
        
        st.write('Generated Captions: ')
        st.write(genCaption.content)
    else:
        st.warning("Please enter a scenario to generate captions.")