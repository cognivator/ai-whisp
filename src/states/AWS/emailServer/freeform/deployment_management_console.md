# Deployment Instructions for AWS SES with Management Console

1. Sign in to the AWS Management Console and open the Amazon SES console at https://console.aws.amazon.com/ses/.
2. In the navigation pane, choose "Domains", and then choose "Verify a New Domain".
3. Enter the domain that you want to verify, and then choose "Verify This Domain".
4. The console will provide you with a set of DNS record entries that you need to add to your DNS provider's console. This will typically include a TXT record for domain verification, and a set of CNAME records for DKIM setup.
5. After you've added the records, the domain status on the Amazon SES console will change to "verified".
6. In the navigation pane, under "Email Receiving", choose "Rule Sets".
7. Choose "Create a Receipt Rule", and then choose "Next".
8. For "Recipient", enter the email address that you want to receive email for, and then choose "Next".
9. For "Actions", choose "Add Action", and then choose "S3".
10. In the "S3" section, for "S3 bucket", choose an existing bucket, or create a new one, and then choose "Next".
11. On the "Rule Details" page, for "Rule Name", enter a name for the rule, and then choose "Next".
12. On the "Review" page, review the settings for the rule, and then choose "Create Rule".
13. In the navigation pane, choose "Sending Statistics".
14. Under "Account Sending Statistics", choose "Request a Sending Limit Increase".
15. In the "Limit Increase Request" form, fill out the required fields and any optional fields that are relevant to your use case, and then choose "Submit".
16. In the navigation pane, under "Email Sending", choose "SMTP Settings".
17. On the "SMTP Settings" page, note the "Server Name" and "Port" settings.
18. Choose "Create My SMTP Credentials".
19. For "IAM User Name", enter a name for the IAM user, and then choose "Create".
20. Download the credentials and store them in a secure location.
21. This will depend on the specific client, but generally, you would go to the settings for the email account, and enter the following settings:
22. SMTP Server: The "Server Name" from the Amazon SES SMTP Settings.
23. Port: One of the "Ports" from the Amazon SES SMTP Settings.
24. Username and Password: The SMTP Credentials you downloaded earlier.
