# Dat Engineering for Streaming Data

## Big Data Challenges

- Building **scalable and reliable pipelines** is a core responsibility for data engineers in modern organizations.
- Data engineers and data scientists encounter four major challenges collectively known as the **4Vs**: **variety**, **volume**, **velocity**, and **veracity**.
- **Variety** poses the challenge of handling diverse data from different sources and formats, such as sensors for self-driving cars and points of sale data.
- Considerations for variety extend to scenarios like managing data from hundreds of thousands of self-driving car sensors, returning various formats including numbers, images, or audio.
- Another variety challenge involves points of sale data from 1,000 different stores, requiring organized alerts to downstream systems without duplicates.
- **Volume** increases the complexity, ranging from gigabytes to petabytes, necessitating evaluation of pipeline code and infrastructure scalability.
- The challenge is magnified by handling an arbitrary variety of input sources with varying data volumes.
- Ensuring that pipeline code and infrastructure can scale is crucial to preventing system crashes or performance halts.
- **Velocity** highlights the need for processing data in near real-time upon reaching the system.
- Addressing velocity challenges involves handling data that arrives late, contains bad data in the message, or requires mid-flight transformations for streaming into a data warehouse.
- **Veracity** is the fourth major challenge, referring to the quality of data in big data scenarios.
- The multidimensionality of data types and sources introduces possibilities of inconsistencies and uncertainties, emphasizing the need for data quality considerations.
- **Common considerations** for pipeline developers include managing the 4Vs effectively.
- The course aims to equip learners with the knowledge to successfully build a **streaming data pipeline** and overcome these challenges.
- The ultimate goal is for learners to understand the available tools for building effective pipelines and avoiding common pitfalls.

### Questions

#### 1. What are the 4Vs commonly associated with challenges in data engineering and data science?

a. Validation, Volume, Velocity, Variety  
b. Veracity, Variety, Velocity, Validation  
c. Variety, Volume, Velocity, Veracity  
d. Velocity, Veracity, Validation, Variety

#### 2. When handling an arbitrary variety of input sources, what is a critical consideration for data engineers?

a. Ensuring data consistency  
b. Evaluating pipeline code and infrastructure scalability  
c. Prioritizing data veracity  
d. Implementing real-time data processing

#### 3. In the context of data processing challenges, what does the term "velocity" refer to?

a. Data quality  
b. Data processing in near real-time  
c. Handling data from various sources  
d. Evaluating infrastructure scalability

#### 4. What is a potential issue related to "veracity" in big data scenarios?

a. Consistent data dimensions  
b. Inconsistencies and uncertainties in gathered data  
c. High data processing speed  
d. Real-time data visualization

#### 5. When dealing with data arriving late or requiring mid-flight transformations, which stage of the data processing pipeline is involved?

a. Data ingestion  
b. Data processing  
c. Data storage  
d. Data visualization

#### 6. What is a core responsibility of data engineers in modern organizations?

a. Real-time data visualization  
b. Building scalable and reliable pipelines  
c. Handling downstream system alerts  
d. Managing data inconsistencies

#### 7. What is the primary goal at the end of the section on data processing challenges?

a. Understanding data visualization tools  
b. Successfully building a streaming data pipeline  
c. Managing 4Vs in data engineering  
d. Improving data veracity

#### 8. Which challenge involves handling data from diverse sources and formats?

a. Velocity  
b. Veracity  
c. Volume  
d. Variety

#### 9. When evaluating pipeline code and infrastructure scalability, what data volume range must be considered?

a. Megabytes to gigabytes  
b. Gigabytes to terabytes  
c. Terabytes to petabytes  
d. Petabytes to exabytes

#### 10. What is the significance of avoiding duplicates in downstream systems when alerting about new transactions?

a. Improving data consistency  
b. Ensuring data veracity  
c. Enhancing data visualization  
d. Organizing alerts in an efficient way

### Solutions

1. c. Variety, Volume, Velocity, Veracity  
2. b. Evaluating pipeline code and infrastructure scalability  
3. b. Data processing in near real-time  
4. b. Inconsistencies and uncertainties in gathered data  
5. b. Data processing  
6. b. Building scalable and reliable pipelines  
7. b. Successfully building a streaming data pipeline  
8. d. Variety  
9. c. Terabytes to petabytes  
10. d. Organizing alerts in an efficient way


## Message oriented architecture

- **Data ingestion** is a critical early stage in data pipelines, handling large volumes of streaming data from diverse sources.
- Challenges in data ingestion, particularly from **IoT devices**, include diverse data streaming methods, potential for bad or delayed data, and difficulty in distributing event messages to the right subscribers.
- Google Cloud addresses these challenges with **Pub/Sub**, a powerful distributed messaging service designed for handling large-scale distributed architectures.
- **Pub/Sub** ensures at least once delivery of messages, operates globally by default, and provides end-to-end encryption for enhanced security.
- The architecture involves the ingestion of data into Pub/Sub, subsequent reading, storage, and broadcast to subscribers, with processing in an elastic streaming pipeline and output to analytics data warehouses like **BigQuery**.
- Connections to data visualization tools such as **Looker** and AI/ML tools like **Vertex AI** facilitate exploration, business insights, and predictions.
- A central element of **Pub/Sub** is the **topic**, serving as a decoupled channel for publishers and subscribers, enabling flexibility without affecting counterparts.
- Illustrated through a practical example, a human resources topic generates notifications to update applications when a new employee joins, showcasing the decoupling concept.
- **Pub/Sub** supports diverse inputs and outputs, even enabling the publication of events from one topic to another.
- The ultimate challenge is to reliably integrate these messages into a data warehouse, necessitating a pipeline that matches **Pub/Sub** in both scale and elasticity.
- Pub/Sub acts as an ideal solution for buffering changes in lightly coupled architectures with multiple publishers and subscribers.
- The service's support for various inputs and outputs enhances its versatility, catering to a broad spectrum of data processing requirements.
- The architecture's end-to-end flow involves global sourcing of data from devices, ingestion into Pub/Sub, processing through an elastic streaming pipeline, and outputting to analytics data warehouses.
- Connectivity to data visualization tools and AI/ML platforms extends the potential for deriving valuable insights and predictions from processed data.
- The decoupling nature of **Pub/Sub topics** allows for zero, one, or more publishers and subscribers, providing flexibility and resilience in architecture design.
- Understanding the decoupling concept is crucial for scenarios like HR topics, where multiple applications independently process notifications about new employees.
- **Pub/Sub's reliability, security, and performance features** make it a cornerstone in efficiently managing the challenges of large-scale distributed data processing.
- **Practical implementation** involves connecting downstream applications, like directory services and facilities systems, to efficiently process relevant notifications from Pub/Sub.
- **Scaling and elasticity** matching the capabilities of Pub/Sub are essential for building a robust and efficient data pipeline, ensuring seamless handling of diverse data processing requirements.
- In conclusion, Pub/Sub stands as a robust solution for data engineers and scientists, offering scalability, reliability, and flexibility in handling the intricacies of large-scale data processing architectures.

### Multiple Choice Questions

1. What is the primary purpose of data ingestion in a data pipeline? (Select all that apply)
   - A. Data analysis
   - B. Data transformation
   - C. Receiving streaming data
   - D. Structuring databases
   - E. Data visualization

2. What challenges are commonly faced in data ingestion from Internet of Things (IoT) devices? (Select all that apply)
   - A. Homogeneous data formats
   - B. Low data volume
   - C. Delayed data arrival
   - D. Limited sources
   - E. Secure communication

3. Which challenges does Pub/Sub address in distributed message-oriented architectures? (Select all that apply)
   - A. Scalability
   - B. Encryption
   - C. Reliable message delivery
   - D. Structured databases
   - E. Data transformation

4. What is the role of a topic in Pub/Sub architecture? (Select all that apply)
   - A. Data storage
   - B. Data visualization
   - C. Handling data ingestion
   - D. Decoupling publishers and subscribers
   - E. Data transformation

5. How does Pub/Sub contribute to handling changes in lightly coupled architectures? (Select all that apply)
   - A. Enforcing strict dependencies
   - B. Buffering changes
   - C. Limiting publishers
   - D. Increasing system resilience
   - E. Decreasing system resilience

6. Which Google Cloud tool is mentioned for visualizing and monitoring pipeline results? (Select all that apply)
   - A. Cloud Storage
   - B. Pub/Sub
   - C. BigQuery
   - D. Looker
   - E. Vertex AI

7. What is the significance of end-to-end encryption in Pub/Sub? (Select all that apply)
   - A. Ensuring secure data transmission
   - B. Data transformation
   - C. Handling data visualization
   - D. Structuring databases
   - E. Decoupling publishers and subscribers

8. What is the primary purpose of a fully operational pipeline in the context of Pub/Sub? (Select all that apply)
   - A. Managing data visualization
   - B. Handling data transformation
   - C. Ensuring secure data transmission
   - D. Connecting to data warehouses
   - E. Facilitating communication between applications

9. How does Pub/Sub handle scenarios where a topic has no subscribers or vice versa? (Select all that apply)
   - A. Stopping data transmission
   - B. Generating errors
   - C. Continuing without impact
   - D. Automatically creating subscribers
   - E. Pausing data processing

10. What are challenges faced when aiming to get messages reliably into a data warehouse from Pub/Sub? (Select all that apply)
    - A. Data encryption
    - B. Scalability
    - C. Data transformation
    - D. Data visualization
    - E. Matching Pub/Sub scale and elasticity

### Solutions

1. C
2. C, E
3. A, B, C
4. C, D
5. B
6. C, D
7. A
8. B, D
9. C
10. B, C, E

## Condensed Abstract: Dataflow and Apache Beam in Data Processing

- **Dataflow** plays a crucial role in piping captured streaming data into a data warehouse for analysis.
- Dataflow establishes a pipeline for processing both streaming and batch data through Extract, Transform, and Load (ETL) steps.
- In the pipeline design phase, **challenges** arise related to coding compatibility for batch and streaming data, SDK capabilities, and handling late data.
- Key questions in pipeline design include considering compatibility with both batch and streaming data, SDK features for transformations, mid-flight aggregations, and windowing, and the existence of **existing templates or solutions**.
- Apache Beam, an open-source tool, serves as a popular solution for pipeline design, offering a unified programming model for ETL, batch, and stream processing.
- Apache Beam's **unified approach** uses a single programming model for both batch and streaming data, ensuring portability across multiple execution environments like Dataflow and Apache Spark.
- Apache Beam's extensibility enables users to write and share their connectors and transformation libraries, enhancing flexibility.
- Pipeline templates provided by Apache Beam eliminate the need to build a pipeline from scratch, and the SDK supports multiple programming languages, including **Java, Python, and Go**.
- The Apache Beam SDK, a collection of development tools, simplifies pipeline creation by offering libraries for transformations and data connectors to sources and sinks.
- Apache Beam's model representation from code is portable across various runners, with Dataflow being a **popular choice** for execution.
- The unified, portable, and extensible nature of Apache Beam makes it a robust solution for overcoming challenges in building scalable data pipelines.

#### Multiple Choice Questions:

1. In the data pipeline design phase, what considerations are crucial for ensuring compatibility with both batch and streaming data?
   - A) Code refactoring
   - B) Utilizing the right SDK
   - C) Handling late data appropriately
   - D) Building from scratch

2. What is the primary role of Dataflow in a data pipeline?
   - A) Streaming data capture
   - B) Data analysis
   - C) Pipeline creation for batch and streaming data
   - D) Software development kit

3. What challenges do data engineers commonly face during the pipeline design and implementation phase?
   - A) Coding pipeline design
   - B) Scaling the pipeline
   - C) Serving the pipeline at scale
   - D) Developing data connectors

4. Why is Apache Beam considered a popular solution for pipeline design?
   - A) Open source
   - B) Unified programming model
   - C) Compatibility with Java, Python, and Go
   - D) Only supports batch processing

5. What does the term "unified" mean in the context of Apache Beam?
   - A) Using multiple programming models
   - B) Single programming model for batch and streaming data
   - C) Limited compatibility
   - D) Exclusive support for Dataflow

6. What makes Apache Beam a portable solution for data processing pipelines?
   - A) Exclusive support for Apache Spark
   - B) Compatibility with Java and Python
   - C) Limited execution environments
   - D) Unified programming model

7. What is the significance of Apache Beam's extensibility feature?
   - A) Exclusive support for Dataflow
   - B) Allows writing and sharing connectors and transformation libraries
   - C) Limited compatibility
   - D) Supports only Java

8. What advantage does Apache Beam provide by offering pipeline templates?
   - A) Eliminates the need for data connectors
   - B) Simplifies coding from scratch
   - C) Facilitates building a pipeline from nothing
   - D) Eases the pipeline creation process

9. Which programming languages can be used to write pipelines with Apache Beam?
   - A) Java
   - B) Python
   - C) Go
   - D) Ruby

10. What is the role of the Apache Beam SDK in data processing?
    - A) Execution on a single runner
    - B) Support for only batch processing
    - C) Collection of development tools
    - D) Limited libraries for transformations

#### Solutions:

1. A, B, C
2. C
3. A, B, C
4. A, B, C
5. B
6. B, C
7. B
8. B
9. A, B, C
10. C

## Key Concepts in Dataflow and Apache Beam Pipelines:

- **Apache Beam:** Enables the creation of data processing pipelines.
- **Execution Engine:** Critical for implementing pipelines, involves considerations like maintenance overhead, reliability, scaling, monitoring, and avoiding vendor lock-in.
- **Dataflow:** A fully managed service within Google Cloud for executing Apache Beam pipelines.
- **Serverless and NoOps:** Dataflow operates in a serverless and NoOps environment, automating infrastructure management, maintenance, and scaling tasks.
- **Low Maintenance Design:** Dataflow minimizes the need for manual intervention, allowing users to focus more on data analysis.
- **Tasks Performed by Dataflow:**
  - Optimization of pipeline model's execution graph.
  - Scheduling distributed work to workers with auto-scaling.
  - Auto-healing worker faults.
  - Automatic rebalancing of efforts for efficient worker utilization.
  - Outputting data, for instance, to BigQuery.
- **BigQuery Integration:** Data can be outputted to BigQuery, a powerful tool for further data analysis.
- **Dataflow Templates:** Beneficial for both experienced Java/Python developers and beginners, covering common use cases across Google Cloud products.
- **Template Categories:**
  - Streaming Templates: Process continuous or real-time data (e.g., Pub/Sub to BigQuery).
  - Batch Templates: Handle bulk data or batch load data (e.g., BigQuery to Cloud Storage).
  - Utility Templates: Address activities related to bulk compression, deletion, and conversion.
- **Continuous Growth:** The list of Dataflow templates is continuously expanding, providing solutions for various scenarios.

#### Questions:

1. When selecting an execution engine for a data processing pipeline, what considerations should be taken into account?
   - A) Amount of maintenance overhead
   - B) Reliability of infrastructure
   - C) Monitoring capabilities
   - D) Pipeline scaling approach

2. What does a NoOps environment imply in the context of data processing pipelines?
   - A) Automated maintenance
   - B) Manual scaling
   - C) Continuous monitoring
   - D) Infrastructure provisioning

3. What tasks does Dataflow perform when a job is received in a data processing pipeline?
   - A) Optimize the pipeline's execution graph
   - B) Schedule distributed work to new workers
   - C) Auto-heal worker faults
   - D) Balance efforts for efficient worker utilization

4. Which service in the Google Cloud ecosystem is specifically designed for executing Apache Beam pipelines?
   - A) Google Cloud Storage
   - B) Google Bigtable
   - C) Google Dataflow
   - D) Google BigQuery

5. What is the primary advantage of using Dataflow templates in data processing pipelines?
   - A) Efficient resource monitoring
   - B) Streamlined code development
   - C) Reduced maintenance overhead
   - D) Manual scaling options

6. In the context of Google Cloud's serverless computing, what tasks are managed on behalf of the users?
   - A) Data pipeline design
   - B) Resource provisioning
   - C) Performance tuning
   - D) Template creation

7. What types of templates are available in Dataflow for processing continuous or real-time data?
   - A) Streaming templates
   - B) Batch templates
   - C) Utility templates
   - D) Compression templates

8. Which task is NOT performed by Dataflow when processing a job in a data pipeline?
   - A) Auto-scaling
   - B) Worker fault auto-healing
   - C) Manual rebalancing
   - D) Optimization of the execution graph

9. What execution model does Dataflow operate in, allowing users to focus more on data analysis?
   - A) MultiOps
   - B) ServerOps
   - C) NoOps
   - D) HyperOps

10. What is a key benefit of Dataflow being built on Google's infrastructure?
   - A) Vendor lock-in
   - B) Reliable auto scaling
   - C) Manual maintenance
   - D) Limited scaling options

**Solutions:**

1. A, B, C, D
2. A
3. A, B, C, D
4. C
5. B, C
6. B, C
7. A
8. C
9. C
10. B

## Abstract: Visulization with Looker Studio

- **Telling a good story with data through a dashboard is crucial for the success of a data pipeline.**
- After data is in BigQuery, **Looker and Looker Studio** from Google Cloud provide solutions for easy data interaction and visualization.
- **Looker supports BigQuery and over 60 SQL databases.**
- Developers can define a semantic modeling layer using **LookML (Looker Modeling Language)**, freeing data engineers to focus on business logic across an organization.
- The Looker platform is 100% web-based, making it easy to integrate into existing workflows and share with multiple teams.
- The **Looker API allows embedding Looker reports in other applications.**
- Dashboards in Looker, like the Business Pulse dashboard, visualize data to make insights easily understandable.
- For a sales organization, dashboards can show figures like new users acquired, monthly sales trends, and year-to-date orders.
- **Looker provides various data visualization options, including area charts, line charts, Sankey diagrams, funnels, and liquid fill gauges.**
- Dashboards, such as the one monitoring New York City taxis, display total revenue, total numbers of passengers, and total number of rides over time.
- Looker allows plotting data on a map to visualize ride distribution, busy areas, and peak hours.
- **The purpose of Looker's features is to help draw insights and make informed business decisions.**
- To share dashboards, you can schedule delivery through storage services like Google Drive, Slack, or Dropbox.

**1. Which databases are supported by Looker for semantic modeling?**

- A. Only BigQuery
- B. More than 60 different SQL databases
- C. Only NoSQL databases
- D. MongoDB and Cassandra

**2. What is the primary purpose of LookML in Looker?**

- A. Allows direct SQL queries
- B. Defines logic and permissions
- C. Manages infrastructure setup
- D. Restricts data access

**3. How does Looker contribute to the collaboration of multiple teams within an organization?**

- A. Provides complex visualizations
- B. Scheduling delivery through storage services
- C. 100% web-based platform
- D. Embedding Looker reports in emails

**4. What types of charts can be used for data visualization in Looker dashboards?**

- A. Pie charts and bubble charts
- B. Area charts, line charts, and Sankey diagrams
- C. Bar charts and scatter plots
- D. Funnels and radar charts

**5. What is the significance of Looker's 100% web-based platform?**

- A. Allows direct SQL queries
- B. Makes integration into existing workflows easy
- C. Restricts sharing options
- D. Only supports on-premises deployment

**6. How can Looker dashboards be shared with a team for collaboration?**

- A. Direct SQL sharing
- B. Scheduling delivery through storage services
- C. Embedding Looker reports in emails
- D. Restricting sharing options

**7. What is the primary purpose of Looker API?**

- A. Embedding Looker reports in other applications
- B. Restricting data access
- C. Providing complex visualizations
- D. Direct SQL sharing

**8. In the context of Looker dashboards, what is a timeseries used for?**

- A. Displaying static charts
- B. Monitoring metrics over time
- C. Restricting data access
- D. Embedding SQL queries

**9. How does Looker contribute to monitoring key metrics related to New York City taxis over time?**

- A. Embedding SQL queries
- B. Displaying information in a timeseries
- C. Using only line charts
- D. Plotting data on a map

**10. What is the purpose of Looker Studio in enhancing data analysis?**

- A. Managing infrastructure setup
- B. Allows direct SQL queries
- C. Provides a 100% web-based platform
- D. Defines a semantic modeling layer

**Answers:**
1. B
2. B
3. C
4. B
5. B, C
6. B, C
7. A
8. B
9. D
10. D


---
---
# Big Data with BigQuery

## Introduction
- Explore Dataflow and Pub/Sub as Google Cloud's solutions for processing streaming data.
- Focus on BigQuery, a fully managed data warehouse that handles terabytes and petabytes of data for management decisions.
- Understand the distinction between a data warehouse and a data lake, emphasizing the structured and organized nature of a data warehouse.
- BigQuery is fully managed and serverless, allowing users to focus on SQL queries without concerns about deployment, scalability, or security.
- Key features include storage and analytics, supporting petabytes of data and offering built-in features like machine learning and geospatial analysis.
- BigQuery operates on a pay-as-you-go pricing model based on query processing and permanent table storage, with an option for flat-rate pricing.
- Data in BigQuery is encrypted at rest by default, providing security without additional customer actions.
- The platform facilitates machine learning by allowing users to write ML models directly in SQL or export datasets to other tools like Vertex AI.
- Data warehouse solution architecture involves handling real-time or batch data, processing through Pub/Sub or Cloud Storage, and using Dataflow for ETL.
- BigQuery acts as the central hub linking data processes through Dataflow and providing data access for analytics, AI, and ML tools.
- The analytics engine of BigQuery ingests, stores, analyzes, and outputs processed data for business intelligence and AI/ML tools.
- Connect visualization tools like Looker, Looker Studio, Tableau, or other BI tools to BigQuery for business or data analysts.
- Query BigQuery datasets directly from Google Sheets, performing operations like pivot tables for spreadsheet users.
- Data scientists and machine learning engineers can call data from BigQuery through AutoML or Workbench as part of Vertex AI.
- BigQuery serves as a staging area for data analytics workloads, granting access to various users for insights and decision-making.

### Questions
**1. What are the main services provided by BigQuery?**

- A. Storage
- B. Analytics
- C. Machine Learning
- D. Business Intelligence

**2. BigQuery is considered a fully managed serverless solution. What does this mean?**

- A. Users have control over the underlying infrastructure.
- B. It requires manual provisioning of resources.
- C. It manages servers in the backend without user intervention.
- D. It's limited to batch processing only.

**3. How is data pricing handled in BigQuery?**

- A. Fixed monthly billing for all users.
- B. Pay-as-you-go based on query processing and table storage.
- C. Free for a limited amount of data.
- D. Flat-rate pricing for individual queries.

**4. Which tools can be connected to BigQuery for business or data analysts?**

- A. Looker
- B. Tableau
- C. Google Sheets
- D. All of the above

**5. What is the purpose of ETL in the data warehouse solution architecture involving BigQuery?**

- A. Encrypt data at rest.
- B. Extract, Transform, and Load data.
- C. Manage server infrastructure.
- D. Connect to Pub/Sub.

**6. What is a distinguishing feature of a data warehouse compared to a data lake?**

- A. Contains raw, unorganized data.
- B. Used for advanced querying.
- C. Primarily structured and organized data.
- D. Has no specified purpose.

**7. In BigQuery, how is machine learning implemented?**

- A. Using custom Python scripts.
- B. Exporting datasets to Vertex AI.
- C. Directly writing ML models in SQL.
- D. Utilizing third-party machine learning tools.

**8. What is the primary function of the analytics engine of BigQuery in a data pipeline?**

- A. Process real-time data.
- B. Manage server infrastructure.
- C. Ingest, store, and analyze processed data.
- D. Extract data from Cloud Storage.

**9. Which challenges of big data are discussed in the text?**

- A. Variety
- B. Volume
- C. Velocity
- D. Veracity
- E. All of the above

**10. What is the role of Dataflow in the typical data warehouse solution architecture?**

- A. Encrypt data at rest.
- B. Connect to Pub/Sub.
- C. Extract, Transform, and Load data.
- D. Process data from both real-time and batch pipelines.

**Solutions:**
> *(The correct answers are indicated with an "X")*

**1.** X - A. Storage  
**2.** X - C. It manages servers in the backend without user intervention.  
**3.** X - B. Pay-as-you-go based on query processing and table storage.  
**4.** X - D. All of the above  
**5.** X - B. Extract, Transform, and Load data.  
**6.** X - C. Primarily structured and organized data.  
**7.** X - C. Directly writing ML models in SQL.  
**8.** X - C. Ingest, store, and analyze processed data.  
**9.** X - E. All of the above  
**10.** X - D. Process data from both real-time and batch pipelines.


## Storage and analysis
- **BigQuery Services:**
  - Provides fully-managed storage and SQL-based analytical engine.
  - Connected by Google's high-speed internal network for scalable storage and compute.

- **Storage and Metadata Management:**
  - Manages datasets from internal, external, multi-Cloud, and public sources.
  - Automatically replicates, backs up, and auto-scales stored data.
  - Supports querying external data sources without ingestion.

- **Data Ingestion Patterns:**
  - Three basic patterns: batch load, streaming, and generated data.
  - Batch load for one-time or scheduled operations.
  - Streaming for continuous near real-time data availability.
  - Generated data through SQL statements.

- **Data Analysis in BigQuery:**
  - Optimized for analytical queries on large datasets.
  - Handles terabytes in seconds and petabytes in minutes.
  - Supports ad hoc analysis using standard SQL.
  - Geospatial analytics with geography data types.
  - Machine learning models through BigQuery ML.
  - Interactive business intelligence dashboards using BigQuery BI Engine.

- **Query Execution in BigQuery:**
  - Default interactive queries executed as needed.
  - Batch queries queued and start when idle resources available.

### Questions:

1. What are the two main services provided by BigQuery?
   - A. Data storage
   - B. Machine learning
   - C. Analytical engine
   - D. Data visualization

2. How is BigQuery's storage and analytical engine connected?
   - A. Fiber-optic cables
   - B. Google's internal network
   - C. Public internet
   - D. Satellite links

3. Which types of data sources can BigQuery ingest from?
   - A. Internal data
   - B. Only Cloud storage
   - C. Multi-Cloud data
   - D. Only external data

4. What is a potential risk of saving and processing data separately in BigQuery?
   - A. Improved query performance
   - B. Inconsistency in data
   - C. Enhanced data security
   - D. Faster data replication

5. What are the three basic patterns for loading data into BigQuery?
   - A. Batch load
   - B. Stream load
   - C. Cloud load
   - D. Generated data load

6. How does BigQuery optimize analytical queries?
   - A. Using machine learning algorithms
   - B. By parallelizing storage and compute
   - C. Restricting query access
   - D. Minimizing data replication

7. What types of analytics features are supported by BigQuery?
   - A. Ad hoc analysis
   - B. Machine learning models
   - C.

Interactive queries
   - D. Streaming analytics

8. What is the purpose of BigQuery BI Engine?
   - A. Data replication
   - B. Business intelligence dashboards
   - C. Cloud storage management
   - D. Geospatial analytics

9. How does BigQuery handle interactive queries by default?
   - A. Execute immediately
   - B. Queue for batch processing
   - C. Schedule for later
   - D. Parallelize processing

10. What option does BigQuery provide for executing queries when resources are idle?
   - A. Batch queries
   - B. Immediate queries
   - C. Parallel queries
   - D. Stream queries

### Solutions:

1. C
2. B
3. A, C
4. B
5. A, B, D
6. B
7. A, B, D
8. B
9. A
10. A

## Using BigQuery ML to predict customer lifetime value

- **Introduction to Machine Learning Models:**
  - Types of ML models are crucial for effective learning.
  - High-quality data is essential for training models.

- **Example: Predicting Customer Lifetime Value (LTV):**
  - Customer LTV estimation is common in marketing.
  - Google Analytics ecommerce dataset is used.
  - Goal: Identify high-value customers for targeted promotions.

- **Key Fields for Analysis:**
  - Relevant fields include customer lifetime pageviews, total visits, average time spent, revenue, and transactions.
  - Columns are fed into the model to predict the label (LTV).

- **Data Preparation:**
  - Explanation of records, labels, and examples in the dataset.
  - Labels can be numeric or categorical, influencing the choice of regression model.

- **Types of Regression Models:**
  - Linear regression for numeric labels (e.g., revenue).
  - Logistic regression for categorical labels (e.g., High Value Customer).

- **Understanding Features:**
  - Columns in the dataset are referred to as features.
  - Feature engineering is the process of working with features, akin to selecting ingredients in cooking.
  - BigQuery ML automates tasks like one-hot encoding for feature preparation.

- **Data Splitting and Evaluation:**
  - BigQuery ML automatically splits data into training and evaluation sets.
  - Feature engineering and data quality evaluation are crucial tasks.

- **Predicting on Future Data:**
  - After training on historical data, the model is used to predict future datasets.
  - Successful predictions allow targeting high-value customers in real-time.

### Questions:

1. What is the primary purpose of predicting customer lifetime value (LTV) in the provided example?
   - A. Identifying high-value customers
   - B. Analyzing historical data
   - C. Improving website design
   - D. Evaluating promotional campaigns

2. In machine learning, what is the role of features in a dataset?
   - A. They are numeric variables.
   - B. They are potential ingredients for cooking.
   - C. They are categorical variables.
   - D. They are known answers from historical data.

3. What is the significance of feature engineering in machine learning?
   - A. It automates model training.
   - B. It transforms calculated fields into features.
   - C. It helps in sifting through data.
   - D. It is the process of defining data columns.

4. Which regression model is suitable for predicting a categorical variable like "High Value Customer"?
   - A. Linear regression
   - B. Logistic regression
   - C. Ridge regression
   - D. Polynomial regression

5. What is the purpose of using one-hot encoding in machine learning?
   - A. Encoding numeric data
   - B. Preparing data for model training
   - C. Converting categorical data to numeric
   - D. Enhancing dataset visualization

6. What is the term used for a single row or record in a machine learning dataset?
   - A. Example
   - B. Label
   - C. Feature
   - D. Observation

7. In machine learning, what is a label?
   - A. A correct answer from historical data
   - B. A numeric variable
   - C. A potential feature
   - D. A calculated field

8. Why is it essential to have a large number of records when training a machine learning model?
   - A. To improve feature engineering
   - B. To reduce the impact of features
   - C. To enhance data visualization
   - D. To train the model effectively

9. What task does BigQuery ML perform automatically in the machine learning process?
   - A. Feature engineering
   - B. Data splitting into training and evaluation sets
   - C. Calculating fields in SQL
   - D. Sifting through historical data

10. Which method helps in preventing the overuse of ingredients (features) in machine learning?
   - A. Feature engineering
   - B. One-hot encoding
   - C. Data splitting
   - D. Understanding data quality

### Solutions:

1. A
2. B
3. C
4. B
5. C
6. A
7. A
8. D
9. B
10. A

## Key Phases of Machine Learning Project:

- **Phase 1: Data Extraction and Loading (ETL)**
  - Extract, transform, and load data into BigQuery.
  - Utilize easy connectors from other Google products for efficient data transfer.
  - Enrich the existing data warehouse with additional sources using SQL joins.

- **Phase 2: Feature Selection and Preprocessing**
  - Select and preprocess features for the model.
  - Use SQL to create the training dataset.
  - Leverage BigQuery ML for automated preprocessing tasks, such as one-hot encoding of categorical variables.

- **Phase 3: Model Creation in BigQuery**
  - Create the machine learning model within BigQuery.
  - Use the `CREATE MODEL` command, specifying the model type and providing a SQL query with the training dataset.
  - Execute the query to initiate model training.

- **Phase 4: Model Evaluation**
  - After training, evaluate the model's performance using the `ML.EVALUATE` query.
  - Analyze key metrics, including root mean squared error for forecasting models and accuracy, precision, and recall for classification models.
  - Detailed exploration of metrics is covered in later sections of the course.

- **Phase 5: Model Deployment and Prediction**
  - Once satisfied with the model's performance, deploy it for predictions.
  - Use the `ML.PREDICT` command on the trained model.
  - Obtain predictions and the model's confidence, with the label field reflecting the model's predictions.

- **Iterative Process: Continuous Improvement**
  - Acknowledge that machine learning projects are iterative.
  - Iterate through phases to improve model performance.
  - Continuously refine features, models, and evaluations based on real-world outcomes.

- **Automation with BigQuery ML**
  - Leverage BigQuery ML's automation for certain preprocessing tasks.
  - Simplify model creation and training with integrated SQL commands.

- **Metric Analysis**
  - Understand and interpret metrics like root mean squared error, accuracy, precision, and recall.
  - Gain insights into model effectiveness and areas for improvement.

- **Confidence in Predictions**
  - Assess the model's confidence in predictions.
  - Identify the predicted outcomes in the label field, enhancing interpretability.

- **Practical Application: Predictive Analytics**
  - Apply machine learning models for practical predictive analytics.
  - Use predictions to inform decision-making processes in real-world scenarios.

- **Model Customization**
  - Tailor models to specific requirements by adjusting parameters during the creation phase.
  - Achieve a balance between model complexity and performance.

- **Data Quality Considerations**
  - Emphasize the importance of data quality in every phase.
  - Ensure that data used for training and evaluation is representative and reliable.

- **Continuous Learning and Exploration**
  - Encourage continuous learning and exploration of machine learning concepts.
  - Stay updated on advancements in BigQuery ML and related tools.

- **Predictive Labeling**
  - Identify the labeled field with predictions added, representing the model's predictive insights.
  - Use predicted labels for further analysis or downstream processes.

- **User-Friendly Commands**
  - Utilize user-friendly commands in BigQuery ML for seamless execution of machine learning tasks.
  - Foster a user-friendly environment for data scientists and practitioners.

### Multiple Choice Questions:

1. In which phase of a machine learning project do you extract, transform, and load data into BigQuery?
   - A) Phase 1
   - B) Phase 2
   - C) Phase 3
   - D) Phase 4

2. How can you enrich an existing data warehouse in BigQuery with additional data sources?
   - A) Use Python scripts
   - B) Utilize SQL joins
   - C) Use external storage only
   - D) Import data manually

3. What is the purpose of one-hot encoding in machine learning?
   - A) Enhance model interpretability
   - B) Convert categorical data to numeric
   - C) Reduce data dimensionality
   - D) Implement feature selection

4. Which command is used to create a machine learning model in Big Query?
   - A) `CREATE MODEL`
   - B) `BUILD MODEL`
   - C) `INITIATE MODEL`
   - D) `GENERATE MODEL`

5. What type of metric is commonly used to evaluate forecasting models in the ML dot evaluate query?
   - A) Precision
   - B) Area under the curve
   - C) Root mean squared error
   - D) Recall

6. During which phase do you use the ML dot predict command to make predictions with your trained model?
   - A) Phase 1
   - B) Phase 3
   - C) Phase 4
   - D) Phase 5

7. Which metric is specifically mentioned for evaluating classification models in the ML dot evaluate query?
   - A) Root mean squared error
   - B) Accuracy
   - C) Precision
   - D) Area under the curve

8. What is added to the field name in the label field after making predictions using the ML dot predict command?
   - A) Actual
   - B) Predicted
   - C) Expected
   - D) Projected

9. What role does SQL play in the machine learning project phases described?
   - A) Only used for data extraction
   - B) Used for creating training datasets
   - C) Not used in any phase
   - D) Primarily used for data visualization

10. Which phase involves analyzing metrics like root mean squared error and area under the curve?
    - A) Phase 2
    - B) Phase 3
    - C) Phase 4
    - D) Phase 5

---

### Solutions:

1. A) Phase 1
2. B) Utilize SQL joins
3. B) Convert categorical data to numeric
4. A) `CREATE MODEL`
5. C) Root mean squared error
6. D) Phase 5
7. B) Accuracy
8. B) Predicted
9. B) Used for creating training datasets
10. C) Phase 4

## Key Commands of BigQuery ML - Abstract

- **Create Model Command:**
  - Create a model using the `create model` command.
  - Overwrite existing models with `create or replace model` command.

- **Model Options:**
  - Models have options; the essential one is the **model type**.
  - Specify options using the `model options` parameter.

- **Inspecting Model Learning:**
  - Use `ml.weights` to inspect what the model learned.
  - Weights indicate feature importance for prediction (range: -1 to 1).

- **Model Evaluation:**
  - Evaluate model performance with `ml.evaluate` on a trained model.
  - Metrics vary based on the chosen model type.

- **Batch Predictions:**
  - Make batch predictions using `ml.predict` on a trained model.
  - Pass through the desired dataset for prediction.

- **Supervised Model Requirements:**
  - Need a **label field** in the training dataset or specify label columns.
  - Define model features as data columns in the `select statement`.

- **Feature Information:**
  - Use `ml.feature info` after training to get statistics and metrics.
  - Provides insights into the features used in the model.

- **Model Object:**
  - Model is an object in BigQuery stored in the dataset.
  - View information like last update and training run count.

- **Creating a New Model:**
  - Simple process: `create model`, choose type, and pass a training dataset.

- **Model Types:**
  - For numeric predictions, use **linear regression** (e.g., sales forecasting).
  - For discrete classes, use **logistic regression** (e.g., spam classification).

- **Training Progress:**
  - Monitor training progress with `ml.training info`.
  - Check weights during and after model completion.

- **Importance of Features:**
  - Understand the significance of each feature using weights.

- **Model Performance:**
  - Assess model performance against evaluation dataset with `ml.evaluate`.

- **Getting Predictions:**
  - Obtain predictions by executing `ml.predict` with the model name and prediction dataset.

---

## Building Machine Learning Models on Google Cloud: Four Options Explained

- **BigQuery ML**: Utilize SQL queries to create and execute machine learning models within BigQuery, suitable for tabular data if your data is already in BigQuery.
- **Pre-built APIs**: Leverage ready-made machine-learning models by Google through APIs, ideal for those lacking training data or machine learning expertise, supporting various data types like image, text, and video.
- **AutoML**: A no-code solution on Vertex AI, allowing you to build machine learning models through a point-and-click interface, providing simplicity and flexibility for users with little coding experience.
- **Custom Training**: Code your own machine learning environment for full control over the ML pipeline, suitable for those with ML expertise, offering flexibility but requiring substantial coding and training data.
- **Data Type Support**: BigQuery ML supports tabular data, while the other three options also support image, text, and video data.
- **Training Data Size**: Pre-built APIs don't need training data; BigQuery ML and custom training require a large amount.
- **ML and Coding Expertise**: Pre-built APIs and AutoML are user-friendly with low requirements; custom training has the highest requirement, and BigQuery ML requires SQL knowledge.
- **Flexibility in Hyperparameter Tuning**: Pre-built APIs and AutoML lack hyperparameter tuning; BigQuery ML and custom training allow experimentation with hyperparameters.
- **Time to Train Model**: Pre-built APIs require no training time, whereas the others' time depends on the project, with custom training usually taking the longest.
- **Decision Factors**: Choose based on business needs and ML expertise, BigQuery ML for SQL-savvy teams, pre-built APIs for minimal ML experience, AutoML for quick custom models, and custom training for full workflow control.
- **Business Users and Developers**: BigQuery ML for SQL familiarity, pre-built APIs for ease, AutoML for minimal coding, and custom training for full control.
- **Pre-built APIs Use Cases**: Address common perceptual tasks like vision, video, and natural language without ML expertise or development effort.
- **AutoML Advantages**: Codeless solution focusing on business problems, abstracting model architecture and ML provisioning.
- **Custom Training Control**: Vertex AI custom training for ML engineers and data scientists seeking full control over workflow, allowing training and serving custom models with code.

### Multiple Choice Questions:

1. Which Google Cloud option is best suited for developers and data scientists seeking full control over the machine learning workflow, allowing custom training and serving with code?
    - A. BigQuery ML
    - B. Pre-built APIs
    - C. AutoML
    - D. Vertex AI custom training

2. What datatype does BigQuery ML specifically support?
    - A. Tabular data
    - B. Image data
    - C. Text data
    - D. Video data

3. In which scenarios might using pre-built APIs be the most appropriate choice? (Select all that apply)
    - A. Developers and data scientists want full control.
    - B. Business users or developers have little ML experience.
    - C. Common perceptual tasks like vision, video, and natural language need addressing.
    - D. The ML model needs to be built from scratch.

4. What is a characteristic of AutoML on Vertex AI?
    - A. It requires extensive coding.
    - B. It is a codeless solution.
    - C. It exclusively supports tabular data.
    - D. It is suitable for SQL-based models.

5. Which Google Cloud option allows experimentation with hyperparameters? (Select all that apply)
    - A. Pre-built APIs
    - B. AutoML
    - C. BigQuery ML
    - D. Vertex AI custom training

6. What is a primary requirement for using BigQuery ML?
    - A. Extensive machine learning expertise
    - B. Understanding of SQL
    - C. Codeless solution
    - D. No training data required

7. When does custom training typically take the longest time?
    - A. When using pre-built APIs
    - B. When using AutoML
    - C. When building the ML model from scratch
    - D. When leveraging BigQuery ML

8. Which Google Cloud option is a no-code solution for building machine learning models?
    - A. BigQuery ML
    - B. Pre-built APIs
    - C. AutoML
    - D. Vertex AI custom training

9. What is a unique characteristic of pre-built APIs?
    - A. They require extensive ML expertise.
    - B. They address common perceptual tasks without ML expertise.
    - C. They support only tabular data.
    - D. They provide full control over the ML workflow.

10. In which scenario is BigQuery ML the most suitable option?
    - A. Little ML experience and minimal coding time
    - B. Full control of ML workflow with code
    - C. Familiarity with SQL and data in BigQuery
    - D. Addressing common perceptual tasks without ML expertise

---
#### Answers

1. D
2. A
3. B, C
4. B
5. B, C
6. B
7. C
8. C
9. B
10. C

## Building Efficient Machine Learning Models with Pre-built APIs

- **Training Data Requirement**: **Hundreds of thousands** of records are necessary for custom model training.
- **Alternative for Limited Data**: If you lack extensive data, consider starting with **pre-built APIs**.
- **Pre-built APIs as Services**: They are provided as services, acting as building blocks for applications without the complexity of custom model creation.
- **Time and Effort Saving**: Pre-built APIs save time by eliminating the need to build, curate, and train a new dataset, allowing quick progression to predictions.
- **Examples of Pre-built APIs**: 
  - **Speech-to-Text API**: Converts audio to text for data processing.
  - **Cloud Natural Language API**: Recognizes entities and sentiment in text.
  - **Cloud Translation API**: Converts text between languages.
  - **Text-to-Speech API**: Converts text to high-quality voice audio.
  - **Vision API**: Recognizes content in static images.
  - **Video Intelligence API**: Recognizes motion and action in videos.
- **Ease of Use**: Pre-built APIs allow experimentation in a browser before building a production model.

### Multi-Choice Questions:

1. What is a crucial consideration for training a custom machine learning model successfully?
    - A. Minimal training data
    - B. Thousands of records
    - C. Expensive pre-built APIs
    - D. Complex model creation

2. Why are pre-built APIs considered advantageous for starting machine learning projects? (Select all that apply)
    - A. They require minimal effort.
    - B. They act as building blocks for applications.
    - C. They eliminate the need for training data.
    - D. They are exclusive to Google datasets.

3. What is the primary function of the Cloud Natural Language API?
    - A. Converting audio to text
    - B. Recognizing entities and sentiment in text
    - C. Converting text between languages
    - D. Converting text into high-quality voice audio

4. Which pre-built API is suitable for recognizing content in static images?
    - A. Speech-to-Text API
    - B. Cloud Natural Language API
    - C. Vision API
    - D. Video Intelligence API

5. What datasets serve as the basis for Google's Vision API? (Select all that apply)
    - A. YouTube captions
    - B. Google's image datasets
    - C. Google's neural machine translation technology
    - D. Cloud Translation API datasets

6. In a browser, where can you experiment with Google's ML APIs, including the Vision API?
    - A. cloud.google.com/speech
    - B. cloud.google.com/translation
    - C. cloud.google.com/vision
    - D. cloud.google.com/natural-language

7. What is the key factor determining the effectiveness of model training?
    - A. Amount of available training data
    - B. Browser used for experimentation
    - C. Quality of pre-built APIs
    - D. Number of ML researchers at Google

8. What is the purpose of passing a JSON object request to an API when building a production model?
    - A. Training the model
    - B. Parsing the returned data
    - C. Uploading an image
    - D. Experimenting with hyperparameters

9. Which API is designed for converting text into high-quality voice audio?
    - A. Cloud Translation API
    - B. Text-to-Speech API
    - C. Video Intelligence API
    - D. Cloud Natural Language API

10. Which option is NOT a benefit of pre-built APIs?
    - A. Reduced time and effort
    - B. Building block for applications
    - C. Exclusive to Google datasets
    - D. Eliminating the need for training data

---
#### Answers

1. B
2. A, B
3. B
4. C
5. B
6. C
7. A
8. B
9. B
10. C


## AutoML

- **Introduction to AutoML**: Explores automated machine learning and its goal to streamline ML pipelines.
- **Challenges in ML Model Training**: Highlights the time-consuming nature of manual tasks such as tuning hyperparameters and model comparison.
- **Foundations of AutoML**: Built on two key technologies - **Transfer Learning** and **Neural Architecture Search**.
- **Transfer Learning Significance**: Allows leveraging pre-trained models, reducing the need for extensive data and computation time.
- **Neural Architecture Search**: Aims to find the optimal model for a project, creating an ensemble of models and selecting the best one.
- **Benefits of AutoML**: A **no-code solution** that requires minimal effort and machine learning expertise, enabling focus on defining business problems.
- **Use Cases of AutoML**: Useful for rapid prototyping, exploring new datasets, and identifying the best features in a dataset.
- **AutoML Data Types and Objectives**: Supports four types - **image, tabular, text, and video**, each solving various objectives.
- **Image Data Processing**: Involves classification and object detection models for tasks like identifying dogs in images.
- **Tabular Data Analysis**: Includes regression, classification, and forecasting models for tasks such as estimating house values or predicting economic trends.
- **Text Data Processing**: Utilizes classification, entity extraction, and sentiment analysis models for tasks like categorizing customer feedback and analyzing sentiment.
- **Video Data Analysis**: Involves classification, object tracking, and action recognition models for tasks like categorizing shots in videos and identifying specific actions.
- **Flexibility of AutoML**: Allows combining **multiple data types** and **objectives** to address complex business problems.
- **Versatility Across Domains**: A powerful tool applicable to diverse data types and objectives in machine learning.

### Multiple Choice Questions:

1. What is the primary purpose of AutoML in machine learning?
    - A. Manual model training
    - B. Hyperparameter tuning
    - C. Automated machine learning pipelines
    - D. Custom-built API models

2. What technologies are crucial for AutoML, as mentioned in the text? (Select all that apply)
    - A. Transfer Learning
    - B. Neural Architecture Search
    - C. Cloud Storage
    - D. Pre-built APIs

3. Why is transfer learning considered a powerful technique in AutoML?
    - A. It requires a large dataset.
    - B. It learns from scratch.
    - C. It leverages pre-trained models.
    - D. It reduces computation time.

4. What is the primary benefit of AutoML mentioned in the text?
    - A. Manual coding requirement
    - B. Minimal effort and no-code solution
    - C. Exclusive use of pre-built models
    - D. Emphasis on hyperparameter tuning

5. In AutoML, what is the major difference between pre-built APIs and AutoML models?
    - A. Use of transfer learning
    - B. Custom-built models in AutoML
    - C. No difference in functionality
    - D. Dependency on cloud services

6. Which data types are supported by AutoML? (Select all that apply)
    - A. Audio
    - B. Image
    - C. Tabular
    - D. Video

7. What is the primary objective of a regression model in tabular data processing?
    - A. Categorizing data
    - B. Predicting numeric values
    - C. Analyzing sentiment
    - D. Object detection

8. How does AutoML handle image data in classification models?
    - A. Returns numeric values
    - B. Identifies objects and locations
    - C. Predicts future values
    - D. Extracts entities from text

9. What is the purpose of an entity extraction model in text data processing?
    - A. Categorizing text
    - B. Analyzing sentiment
    - C. Labeling known entities
    - D. Predicting numeric values

10. In video data analysis, what does an action recognition model focus on?
    - A. Categorizing shots and segments
    - B. Analyzing sentiment in videos
    - C. Predicting numeric values in videos
    - D. Tracking objects in videos

---
#### Answers

1. C
2. A, B
3. C
4. B
5. B
6. B, C, D
7. B
8. B
9. C
10. A



## Additional information

### Difference between linear and logistic regression
Linear regression and logistic regression are both techniques used in machine learning, but they serve different purposes and are applied in distinct scenarios.

**Linear Regression:**
1. **Purpose:** Linear regression is used for predicting a continuous outcome variable (also called dependent variable) based on one or more predictor variables (independent variables).
2. **Output Type:** The output of a linear regression model is a continuous numeric value. It predicts a quantity, and the relationship between the independent and dependent variables is assumed to be linear.
3. **Example:** Predicting house prices based on features like square footage, number of bedrooms, and location.

**Logistic Regression:**
1. **Purpose:** Logistic regression is used for predicting the probability of an event occurring (binary outcome) based on one or more predictor variables.
2. **Output Type:** The output of a logistic regression model is a probability score between 0 and 1. This probability is then transformed into a binary outcome (0 or 1) using a threshold. It is commonly used for binary classification problems.
3. **Example:** Predicting whether an email is spam or not based on features like the sender, subject, and content.

In summary, the key difference lies in the type of outcome variable each model predicts. Linear regression predicts continuous values, while logistic regression predicts probabilities for binary outcomes.


TODO
====
- https://cloud.google.com/bigquery/docs/bqml-introduction