import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from tqdm import tqdm
from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
                                                    load_model_and_predict,
                                                    resize_input_image,
                                                    plot_predictions_probabilities
                                                    )

def page_powdery_mildew_detector():
    st.info(
        f"* The client is interested in conducting a study to visually differentiate a cherry leaf"
        f" that is healthy from one that contains powdery mildew. "
        )

    st.write(
        f"* You can download a set of powdery mildew infected and healthy images for live prediction. "
        f"You can download the images from [here](https://www.kaggle.com/codeinstitute/cherry-leaves)."
        )

    st.write("---")

    images_buffer = st.file_uploader('Upload cherry leaves samples. You may select more than one.',
                                     type='jpg', accept_multiple_files=True)
   
    if images_buffer is not None:

        df_report = pd.DataFrame(columns=['Name', 'Result', 'Probability'])

        for image in tqdm(images_buffer, desc="Processing images"):
            try:
                img_pil = Image.open(image)
                st.info(f"Cherry leaves sample: **{image.name}**")
                
                img_array = np.array(img_pil)
                st.image(img_pil, caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height")

                version = 'v11'
                resized_img = resize_input_image(img=img_pil, version=version)
                pred_proba, pred_class = load_model_and_predict(resized_img, version=version)
                plot_predictions_probabilities(pred_proba, pred_class)

                df_report = df_report._append({'Name': image.name, 'Result': pred_class, 'Probability': pred_proba}, ignore_index=True)
            
            except Exception as e:
                st.error(f"Error processing image {image.name}: {str(e)}")

        st.dataframe(df_report)



        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(df_report), unsafe_allow_html=True)