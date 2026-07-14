import streamlit as st
from streamlit_option_menu import option_menu

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Neetu Sahu Portfolio",
    page_icon="👩‍💻",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    /* Global Background */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: #ffffff;
    }

    /* Glassmorphism Project Cards */
    .project-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.1);
        padding: 25px;
        border-radius: 20px;
        margin-bottom: 25px;
        transition: transform 0.3s ease;
    }

    .project-card:hover {
        transform: translateY(-5px);
        border: 1px solid #ff4b4b;
        background: rgba(255,255,255,0.08);
    }

    /* Skill Tags */
    .skill-tag {
        display: inline-block;
        padding: 6px 15px;
        margin: 4px;
        border-radius: 50px;
        background: rgba(255,75,75,0.2);
        border: 1px solid #ff4b4b;
        font-size: 14px;
        font-weight: 500;
    }

    /* Titles */
    h1,h2,h3 {
        background: -webkit-linear-gradient(#fff,#ff4b4b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Sidebar */
    section[data-testid="stSidebar"]{
        background-color: rgba(15,12,41,0.8)!important;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    selected = option_menu(
        menu_title="Explore",
        options=["Home", "About Me", "Projects", "Contact"],
        icons=["house-heart", "person-badge", "cpu", "send"],
        menu_icon="layers",
        default_index=0,
        styles={
            "container":{
                "padding":"5!important",
                "background-color":"transparent"
            },
            "icon":{
                "color":"#ff4b4b",
                "font-size":"20px"
            },
            "nav-link":{
                "font-size":"16px",
                "text-align":"left",
                "margin":"0px",
                "--hover-color":"#262730"
            },
            "nav-link-selected":{
                "background-color":"#ff4b4b"
            }
        }
    )

# ---------------- HOME ----------------
if selected == "Home":

    st.title("👩‍💻 Neetu Sahu")
    st.subheader("MCA Student | Aspiring Full Stack Developer")

    st.write("📧 **Email:** neetusahu072003@gmail.com")
    st.write("📱 **Phone:** +91 8982826635")
    st.write("📍 **Location:** Indore, Madhya Pradesh")
    st.write("🐙 **GitHub:** https://github.com/Neetu0707")
    st.write("💼 **LinkedIn:** https://www.linkedin.com/in/neetu-sahu-21843a2b0")

# ---------------- ABOUT ----------------
elif selected == "About Me":

    st.header("About Me")

    st.write("""
I am a MCA student with knowledge of HTML, CSS, JavaScript,
React.js, Node.js, C, C++, Python, Java and MongoDB.

I enjoy creating websites and learning new technologies.

I am looking for an opportunity to start my career as a Software Developer.
""")

    st.divider()

    st.header("Education")

    st.subheader("Master of Computer Applications (MCA)")
    st.write("Shri Govindram Seksaria Institute of Technology and Science, Indore")
    st.write("2025 - 2027")

    st.write("")

    st.subheader("Bachelor of Computer Applications (BCA)")
    st.write("Medi-Caps University, Indore")
    st.write("2022 - 2025")

    st.divider()

    st.header("Skills")

    skills = [
        "C","C++","Java","Python","HTML","CSS",
        "JavaScript","React.js","Node.js",
        "MongoDB","MySQL","Git","GitHub"
    ]

    for skill in skills:
        st.markdown(
            f'<span class="skill-tag">{skill}</span>',
            unsafe_allow_html=True
        )

# ---------------- PROJECTS ----------------
elif selected == "Projects":

    st.header("Projects")

    st.markdown("""
<div class="project-card">
<h3>📚 LearnVibe (E-Learning Platform)</h3>

✔ Online Learning Platform

✔ User Login

✔ Course Management

✔ Progress Tracking
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="project-card">
<h3>💻 Deadlock Detector</h3>

✔ Detects Deadlocks in Operating Systems

✔ Uses Resource Allocation Graph

✔ Identifies Circular Wait Conditions
</div>
""", unsafe_allow_html=True)

# ---------------- CONTACT ----------------
elif selected == "Contact":

    st.header("📩 Contact Me")

    st.markdown("### 👤 Your Name")
    name = st.text_input("", key="name", placeholder="Enter your name")

    st.markdown("### 📧 Your Email")
    email = st.text_input("", key="email", placeholder="Enter your email")

    st.markdown("### 💬 Message")
    message = st.text_area("", key="message", placeholder="Write your message here...")

    if st.button("📨 Send Message"):
        st.success("✅ Thank you! Your message has been received.")

    st.divider()
    st.write("Made with ❤️ by Neetu Sahu")