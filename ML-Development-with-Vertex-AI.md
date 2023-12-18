## Vertex AI Components

- **Unified ML Approach:**
  - Emphasizes a unified approach from ML experimentation to production.
  - Facilitates the transition of ML projects.

- **Vertex AI Dashboard:**
  - Presents a comprehensive workflow in a navigation bar.
  - Key components include Datasets, Feature Store, Data Labeling, Workbench, and Pipelines.

- **Datasets Management:**
  - Manages data loaded from Cloud storage or BigQuery.
  - Linked to ML models for streamlined integration.

- **Feature Store:**
  - Fully managed repository for ingesting, serving, and sharing ML feature values.
  - Manages infrastructure, providing storage and scalable compute resources.

- **Data Labeling Tasks:**
  - Enables human labeling requests for video, image, or text datasets.
  - Requires a sample of labeled data with specified labels and instructions.

- **Vertex AI Workbench:**
  - Jupyter notebook-based development environment for data science workflow.
  - Allows data access, processing, model training, and result sharing within Jupyter Lab.

- **Vertex AI Pipelines:**
  - Orchestrates ML workflows in a serverless manner.
  - Stores workflow artifacts using Vertex ML metadata for lineage analysis.

- **ML Pipeline Automation:**
  - Automates, monitors, and governs ML systems.
  - Artifacts analysis includes model lineage, hyperparameters, and code.

- **Components and Steps:**
  - Pipelines use components (defined by code) to create steps.
  - Portable, scalable, container-based ML pipelines.

- **Custom Training in Vertex AI:**
  - Allows for customization with various machine types.
  - Enables distributed training, hyperparameter tuning, and GPU acceleration.

- **Vertex AI Experiments:**
  - Includes Vertex Vizier for hyperparameter tuning.
  - Allows running studies and comparison using TensorBoard.

- **Model Management:**
  - Various ML models available based on use cases.
  - Vertex AI handles both AutoML models and custom-trained models.

- **Model Deployment:**
  - Vertex AI deploys trained models to endpoints for serving predictions.
  - Supports both AutoML and custom-trained models.

- **Batch Prediction:**
  - Processes grouped prediction requests with delayed responses.
  - Useful for scenarios not requiring immediate predictions.

- **Vertex ML Metadata:**
  - Stores artifacts and metadata for Vertex AI Pipelines runs.
  - Includes training, test, and evaluation data, hyperparameters, and model accuracy.

- **Continued Learning:**
  - Additional courses cover Feature Engineering and ML in the Enterprise.
  - In-depth exploration of training, testing, evaluation data, hyperparameters, and batch predictions.

#### Questions on Vertex AI Components 

1. What is the primary purpose of Vertex AI Pipelines?
   - A. Data labeling
   - B. Automate, monitor, and govern ML workflows
   - C. Jupyter notebook development
   - D. Vertex AI Feature Store management

2. Which Vertex AI component is a fully managed repository for ML feature values?
   - A. Vertex AI Pipelines
   - B. Vertex AI Workbench
   - C. Vertex ML Metadata
   - D. Vertex AI Feature Store

3. What role does Vertex Vizier play in Vertex AI Experiments?
   - A. Model deployment
   - B. Optimization service for tuning hyperparameters
   - C. Serving predictions
   - D. Batch prediction processing

4. In Vertex AI, what is the function of Batch Prediction?
   - A. Immediate response prediction
   - B. Processing accumulated data with a single request
   - C. Hyperparameter tuning
   - D. Data labeling

5. When managing and deploying models manually, what might be involved?
   - A. Writing Jupyter notebooks
   - B. Hyperparameter tuning
   - C. Application or framework development
   - D. AutoML deployment

6. What is the significance of Vertex ML Metadata in ML workflows?
   - A. Data labeling tasks
   - B. Analysis of ML workflows lineage
   - C. Jupyter notebook sharing
   - D. AutoML model deployment

7. Which step is NOT part of Vertex AI Pipelines?
   - A. Automate
   - B. Monitor
   - C. Jupyter notebook access
   - D. Govern

8. In custom training on Vertex AI, what options are available for machine types?
   - A. Only one predefined machine type
   - B. Select from a variety of machine types
   - C. Limited to CPU options
   - D. GPU types only

9. What does Vertex AI Workbench facilitate in the data science workflow?
   - A. Data labeling
   - B. Model deployment
   - C. Jupyter notebook-based development
   - D. Batch prediction processing

10. Why is Vertex AI Feature Store considered advantageous?
    - A. Requires manual infrastructure management
    - B. Ingests and shares ML feature values
    - C. Depends on external data sources
    - D. Exclusively for data labeling tasks

---
#### Answers

1. B
2. D
3. B
4. B
5. C
6. B
7. C
8. B
9. C
10. B