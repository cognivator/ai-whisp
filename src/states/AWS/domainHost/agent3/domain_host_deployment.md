
# Deploying the CloudFormation Template for DomainHost Project

## AWS Management Console

1. **Log in** to the AWS Management Console.
2. **Navigate** to the CloudFormation service.
3. Click on '**Create stack**' > '**With new resources**'.
4. **Upload** the provided CloudFormation template (final_with_monitoring.yaml).
5. **Fill in the required Parameters**:
   - DomainName: Your domain name (e.g., yourdomain.com).
   - SubdomainName: Subdomain name (e.g., subdomain).
   - IAMRolePrincipalService: Service that assumes the IAM role (e.g., ec2.amazonaws.com).
   - CloudTrailS3BucketName: S3 bucket name for CloudTrail logs.
6. **Review** the settings, acknowledge that AWS might create IAM resources, and click '**Create stack**'.
7. **Monitor** the stack creation progress in the 'Events' tab.

## AWS CLI

Alternatively, you can deploy the template using the AWS CLI:

1. **Install** the AWS CLI if not already installed.
2. **Configure** the AWS CLI with your credentials.
3. **Run** the following command, replacing the values with your specific details:
\`\`\`
aws cloudformation create-stack --stack-name DomainHostStack --template-body file://path/to/final_with_monitoring.yaml --parameters ParameterKey=DomainName,ParameterValue=yourdomain.com ParameterKey=SubdomainName,ParameterValue=subdomain ParameterKey=IAMRolePrincipalService,ParameterValue=ec2.amazonaws.com ParameterKey=CloudTrailS3BucketName,ParameterValue=your-s3-bucket-name
\`\`\`
4. **Monitor** the stack creation using the AWS Management Console or additional AWS CLI commands.

## Troubleshooting

- **Stack Creation Errors**: Check the 'Events' tab in CloudFormation for detailed error messages.
- **Domain Transfer Issues**: Review [AWS Route 53 Domain Transfer documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-to-route-53.html) for guidance.
- **Monitoring Concerns**: Refer to [CloudWatch Documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) and [CloudTrail Documentation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/what-is-cloudtrail.html) for further assistance.
