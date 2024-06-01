import streamlit as st
import pickle
df=pickle.load(open('dataframe.pkl','rb'))
pipe=pickle.load(open('pipe_model.pkl','rb'))

st.title("Laptop Price Predictor App")
st.write("This app work on the Machine Learning model, created from a small sample of real-world data")
company=st.selectbox("Select the Manufacturer of the laptop",df['Company'].unique())
typename=st.selectbox("Select the type of the Laptop",df['TypeName'].unique())
cpu=st.selectbox("Processor Name",df['Cpu'].unique())
ram=st.selectbox("Amount of RAM on the system",[4,8,12,16,24,32,64,128])
gpu=st.selectbox("Graphics Card",df['Gpu'].unique())
os=st.selectbox("Operating System",df['OpSys'].unique())
