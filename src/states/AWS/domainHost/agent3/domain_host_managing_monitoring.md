
# Managing and Monitoring the DomainHost Project

## Route 53

- **Manage DNS Settings**: Use the Route 53 dashboard to update DNS records, add subdomains, or configure domain forwarding.
- **Health Checks**: View and create health checks for monitoring domain health.

## ACM (AWS Certificate Manager)

- **Manage Certificates**: View, renew, or delete SSL/TSL certificates.
- **Validation**: Monitor certificate validation status and ensure proper DNS configuration.

## CloudWatch

- **Set Up Alarms**: Create additional alarms or view metrics in the CloudWatch dashboard for monitoring domain health or certificate expirations.
- **Logs**: If specific logging is enabled, view logs in CloudWatch Log Groups.

## CloudTrail

- **Review Audit Logs**: Track changes to Route 53, ACM, and other services through CloudTrail logs stored in the specified S3 bucket.
- **Security Analysis**: Use CloudTrail logs for security auditing and analysis.
