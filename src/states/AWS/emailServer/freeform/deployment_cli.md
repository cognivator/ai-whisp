# Deployment Instructions for AWS SES with CLI

1. Install and configure the AWS CLI. You can find instructions in the AWS CLI User Guide.
2. Use the `aws ses verify-domain-identity` command to verify your domain.
3. Use the `aws ses create-receipt-rule-set` and `aws ses create-receipt-rule` commands to create a receipt rule.
4. Use the `aws ses create-smtp-credentials` command to create SMTP credentials.
5. Use the `aws ses get-send-quota` command to check your sending quota. If you need to increase your quota, you can use the `aws ses increase-send-quota` command.
6. Configure your email client with the SMTP server, port, and credentials.
