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