# Vertex AI

## Data preparation and feature engineering

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

### Questions on Data preparation and feature engineering

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


### Model training

- **Data Preparation and Model Training:**
  - Data readiness is like preparing ingredients for cooking.
  - Model training and evaluation are akin to experimenting with and tasting recipes.
  - This stage can be iterative for optimal results.

- **Defining AI and Machine Learning:**
  - Artificial Intelligence (AI) encompasses computer activities mimicking human intelligence.
  - Machine Learning (ML) is a subset of AI focusing on supervised and unsupervised learning.
  - Deep learning is a subset of ML involving layered neural networks for in-depth learning.

- **Supervised vs. Unsupervised Learning:**
  - Supervised learning is task-driven and provides labeled data points.
  - Unsupervised learning is data-driven and identifies patterns without labels.
  - Classification and regression are major types of supervised learning.
  - Clustering, association, and dimensionality reduction are types of unsupervised learning.

- **Google Cloud ML Options:**
  - Google Cloud offers four ML options: AutoML, pre-built APIs, BigQuery ML, and custom training.
  - AutoML and pre-built APIs eliminate the need to specify a model, with Google selecting the best fit.
  - BigQuery ML and custom training require specifying models and adjusting hyperparameters.

- **Hyperparameters and AutoML:**
  - Hyperparameters are user-defined settings guiding the ML process.
  - AutoML automates hyperparameter tuning through neural architecture search.
  - Neural architecture search compares model performance against thousands of others for optimization.

### Questions on Model training

1. What is the primary purpose of supervised learning?
    - A. Identifying patterns in data
    - B. Predicting continuous numbers
    - C. Predicting categorical variables
    - D. Reducing dimensions in a dataset

2. In unsupervised learning, what is the role of each data point?
    - A. Assigned a label
    - B. Used to predict future trends
    - C. Grouped based on common characteristics
    - D. Used for clustering

3. What is a characteristic of deep learning?
    - A. Reduces the number of features
    - B. Adds layers between input and output
    - C. Predicts continuous numbers
    - D. Focuses on categorical variables

4. Which Google Cloud option does not require specifying a machine learning model?
    - A. AutoML
    - B. Pre-built APIs
    - C. BigQuery ML
    - D. Custom training

5. What are hyperparameters in machine learning?
    - A. User-defined settings guiding the ML process
    - B. Data-driven variables
    - C. Automatically tuned by AutoML
    - D. Defined by Google Cloud backend

6. What is the primary objective of dimensionality reduction in unsupervised learning?
    - A. Grouping data points
    - B. Improving model efficiency
    - C. Predicting continuous numbers
    - D. Assigning labels to data points

7. What does AutoML do automatically during the machine learning process?
    - A. Assigns hyperparameters
    - B. Defines the objective
    - C. Adjusts learning rate
    - D. Tunes hyperparameter knobs

8. In supervised learning, what is regression modeling used for?
    - A. Predicting categorical variables
    - B. Reducing dimensions in a dataset
    - C. Predicting continuous numbers
    - D. Grouping data points

9. What is the purpose of neural architecture search in AutoML?
    - A. Assigning hyperparameters
    - B. Finding the best-fit model
    - C. Defining machine learning objectives
    - D. Reducing dimensions in a dataset

10. Which of the following is not a type of unsupervised learning?
    - A. Clustering
    - B. Association
    - C. Dimensionality reduction
    - D. Regression modeling

---
#### Answers

1. C
2. C
3. B
4. A
5. A
6. B
7. D
8. C
9. B
10. D

### Model Evaluation

- **Model Evaluation in Vertex AI:**
  - Model evaluation is akin to tasting and refining a recipe during the training stage.
  - **Vertex AI provides extensive evaluation metrics** to assess model performance.

- **Confusion Matrix:**
  - Foundation for evaluating classification problems in machine learning.
  - Includes combinations of predicted and actual values for two classes.
  - True positive, true negative, false positive, and false negative combinations explained.

- **Performance Metrics - Recall and Precision:**
  - Recall: Evaluates how many positive cases were predicted correctly.
  - Precision: Assesses the accuracy of positive predictions.
  - **Recall and precision are often a trade-off,** depending on the use case.

- **Trade-off in Precision and Recall:**
  - Illustration using a fishing analogy, emphasizing the trade-off between precision and recall.

- **Adjusting Precision and Recall in Vertex AI:**
  - Vertex AI platform visualizes precision and recall curves.
  - Users can adjust based on specific problem-solving requirements.

- **Feature Importance:**
  - Displayed through a bar chart illustrating how each feature contributes to predictions.
  - **Vertex AI's Explainable AI** includes feature importance, aiding in understanding model decisions.

- **Comprehensive Functionality of Explainable AI:**
  - Part of Vertex AI, Explainable AI offers tools and frameworks for interpreting machine learning predictions.
  - Enables understanding and interpreting predictions made by machine learning models.

### Questions on Model Evaluation and Metrics in Machine Learning

1. **What is the primary purpose of the confusion matrix in machine learning?**
   - A. Identifying feature importance
   - B. Measuring model performance
   - C. Evaluating precision and recall
   - D. Adjusting precision and recall curves

2. **Which combination in a confusion matrix is considered a Type 1 Error?**
   - A. True positive
   - B. True negative
   - C. False positive
   - D. False negative

3. **What does precision measure in a machine learning model?**
   - A. True positives divided by false negatives
   - B. True positives divided by false positives
   - C. False positives divided by true positives
   - D. False positives divided by false negatives

4. **When might Gmail prioritize recall in a classification model?**
   - A. To catch potential spam emails
   - B. To ensure precision in spam detection
   - C. To block non-spam emails
   - D. To prioritize false negatives

5. **In Vertex AI, what is the purpose of visualizing precision and recall curves?**
   - A. Adjusting feature importance
   - B. Measuring feature performance
   - C. Evaluating model effectiveness
   - D. Optimizing hyperparameters

6. **What does the feature importance chart in Vertex AI illustrate?**
   - A. Model training progress
   - B. The confusion matrix
   - C. How each feature contributes to a prediction
   - D. Adjustments made to precision and recall

7. **What is the primary goal of Explainable AI in Vertex AI?**
   - A. Enhancing model accuracy
   - B. Simplifying machine learning complexity
   - C. Aiding in model interpretation and understanding
   - D. Visualizing hyperparameter tuning

8. **Which metric is calculated as true positives divided by the sum of true positive and false negatives?**
   - A. Precision
   - B. Recall
   - C. F1 score
   - D. Specificity

9. **Why is feature importance important in machine learning models?**
   - A. It determines model architecture
   - B. It influences precision and recall
   - C. It helps decide which features predict the goal
   - D. It defines hyperparameter values

10. **What does the trade-off between precision and recall imply?**
    - A. Increasing precision reduces recall
    - B. Maximizing precision may lower recall
    - C. High precision guarantees high recall
    - D. Precision and recall are always independent

#### Answers

1. B, C
2. C
3. B
4. A
5. C
6. C
7. C
8. B
9. C
10. B

### Model deployment and monitoring

- **Final Stage:** Model serving is the concluding phase of the machine learning workflow, equivalent to serving a prepared meal.
- **Model Deployment:** Involves putting the model into action, analogous to presenting food to customers.
- **Model Monitoring:** Similar to checking the efficiency of a restaurant, model monitoring ensures the system operates smoothly.
- **Model Management:** Maintains the underlying machine-learning infrastructure throughout the workflow.
- **MLOps (Machine Learning Operations):** Integrates machine-learning development with operational principles, addressing production challenges.
- **Continuous Integration, Training, and Delivery:** MLOps promotes automation and monitoring at each step, adopting DevOps principles for machine-learning models.
- **Deployment Options:**
  - **Endpoint Deployment:** Ideal for immediate, low-latency results, such as real-time recommendations based on user behavior.
  - **Batch Prediction Deployment:** Suited for scenarios where no immediate response is needed, and data is processed periodically.
  - **Offline Prediction Deployment:** Best for deploying models in specific environments off the cloud.
- **Vertex AI Pipelines:** The backbone of MLOps and Vertex AI, it automates, monitors, and governs machine-learning systems in a serverless manner.
- **Monitoring with Vertex AI Pipelines:** Offers real-time monitoring, triggering warnings if predefined thresholds are exceeded.
- **Vertex AI Workbench:** A Notebook tool enabling the definition of custom pipelines with prebuilt components, streamlining the workflow.
- **Predicting with Endpoint:** A practical lab exercise involving endpoint prediction in real-time.
- **Completion of Workflow:** Model deployment and monitoring mark the culmination of the machine learning workflow, ensuring smooth operation.
- **Analogous to Restaurant Operation:** The analogy of a restaurant operating smoothly signifies the successful execution of the machine learning process.
- **Bon Appétit:** The final touch, emphasizing the successful implementation of machine learning solutions.

### Questions on Model deployment and monitoring

1. What is the primary purpose of MLOps in the machine learning workflow?
    - A. Model serving
    - B. Data encryption
    - C. Integration with DevOps
    - D. Data visualization

2. Why is model management essential throughout the machine learning workflow?
    - A. It focuses on continuous integration
    - B. It manages machine-learning infrastructure
    - C. It prioritizes data encryption
    - D. It enhances data visualization

3. Which option is suitable for immediate results with low latency when deploying a machine-learning model?
    - A. Endpoint deployment
    - B. Batch prediction deployment
    - C. Offline prediction deployment
    - D. Data visualization deployment

4. In the context of model serving, what does model deployment compare to in a restaurant analogy?
    - A. Cooking a recipe
    - B. Checking with the waitstaff
    - C. Serving the meal to a customer
    - D. Monitoring the workflow

5. What is the backbone tool for MLOps and Vertex AI, orchestrating the machine-learning workflow in a serverless manner?
    - A. Vertex AI Workbench
    - B. Vertex AI Pipelines
    - C. Data visualization tool
    - D. DevOps integration tool

6. When is batch prediction deployment the most suitable option?
    - A. When immediate results are needed
    - B. When no immediate response is required
    - C. When deploying in a specific environment off the cloud
    - D. When practicing endpoint prediction

7. What is the primary role of Vertex AI Workbench in the machine learning workflow?
    - A. Endpoint deployment
    - B. Model monitoring
    - C. Defining custom pipelines
    - D. Data encryption

8. What is the purpose of continuous integration, continuous training, and continuous delivery in MLOps?
    - A. Enhancing data visualization
    - B. Adopting serverless architecture
    - C. Automating and monitoring each step of the ML system construction
    - D. Improving model deployment efficiency

9. What triggers warnings in Vertex AI Pipelines if something goes wrong in the production control room?
    - A. Continuous integration
    - B. Predefined thresholds
    - C. Endpoint deployment
    - D. Data visualization

10. In the machine learning workflow, what marks the completion of the process similar to a restaurant operating smoothly?
    - A. Continuous delivery
    - B. Bon appetit
    - C. Endpoint deployment
    - D. Vertex AI Pipelines

---
#### Answers

1. C
2. B
3. A
4. C
5. B
6. B
7. C
8. C
9. B
10. B
