## ML Development with Vertex Notebooks

### Google Cloud Vertex AI Workbench: Managed and User-Managed Notebooks

- **Vertex AI Workbench Overview:** Explore two Jupyter notebook-based options for ML workflows: Managed Notebooks and User-Managed Notebooks.
- **Managed Notebooks:** Google-managed environments tailored for end-to-end notebook-based production environments.
- **User-Managed Notebooks:** Deep learning VM instances with high customizability for users requiring extensive control.
- **Pre-Packaged Frameworks:** Both options include JupyterLab and pre-installed deep learning packages, supporting TensorFlow and PyTorch.
- **GPU Acceleration:** GPU support for enhanced computational performance in both managed and user-managed notebooks.
- **GitHub Integration:** Seamless syncing with GitHub repositories for version control and collaboration.
- **Google Cloud Authentication:** Robust authentication and authorization mechanisms to secure both notebook options.
- **Workflow Tasks in JupyterLab:** Managed notebooks facilitate workflow-oriented tasks directly within the JupyterLab interface.
- **Hardware and Framework Control:** Determine compute resources, RAM, and framework settings within JupyterLab for managed notebooks.
- **Easy Scaling:** Scale hardware up or down within JupyterLab for efficient testing and processing of varying data sizes.
- **Custom Containers:** Add custom Docker container images alongside pre-installed frameworks in managed notebooks.
- **Data Access:** Access data within JupyterLab using Cloud Storage and BigQuery extensions for seamless integration.
- **Dataproc Integration:** Process data quickly by running notebooks on a Dataproc cluster directly from JupyterLab.
- **Automated Shutdown:** Manage costs effectively by setting up automated shutdown for idle instances of managed notebooks.
- **Customizable VM Instances:** User-managed notebooks offer customizable VM instances, allowing users to select machine type and framework.
- **Framework Changes:** Change machine type after creation, but changing the framework requires a restart of the user-managed notebook instance.
- **Health Status Monitoring:** User-managed notebooks provide built-in diagnostic tools to monitor core services, disk space, and instance logs.
- **Networking and Security:** User-managed notebooks offer VPC Service Controls and manual configurations for specific networking and security needs.

#### Questions on ml-development-with-vertex-notebooks

1. What are the key features of managed notebooks in Google Cloud Vertex AI Workbench? (Select all that apply)
    - A. Customizable VM instances
    - B. Automated shutdown for idle instances
    - C. Seamless syncing with GitHub repositories
    - D. Access to data using Cloud Storage extension

2. When considering user-managed notebooks, what is a significant advantage they offer over managed notebooks?
    - A. Automated shutdown
    - B. Customizable deep learning VM instances
    - C. Pre-installed deep learning packages
    - D. Integration with Dataproc clusters

3. Which aspects can be monitored using the diagnostic tool in user-managed notebooks? (Select all that apply)
    - A. Disk space for boots and data disks
    - B. Proxy server status
    - C. Data encryption
    - D. Core Services status

4. What is a notable benefit of using custom containers in managed notebooks?
    - A. Access to data in JupyterLab
    - B. Integration with Dataproc clusters
    - C. Addition of common data science frameworks
    - D. Inclusion of pre-installed deep learning packages

5. In managed notebooks, where can you determine compute resources, such as vCPUs and GPUs, and select the framework for running code?
    - A. JupyterLab interface
    - B. Google Cloud Console
    - C. GitHub repository
    - D. Dataproc cluster settings

6. What role does VPC Service Controls play in user-managed notebooks?
    - A. Automating notebook instances
    - B. Implementing networking and security features
    - C. Determining compute resources
    - D. Managing GitHub repositories

7. Why is changing the framework on a user-managed notebook instance considered challenging?
    - A. It requires a restart of the instance
    - B. It is not supported by Google Cloud
    - C. It conflicts with Docker settings
    - D. It violates security protocols

8. What is a primary purpose of Dataproc integration in managed notebooks?
    - A. Accessing data in JupyterLab
    - B. Processing data quickly on a Dataproc cluster
    - C. Automating shutdown for idle instances
    - D. Monitoring health status using the diagnostic tool

9. Which Google Cloud service is NOT mentioned in the text but is generally relevant to machine learning workflows?
    - A. Cloud Storage
    - B. BigQuery
    - C. Cloud Pub/Sub
    - D. Cloud Functions

10. What is a common feature between managed and user-managed notebooks in terms of authentication and authorization?
    - A. Use of VPC Service Controls
    - B. Integration with GitHub repositories
    - C. Protected by Google Cloud authentication and authorization
    - D. Access to data using Cloud Storage extension

---
#### Answers

1. B, C, D
2. B
3. A, B, D
4. C
5. A
6. B
7. A
8. B
9. D
10. C

### Best Practices for Machine Learning with Vertex AI notebooks

- **Data Preparation Best Practices:**
  - Extract and convert data from source systems, optimizing for ML training.
  - Store tabular data in BigQuery for optimal performance.
  - Store materialized data for speed, avoiding views or subqueries.
  - Optimize storage of image, video, audio, and unstructured data in cloud storage.

- **Data Labeling and Management:**
  - Use Vertex Data Labeling for unstructured data, involving human labelers.
  - Avoid storing data in block storage or reading directly from databases like Cloud SQL.
  - Leverage cloud storage buckets and directories for efficient data grouping.

- **Vertex AI Feature Store:**
  - Search existing features in Vertex AI Feature Store.
  - Fetch features from the store or create new features for structured data.
  - Set up periodic jobs for updating feature values.

- **Training Model with Vertex AI:**
  - Use Vertex Training service for large datasets and distributed training.
  - Utilize pre-built algorithms or bring custom code for training.
  - Simplify training with pre-built containers and cloud storage.

- **Vertex Explainable AI:**
  - Gain insights into model predictions with feature attributions.
  - Supports custom-trained models based on tabular and image data.

- **Hyperparameter Tuning:**
  - Use automated hyperparameter tuning provided by Vertex Training.
  - Eliminate manual adjustments to find optimal hyperparameter values.

- **Workbench Notebooks:**
  - Evaluate and understand models using Workbench Notebooks.
  - Utilize What-If Tool (WIT) and Language Interpretability Tool (LIT) for bias analysis.

- **Vertex AI TensorBoard:**
  - Track experiment metrics, visualize model graphs, and project embeddings.
  - Collaborate easily with a cost-effective, secure solution for experiment tracking.


### Questions on best-practices-for-machine-learning-with-vertex-ai-notebooks

1. What is a recommended practice for optimizing cloud storage for image, video, audio, and unstructured data used in machine learning?
   - A. Store data in small individual files.
   - B. Combine many individual files into large container formats.
   - C. Use views or subqueries for efficient training data.
   - D. Optimize storage for maximum file count.

2. When working with tabular data in machine learning, why does Google recommend storing all data in BigQuery?
   - A. BigQuery offers the lowest cost for storage.
   - B. It simplifies project structure.
   - C. BigQuery ensures maximum speed for training data.
   - D. It provides built-in support for materialized data.

3. What is a key advantage of using Vertex AI Data Labeling for unstructured data?
   - A. Automated data extraction
   - B. Integration with block storage
   - C. Seamless cloud storage optimization
   - D. Human-provided labels for data

4. Which of the following is NOT a best practice for training a machine learning model with Vertex AI?
   - A. Utilizing pre-built algorithms
   - B. Using the vertex training service for larger datasets
   - C. Running training jobs directly from virtual machine hard-disks
   - D. Employing pre-built containers for training simplicity

5. How does Vertex AI Feature Store contribute to effective model training with structured data?
   - A. It provides automated hyperparameter tuning.
   - B. Features can be fetched for training labels using batch serving.
   - C. It replaces the need for Workbench Notebooks.
   - D. It offers direct integration with Cloud SQL.

6. Why is using cloud storage buckets and directories recommended for data management in machine learning?
   - A. To optimize training speed
   - B. For efficient data grouping
   - C. To minimize storage costs
   - D. To automate data labeling

7. What role does Vertex Explainable AI play in the machine learning implementation process?
   - A. It provides insights into model predictions.
   - B. It automates feature extraction.
   - C. It replaces hyperparameter tuning.
   - D. It offers seamless collaboration in Notebooks.

8. How does hyperparameter tuning enhance the machine learning modeling process?
   - A. It automates model deployment.
   - B. It removes the need for manual hyperparameter adjustments.
   - C. It optimizes cloud storage costs.
   - D. It enables real-time model predictions.

9. What functionality does Vertex AI TensorBoard provide for machine learning experiments?
   - A. Efficient data labeling
   - B. Automated feature extraction
   - C. Seamless collaboration between data scientists
   - D. Tracking experiment metrics and visualizing model graphs

10. In machine learning, why is using pre-built containers in Vertex Training considered simpler than creating custom Docker images?
    - A. Pre-built containers offer better performance.
    - B. Custom Docker images are not supported.
    - C. It simplifies the packaging and deployment process.
    - D. Pre-built containers are less secure.

---
#### Answers

1. B
2. C
3. D
4. C
5. B
6. B
7. A
8. B
9. D
10. C

### Best Practices for Data Processing and Machine Learning

- **Overview of Data Preprocessing:**
  - Preprocessed features are essential for model training and evaluation.
  - Best practices involve using **BigQuery for tabular data** and **Dataflow for unstructured data processing**.

- **Data Processing with BigQuery:**
  - Utilize BigQuery for processing and transformation steps with tabular data.
  - Employ **BigQuery ML in BigQuery** when working with machine learning.

- **Managed Datasets in Vertex AI:**
  - Managed datasets in Vertex AI establish a clear link between data and models.
  - Provide descriptive statistics and automatic/manual splitting into train, test, and validation sets.

- **Considerations for Unstructured Data:**
  - For large volumes of unstructured data, use Dataflow with the Apache Beam model.
  - Convert unstructured data into binary formats like **TF record for improved data ingestion** during training.

- **Data Transformations with Dataflow:**
  - Use Dataflow and the pandas library for transformations not expressible in Cloud SQL or for streaming.

- **TensorFlow Extended (TFX) for Model Development:**
  - Use TensorFlow Extended for preparing data for training.
  - TensorFlow Transform, a TFX component, facilitates defining and executing preprocessing functions.

---

### Questions on Data Preprocessing and Machine Learning Best Practices

1. What is a recommended best practice for processing tabular data in Google Cloud?
   - A. Use Dataflow
   - B. Utilize BigQuery
   - C. Employ pandas library
   - D. Opt for managed datasets

2. When dealing with large volumes of unstructured data, which tool in Google Cloud is suggested for conversion into binary formats like TF record?
   - A. TensorFlow Extended (TFX)
   - B. Cloud SQL
   - C. Dataflow
   - D. Vertex AI

3. In machine learning, what is TensorFlow Transform primarily used for?
   - A. Data encryption
   - B. Model training
   - C. Data preprocessing
   - D. Data visualization

4. Which component of TensorFlow Extended (TFX) allows for defining and executing preprocessing functions?
   - A. TensorBoard
   - B. TensorFlow Transform
   - C. BigQuery ML
   - D. Cloud SQL

5. When is it advisable to use managed datasets in Vertex AI?
   - A. For maximum control over data splitting
   - B. When lineage between data and model is not critical
   - C. When using TensorFlow Extended
   - D. For better performance in data ingestion

6. What is the recommended Google Cloud tool for processing unstructured data using the Apache Beam programming model?
   - A. Cloud Dataflow
   - B. Vertex AI
   - C. BigQuery
   - D. Cloud SQL

7. Which Google Cloud service is suitable for converting unstructured data into binary formats for improved data ingestion during training?
   - A. Vertex AI
   - B. Cloud SQL
   - C. Dataflow
   - D. BigQuery

8. What is the purpose of TensorFlow Extended (TFX) in machine learning?
   - A. Data preprocessing
   - B. Model serving
   - C. Hyperparameter tuning
   - D. Data encryption

9. When using TensorFlow for model development, what tool within TensorFlow Extended is recommended for preparing data for training?
   - A. TensorBoard
   - B. TensorFlow Transform
   - C. BigQuery ML
   - D. Cloud SQL

10. Which best practice involves creating a clear link between data and custom-trained models and provides descriptive statistics?
    - A. Utilizing TensorFlow Extended
    - B. Using BigQuery ML
    - C. Employing managed datasets in Vertex AI
    - D. Leveraging Cloud Dataflow

---
#### Answers

1. B
2. C
3. C
4. B
5. B
6. A
7. C
8. A
9. B
10. C

### Best Practices for Setting Up Your Machine Learning Environment

- **Notebooks for Experimentation:** Utilize notebooks for experimentation and development, covering tasks like writing code, starting jobs, running queries, and checking status.
- **Secure Set of Software:** Notebooks provide a secure set of software and access patterns by default, ensuring a safe environment for development.
- **Customizing Google Cloud Properties:** It's a common practice to customize Google Cloud properties such as network settings, cloud identity, access management, and software for a container associated with a notebook.
- **Notebook Instances for Each Team Member:** Create a new notebook instance for each member of your data science team, treating each instance as a virtual workspace.
- **Multiple Notebooks Instances for Different Projects:** If a team member is involved in multiple projects with different dependencies, it's recommended to use multiple notebook instances for each project.
- **Stopping Instances for Inactivity:** Stop notebook instances when they're not in use to optimize resource utilization and costs.
- **Securing Personally Identifiable Information (PII):** Explore the notebook security blueprint and the guide on protecting PII data to apply data governance and security policies.
- **Deployable Blueprint on GitHub:** Access the accompanying deployable blueprint on GitHub for practical implementation of security policies.
- **Storing Prepared Data:** Store prepared data in the same Google Cloud project where your model is stored to ensure accessibility and reproducibility.
- **Ensuring Data Access for Modeling:** Storing data and models in the same project ensures that your AI project has access to all required datasets, minimizing breaks in reproducibility.
- **Organization-Specific Data Storage:** Different parts of your organization may store data in different projects, necessitating coordination for seamless data access.
- **Enhancing Performance and Reducing Costs:** Comprehensive guidelines for enhancing the performance and reducing costs in machine learning workloads are beyond the scope of this course.
- **Use of Vertex SDK for Python:** Leverage the Vertex SDK for Python to streamline machine learning workflows.
- **Consideration for Team Members in Multiple Projects:** For team members engaged in multiple projects, especially with diverse dependencies, the use of multiple notebook instances is recommended.
- **Optimizing Resource Usage:** Stopping notebook instances during periods of inactivity helps optimize resource usage and reduce associated costs.
- **Guidance on Protecting PII Data:** Explore the notebook security blueprint and associated guidance for securing personally identifiable information (PII) in your machine learning workflows.
- **Reproducibility with Stored Data:** Storing prepared data in the same project as your model contributes to reproducibility and consistent access to required datasets.
- **Organization-Wide Data Storage:** Address the challenge of different parts of your organization storing data in various projects, emphasizing the need for coordination.
- **Performance Enhancement and Cost Reduction:** Enhancing the performance and decreasing the cost of machine learning workloads is a broad topic, extending beyond the scope of this course.


### Questions on Setting Up Machine Learning Environment

1. What is a common practice for customizing Google Cloud properties associated with a notebook?
    - A. Modifying data encryption
    - B. Customizing network settings
    - C. Adjusting cloud identity
    - D. Tweaking data visualization
    - E. Managing software for a notebook container

2. Why is creating a new notebook instance for each data science team member recommended?
    - A. To simplify cloud identity management
    - B. To ensure access to raw data
    - C. To provide a secure set of software
    - D. To optimize performance
    - E. To enhance data visualization

3. What is the purpose of stopping notebook instances when they're not in use?
    - A. To reduce costs
    - B. To improve data transformation
    - C. To enhance data governance
    - D. To prevent data visualization issues
    - E. To optimize cloud identity

4. Which security aspect is addressed by the notebook security blueprint and protecting PII data guide?
    - A. Data transformation
    - B. Notebook customization
    - C. Protection of personally identifiable information (PII)
    - D. Data governance
    - E. Network settings adjustment

5. Why might multiple notebook instances be recommended for a team member involved in multiple projects?
    - A. To optimize data visualization
    - B. To separate different dependencies
    - C. To enhance cloud identity
    - D. To simplify data governance
    - E. To secure PII in notebooks

6. What is the purpose of storing prepared data in the same Google Cloud project as the model?
    - A. To reduce data transformation efforts
    - B. To ensure access to required datasets
    - C. To enhance cloud identity management
    - D. To optimize performance
    - E. To streamline data governance

7. Which part of the organization may store data in different projects?
    - A. Data transformation team
    - B. Cloud identity management team
    - C. Data science team
    - D. Machine learning models team
    - E. Different departments or units

8. What is considered out of scope for the discussed course?
    - A. Customizing Google Cloud properties
    - B. Enhancing performance of machine learning workloads
    - C. Data transformation best practices
    - D. Stopping notebook instances
    - E. Deployable blueprint on GitHub

9. How does creating a new notebook instance contribute to virtual workspace management?
    - A. Simplifying data governance
    - B. Enhancing cloud identity
    - C. Treating each instance as a separate workspace
    - D. Optimizing performance
    - E. Securing personally identifiable information (PII)

10. What does the notebook security blueprint aim to provide guidance on?
    - A. Applying data governance
    - B. Enhancing data visualization
    - C. Optimizing cloud identity
    - D. Protecting personally identifiable information (PII)
    - E. Adjusting network settings

---
#### Answers

1. B, C, E
2. C, D, E
3. A
4. C, D
5. B, E
6. B, D
7. E
8. B
9. C
10. D