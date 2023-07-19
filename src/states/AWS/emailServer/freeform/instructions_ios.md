# Instructions for Configuring iOS Mail to Use AWS SES

1. Open the Settings app on your iOS device.
2. Scroll down and tap on 'Mail', then 'Accounts', then 'Add Account'.
3. Scroll down and tap on 'Other', then 'Add Mail Account'.
4. Enter your name, email address, password, and a description for your account, then tap 'Next'.
5. Select 'POP' at the top of the screen.
6. Under 'Incoming Mail Server', enter the 'Server Name' from the Amazon SES SMTP Settings for the Host Name field. Enter your full email address for the User Name field, and your password for the Password field.
7. Under 'Outgoing Mail Server', do the same as above.
8. Tap 'Next'. If you see a message that says 'Cannot Connect Using SSL', click 'Yes' to setup the account without SSL.
9. If the email account setup is successful, tap 'Save' to complete the process.
