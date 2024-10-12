# <h1 align="center">**Powdery Mildew Detector**<h1>

## Deployed version at [Powdery Mildew Detector](https://cherry-powdery-mildew-detector-1f2a15f26a31.herokuapp.com/)

# Table of Contents 
1. [Dataset Content](#dataset-content)
2. [Business Requirements](#business-requirements)
3. [Hypotheses and Validations](#hypotheses-and-validations)
4. [Rationale to Map Business Requirements to Data Visualizations and ML Tasks](#rationale-to-map-business-requirements-to-data-visualizations-and-ml-tasks)
5. [ML Business Case](#ml-business-case)
6. [Dashboard Design](#dashboard-design)
7. [Bugs](#bugs)
8. [Deployment](#deployment)
9. [Technologies used](#technologies-used)
10. [Credits](#credits)
11. [Acknowledgements](#acknowledgements)

## Dataset Content
- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Categories Included
- Healthy (2104 images)
- Powdery Mildew (2104 images)


[Back to top ⇧](#table-of-contents)

# Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

We have agreed on the following business requirements with our client:

1.  Business Requirement 1 (BR1): Data Visualization - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
    
2.  Business Requirement 2 (BR2): CNN Model for Health State Classification - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew in a dashboard.

## Epics & User Stories
To address these business requirements, we have outlined the following epics and user stories. Each user story is broken down into manageable tasks, following an agile development process.

- Epic: Information Gathering and Data Collection
    1. User story 1: As a user, I want to know the source and content of the data used in training the model to be confident in the quality of the trained model. (Business Requirements Covered: BR2)
- Epic: Data Visualization, Cleaning, and Preparation
    1. User story 1: As a client, I want to see visualizations that differentiate healthy cherry leaves from leaves affected by powdery mildew and understand the distinguishing features. (Business Requirement Covered: BR1)
    2. User story 2: As a user, I want access to the data cleaning and preparation pipeline to quickly process new data for health state classification. (Business Requirement Covered: BR2)
    3. User story 3: As a user, I want to understand the project hypotheses and how they were validated to understand the mechanisms behind health state detection. (Business Requirement Covered: BR2)
- Epic: Model Training, Optimization, and Validation
    1. User story 1: As a client, I want a reliable model to classify the health states of cherry leaves. (Business Requirement Covered: BR2)
    2. User story 2: As a technical user, I want to understand the machine learning steps used to develop the health state classification model to ensure transparency and reproducibility. (Business Requirement Covered: BR2)
    3. User story 3: As a technical user, I want to know the model performance metrics to ensure that the predictions are reliable. (Business Requirement Covered: BR2)
- Epic: Dashboard Planning, Designing, and Development
    1. User story 1: As a client, I want an interactive dashboard to display the classification results and visualize the differences between healthy leaves and those affected powdery mildew. (Business Requirements Covered: BR1, BR2)
    2. User story 2: As a user, I want interactive input widgets to provide real-time data and get health state classification results instantly. (Business Requirement Covered: BR2)
- Epic: Dashboard Deployment and Release
    1. User story 1: As a client, I want a detailed prediction report for each examined leaf to make informed decisions about disease management. (Business Requirement Covered: BR2)

[Back to top ⇧](#table-of-contents)

# Hypotheses and Validations
1. Hypothesis 1: Symptom Correlation
    - **Hypothesis:**
        - We suspect cherry leaves infected with powdery mildew have clear marks/signs, infected leaves have white powdery spots and stems, that can differentiate them from an uninfected leaf.
        - An Image Montage shows that typically a leaf infected with powdery mildew has white powdery spots and structure.
        - Average Image, Variability Image and Difference between Averages studies did not reveal any clear pattern to differentiate one from another.
    - **Validation:**
        - **Average Image Study:** Conduct an average image study to investigate the common features in healthy, and powdery mildew infected leaves.
        - **Data Annotation:** Annotate the images with specific symptoms such as leaf spots and stems.
        - **Symptom Feature Extraction:** Use image processing techniques to extract features related to these symptoms.
        - **Visualization:** Create visualizations such as heatmaps, and annotated average images to illustrate the correlation.

[Back to top ⇧](#table-of-contents)

# Rationale to Map Business Requirements to Data Visualizations and ML Tasks
1. Business Requirement 1 (BR1): Data Visualization
    - We will display the "mean" and "standard deviation" images for healthy, powdery mildew.
    - We will display the difference between average leaves.
    - We will display an image montage for healthy, powdery mildew.

2. Business Requirement 2 (BR2): CNN Model for Health State Classification
    - We want to predict if a given leaf is healthy or has powdery mildew.
    - We want to build a caterogical classifier and generate reports.

[Back to top ⇧](#table-of-contents)

# ML Business Case

## Predict Cherry Leaves Health States
**Model:** Convolutional Neural Network (CNN)

To meet the second business requirement (BR2), we will train a CNN model.
- Objective: Enable accurate identification and classification of cherry leaves health states.
- Approach: Supervised learning using a CNN to process high-resolution images.
- Success Metrics:
    - Achieve at least 97% accuracy on the validation set.
    - The model is considered a failure if it misclassifies more than 3% of the images.
- Output: A health state classification for each input image.

[Back to top ⇧](#table-of-contents)

# Dashboard Design

Page 1: Quick Project Summary
- Genaral information about the project
- Information about the Dataset
- Link to Project README file
- Information about the business requirements.

Page 2: Leaves Visualizer
- Describe Business Requirement 1
- Difference between average and variability image - Interactive visualizations to differentiate between healthy and diseased leaves.
- Difference between average Powdery Mildew Infected and average Healthy - Display mean and standard deviation images for each health category.
- Image Montage - Create a fresh montage of 24 Powdery Mildew Infected or Healthy images

Page 3: Health State Detector
- Describe Business Requirement 2
- Link to Cherry-Leaves Kaggle Dataset where you can download a set of powdery mildew infected and healthy images for live prediction.
- Upload leaf images to get real-time classification results, where you can browse for sample files or drag and drop.
- Display prediction statements and associated probabilities.
- Provide a downloadable report of the examined leaves.

Page 4: Project Hypotheses and Validation
- Present hypothesis, explanation, validation process, and conclusion.

Page 5: ML Evaluation Metrics
- Label Distribution for Training, Validation, and Test Sets:
    - Frequency counts for each label across the training, validation, and test datasets to ensure balanced representation.
- Dataset Allocation:
    - Percentage breakdown of the entire dataset across training, validation, and test sets to understand the data split.
- Performance Metrics:
    - ROC Curve: A graphical representation of the model's diagnostic ability, illustrating the true positive rate against the false positive rate at various threshold settings.
    - Confusion Matrix: A table that shows the number of true positives, true negatives, false positives, and false negatives to evaluate the model's accuracy.
- Training Progress:
    - Model History: Tracking accuracy and loss metrics over epochs to observe the model's learning process, specifically using a CNN model.
- Final Model Assessment:
    - Test Set Evaluation: Final performance results on the test set to validate the model's generalization ability and real-world applicability.

[Back to top ⇧](#table-of-contents)

# Bugs

## Known Bugs
No known bugs

## Fixed Bugs

[Back to top ⇧](#table-of-contents)

# Deployment

## Creating the Heroku App
To deploy this project on Heroku, follow these steps:
1. **Create a `requirements.txt` File**: This file should list all the dependencies the program needs to run. Heroku uses this file to install the necessary packages.
2. **Set the Python Runtime**: Create a `runtime.txt` file specifying a Python version compatible with the Heroku-20 stack.
3. **Push Changes to GitHub**: Commit and push your recent changes to GitHub.
4. **Create a Heroku App**:
   - Log into your Heroku account.
   - Click "CREATE NEW APP," provide a unique name, and select a geographical region.
5. **Add Buildpacks**: From the Settings tab, add the `heroku/python` buildpack.
6. **Deploy the App**:
   - Go to the Deploy tab, choose GitHub as the deployment method.
   - Connect to GitHub and select your project's repository.
   - Choose the branch you want to deploy and click "Deploy Branch."
7. **Enable Deploys**:
   - You can either enable automatic deploys or manually deploy by selecting "Deploy Branch."
8. **Monitor the Logs**: Wait for the logs to show the dependencies being installed and the app being built.
9. **Access the App**: Once deployed, your app will be accessible via a link like `https://your-project-name.herokuapp.com/`.
10. **Manage Slug Size**: If the slug size is too large, add unnecessary large files to the `.slugignore` file.

## Clone a GitHub Repository

To make a clone of this repository, follow these steps:

1. **Login to your GitHub account**.
2. **Go to the repository** by visiting the link: [Charlie McGoldrick Github - SpudScan Repo](https://github.com/CharlieMcGoldrick/ci-ms5-spudscan).
3. **Click the "Code" button** and then use the copy button next to the link to copy the link.
4. **In your IDE of choice, open a new terminal** and use the following clone command:
   `git clone https://github.com/CharlieMcGoldrick/ci-ms5-spudscan`

## Forking the GitHub Repository

To fork this repository, follow these steps:

1. **Log in to your GitHub account**.
2. **Go to the repository you want to fork**, which is located at: [Charlie McGoldrick Github - SpudScan Repo](https://github.com/CharlieMcGoldrick/ci-ms5-spudscan).
3. **In the top-right corner of the repository page, click on the "Fork" button**.
4. **GitHub will prompt you to select where you want to fork the repository**. Choose your personal account or organization.
5. **Wait for the forking process to complete**. Once it's done, you will be redirected to your forked repository under your GitHub account.

**NOTE**: Any changes pushed to the main branch automatically show up on the website.

[Back to top ⇧](#table-of-contents)

# Technologies used
## Platforms
- GitHub: Repository for storing the project code.
- Kaggle: Source for downloading datasets.
- Gitpod: Development environment used for writing code, committing changes, and pushing to GitHub.
- Jupyter Notebook: Utilized for editing and running code.
- Heroku: Used to deploy the project.

## Languages
- Markdown
- Python

## Main Data Analysis and Machine Learning Libraries
**numpy 1.26.4**: Utilized for array conversions.
**joblib 1.4.2**:
**matplotlib 3.9.2**: Plotted dataset distributions.
**seaborn 0.13.2**: Plotted the model's confusion matrix.
**streamlit 1.38.0**: Developed the project dashboard.
**tensorflow-cpu 2.17.0**: Used for creating the model.
**tqdm 4.66.5**:
**scipy 1.14.1**:  
**scikit-learn 1.5.2**: Applied for model evaluation.


- **matplotlib 3.3.1**: Plotted dataset distributions.
- **numpy 1.19.2**: Utilized for array conversions.
- **pandas 1.1.2**: Managed data creation and storage as dataframes.
- **tensorflow-cpu 2.6.0**: Used for creating the model.
- **keras 2.6.0**: Set model hyperparameters.
- **scikit-learn 0.24.2**: Applied for model evaluation.
-X **plotly 5.12.0**: Visualized the model's learning curve.
- **seaborn 0.11.0**: Plotted the model's confusion matrix.
- **streamlit 0.85.0**: Developed the project dashboard.

[Back to top ⇧](#table-of-contents)

# Credits

## Dataset
- The Cherry Leaves dataset is from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves)