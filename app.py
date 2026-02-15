import pandas as pd
import streamlit as st
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("fondzombie.css")

st.write("Hello World, Bienvenue sur Streamlit ! ")
st.title("🧟 ZOMBIE APOCALYPSE SURVIVAL GUIDE 🩸")
st.markdown("## ⚠️ THE OUTBREAK HAS BEGUN...")
st.error("🚨 WARNING: Infection spreading rapidly. Survival chances decreasing...")
st.header("1. Find a safe shelter")
st.subheader("Your shelter is your safe haven during a zombie apocalypse. It should provide protection from zombies and other dangers, as well as a place to rest and store supplies.") 
st.text("during a zombie apocalypse. It should provide protection from zombies and other dangers, as well as a place to rest and store supplies.") 
st.markdown(''':rainbow: :rainbow[ZOMBIE APOCALYPSE SURVIVAL GUIDE] :rainbow: ''')

st.markdown('''- Look for a secure location with strong doors and windows. Avoid places that are easily accessible to zombies, such as abandoned buildings or areas with high foot traffic. Consider fortifying your shelter with barricades and traps to keep zombies out.''')
st.write(
    pd.DataFrame({
        "Step": ["1. Find a safe shelter", "2. Gather supplies", "3. Stay informed", "4. Stay healthy", "5. Stay calm"],
        "Description": ["Look for a secure location with strong doors and windows. Avoid places that are easily accessible to zombies, such as abandoned buildings or areas with high foot traffic. Consider fortifying your shelter with barricades and traps to keep zombies out.", "Stock up on food, water, and medical supplies. You will need enough supplies to last for an extended period of time.", "Stay updated on the latest news and developments in your area. Listen to local radio stations and follow official social media accounts for updates.", "Maintain good hygiene and take care of your physical and mental health. Exercise regularly, eat healthy foods, and get enough sleep.", "Stay calm and avoid panic. Keep a positive attitude and focus on survival strategies."]
    })
)
st.checkbox(label = "I have read and understood the survival guide.")
st.write("Thank you for reading the Zombie Apocalypse Survival Guide. Stay safe and good luck!")
st.radio("Do you feel prepared for a zombie apocalypse?", ("Yes", "No", "Maybe"))
st.write("Remember, the key to surviving a zombie apocalypse is to stay calm, stay informed, and be prepared. With the right mindset and resources, you can increase your chances of survival. Stay safe out there!")
st.toggle("Do you want to receive updates on the latest zombie apocalypse news?", True)
st.write("Thank you for your interest in staying informed about the latest zombie apocalypse news. We will keep you updated with the latest developments and information to help you stay prepared. Stay safe!")
st.selectbox("Choose your preferred method of communication for receiving updates:", ("Email", "SMS", "Push Notifications"))
st.write("Thank you for choosing your preferred method of communication. We will use this method to send you updates on the latest zombie apocalypse news. Stay safe and stay informed!")
st.multiselect("Select the types of updates you would like to receive:", ("News", "Survival Tips", "Emergency Alerts", "Community Events"))
st.write("Thank you for selecting the types of updates you would like to receive. We will send you updates on the latest news, survival tips, emergency alerts, and community events related to the zombie apocalypse. Stay safe and stay informed!")
st.select_slider("On a scale of 1 to 10, how prepared do you feel for a zombie apocalypse?", options=range(1, 11))
st.write("Thank you for sharing your level of preparedness. Remember, it's important to take steps to increase your preparedness for a zombie apocalypse. Consider creating a survival plan, gathering supplies, and staying informed to increase your chances of survival. Stay safe!")
st.text_input("Enter your name to receive personalized survival tips:")
st.text_area("Enter any specific concerns or questions you have about surviving a zombie apocalypse:")
st.write("Thank you for entering your name. We will send you personalized survival tips to help you prepare for a zombie apocalypse. Stay safe and stay informed!")
st.number_input("How many days' worth of supplies do you currently have?", min_value=0, max_value=365, step=1)
confidence = st.slider(
    "On a scale of 1 to 10, how confident do you feel in your ability to survive a zombie apocalypse?",
    min_value=1,
    max_value=10,
    value=5  # valeur par défaut
)

st.write("Your confidence level:", confidence)

st.write("Thank you for sharing the number of days' worth of supplies you currently have. Remember, it's important to have enough supplies to last for an extended period of time during a zombie apocalypse. Consider stockpiling food, water, and medical supplies to increase your chances of survival. Stay safe!")
st.date_input("Select the date you would like to start your zombie apocalypse preparedness plan:")
st.time_input("Select the time you would like to start your zombie apocalypse preparedness plan:")
st.write("Thank you for selecting the date and time to start your zombie apocalypse preparedness plan. Remember, it's important to have a plan in place and to take action to increase your preparedness. Consider creating a checklist of tasks to complete and setting reminders to stay on track. Stay safe and stay prepared!")
st.text("Remember, the key to surviving a zombie apocalypse is to stay calm, stay informed, and be prepared. With the right mindset and resources, you can increase your chances of survival. Stay safe out there!")
task1 = st.checkbox("Create a survival plan")
task2 = st.checkbox("Gather supplies")
task3 = st.checkbox("Stay informed")
task4 = st.checkbox("Maintain good hygiene")
task5 = st.checkbox("Exercise regularly")
st.write("\n\n")

if task1 and task2 and task3:
    st.success("Great job! You are on your way to being prepared for a zombie apocalypse. Keep up the good work and stay safe!")
elif task1 and task2:
    st.warning("You're making progress, but don't forget to stay informed about the latest developments in your area. Stay safe!")
elif task1 and task3:
    st.warning("You're making progress, but don't forget to gather supplies to ensure you have enough resources to survive. Stay safe!")
elif task2 and task3:
    st.warning("You're making progress, but don't forget to create a survival plan to increase your chances of survival. Stay safe!")
else:
    st.error("It looks like you still have some work to do to prepare for a zombie apocalypse. Consider creating a survival plan, gathering supplies, and staying informed to increase your chances of survival. Stay safe!")
st.subheader("Zombie Apocalypse Training Video 🧟‍♂️")

st.video("https://www.youtube.com/watch?v=C7YxUh34bVs")
st.markdown("""
<audio autoplay loop>
  <source src="https://www.fesliyanstudios.com/play-mp3/4386" type="audio/mpeg">
</audio>
""", unsafe_allow_html=True)


