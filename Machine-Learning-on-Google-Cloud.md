##  What is ML ?

- **Machine Learning Overview:**
  - Deriving predictive insights from data using general algorithms.
  - Contrasting backward-looking data use (business intelligence) with predictive decision-making.

- **AI vs. Machine Learning:**
  - AI as a discipline, while machine learning is a toolset.
  - Highlighting machine learning as a means for machines to become intelligent through learning.

- **Supervised Learning:**
  - Focusing on supervised learning, starting with labeled examples (input + true answer).
  - Training models to make predictive decisions based on labeled datasets.

- **Generalization in Machine Learning:**
  - The importance of labeled data for successful machine learning.
  - Generalizing models using extensive datasets for accurate predictions on new data.

- **Training and Inference:**
  - Distinguishing between the training and inference stages in machine learning.
  - Emphasizing the need to operationalize models for production.

- **Neural Networks:**
  - Explaining the structure of neural networks with layers and functions.
  - Highlighting the historical development of neural networks and their recent impact.

- **Deep Learning at Google:**
  - Noting the widespread use of deep learning at Google.
  - Mentioning the exponential growth of deep learning models at Google.

- **Building Multiple Models:**
  - Discouraging the idea of solving complex problems with a single monolithic model.
  - Advocating for breaking down business problems into smaller, manageable models.

- **Google's ML Integration:**
  - Showcasing Google's extensive use of machine learning across various products.
  - The prevalence of multiple machine learning models within each product.

- **Evolution of Deep Learning:**
  - Illustrating the evolution of deep learning through Google Photos, Translate, and Gmail's Smart Reply.
  - Highlighting the sophistication of Smart Reply as a sequence-to-sequence model.

- **Sequence Models:**
  - Introducing the concept of sequence models in machine learning.
  - Teasing future content by mentioning the exploration of sequence models later in the course.

### Questions on topic What is ML ?

1. What is the primary purpose of using machine learning in business intelligence?
   - A. Generating historical reports
   - B. Making repeatable predictive decisions
   - C. Creating backward-looking dashboards
   - D. Analyzing monthly reports

2. In supervised learning, what does an example consist of?
   - A. Only input
   - B. Only label
   - C. Both input and label
   - D. Neither input nor label

3. When training a machine learning model, what is crucial for generalization?
   - A. Complex algorithms
   - B. Small datasets
   - C. Labeled data
   - D. Predictive decisions

4. What is a key characteristic of neural networks in machine learning?
   - A. Single-layer architecture
   - B. Lack of adjustable parameters
   - C. Mathematical functions in each layer
   - D. Static input processing

5. Why do deep neural networks historically have had only one hidden layer?
   - A. Lack of interest in deep learning
   - B. Limited computational power
   - C. Inefficient training process
   - D. Minimal impact on predictions

6. How does Google Photos utilize machine learning?
   - A. Tagging images based on user input
   - B. Uploading photos without any analysis
   - C. Automatically tagging images using ML software
   - D. Allowing users to manually tag photos

7. In solving complex business problems with machine learning, what is advised?
   - A. Building a single monolithic model
   - B. Focusing only on predictive decisions
   - C. Breaking down problems into smaller models
   - D. Avoiding the use of labeled data

8. What is Smart Reply in Gmail based on?
   - A. Simple keyword matching
   - B. Randomly generated responses
   - C. Sequence-to-sequence model
   - D. Manual input from users

9. Which Google product showcases the use of multiple intuitive models?
   - A. Google Translate
   - B. Google Photos
   - C. Gmail
   - D. Google Cloud Platform

10. What is the primary challenge when aiming to get messages reliably into a data warehouse from Pub/Sub? (Select all that apply)
   - A. Data encryption
   - B. Scalability
   - C. Data transformation
   - D. Data visualization
   - E. Matching Pub/Sub scale and elasticity

#### Answers

1. B
2. C
3. C
4. C
5. B
6. C
7. C
8. C
9. B, C
10. B, C, E

## Machine Learning for Problem Solving with Google Cloud

- **Machine Learning Overview:**
  - Deriving repeated predictive insights from data.
  - Understanding the two key stages of machine learning: training and inference.

- **Google's ML Applications:**
  - Showcasing real-world ML applications at Google, including Google Photos, Translate, and Smart Reply.

- **Challenges of Hand-Coded Rules:**
  - Discussing the limitations of hand-coded rules in complex systems.
  - Introducing the need for machine learning to handle diverse and evolving queries.

- **Introduction to RankBrain:**
  - Exploring RankBrain as a deep neural network for search ranking.
  - Emphasizing the superior performance of ML over hand-coded rules.

- **Scaling ML for Automation:**
  - Highlighting how machine learning scales better due to automation.
  - Describing how ML can continuously improve itself based on user preferences.

- **Expansive Scope of ML:**
  - Expanding the understanding of ML problem-solving beyond predictive analytics.
  - Google's perspective on being an "AI first" company, leveraging ML for automation and personalization.

- **Mindset Shift with ML:**
  - Shifting from coding rules to training models based on data.
  - Emphasizing continuous training of models with new data.

- **Addressing Evolving Problems:**
  - Adapting to changes in user queries, especially for local and complex search scenarios.
  - Introducing the ML perspective on collecting and using data for problem-solving.

- **Data Collection for ML:**
  - Discussing the importance of collecting data to convert problems into ML tasks.
  - Example scenario: Choosing a coffee shop based on distance and user preferences.

- **User Preferences in ML:**
  - Exploring the trade-off in decision-making, such as distance versus quality of coffee.
  - Emphasizing the need for labeled data to train ML models effectively.

- **AI-First Approach:**
  - Starting with heuristics but transitioning to data-driven decision-making.
  - Focusing on machine learning as an iterative process of collecting and learning from examples.

- **Balancing Learning in ML:**
  - Stressing the significance of finding the right balance in machine learning.
  - Trusting the examples and continuously improving models based on user feedback.

### Questions on: Learning for Problem Solving with Google Cloud

1. What is the primary advantage of using machine learning (ML) over hand-coded rules in Google Search?
    - A. ML is more cost-effective
    - B. ML provides automated scalability
    - C. Hand-coded rules offer better precision
    - D. ML requires less computational power

2. In the context of ML, what distinguishes Google's approach as an "AI first" company?
    - A. Focusing on predictive analytics
    - B. Prioritizing heuristic rule coding
    - C. Emphasizing automation and personalization
    - D. Using ML only for complex queries

3. When discussing ML applications, which Google product utilizes ML for image tagging without manual tagging?
    - A. Google Search
    - B. Google Translate
    - C. Google Photos
    - D. Google Smart Reply

4. In ML, what is the purpose of the training phase?
    - A. Making predictions on new data
    - B. Applying rules to inputs
    - C. Training the algorithm with labeled examples
    - D. Deploying models at scale

5. What does "RankBrain" represent in Google's context, particularly in search ranking?
    - A. A search engine algorithm
    - B. A deep neural network for search ranking
    - C. A set of heuristic rules
    - D. A manual ranking system

6. In solving complex queries using ML, what does an "AI first" company like Google rely on to make decisions?
    - A. Hand-coded rules
    - B. Predictive analytics
    - C. User preferences and data
    - D. Automated heuristics

7. When transitioning from rule-based coding to ML, what becomes the primary focus?
    - A. Writing complex rules
    - B. Training models based on data
    - C. Continuous bug fixing
    - D. Manual data collection

8. In the context of ML models, why is collecting diverse examples important?
    - A. To make the model complex
    - B. To confuse the model
    - C. To improve model training
    - D. To decrease model accuracy

9. What is the fundamental idea behind ML's approach to solving problems compared to traditional rule-based coding?
    - A. Writing exhaustive rules
    - B. Continuously training models
    - C. Minimizing data collection
    - D. Avoiding user preferences

10. Which factor is emphasized as crucial for successful ML in the given context?
    - A. Limiting data collection
    - B. Balancing good learning
    - C. Ignoring user preferences
    - D. Avoiding model adjustments

---
#### Answers

1. B
2. C
3. C
4. C
5. B
6. C
7. B
8. C
9. B
10. B

### The secret sauce

- **Organizational Know-How:**
  - The secret source for successful ML is not just code or algorithms but organizational know-how.
  - Google emphasizes sharing this organizational expertise to build effective ML systems.

- **Technical ML Skills:**
  - The course advocates developing hands-on technical ML skills to become effective ML strategists.
  - These skills mainly revolve around software and data handling, leveraging existing competencies.

- **Common Pitfalls:**
  - A list of the top 10 pitfalls organizations face in ML implementation is provided.
  - Highlights include the misconception that training ML algorithms is faster than writing software and the importance of collecting quality data.

- **Data Collection Challenges:**
  - Emphasizes the significance of data collection, stating that great ML is impossible without quality data.
  - Warns against neglecting collected data and the importance of regular reviews to prevent it from going stale.

- **Human Involvement:**
  - Stresses the necessity of keeping humans in the loop for ML systems performing critical tasks.
  - Discusses the role of humans in reviewing data, handling edge cases, and curating training inputs.

- **Value Proposition:**
  - Caution against launching a product solely based on its ML algorithm, as users often prioritize features over the underlying technology.
  - Discusses the need for continuous evaluation to ensure the ML algorithm aligns with user needs.

- **Optimizing for the Right Metrics:**
  - Advises on avoiding optimizing ML algorithms for metrics that may have unintended consequences.
  - Highlights the importance of measuring real-world impact and customer engagement to demonstrate success.

- **Ease of Use vs. Building Your Own:**
  - Discusses the trade-off between using pre-trained ML APIs for ease of use and building custom ML algorithms for specific needs.
  - Emphasizes the effort required in training and retraining ML models for ongoing improvements.

- **Retraining ML Algorithms:**
  - Challenges the misconception that ML algorithms are trained only once and highlights the need for frequent retraining.
  - Stresses the importance of making the retraining process seamless for long-term success.

- **In-House Perception Algorithms:**
  - Cautions against designing in-house perception algorithms without recognizing the challenges involved.
  - Encourages leveraging existing, highly-tuned algorithms for tasks like image or speech recognition.

- **Value Along the Journey:**
  - Acknowledges that most of the value in adopting ML comes during the journey rather than achieving a fully automated solution.
  - Highlights the improvement even if the final ML goal is not fully realized.

- **Industry Impact:**
  - Suggests that once ML becomes a part of a company's processes, it provides a significant competitive advantage.
  - Stresses the value of an ML-enabled product or process that continuously improves through data feedback loops.

### Questions on The secret sauce

1. What is the significance of starting with technical ML skills, according to the text?
   - A. To prioritize coding proficiency
   - B. To become effective ML strategists
   - C. To focus on algorithmic complexity
   - D. To avoid organizational challenges

2. When organizations first try ML, what is a common misconception mentioned in the text?
   - A. Training ML algorithms is faster than writing software.
   - B. ML algorithms don't require a software stack.
   - C. Data collection is not essential for ML success.
   - D. ML algorithms only need to be trained once.

3. What is emphasized as crucial for the success of ML but is often overlooked by practitioners?
   - A. Algorithm complexity
   - B. Data collection
   - C. Software stack
   - D. Uptime management

4. In ML systems performing core tasks, why is keeping humans in the loop considered important?
   - A. To replace ML algorithms
   - B. To mitigate organizational risks
   - C. To automate all processes
   - D. To reduce human involvement

5. Why might launching a product solely based on its ML algorithm be a challenge?
   - A. Users prioritize ML over features
   - B. Users are indifferent to ML
   - C. ML algorithms need continuous data
   - D. ML algorithms are difficult to implement

6. What caution is given regarding optimizing ML algorithms for specific metrics?
   - A. Optimizing for user engagement is always beneficial.
   - B. Optimizing for any metric is acceptable.
   - C. Perverse incentives should be considered.
   - D. Metrics should be ignored in ML.

7. Why is measuring the impact of an ML algorithm on real-world outcomes essential?
   - A. To satisfy organizational goals
   - B. To impress users with technical achievements
   - C. To secure funding for ML projects
   - D. To demonstrate success and improvements

8. What is a key distinction between using pre-trained ML APIs and building custom ML algorithms?
   - A. Pre-trained ML APIs are less effective.
   - B. Custom ML algorithms require less effort.
   - C. Pre-trained ML APIs don't need data collection.
   - D. Building custom ML algorithms is more challenging.

9. What is the misconception addressed about the training frequency of production ML algorithms?
   - A. ML algorithms are trained only once.
   - B. Training ML algorithms is a continuous process.
   - C. ML algorithms are trained solely on laptops.
   - D. Retraining ML algorithms is unnecessary.

10. Why does the text discourage designing in-house perception algorithms without caution?
   - A. It's an unnecessary step in ML implementation.
   - B. Existing algorithms are not effective.
   - C. Designing in-house algorithms is less expensive.
   - D. Challenges in perception algorithms are often underestimated.

---
#### Answers

1. B
2. A
3. B
4. B
5. D
6. C
7. D
8. D
9. B
10. D

### Path to Machine Learning: Key Concepts

- **Automation Phases:**
  - The path to machine learning involves automating various business process phases.
  - The initial phase often starts with a single individual contributor handling the task.
  - Gradually, as the task gains importance, it moves to multiple individuals working in parallel.

- **Digitization:**
  - Digitization occurs when the repeatable part of a task is automated using computers.
  - An example is ATM services, where specific interactions with users are well-automated.

- **Delegation and Formalization:**
  - Delegation involves multiple individuals performing the same task concurrently.
  - Formalization is introduced to standardize roles and bring repeatability to the task.

- **Big Data and Analytics:**
  - Big data and analytics involve using extensive data to derive operational and user insights.
  - Toyota's lean manufacturing philosophy is cited as an example of measuring and optimizing processes.

- **Machine Learning (ML):**
  - ML is the final phase in the path to ML, leveraging data from previous steps to enhance automated processes.
  - YouTube recommendations exemplify how ML continuously learns user preferences based on interactions.

- **Five Phases in ML Processes:**
  - Business processes leading to ML typically go through five phases.
  - The time spent on each phase can vary, but skipping phases is generally not advisable.

- **Individual Contributor Phase:**
  - Tasks performed by a single person characterize the individual contributor phase.
  - Receptionist duties serve as an example, showcasing informal and non-scaled activities.

- **Interactive Learning in ML:**
  - ML involves continuous learning from user interactions, such as YouTube adapting recommendations.
  - Algorithms analyze user behavior to understand preferences, enhancing the overall user experience.

- **Practical Application:**
  - Practical application is encouraged by sketching the ML path diagram for specific organizational examples.
  - Organizations are prompted to consider the phase of the ML path for their examples and explore diverse scenarios.

- **Consideration for Organizations:**
  - Organizations are advised to avoid skipping phases in the path to ML for effective implementation.
  - The importance of understanding and applying the ML path to diverse business processes is emphasized.

### Questions on Path to Machine Learning

1. **Path to ML Phases:**
   - What are the primary phases involved in the path to machine learning?
     - A. Automation
     - B. Delegation
     - C. Digitization
     - D. Big Data and Analytics
     - E. Machine Learning

2. **Individual Contributor Phase:**
   - In the individual contributor phase, tasks are performed by a single person. Which of the following characteristics apply to this phase?
     - A. Parallelization
     - B. Scalability
     - C. Informality
     - D. Formalization
     - E. Delegation

3. **Digitization Examples:**
   - Digitization involves automating the core repeatable part of a task. Which of the following are examples of digitized processes?
     - A. Cash withdrawal at an ATM
     - B. Opening a mortgage through an ATM
     - C. Store checking
     - D. Toyota's lean manufacturing philosophy
     - E. Operational and user insights

4. **Big Data and Analytics at Toyota:**
   - How does Toyota utilize big data and analytics according to the text?
     - A. Measure everything about construction facilities
     - B. Tune each part of the process for better outcomes
     - C. Implement the lean manufacturing philosophy
     - D. Conduct ultimate marketing research
     - E. Use machine learning for insights

5. **Machine Learning Improvements:**
   - In the context of machine learning, what does the algorithm automatically improve based on user interactions?
     - A. Data collection
     - B. Scalability
     - C. User engagement
     - D. Operational insights
     - E. Parallelization

6. **YouTube Recommendations Learning:**
   - How does the YouTube algorithm learn and improve recommendations in the background?
     - A. User engagement metrics
     - B. Viewer demographics
     - C. Likes and dislikes
     - D. Time spent watching videos
     - E. Implementation of formal rules

7. **Organizational Example:**
   - When considering an organizational example for the path to ML, what is encouraged?
     - A. Skipping phases for efficiency
     - B. Focusing solely on machine learning
     - C. Sketching a diagram for any business process
     - D. Ignoring the digitization phase
     - E. Exploring diverse scenarios

8. **ML Implementation Journey:**
   - Why is it advised for organizations to avoid skipping phases in the path to ML?
     - A. To simplify the process
     - B. To accelerate machine learning adoption
     - C. To ensure comprehensive implementation
     - D. To reduce the impact on core processes
     - E. To prioritize digitization over automation

9. **ML Path Application:**
   - What is the significance of applying the ML path to diverse business processes in an organization?
     - A. Enhanced scalability
     - B. Improved user engagement
     - C. Increased repeatability
     - D. Unique marketing opportunities
     - E. Accelerated lean manufacturing

10. **ML Process Understanding:**
    - How does understanding and applying the ML process contribute to organizational outcomes?
      - A. Reduced focus on automation
      - B. Limited impact on user experiences
      - C. Improved products and services
      - D. Ignoring big data and analytics
      - E. Stagnation in the delegation phase

---
#### Answers

1. A, B, C, D, E
2. C, E
3. A, C
4. A, B, C
5. C
6. C, D
7. C, E
8. C
9. C, D
10. C
