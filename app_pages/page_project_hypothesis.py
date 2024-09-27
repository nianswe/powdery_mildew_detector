import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We suspect Cherry leaves infected with Powdery Mildew have clear marks/signs, "
        f"a white faded colour, that can differentiate them from an uninfected leaf. \n\n"
        f"* An Image Montage shows that typically a leaf infected with powdery mildew has white faded structure. \n"
        f"Average Image, Variability Image and Difference between Averages studies did not reveal "
        f"any clear pattern to differentiate one from another."

    )
