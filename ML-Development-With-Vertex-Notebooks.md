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