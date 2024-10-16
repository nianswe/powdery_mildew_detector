import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def page_ml_performance_metrics():
    version = 'v11'

    st.write("## **ML Performance Metrics**")

    st.write("---")

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    st.info(
        "The cherry leaves dataset contains 4208 images.\n"
        "Half of the images show healthy leaves, and half show leaves \
            infected with powdery mildew.\n"
        "The dataset was divided into 3 sets:\n"
        "- Train Set - 70% of the dataset.\n"
        "- Test Set - 20% of the dataset.\n"
        "- Validation Set - 10% of the dataset.\n"
        )

    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution,
             caption='Labels Distribution on Train, Validation and Test Sets')

    st.success("The graph shows the dataset was divided correctly.")

    st.write("---")

    st.write("### Model History")

    st.info(
        "The following plots show the model training accuracy and losses. \n\n"
        "The accuracy is the measure of the model's prediction accuracy \
            compared to the true data (val_acc). \n\n"
        "The loss indicates incorrect predictions on the train set (loss) \
            and validation set (val_loss)."
        )

    model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
    st.image(model_acc, caption='Model Training Accuracy')

    model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
    st.image(model_loss, caption='Model Training Losses')

    st.success(
        "Both plots suggests the model exhibits a normal fit with no \
            severe overfitting \n"
        "or underfitting as the two lines follow the same pattern.")

    st.write("---")

    st.write("### Generalised Performance on Test Set")

    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))

    st.success(
        "The prediction accuracy of the test set data is above 97%. \n\n"
        "This is below 100%, suggesting the model is not overfitting.")

    st.info(
        "The following plot shows the confusion matrix for the test dataset. \n\n"
        "It shows the four possible combinations of outcomes: \n\n"
        "True Positive / Negative - The model prediction is correct (green) \n\n"
        "False Positive / Negative - The model prediction is incorrect (red). \n\n"
        "A good model has a high True rate and a low False rate."
        )

    model_loss = plt.imread(f"outputs/{version}/confusion_matrix.png")
    st.image(model_loss, caption='Confusion Matrix of Test Dataset')

    st.success(
        "The confusion matrix shows the model made 2 incorrect predictions \
            when evaluating the test dataset where a cherry leaf was \
                predicted to be healthy when it was infected, and 1 when it was \
                predicted to be infected when it was healthy."
        )

    st.write("---")

    st.write("### Conclusions")

    st.info(
        "The ML model/pipeline has been successful:\n"
        "- Business Requirement 1: \n\n This requirement is met as the Leaves \
            Visualizer page \n"
        "shows that a cherry leaf that is healthy can be differentiated from \
            one that contains powdery mildew.\n"
        "- Business Requirement 2: \n\n This requirement is met as the Powdery \
            Mildew Detection page \n"
        "will predict if a cherry tree is healthy or contains powdery mildew \
            with a 99% accuracy rate.")

    st.write("---")
    st.write("---")
