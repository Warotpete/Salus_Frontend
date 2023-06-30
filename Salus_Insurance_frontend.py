import streamlit as st
import joblib

def main():
    html_temp = """
    <div style="background-color:#1CAE81;padding: 16px">
    <h2 style="color:white";text-align:center> Salus Insurance's Cost Determiner </h2>
    </div>
    
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    model = joblib.load('model_joblib_Rf')
    
    p1 = st.slider('Enter Your Age', 18, 100)
    
    s1 = st.selectbox('Sex',('Male','Female'))
    
    if s1=='Male':
        p2=0
    else:
        p2=1
    
    s2 = st.number_input('Enter Your Height (cm)')
    s3 = st.number_input('Enter your weight (kg)')
    if s2 != 0:
        p3 = (s3*10000) / (s2 ** 2)
    else:
        p3 = 0
        
        
    s4 = st.selectbox("Smoker", ("Yes", "No"))
    if s4=='Yes':
        p4=0
    else:
        p4=1
    
    s5 = st.selectbox('Enter your Region',('Southeast','Southwest','Northeast','Northwest'))
    
    if s5=='Southeast':
        p5=0
    elif s5=='Southwest':
        p5=1
    elif s5=='Northeast':
        p5=2
    elif s5=='Northwest':
        p5=3
    
    p6 = st.slider("Enter Number of Children", 0,5)
    
    if st.button('Predict'):
        pred = model.predict([[p1,p2,p3,p4,p5,p6]])
    
        st.success('Your Insurance Cost is {} THB/year'.format(round(pred[0])))

        printf("suggestions\n")

        if p3 >= 35:
            printf("You are fucking obese")
        elif (p3 < 35) and (p3 >= 30):
            printf("You are obese")
        elif (p3 < 30) and (p3 >= 25):
            printf("You are obese")
        elif (p3 < 25) and (p3 >= 18.5):
            printf("You are normal")
        else:
            printf("You need to eat more bro")
        
        
if __name__ == '__main__':
    main()

