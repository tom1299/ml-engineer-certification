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