import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Powdery mildew is a fungal disease that affects a wide range of plants.\n"
        f"Powdery mildew diseases are caused by many different species of ascomycete fungi in the order Erysiphales.\n"
        f"Powdery mildew is one of the easier plant diseases to identify, as the signs of the causal pathogen are quite distinctive."
        f"Infected plants display white powdery spots on the leaves and stems."
        f"This mycelial layer may quickly spread to cover all of the leaves."
        f"The lower leaves are the most affected, but the mildew can appear on any above-ground part of the plant."
        f"As the disease progresses, the spots get larger and denser as large numbers of asexual spores are formed,\n"
        f"and the mildew may spread up and down the length of the plant.\n\n"
        f"**Project Dataset**\n"
        f"* The available dataset contains 4208 images taken from "
        f"infected and healthy leaves of cherry trees.")
        
        
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/nianswe/CherryLeaves_Sample1/blob/main/README.md).")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* The client is interested in conducting a study to visually "
        f"differentiate a cherry leaf that is healthy from one that contains powdery mildew.\n"
        f"* The client is interested in predicting if a cherry tree is healthy or contains powdery mildew. "
        )
