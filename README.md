# ERIC-Robotics-PSIPL

🚀 **Running the Application and Pipeline** 🚀

1. **Clone Repository**: Start by cloning the repository to your local machine using the following command:
   ```
   git clone https://github.com/Atanub707/ERIC-Robotics-PSIPL.git
   ```

2. **Install Dependencies**: Navigate to the project directory and install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```

3. **Run the Application Locally**: Launch the application locally by executing the following command:
   ```
   python app.py
   ```
   This will start the Flask development server, and you can access the application at `http://localhost:5000` in your web browser.

4. **Testing the Application**: Execute the unit tests by running:
   ```
   python unit_tests.py
   ```
   Ensure that all tests pass before proceeding with the pipeline.

5. **GitHub Actions Pipeline**: The CI/CD pipeline is triggered automatically on each push to the `main` branch. It consists of the following stages:
   - **Test**: Run unit tests to ensure code quality.
   - **Build**: Docker build stage to create the Docker image.
   - **Deploy**: Deploy the Docker image to AWS EC2 using GitHub Runner.

7. **Monitoring Pipeline**: Monitor the pipeline progress and logs on GitHub Actions dashboard. Any failures will be reported, and notifications will be sent to the relevant stakeholders.

8. **Accessing Deployed Application**: Once the deployment stage is successful, access the deployed application on the AWS EC2 instance. The application will be available at the public IP or domain name of the EC2 instance.

9. **Maintenance and Updates**: Regularly update the codebase, run tests, and monitor the pipeline to ensure smooth operation. Scale the setup as needed to accommodate larger applications.

🔧 **CI/CD Process Report** 🔧

**Overview**:
The CI/CD process for this application leverages GitHub Actions, AWS EC2, GitHub Runner, and Docker. It automates the build, test, and deployment processes, ensuring rapid and reliable delivery of software changes.

**Tool Choices**:
1. **GitHub Actions**: Chosen for its seamless integration with GitHub repositories and easy setup for CI/CD workflows.
2. **AWS EC2**: Provides scalable compute capacity in the cloud, ideal for deploying and running applications.
3. **GitHub Runner**: Used to execute CI/CD pipeline jobs on self-hosted infrastructure, offering flexibility and control over the execution environment.
4. **Docker**: Utilized for containerizing the application, enabling consistent deployment across different environments.

**CI/CD Process**:
1. **Build Stage**: Docker image is built using a Dockerfile, ensuring reproducibility and consistency.
2. **Test Stage**: Unit tests are executed for test only.
3. **Deploy Stage**: Docker image is deployed to AWS EC2 using GitHub Runner, automating the deployment process and ensuring consistency across environments.

**Scaling for Larger Applications**:
1. **Infrastructure Scaling**: Use AWS services like ECS or EKS for container orchestration to scale the application infrastructure dynamically.
2. **Pipeline Optimization**: Optimize CI/CD pipeline by parallelizing jobs, caching dependencies, and using efficient Docker build strategies.
3. **Monitoring and Observability**: Implement monitoring and logging solutions to track pipeline performance and application health, enabling proactive response to issues.
4. **Infrastructure as Code (IaC)**: Manage infrastructure configuration using tools like Terraform or AWS CloudFormation to automate provisioning and scaling of resources.

🚀 **Conclusion** 🚀
The CI/CD process described above streamlines the development and deployment of applications, enabling faster delivery of features and improvements. By leveraging GitHub Actions, AWS EC2, GitHub Runner, and Docker, the setup provides a robust foundation for building and scaling applications in a cloud-native environment.
