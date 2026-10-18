from PIL import Image
from pathlib import Path
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import matplotlib.pyplot as plt
from datetime import date
from streamlit.components.v1 import html
import json
import base64

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
profile_pic = current_dir / "assets" / "profile-pic-formal.png"

# ---- HEADER SECTION ----
with st.container():
    left_column, right_column = st.columns((2, 1))
    with left_column:
        st.header("Hi, I am Wee Ye Zhi :wave:")
        st.title("A Postgraduate Researcher from National University of Malaysia (UKM) 👨‍🔬")
        st.write("###")
        st.write("🏠 Kuching, Sarawak, Malaysia")
        st.write("✉ weeyezhi@gmail.com")
        st.write("📞 012-8517668")
        st.markdown(
            "[LinkedIn](https://www.linkedin.com/in/wee-ye-zhi-121960224) | "
            "[ResearchGate](https://www.researchgate.net/profile/Wee-Ye-Zhi) | "
            "[Google Scholar](https://scholar.google.com/citations?user=OkSJ1CwAAAAJ&hl=en) | "
            "[ORCID](https://orcid.org/0009-0008-5833-9636) | "
            "[GitHub](https://github.com/WeeYeZhi) | "
            "[Medium](https://medium.com/@weeyezhi) | "
            "[Credly](https://www.credly.com/users/ye-zhi-wee/badges/credly)"
        )
    with right_column:
        profile_pic = Image.open(profile_pic)
        st.image(profile_pic)

#----CONTENT SECTION----

# CAREER OBJECTIVE

with st.container():
    st.write("---")
    st.header("Career Objective 🎯")
    st.write("###")
    st.write("I am passionate to utilize my knowledge and expertise in the field of molecular biology and bioinformatics, strong proficiency in both written and spoken English, and my extreme enthusiasm in the field of research to explore and unravel more unprecedented potent antibiotics and vaccines to combat various bacterial and viral infections via molecular docking and molecular dynamics simulation. Also, I am eager to document all big data of my research into a SQL database for easy querying and management.")

# EDUCATION

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Education 🎓")
        st.write("###")
        st.write("**Master of Science in Systems Biology**")
        st.write("Universiti Kebangsaan Malaysia (UKM), Malaysia")
        st.write("October 2024 - Present")
        st.write("###")
        st.write("**B.Sc. (Hons) Biological Sciences**")
        st.write("Universiti Malaysia Terengganu(UMT), Malaysia")
        st.write("October 2021 - August 2024")
        st.write("CGPA: 3.96/4.00")
        st.write("###")
        st.write("**Foundation STEM**")
        st.write("Universiti Malaysia Terengganu(UMT), Malaysia")
        st.write("July 2020 - July 2021")
        st.write("CGPA: 4.00/4.00")
        st.write("###")
        st.write("**Sijil Pelajaran Malaysia (SPM)**")
        st.write("SMK Sungai Maong, Kuching, Sarawak, Malaysia")
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
            My final year project (FYP) is fully-computational (<em>in-silico</em> study) whereby it involved using bioinformatics softwares for instance PyMOL, UCSF ChimeraX, AlphaFold2, AutoDock4, Biovia Discovery Studio and LigPlot+ to perform homology modelling, protein visualisation & molecular docking between 8 marine natural products (ligands) and <em>S. agalactiae</em> phosphopentomutase (protein) to investigate whether marine natural products (derived from the Comprehensive Marine Natural Product Database, CMNPD) can bind to and inhibit the function of <em>S. agalactiae</em> phosphopentomutase since phosphopentomutase (UniProt ID: Q8CMH7) is a crucial precursor that is required by the bacterium to synthesize its own nucleotides in order to help treat and combat <em>S. agalactiae</em> bacterial infection.
            <br><br> After virtual screening & selecting 3 of the best marine natural products that can dock with <em>S. agalactiae</em> phosphopentomutase with the least binding affinity via molecular docking approach, the pharmacokinetic & toxicity properties of the 3 marine natural products were evaluated by using Swiss ADMET in order to investigate whether the 3 marine natural products follow Lipinski's rule of 5 (Pfizer's rule of 5) to ensure they are orally active and can be safely consumed by humans in the form of oral antibiotics. <br><br>
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
    timeline(data, height=2000)

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
        st.write("🚀 Antimicrobial sSusceptibility Testing (AST) for MIC and MBC Measurement")
        st.write("🚀 Animal & Plant Cell Culture & Media Selection")
        st.write("🚀 DNA extraction, RNA extraction, Polymerase chain reaction (PCR) & Gel Electrophoresis")
        st.write("🚀 UV-Vis Spectrophotometry")
        st.write("🚀 Homology Modelling of 3D Protein Structure with AlphaFold3, SwissModel, I-TASSER & MODELLER")
        st.write("🚀 Molecular Docking with AutoDock4 & AutoDock Vina")
        st.write("🚀 Molecular Dynamics Simulation with CHARMM-GUI & GROMACS")
        st.write("🚀 Computer-Aided Drug Design (CADD)")
        st.write("🚀 Research and Development (R&D) with Good Writing & Communication Skill")
    with right_column:
        st.write("🚀 Good Laboratory Practice (GLP)")
        st.write("🚀 Standard First Aid, CPR & AED")
        st.write("🚀 Debating in English")
        st.write("🚀 Data Analysis with Python")
        st.write("🚀 Data Analysis with R")
        st.write("🚀 Web Development with HTML, CSS & Streamlit")
        st.write("🚀 Next Generation Sequencing (NGS) Data Analysis")
        st.write("🚀 High Performance Computing (HPC) and Linux-based Bioinformatics")
        st.write("🚀 Version Control with Git and GitHub")

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
        st.write("**Academic Excellence Student Award** (October 2024)")
        st.write("**Dean's List in Semesters 1-6** (October 2021 - August 2024)")
        st.write("**Faculty Awards: Best Research Project Awards (UMT Student Research Day 2024)** (25 June 2024)")
        st.write("**First-Runner Up of International Debate Johor Cup 2.0** (10 September 2022 - 11 September 2022)")
        st.write("**Second-Runner Up of USM Open Debate Championship 2022** (9 June 2022 - 11 June 2022)")
    with right_column:
        st_lottie(lottie2, height=200, width=250)

# CERTIFICATES

with st.container():
    st.write("---")
    st.header("Certificates of Accomplishment 📜")
    st.write("###")

    certificates = [
        {
            "title": "Google Data Analytics Professional Certificate",
            "issuer": "Google / Coursera",
            "date": "Oct 2026",
            "url": "https://weeyezhi.github.io/certificates/Google_Data_Analytics_Professional_Certificate.pdf"
        },

        {
            "title": "Learn Bash Scripting",
            "issuer": "Codecademy",
            "date": "Aug 2026",
            "url": "https://weeyezhi.github.io/certificates/Learn_Bash_Scripting.pdf"
        },

        {
            "title": "Asian Regional Conference on Systems Biology (ARCSB) X International Conference on Natural Products (ICNP) 2025 (Oral Presentation)",
            "issuer": "INBIOSIS, Malaysian Natural Product Society (MNPS), Malaysian Society of Systems and Synthetic Biology (MyBioSS)",
            "date": "Oct 2025",
            "url": "https://weeyezhi.github.io/certificates/ARCSBxICNP2025_Oral_Presentation_Certificate.pdf"
        },

        {
            "title": "Cloud Computing",
            "issuer": "Programming Hub",
            "date": "Sept 2025",
            "url": "https://weeyezhi.github.io/certificates/Cloud_computing.pdf"
        },

        {
            "title": "AWS Cloud Computing",
            "issuer": "Programming Hub",
            "date": "Sept 2025",
            "url": "https://weeyezhi.github.io/certificates/AWS_Cloud_Computing.pdf"
        },

        {
            "title": "Python Programming",
            "issuer": "Programming Hub",
            "date": "Sept 2025",
            "url": "https://weeyezhi.github.io/certificates/Python.pdf"
        },

        {
            "title": "Docker",
            "issuer": "Programming Hub",
            "date": "Aug 2025",
            "url": "https://weeyezhi.github.io/certificates/Docker.pdf"
        },

        {
            "title": "HTML Advanced",
            "issuer": "Programming Hub",
            "date": "Aug 2025",
            "url": "https://weeyezhi.github.io/certificates/HTML_advanced.pdf"
        },

        {
            "title": "HTML",
            "issuer": "Programming Hub",
            "date": "Aug 2025",
            "url": "https://weeyezhi.github.io/certificates/HTML.pdf"
        },

        {
            "title": "R Programming",
            "issuer": "Programming Hub",
            "date": "Aug 2025",
            "url": "https://weeyezhi.github.io/certificates/R_Programming.pdf"
        },

        {
            "title": "Linux Programming",
            "issuer": "Programming Hub",
            "date": "Aug 2025",
            "url": "https://weeyezhi.github.io/certificates/Linux.pdf"
        },

        {
            "title": "Git",
            "issuer": "Programming Hub",
            "date": "Aug 2025",
            "url": "https://weeyezhi.github.io/certificates/Git.pdf"
        },

        {
            "title": "Bioinformatics Workflows for Life Sciences Using Snakemake",
            "issuer": "Udemy",
            "date": "Jul 2025",
            "url": "https://weeyezhi.github.io/certificates/Bioinformatics_Workflows_for_Life_Sciences_Using_SnakeMake.jpg"
        },

        {
            "title": "Malaysian International Cocoa Fair (MICF) and Cocoa Conference (MICC) 2025 (Poster Presentation)",
            "issuer": "Malaysian Cocoa Board (MCB)",
            "date": "May 2025",
            "url": "https://weeyezhi.github.io/certificates/MICC2025_Poster_Presentation_Certificate.pdf"
        },

        {
            "title": "Machine Learning",
            "issuer": "Programming Hub",
            "date": "April 2025",
            "url": "https://weeyezhi.github.io/certificates/Machine_Learning.pdf"
        },

        {
            "title": "Basics of NGS and Tips of Getting Started",
            "issuer": "Biomics Solution Sdn Bhd",
            "date": "Sept 2024",
            "url": "https://weeyezhi.github.io/certificates/Next_Generation_Sequencing_Basics_of_NGS_and_Tips_of_Getting_Started.pdf"
        },

        {
            "title": "Data Analysis with Python",
            "issuer": "IBM / Coursera",
            "date": "Jul 2024",
            "url": "https://weeyezhi.github.io/certificates/Data_Analysis_with_Python.pdf"
        },

        {
            "title": "Real Time PCR Hands-on Workshop 2024",
            "issuer": "INBIOSIS, UKM",
            "date": "Jul 2024",
            "url": "https://weeyezhi.github.io/certificates/Hands_On_PCR_Workshop.png"
        },

        {
            "title": "Data Analysis with R Programming",
            "issuer": "Google / Coursera",
            "date": "May 2024",
            "url": "https://weeyezhi.github.io/certificates/Data_Analysis_with_R_programming.pdf"
        },

        {
            "title": "Introduction to AI and Machine Learning on Google Cloud",
            "issuer": "Google Cloud",
            "date": "May 2024",
            "url": "https://weeyezhi.github.io/certificates/Introduction_to_AI_and_Machine_Learning_on_Google_Cloud.jfif"
        },

        {
            "title": "Laboratory Safety Induction (LSI)",
            "issuer": "INBIOSIS, UKM",
            "date": "Mac 2024",
            "url": "https://weeyezhi.github.io/certificates/Laboratory_Safety_Induction_IKeM.pdf"
        },

        {
            "title": "Bioinformatics (Learn Docking and Molecular Dynamics Simulation)",
            "issuer": "Udemy",
            "date": "Dec 2023",
            "url": "https://weeyezhi.github.io/certificates/Bioinformatics_Learn_Molecular_Docking_and_Molecular_Dynamic_Simulation.pdf"
        },

        {
            "title": "Learn HTML",
            "issuer": "Codecademy",
            "date": "Dec 2023",
            "url": "https://weeyezhi.github.io/certificates/Learn_HTML.pdf"
        },

        {
            "title": "Drug Discovery Using Computer Approaches",
            "issuer": "Biomics Solution Sdn Bhd",
            "date": "Nov 2022",
            "url": "https://weeyezhi.github.io/certificates/Drug_Discovery_using_Computer_Approaches.pdf"
        },

        {
            "title": "Basics of Research Paper Writing",
            "issuer": "A2Z EduLearningHub",
            "date": "Sept 2022",
            "url": "https://weeyezhi.github.io/certificates/Basics_of_Research_Paper_Writing.pdf"
        },

        {
            "title": "The Do's and Don'ts of Biosafety Cabinet",
            "issuer": "Gaia Science (M) Sdn Bhd",
            "date": "Sept 2022",
            "url": "https://weeyezhi.github.io/certificates/Dos_and_donts_of_biosafety_cabinet.pdf"
        },

        {
            "title": "PCR and Gel Electrophoresis",
            "issuer": "Biomics Solution Sdn Bhd",
            "date": "April 2022",
            "url": "https://weeyezhi.github.io/certificates/PCR_&_Gel_Electrophoresis.pdf"
        },

    ]

 # -----------------------------------
    # Initialize session state
    # -----------------------------------
    if "certificate_index" not in st.session_state:
        st.session_state.certificate_index = 0

    current = certificates[st.session_state.certificate_index]

    # -----------------------------------
    # Display current certificate
    # -----------------------------------

    st.subheader(current["title"])

    col1, col2 = st.columns([3,1])

    with col1:
        st.write(f"**Issuer:** {current['issuer']}")
        st.write(f"**Date:** {current['date']}")

    with col2:
        st.link_button(
            "📄 View Certificate",
            current["url"],
            use_container_width=True
        )

    st.write("")

    # -----------------------------------
    # Navigation Buttons
    # -----------------------------------

    left, center, right = st.columns([1,4,1])

    with left:
        if st.button("◀", use_container_width=True):

            st.session_state.certificate_index = (
                st.session_state.certificate_index - 1
            ) % len(certificates)

            st.rerun()

    with center:

        st.markdown(
            f"""
            <div style='text-align:center; font-size:18px;'>

            <b>{st.session_state.certificate_index+1}</b>
            /
            <b>{len(certificates)}</b>

            </div>
            """,
            unsafe_allow_html=True
        )

    with right:
        if st.button("▶", use_container_width=True):

            st.session_state.certificate_index = (
                st.session_state.certificate_index + 1
            ) % len(certificates)

            st.rerun()

#PUBLICATIONS

with st.container():
    st.write("---")
    st.header("Publications 📰")
    st.write("###")
    st.markdown("[1. Marine Natural Products as Potential Inhibitors Against Pathogenic *Streptococcus agalactiae* Using Molecular Docking Study for Human and Fish Disease Control](https://www.researchgate.net/publication/386218195_Marine_Natural_Products_as_Potential_Inhibitors_Against_Pathogenic_Streptococcus_agalactiae_Using_Molecular_Docking_Study_For_Human_and_Fish_Disease_Control)")
    left_column, center_column, right_column=st.columns(3)
    with left_column:
        st.write("Received: 13 March 2024")
    with center_column:
        st.write("Accepted: 10 August 2024")
    with right_column:
        st.write("Published: 15 November 2024")
    st.write("Published in Journal of Sustainability Science and Management (JSSM)")
    st.write("Volume 19, Number 11, November 2024, 15-38")
    st.write("Scopus Q3")

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
        st.write("📞 (+60)96683832")
        st.write("✉ fatimah.h@umt.edu.my")
    with right_column:
        st.write("**Dr. Ramesh Kumar Santhanam**")
        st.write("Mentor")
        st.write("Universiti Malaysia Terengganu")
        st.write("📞 (+60)96683609")
        st.write("✉ ramesh@umt.edu.my")
    st.write("###")
    left_column, right_column=st.columns(2)
    with left_column:
        st.write("**Dr. Siti Aisyah binti Razali**")
        st.write("Final Year Project (FYP) Supervisor (Corresponding Author)")
        st.write("Universiti Malaysia Terengganu")
        st.write("📞  (+60)96683325")
        st.write("✉ aisyarazali@umt.edu.my")
    with right_column:
        st.write("**Dr. Sairatul Dahlianis Ishak**")
        st.write("FYP Co-Supervisor (Coauthor)")
        st.write("Universiti Malaysia Terengganu")
        st.write("📞 +(60)96683810")
        st.write("✉ sairatul.ishak@umt.edu.my")
    st.write("###")
    left_column, right_column=st.columns(2)
    with left_column:
        st.write("**Assoc. Prof. Dr. Siti Nor Khadijah binti Addis**")
        st.write("UMT Internship Supervisor")
        st.write("Universiti Malaysia Terengganu")
        st.write("📞 (+60)96683402")
        st.write("✉ khadijah@umt.edu.my")
    with right_column:
        st.write("**Ts. Dr. Nor Azlan bin Nor Muhammad**")
        st.write("Master Main Supervisor, INBIOSIS, UKM (Corresponding Author)")
        st.write("Institute of Systems Biology (INBIOSIS), Universiti Kebangsaan Malaysia")
        st.write("📞 (+60)389215555")
        st.write("✉ norazlannm@ukm.edu.my")
    st.write("###")
    left_column, right_column=st.columns(2)
    with left_column:
        st.write("**Dr. Sarahani binti Harun**")
        st.write("Master Cosupervisor, INBIOSIS, UKM (Coauthor)")
        st.write("Institute of Systems Biology (INBIOSIS), Universiti Kebangsaan Malaysia")
        st.write("📞 (+60)389215555")
        st.write("✉ sarahani@ukm.edu.my")
    with right_column:
        st.write("**Dr. Norfarhan binti Mohd Assa'ad**")
        st.write("Master Cosupervisor, INBIOSIS, UKM (Coauthor)")
        st.write("Department of Applied Physics, Faculty of Science and Technology (FST), Universiti Kebangsaan Malaysia")
        st.write("📞 (+60)389215555")
        st.write("✉ n_farhan@ukm.edu.my")
    st.write("###")
    left_column, right_column=st.columns(2)
    with left_column:
        st.write("**Prof. Dr. Masanori Arita**")
        st.write("Master Cosupervisor, DDBJ, NIG (Coauthor)")
        st.write("Department of Informatics, National Institute of Genetics (NIG), Mishima, Shizuoka, Japan")
        st.write("📞 (+81)559819449")
        st.write("✉ arita@nig.ac.jp")
    with right_column:
        st.write("**Encik Mohd Zulhilmi Abdul Rahman**")
        st.write("Data Supplier (Coauthor)")
        st.write("Biotechnology Division, Centre for Cocoa Biotechnology Research, Malaysia Cocoa Board, Kota Kinabalu, Sabah, Malaysia")
        st.write("📞 (+60)88489101")
        st.write("✉ hilmi@koko.gov.my")

# CONTACT

# CONTACT

with st.container():
    st.write("---")
    st.header("Contact Me ✉")
    st.write("###")

    contact_form = """
    <form action="https://formsubmit.co/weeyezhi@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Kindly enter your name here" required style="width: 100%; max-width:1400px;"><br><br>
        <input type="email" name="email" placeholder="Kindly enter your email here" required style="width: 100%; max-width:1400px;"><br><br>
        <textarea name="message" placeholder="Kindly enter your message here" required style="width: 100%; max-width:1400px; height:120px;"></textarea><br><br>
        <button type="submit">Submit</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    st_lottie(lottie4, height=800, width=800)

