import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.info(
        f"* We suspect Cherry leaves infected with Powdery Mildew have \
            clear marks/signs, "
        f"infected plants display white powdery spots on the leaves and \
            stems, that can differentiate them from an uninfected leaf. \n"
        f"* An Image Montage shows that typically a leaf infected with \
            powdery mildew has white powdery spots and structure. \n"
    )

    st.success(
        "The model was able to detect such differences and learn how to \
            differentiate and generalize in order to make accurate \
                predictions. \n"
        "It exceeded well above the 77% accurarcy rate set out by the \
            client and so has been a success \n"
        "A good model trains its ability to predict classes on a batch \
            of data without adhering too closely to that set of data. \n"
        "In this way, the model is able to generalize and predict future \
            observations reliably because it didn't 'memorize' the \
                relationships \n "
        "between features and labels as seen in the training dataset but \
            the general pattern from feature to labels."
    )

    st.warning(
        f"Average Image, Variability Image and Difference between Averages \
            studies did not reveal \n"
        f"any clear pattern to differentiate one from another."
    )

    st.write("To explore the validation of these processes, visit the pages \
        using the navigation on the left:"
             )

    st.markdown(
        """
        - **Leaves Visualizer**
        - **Powdery Mildew Detection**
        - **ML Performance Metrics**
        """
        )
