# Authors and Contributions
# Date: 2023-08-14 14:25:59
# -----------------------------------
# Steve Henty - DevOps, AIWhisperer
# ChatGPT-4 - AWS Solutions Architect
# Applying the CloudFormation Template in AWS

Follow these steps to apply the CloudFormation template within your AWS account:

1. **Log in to AWS Console**: Open your AWS Management Console and sign in.

2. **Navigate to CloudFormation**: Select "Services" and then "CloudFormation" from the menu.

3. **Create a New Stack**: Click on "Create Stack" and then "With new resources (standard)."

4. **Upload the Template**: Choose "Upload a template file" and select the downloaded YAML file.

5. **Configure Stack**: Fill in the necessary parameters, such as Stack Name and any other required input based on the template.

6. **Review and Create**: Review the configuration and click "Create Stack."

7. **Monitor Progress**: You can monitor the progress and view the created resources within the "Stacks" section.

8. **Test Configuration**: Verify that the DNS settings and SSL/TLS certificates are configured correctly by accessing the domain and checking the DNS records.

**Note**: Ensure that you have the necessary permissions and that the values in the template are correctly set for your specific domain and requirements.
9. **Manage IAM User**: Navigate to the IAM dashboard in the AWS Console to manage the created IAM user. You can reset access keys, assign permissions, and more.

10. **Security Considerations**: Ensure that the IAM user's permissions are restricted to only the necessary resources and actions. Regularly review and update security configurations as needed.