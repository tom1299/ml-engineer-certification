# Vertex AI

## AutoML Workflow and Feature Engineering Overview

- **AutoML Workflow Stages:**
    - Data preparation is the first stage.
    - It involves uploading data and preparing it for model training with feature engineering.
- **Data Type and Objective Selection:**
    - AutoML supports four data types: image, tabular, text, and video.
    - Correct selection involves checking data requirements and adding labels for training targets.
- **Labeling Process:**
    - Labels, representing training targets, are added manually or through Google's paid label service.
    - Human labellers can provide accurate labels.
- **Data Upload:**
    - Data can be uploaded from local sources, BigQuery, or Cloud Storage.
    - Practical exercises on data uploading are part of the course.
- **Feature Engineering Analogy:**
    - Feature engineering is likened to preparing ingredients before cooking.
    - It involves processing data before model training.
- **Feature Definition:**
    - Features, discussed in the BigQuery module, are factors contributing to predictions.
    - They represent independent variables or columns in a table.
- **Vertex AI Feature Store:**
    - Feature Store is a centralized repository for organizing, storing, and serving machine learning features.
    - It aggregates features from various sources, updating them in a central repository.
- **Benefits of Vertex AI Feature Store:**
    - Features are shareable, enhancing consistency.
    - Features are reusable, saving time and reducing duplicative efforts.
    - Features are scalable, providing low-latency serving.
    - Features are easy to use, facilitated by an intuitive user interface.
- **Automation in Feature Aggregation:**
    - Vertex AI automates the feature aggregation process to scale efficiently.
    - This helps engineers focus on creating features without deployment concerns.

### Questions on AutoML Workflow and Feature Engineering

1. In the AutoML workflow, what is the primary purpose of the data preparation stage?
    - A. Model training
    - B. Feature engineering
    - C. Uploading data
    - D. Data cleansing

2. What are the different types of data supported by AutoML? (Select all that apply)
    - A. Numeric
    - B. Image
    - C. Tabular
    - D. Audio
    - E. Spatial

3. How do you determine the correct data type and objective when uploading data to Vertex AI?
    - A. Random selection
    - B. Reviewing data requirements
    - C. Choosing the most complex option
    - D. Skipping the selection process

4. What is the purpose of adding labels to data in the context of machine learning?
    - A. Enhancing data visualization
    - B. Defining data types
    - C. Identifying training targets
    - D. Improving feature engineering

5. What is the function of the Vertex AI Feature Store?
    - A. Automating model deployment
    - B. Centralized storage of machine learning features
    - C. Data encryption during model training
    - D. Manual labeling of features

6. What is a feature in the context of machine learning?
    - A. An independent variable contributing to predictions
    - B. A visualization tool for data
    - C. A model deployment technique
    - D. A pre-built API in Vertex AI

7. Why is feature engineering considered challenging and tedious?
    - A. It requires advanced coding skills
    - B. It involves complex mathematical calculations
    - C. It demands manual processing of data
    - D. It is prone to data loss during the process

8. What are the benefits of Vertex AI Feature Store? (Select all that apply)
    - A. Shareable features for training or serving tasks
    - B. Manual labeling of features
    - C. Reusable features, saving time and effort
    - D. Non-scalable features
    - E. Complicated user interface

9. What does the Feature Store dictionary in Vertex AI help engineers do?
    - A. Access pre-trained models
    - B. Build a dataset using available features
    - C. Conduct data cleansing
    - D. Automate feature selection

10. In the context of feature engineering, what does it mean to say features are scalable?
    - A. They can handle large datasets
    - B. They automatically adjust to low-latency serving
    - C. They are shareable across organizations
    - D. They can be reused for multiple projects

---
#### Answers

1. C
2. B, C
3. B
4. C
5. B
6. A
7. C
8. A, C
9. B
10. B

