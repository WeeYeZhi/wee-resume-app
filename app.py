from PIL import Image
from pathlib import Path
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import matplotlib.pyplot as plt
from datetime import date
import json

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
# Find more animations here: https://lottiefiles.com/search?category=animations&utm_source=search&utm_medium=platform

st.set_page_config(page_title="My Resume", page_icon=":🎓:", layout="wide")

#Create a function to access the json data of the lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#----LOAD ASSETS----
lottie1 = load_lottieurl("https://lottie.host/eb9ffb9f-d744-4403-8b66-04e1b21dc05e/E3vQdC8K3R.json")
lottie2 = load_lottieurl("https://lottie.host/75882b5a-a42c-42ea-9c65-309ad82488a5/gK1AckAP0t.json")
lottie3 = load_lottieurl("https://lottie.host/f60ae7a0-239a-4477-8d02-dcea435d3d71/5O9BJped9y.json")
lottie4 = load_lottieurl("https://lottie.host/4cc742cf-30d6-4522-9a51-41d512e2f886/YZHnoeW63L.json")

#----PATH SETTINGS----
current_dir = Path(_file_).parent if "_file_" in locals() else Path.cwd()
fypposter_file = current_dir / "assets" / "fypposter.pdf"
experience_file = current_dir / "assets" / "experience.json"
profile_pic = current_dir / "assets" / "profile-pic.png"

# ---- HEADER SECTION ----
with st.container():
    left_column, right_column = st.columns((2, 1))
    with left_column:
        st.header("Hi, I am Wee Ye Zhi :wave:")
        st.title("A Biological Science Student from Universiti Malaysia Terengganu (UMT) 👨‍🔬")
        st.write("###")
        st.write("🏠 Kuching, Sarawak, Malaysia")
        st.write("✉ weeyz02@gmail.com")
        st.write("📞 012-8517668")
        st.markdown("[LinkedIn profile](https://www.linkedin.com/in/wee-ye-zhi-121960224)")
    with right_column:
        profile_pic = Image.open(profile_pic)
        st.image(profile_pic)

#----CONTENT SECTION----

# CAREER OBJECTIVE

with st.container():
    st.write("---")
    st.header("Career Objective 🎯")
    st.write("###")
    st.write("I am passionate to utilize my knowledge and expertise in the field of molecular biology and bioinformatics, strong proficiency in both written and spoken English, and my extreme enthusiasm in the field of research to explore and unravel more unprecedented potent antibiotics and vaccines to combat various bacterial and viral infections via molecular docking and molecular dynamics simulation.")

# EDUCATION

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Education 🎓")
        st.write("###")
        st.write("**B.Sc. (Hons) Biological Sciences** (Universiti Malaysia Terengganu)")
        st.write("October 2021 - October 2024")
        st.write("Current CGPA: 3.96/4.00")
        st.write("###")
        st.write("**Foundation STEM** (Universiti Malaysia Terengganu)")
        st.write("July 2020 - July 2021")
        st.write("CGPA: 4.00/4.00")
        st.write("###")
        st.write("**Sijil Pelajaran Malaysia (SPM)** (SMK Sungai Maong, Kuching, Sarawak)")
        st.write("January 2018 - December 2019")
        st.write("Grade: 6A+ & 3A")

    with right_column:
        st_lottie(lottie1, height=450)

#Final Year Project

with st.container():
    st.write("---")
    st.header("Final Year Project (FYP) 🧑‍💻")
    st.write("###")
    left_column, right_column=st.columns(2)
    with left_column:

        st.write("<u>**Marine Natural Products as Potential Inhibitors Against Pathogenic *Streptococcus agalactiae* Using Molecular Docking Study for Human & Fish Disease Control**</u>", unsafe_allow_html=True)
        st.markdown("""
        <div style="text-align: justify;">
            My final year project (FYP) is fully-computational (<em>in-silico</em> study) whereby it involved using bioinformatics softwares for instance Pymol, UCSF ChimeraX, AlphaFold2, AutoDock4, Biovia Discovery Studio and LigPlot+ to perform homology modelling, protein visualisation & molecular docking between 8 marine natural products (ligands) and <em>S. agalactiae</em> phosphopentomutase (protein) to investigate whether marine natural products (derived from the Comprehensive Marine Natural Product Database, CMNPD) can bind to and inhibit the function of <em>S. agalactiae</em> phosphopentomutase since phosphopentomutase (UniProt ID: Q8CMH7) is a crucial precursor that is required by the bacterium to synthesize its own nucleotides in order to help treat and combat <em>S. agalactiae</em> bacterial infection.
            <br><br> After virtual screening & selecting 3 of the best marine natural products that can dock with <em>S. agalactiae</em> phosphopentomutase with the least binding energy via molecular docking approach, the pharmacokinetic & toxicity properties of the 3 marine natural products were evaluated by using Swiss ADMET in order to investigate whether the 3 marine natural products follow Lipinski's rule of 5 (Pfizer's rule of 5) to ensure they are orally active and can be safely consumed by humans in the form of oral antibiotics. <br><br>
        </div>
        """, unsafe_allow_html=True)

        #----LOAD FYP POSTER FILE----
        with open(fypposter_file, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(
            label="Download FYP Poster",
            data=PDFbyte,
            file_name=fypposter_file.name,
            mime="application/octet-stream",
        )
    with right_column:
        st_lottie(lottie3, height=450)

# EXPERIENCE

with st.container():
    st.write("---")
    st.header('Leadership & Experience 🕶')
    st.write("###")

    # load data
    with open(experience_file, "r", encoding='utf-8') as f:
        data = json.load(f)
    data['events'][0]['end_date']={}
    data['events'][0]['end_date']['year']=str(date.today().year)
    data['events'][0]['end_date']['month']=str(date.today().month)

    # render timeline
    timeline(data, height=650)

# LANGUAGE

with st.container():
    st.write("---")
    st.header("Language 🗣")
    st.write("###")
    st.write("Malaysian University English Test (MUET) score: Band 4.5")

# Data
languages = ["English", "Malay", "Mandarin"]
scales = [8, 8, 9]
colors = ['#3498db', '#2ecc71', '#e74c3c']  # Different colors for each language

# Create horizontal bar plot
fig, ax = plt.subplots(figsize=(7, 1))
bars = ax.barh(languages, scales, color=colors)

# Labels and Title
ax.set_xlabel('Proficiency Scale', fontsize=7)
ax.set_ylabel('Languages', fontsize=7)
ax.set_title('Language Proficiency Levels', fontsize=8)
ax.tick_params(axis='x', labelsize=6)
ax.tick_params(axis='y', labelsize=6)

# Display plot in Streamlit
st.pyplot(fig)

#SKILLS

with st.container():
    st.write("---")
    st.header("Skills")
    st.write("###")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("🚀 Antimicrobial Susceptibility Testing (AST) for MIC and MBC Measurement")
        st.write("🚀 Animal & Plant Cell Culture & Media Selection")
        st.write("🚀 DNA extraction, RNA extraction, Polymerase chain reaction (PCR) & Gel Electrophoresis")
        st.write("🚀 UV-Vis Spectrophotometry")
        st.write("🚀 Homology Modelling of 3D Protein Structure with AlphaFold2, SwissModel, I-TASSER & MODELLER")
        st.write("🚀 Molecular Docking with AutoDock4 & AutoDock Vina")
        st.write("🚀 Molecular Dynamics Simulation with CHARMM-GUI & GROMACS")
        st.write("🚀 Computer-Aided Drug Design (CADD)")
    with right_column:
        st.write("🚀 Research and Development (R&D) with Good Writing & Communication Skill")
        st.write("🚀 Good Laboratory Practice (GLP)")
        st.write("🚀 Standard First Aid, CPR & AED")
        st.write("🚀 Debating in English")
        st.write("🚀 Data Analysis with Python")
        st.write("🚀 Data Analysis with R")
        st.write("🚀 Web Development with HTML, CSS & Streamlit")

#QUALITIES

with st.container():
    st.write("---")
    st.header("Qualities 🌟")
    st.write("###")
    st.write("A diligent, highly self-incentivized, committed and self-reliant fast learner who is eager to conduct research work with minimal supervision and learn from other potential, professional researchers irrespective of races and religion with a positive attitude and strong sense of obligation.")

#HONORS & AWARDS

with st.container():
    st.write("---")
    st.header("Honors & Awards 🏆")
    st.write("###")
    left_column, right_column=st.columns(2)
    with left_column:
        st.write("**Dean's List in Semesters 1-5** (October 2021 - March 2024)")
        st.write("**Faculty Awards: Best Research Project Awards (UMT Student Research Day 2024)** (25 June 2024)")
        st.write("**First-Runner Up of International Debate Johor Cup 2.0** (10 September 2022 - 11 September 2022)")
        st.write("**Second-Runner Up of USM Open Debate Championship 2022** (9 June 2022 - 11 June 2022)")
    with right_column:
        st_lottie(lottie2, height=200, width=250)

#REFERENCES

with st.container():
    st.write("---")
    st.header("References")
    st.write("###")
    left_column, right_column=st.columns(2)
    with left_column:
        st.write("**Assoc. Prof Dr. Fatimah binti Hashim**")
        st.write("Head of Biological Science Program")
        st.write("Universiti Malaysia Terengganu")
        st.write("📞 +(609)6683832")
        st.write("✉ fatimah.h@umt.edu.my")
    with right_column:
        st.write("**Dr. Ramesh Kumar Santhanam**")
        st.write("Mentor")
        st.write("Universiti Malaysia Terengganu")
        st.write("📞 +(609)6683609")
        st.write("✉ ramesh@umt.edu.my")
    st.write("###")
    left_column, right_column=st.columns(2)
    with left_column:
        st.write("**Dr. Siti Aisyah binti Razali**")
        st.write("Final Year Project (FYP) Supervisor")
        st.write("Universiti Malaysia Terengganu")
        st.write("📞 +(609)6683325")
        st.write("✉ aisyarazali@umt.edu.my")
    with right_column:
        st.write("**Dr. Sairatul Dahlianis Ishak**")
        st.write("FYP Co-Supervisor")
        st.write("Universiti Malaysia Terengganu")
        st.write("📞 +(609)6683810")
        st.write("✉ sairatul.ishak@umt.edu.my")
    st.write("###")
    left_column, right_column=st.columns(2)
    with left_column:
        st.write("**Assoc. Prof. Dr. Siti Nor Khadijah binti Addis**")
        st.write("UMT Internship Supervisor")
        st.write("Universiti Malaysia Terengganu")
        st.write("📞 +(609)6683402")
        st.write("✉ khadijah@umt.edu.my")
    with right_column:
        st.write("**Ts. Dr. Nor Azlan bin Nor Muhammad**")
        st.write("INBIOSIS, UKM Internship Supervisor")
        st.write("Institute of Systems Biology (INBIOSIS), Universiti Kebangsaan Malaysia")
        st.write("📞 +(603)89214550")
        st.write("✉ norazlannm@ukm.edu.my")

# CONTACT

# CONTACT

with st.container():
    st.write("---")
    st.header("Contact Me ✉")
    st.write("###")
    left_column, right_column=st.columns(2)
    with left_column:
        contact_form = f"""
        <form action="https://formsubmit.co/weeyz02@gmail.com" method="POST">
            <input type="hidden" name="_captcha value="false">
            <input type="text" name="name" placeholder="Kindly enter your name here" required style="width: 600px;"><br>
            <input type="email" name="email" placeholder="Kindly enter your email here" required style="width: 600px;"><br>
            <textarea name="message" placeholder="Kindly enter your message here" required style="width: 600px;"></textarea><br>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st_lottie(lottie4, height=300, width=450)

