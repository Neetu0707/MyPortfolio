import streamlit as st
from streamlit_option_menu import option_menu

# --- PAGE CONFIG ---
st.set_page_config(page_title="Neetu Sahu | Portfolio", page_icon="👩‍💻", layout="wide")

# --- ADVANCED CUSTOM CSS ---
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
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 20px;
        margin-bottom: 25px;
        transition: transform 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        border: 1px solid #ff4b4b;
        background: rgba(255, 255, 255, 0.08);
    }

    /* Skill Tags */
    .skill-tag {
        display: inline-block;
        padding: 6px 15px;
        margin: 4px;
        border-radius: 50px;
        background: rgba(255, 75, 75, 0.2);
        border: 1px solid #ff4b4b;
        font-size: 14px;
        font-weight: 500;
    }

    /* Titles */
    h1, h2 {
        font-family: 'Inter', sans-serif;
        background: -webkit-linear-gradient(#fff, #ff4b4b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: rgba(15, 12, 41, 0.8) !important;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    selected = option_menu(
        menu_title="Explore",
        options=["Home", "About Me", "Projects", "Contact"],
        icons=["house-heart", "person-badge", "cpu", "send"],
        menu_icon="layers",
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "transparent"},
            "icon": {"color": "#ff4b4b", "font-size": "20px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#262730"},
            "nav-link-selected": {"background-color": "#ff4b4b"},
        }
    )

# --- HOME SECTION ---
if selected == "Home":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("## ✨ Welcome to my Portfolio")
        st.title("I'm Neetu Sahu")
        st.subheader("MCA Student | Web Developer | Tech Enthusiast")
        st.markdown("""
        I build digital experiences that are as **technically sound** as they are **visually pleasing**. 
        Currently focusing on full-stack development and system utilities.
        """)
        if st.button("🚀 View My Work"):
            st.info("Scroll down or use the sidebar to explore!")
            
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/6840/6840478.png", width=250)

# --- ABOUT ME SECTION ---
elif selected == "About Me":
    st.header("📖 My Journey")
    st.write("---")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        #### Passion & Education
        I am an MCA student passionate about Web Development and building real-world projects. 
        I love solving complex problems and turning ideas into functional, user-friendly applications.
 """)
        
    with col2:
        st.markdown("#### ✨ My Core Skills")
        skills = ("C", "C++", "Python", "HTML/CSS", "JavaScript", "SQL", "UI/UX Design", "System Utilities")
        skill_html = "".join([f'<div class="skill-tag">{s}</div>' for s in skills])
        st.markdown(skill_html, unsafe_allow_html=True)

# --- PROJECTS SECTION ---
elif selected == "Projects":
    st.header("🚀 My Projects")
    st.write("---")

    def render_project(title, desc, features, link):
        st.markdown(f"""
        <div class="project-card">
            <h3 style="color: #ff4b4b; margin-top: 0;">{title}</h3>
            <p style="font-size: 16px; opacity: 0.9;">{desc}</p>
            <p><b>✨ Key Tech:</b> {features}</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button(f"Explore {title}", link)
        st.write("")

    render_project(
        "My-Portfolio", 
        "A high-performance personal hub for recruiters to view my resume and technical trajectory.", 
        "Streamlit, CSS Animations, Responsive UI",
        "https://github.com/Neetu0707/My-Portfolio"
    )

    render_project(
        "Deadlock Detector", 
        "A logic-heavy system utility simulating multi-process resource allocation.", 
        "Banker’s Algorithm, Resource Visualization, Python Logic",
        "https://github.com/Neetu0707/Deadlock-Detector"
    )

    render_project(
        "LearnVibe", 
        "A modern EdTech platform streamlining student progress tracking and content delivery.", 
        "Authentication, Progress Dashboards, UX Optimization",
        "https://github.com/Neetu0707/Learnvibe"
    )

# --- CONTACT SECTION ---
elif selected == "Contact":
    st.header("📩 Let's Connect")
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Contact Details")
        st.write("📧 **Email:** neetusahu072003@gmail.com")
        st.write("📞 **Phone:** +91 8982826635")
        st.write("📍 **Location:** Indore, India")
        
        st.markdown("### Socials")
        st.markdown("[🐙 GitHub](https://github.com/Neetu0707) | [🔗 LinkedIn](https://linkedin.com)")

    with col2:
        with st.form("contact"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            msg = st.text_area("How can I help you?")
            if st.form_submit_button("Send Message"):
                st.success(f"Thanks {name}! Your message has been sent (simulation).")