
import time
import streamlit as st


# Get current hour, minute, and second
current_hour = int(time.strftime("%H"))
current_minute = int(time.strftime("%M"))
current_second = int(time.strftime("%S"))
current_time = f"{current_hour}:{current_minute}:{current_second}"
# Determine greeting based on the hour
def get_greeting(hour):
    if hour < 12:
        return "Good Morning"
    elif 12 <= hour < 16:
        return "Good Afternoon"
    elif 16 <= hour < 20:
        return "Good Evening"
    else:
        return "Good Night"

# Example usage
greeting = get_greeting(current_hour)
print(f"{greeting}, the time is {current_hour}:{current_minute}:{current_second}")


# App application
st.title("Real-Time Greeting Identification Tool")

# Display an image
st.markdown(
    r"![Real-Time Greeting Identification Tool](https://e7.pngegg.com/pngimages/300/655/png-clipart-cuckoo-clock-black-forest-pendulum-clock-alarm-clock-retro-alarm-clock-electronics-painted-thumbnail.png)", 
    unsafe_allow_html=True
)

# Set a button to show greetings
st.write("Real Time :",current_time)
if st.button("Greetings"):
    greeting = get_greeting(current_hour)
    # Display the greeting and current time in large, bold font
    st.markdown(f"<h1 style='color: black; font-size: 50px; font-weight: bold;'>{greeting}</h1>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='color: gray; font-size: 30px;'>Current Time: {current_hour}:{current_minute}:{current_second}</h2>", unsafe_allow_html=True)


st.write("Have a nice day!")

