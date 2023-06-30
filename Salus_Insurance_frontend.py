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

        st.divider()
        st.header("suggestions\n")
        provide_feedback(p3,p4)
        st.divider()

        



def provide_feedback(bmi, smoking_status):
    if bmi < 18.5:
        st.text("Your BMI indicates that you are underweight.")
        if smoking_status == 0:
            st.markdown("It's important to focus on nourishing your body with a balanced and varied diet. Include lean proteins, whole grains, fruits, and vegetables in your meals. Ensure you meet your daily calorie requirements to support healthy weight gain. Engage in strength-building exercises to build muscle mass and improve your overall strength. Prioritize quality sleep of 7-9 hours each night to support your body's growth and recovery. Consider quitting smoking to improve overall health. (Website: https://www.smokefree.gov) For additional information, you can visit: (Website: https://www.nhs.uk/live-well/healthy-weight/advice-for-underweight-adults/)")
        else:
            st.text("It's important to focus on nourishing your body with a balanced and varied diet.")
            st.text("Include lean proteins, whole grains, fruits, and vegetables in your meals.")
            st.text("Ensure you meet your daily calorie requirements to support healthy weight gain.")
            st.text("Engage in strength-building exercises to build muscle mass and improve your overall strength.")
            st.text("Prioritize quality sleep of 7-9 hours each night to support your body's growth and recovery.")
            st.markdown("For additional information, you can visit: (Website: https://www.nhs.uk/live-well/healthy-weight/advice-for-underweight-adults/)")
    elif bmi >= 18.5 and bmi < 25:
        st.text("Your BMI is within the normal range.")
        if smoking_status == 0:
            st.text("It's important to continue maintaining a balanced diet with a variety of nutritious foods.")
            st.text("Focus on portion control and listen to your body's hunger and fullness cues.")
            st.text("Engage in regular physical activity that you enjoy, aiming for at least 150 minutes per week.")
            st.text("Include a mix of cardiovascular exercises, strength training, and flexibility exercises in your routine.")
            st.text("Make sure to prioritize a consistent sleep schedule, aiming for 7-9 hours of sleep each night.")
            st.markdown("Consider quitting smoking to further improve your overall health and well-being. (Website: https://www.smokefree.gov)")
            st.markdown("For additional information, you can visit: (Website: https://www.nhs.uk/live-well/healthy-weight/advice-for-adults-with-a-healthy-weight/)")
        else:
            st.text("It's important to continue maintaining a balanced diet with a variety of nutritious foods.")
            st.text("Focus on portion control and listen to your body's hunger and fullness cues.")
            st.text("Engage in regular physical activity that you enjoy, aiming for at least 150 minutes per week.")
            st.text("Include a mix of cardiovascular exercises, strength training, and flexibility exercises in your routine.")
            st.text("Make sure to prioritize a consistent sleep schedule, aiming for 7-9 hours of sleep each night.")
            st.markdown("For additional information, you can visit: (Website: https://www.nhs.uk/live-well/healthy-weight/advice-for-adults-with-a-healthy-weight/)")
    elif bmi >= 25 and bmi < 30:
        st.text("Your BMI indicates that you are overweight.")
        if smoking_status == 0:
            st.text("It's important to adopt a healthy eating plan that focuses on whole, unprocessed foods.")
            st.text("Practice portion control and be mindful of your calorie intake.")
            st.text("Engage in regular physical activity for at least 150 minutes per week to support weight management.")
            st.text("Incorporate both cardiovascular exercises and strength training into your routine.")
            st.text("Prioritize quality sleep of 7-9 hours each night to support your body's recovery.")
            st.markdown("Consider quitting smoking to improve overall health. (Website: https://www.smokefree.gov)")
            st.text("For additional information, you can visit:")
            st.markdown("(Website: https://www.nhs.uk/live-well/healthy-weight/advice-for-adults-with-an-overweight/)")
        else:
            st.text("It's important to adopt a healthy eating plan that focuses on whole, unprocessed foods.")
            st.text("Practice portion control and be mindful of your calorie intake.")
            st.text("Engage in regular physical activity for at least 150 minutes per week to support weight management.")
            st.text("Incorporate both cardiovascular exercises and strength training into your routine.")
            st.text("Prioritize quality sleep of 7-9 hours each night to support your body's recovery.")
            st.text("For additional information, you can visit:")
            st.markdown("(Website: https://www.nhs.uk/live-well/healthy-weight/advice-for-adults-with-an-overweight/)")
    else:
        st.text("Your BMI indicates that you are obese.")
        if smoking_status == 0:
            st.text("It's important to adopt a healthy eating plan that focuses on whole, unprocessed foods.")
            st.text("Practice portion control and be mindful of your calorie intake.")
            st.text("Engage in regular physical activity for at least 150 minutes per week to support weight management.")
            st.text("Incorporate both cardiovascular exercises and strength training into your routine.")
            st.text("Prioritize quality sleep of 7-9 hours each night to support your body's recovery.")
            st.markdown("Consider quitting smoking to improve overall health. (Website: https://www.smokefree.gov)")
            st.text("For additional information, you can visit:")
            st.markdown("(Website: https://www.nhs.uk/live-well/healthy-weight/advice-for-adults-with-obesity/)")
        else:
            st.text("It's important to adopt a healthy eating plan that focuses on whole, unprocessed foods.")
            st.text("Practice portion control and be mindful of your calorie intake.")
            st.text("Engage in regular physical activity for at least 150 minutes per week to support weight management.")
            st.text("Incorporate both cardiovascular exercises and strength training into your routine.")
            st.text("Prioritize quality sleep of 7-9 hours each night to support your body's recovery.")
            st.markdown("For additional information, you can visit:")
            st.markdown("(Website: https://www.nhs.uk/live-well/healthy-weight/advice-for-adults-with-obesity/)")

        
        
if __name__ == '__main__':
    main()

