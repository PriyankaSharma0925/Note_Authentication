#import numpy
import numpy as np
import pandas as pd
import pickle
import streamlit as st
#from PIL import Image


classifier=pickle.load(open('Note_Authentication.pkl','rb'))


def welcome():
    return "Welcome"


def predict_note_authentication(variance,skewness,curtosis,entropy):
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    return "The predicted value is"+ str(prediction)



def main():
    st.title("Bank Note Authentication")
    html_temp="""
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">StreamLit Bank Authentication App</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance=int(float(st.text_input("Variance","Type here")))
    skewness = int(float(st.text_input("Skewness", "Type here")))
    curtosis = int(float(st.text_input("Curtosis", "Type here")))
    entropy = int(float(st.text_input("Entropy", "Type here")))
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
        st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Build with StreamLit")






if __name__ == '__main__':
    main()
