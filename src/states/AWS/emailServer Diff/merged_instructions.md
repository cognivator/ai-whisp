
# Configuring Gmail with Amazon SES

1. **Open Gmail and Add a New Account**
   - Open Gmail and click on the gear icon in the upper right corner, then select "See all settings".
   - Go to the "Accounts and Import" tab.
   - In the "Check mail from other accounts" section, click on "Add a mail account".

2. **Configure the Server Settings**
   - In the new window that pops up, enter your email address and click "Next".
   - Select "Import emails from my other account (POP3)" and click "Next".
   - For the "POP Server" field, enter the endpoint provided by Amazon SES. It should look like this: `email-smtp.us-west-2.amazonaws.com`.
   - For the "Port", enter `995`.
   - Enter your username and password. These are the SMTP credentials provided by Amazon SES.
   - Check the box for "Always use a secure connection (SSL) when retrieving mail".
   - Click 'Add Account'.

3. **Configure Gmail to Send as Your SES Email**
   - In the "Accounts and Import" settings, go to the "Send mail as" section and click "Add another email address".
   - In the new window, enter your name and email address, then click "Next Step".
   - For the "SMTP Server" field, enter the same endpoint as before: `email-smtp.us-west-2.amazonaws.com`.
   - For the "Port", you can use `587` with TLS, or `465` with SSL.
   - Enter the same SMTP credentials as before.
   - Select "Secured connection using TLS" and click "Add Account".

4. **Verify Your Email Address**
   - Gmail will send a confirmation email to your address. Enter the confirmation code from this email and click 'Verify'.

You should now be able to send and receive emails in Gmail using your Amazon SES email address.

Please note that Amazon SES is in the AWS sandbox while you're testing, so you'll only be able to send emails to verified email addresses. To lift this restriction, you can request to move out of the sandbox.
