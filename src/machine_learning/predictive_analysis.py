import streamlit as st
import numpy as np
import pandas as pd
# import plotly.express as px
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file


def plot_predictions_probabilities(pred_proba, pred_class):
    """
    Plot prediction probability results
    """

    prob_per_class = pd.DataFrame(
        data=[0, 0],
        index={'healthy': 0, 'powdery_mildew': 1}.keys(),
        columns=['Probability']
    )
    prob_per_class.loc[pred_class] = pred_proba
    for x in prob_per_class.index.to_list():
        if x not in pred_class:
            prob_per_class.loc[x] = 1 - pred_proba
    prob_per_class = prob_per_class.round(3)
    prob_per_class['Diagnostic'] = prob_per_class.index

    # fig = px.bar(
    #    prob_per_class,
    #    x='Diagnostic',
    #    y=prob_per_class['Probability'],
    #    range_y=[0, 1],
    #    width=600, height=300, template='seaborn')
    # st.plotly_chart(fig)

    # Assuming prob_per_class is already defined

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.bar(prob_per_class['Diagnostic'], prob_per_class['Probability'])

    # Customize the appearance
    ax.set_xlabel('Diagnostic')
    ax.set_ylabel('Probability')
    ax.set_title('Probability Distribution by Diagnostic')

    # Set y-axis range
    ax.set_ylim(0, 1)

    # Add grid lines
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')

    # Adjust layout and display the plot
    plt.tight_layout()
    plt.show()


def resize_input_image(img, version):
    """
    Reshape image to average image size
    """
    image_shape = load_pkl_file(file_path=f"outputs/{version}/image_shape.pkl")
    img_resized = img.resize((image_shape[1], image_shape[0]), Image.LANCZOS)
    my_image = np.expand_dims(img_resized, axis=0)/255

    return my_image


def load_model_and_predict(my_image, version):
    """
    Load and perform ML prediction over live images
    """

    model = load_model(f"outputs/{version}/cherry_leaves_model.keras")

    pred_proba = model.predict(my_image)[0, 0]

    target_map = {v: k for k, v in {'healthy': 0, 'powdery_mildew': 1}.items()}
    pred_class = target_map[pred_proba > 0.5]
    if pred_class == target_map[0]:
        pred_proba = 1 - pred_proba

    st.write(
        f"The predictive analysis indicates the sample leaves is "
        f"**{pred_class.lower()}**.")

    return pred_proba, pred_class