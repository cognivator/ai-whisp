
# Configuring Gmail with Amazon SES

Configuring your Gmail client to send and receive emails through Amazon SES involves several steps. Here's a high-level overview:

1. **Add a new account in Gmail**
   - In Gmail, click on the gear icon and select "See all settings".
   - Go to the "Accounts and Import" tab.
   - In the "Check mail from other accounts" section, click on "Add a mail account".

2. **Configure the server settings**
   - In the new window that pops up, enter your email address and click "Next".
   - Select "Import emails from my other account (POP3)" and click "Next".
   - For the "POP Server" field, enter the endpoint provided by Amazon SES. It should look like this: `email-smtp.us-west-2.amazonaws.com`.
   - For the "Port", enter `995`.
   - Enter your username and password. These are the SMTP credentials provided by Amazon SES.
   - Check the box for "Always use a secure connection (SSL) when retrieving mail".

3. **Configure Gmail to send as your SES email**
   - In the "Accounts and Import" settings, go to the "Send mail as" section and click "Add another email address".
   - In the new window, enter your name and email address, then click "Next Step".
   - For the "SMTP Server" field, enter the same endpoint as before: `email-smtp.us-west-2.amazonaws.com`.
   - For the "Port", enter `587`.
   - Enter the same SMTP credentials as before.
   - Select "Secured connection using TLS" and click "Add Account".

4. **Verify your email address**
   - Gmail will send a confirmation email to your address. Click the link in that email to confirm that you own the address.

You should now be able to send and receive emails in Gmail using your Amazon SES email address.

Please note that Amazon SES is in the AWS sandbox while you're testing, so you'll only be able to send emails to verified email addresses. To lift this restriction, you can request to move out of the sandbox.
