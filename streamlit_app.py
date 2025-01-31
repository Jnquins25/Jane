import streamlit as st
import json
import os

DATA_FILE = "data.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as file:
        json.dump({"certificates": [], "education": []}, file)

def load_data():
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

def main():
    st.set_page_config(page_title="My Personal Blog", layout="wide")

    st.markdown(
        """
        <style>
        body {
            background-color: #f8f9fa;
        }
        .main-container {
            background: linear-gradient(to bottom, #000000, #f1f1f1);
            border-radius: 15px;
            padding: 30px;
            margin: 20px auto;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .header {
            text-align: center;
            padding: 20px;
        }
        .profile-pic {
            border-radius: 50%;
            width: 150px;
            height: 150px;
            object-fit: cover;
            margin-top: 10px;
        }
        .personal-info {
            font-size: 18px;
            color: #000000;
            margin-top: 10px;
        }
        .about-me {
            font-size: 16px;
            color: #333;
            line-height: 1.8;
        }
        .section-title {
            color: #4CAF50;
            font-size: 24px;
            font-weight: bold;
            margin-top: 30px;
            margin-bottom: 10px;
        }
        .button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            font-size: 16px;
            margin: 10px;
            cursor: pointer;
            border-radius: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    data = load_data()

    st.markdown(
        """
        <div class="main-container">
            <div class="header">
                <h1>My Personal Blog</h1>
                <img src="Janeee.JPG" alt="Profile Picture" class="profile-pic">
                <div class="personal-info">
                    <p><b>Jane Quinda B. Eriga</b></p>
                    <p>Birthday: March 25, 2006 | Age: 18</p>
                    <p>From: Siargao Island, Surigao Del Norte</p>
                    <p>Course: Bachelor of Science in Computer Engineering (1st Year)</p>
                </div>
            </div>
            <div class="about-me">
                <h3>About Me</h3>
                <p>I have loved dancing since I was a toddler, and my passion for it continues to this day. I am a dog lover and find joy in spending time with my furry companions. My zodiac sign is Aries, which reflects my enthusiastic and driven nature.</p>
                <p>I have a deep appreciation for sunsets, the moon, peace, and nature. I find beauty in the ethereal and enjoy exploring fashion, reading, sleeping, watching movies, and listening to the soothing sound of the rain.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.title("Manage Information")
    menu = st.sidebar.radio("Menu", ["Certificates", "Educational Attainments"])

    if menu == "Certificates":
        st.markdown('<div class="section-title">Certificates</div>', unsafe_allow_html=True)

        if data["certificates"]:
            for i, cert in enumerate(data["certificates"]):
                st.markdown(f"### {i + 1}. {cert['title']}")
                st.write(f"**Hours:** {cert['hours']}")
                st.write(f"**Venue:** {cert['venue']}")
                st.write(f"**Host:** {cert['host']}")
                st.write("---")
        else:
            st.info("No certificates found. Add some using the sidebar!")

        st.markdown('<div class="section-title">Add Certificate</div>', unsafe_allow_html=True)
        cert_title = st.text_input("Title of the Certificate")
        cert_hours = st.text_input(" Hours")
        cert_venue = st.text_input("Venue")
        cert_host = st.text_input("Host")
        if st.button("Add Certificate"):
            if cert_title and cert_hours and cert_venue and cert_host:
                data["certificates"].append(
                    {"title": cert_title, "hours": cert_hours, "venue": cert_venue, "host": cert_host}
                )
                save_data(data)
                st.success("Certificate added successfully!")
            else:
                st.error("Please fill in all fields.")

    elif menu == "Educational Attainments":
        st.markdown('<div class="section-title">Educational Attainments</div>', unsafe_allow_html=True)

        # View Educational Attainments
        if data["education"]:
            for i, edu in enumerate(data["education"]):
                st.markdown(f"### {i + 1}. {edu['title']}")
                st.write(edu["details"])
                st.write("---")
        else:
            st.info("No educational attainments found. Add some using the sidebar!")

        st.markdown('<div class="section-title">Add Educational Attainment</div>', unsafe_allow_html=True)
        edu_title = st.text_input("Title of the Educational Attainment")
        edu_details = st.text_area("Details")
        if st.button("Add Educational Attainment"):
            if edu_title and edu_details:
                data["education"].append({"title": edu_title, "details": edu_details})
                save_data(data)
                st.success("Educational attainment added successfully!")
            else:
                st.error("Please fill in all fields.")

    st.markdown(
        """
        <footer style="text-align: center; padding: 10px; font-size: 14px; color: #777;">
            <p>© 2024 Jane Quinda B. Eriga | All Rights Reserved</p>
        </footer>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
