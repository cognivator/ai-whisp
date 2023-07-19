# Instructions for Configuring GMail to Use AWS SES

1. Open Gmail and click on the gear icon in the upper right corner, then see all settings.
2. Go to the 'Accounts and Import' tab.
3. Under the 'Check mail from other accounts' section, click on 'Add a mail account'.
4. Enter your email address and click 'Next'.
5. Select 'Import emails from my other account (POP3)' and click 'Next'.
6. Enter your email address in the 'Username' field and your password in the 'Password' field.
7. For the POP Server field, enter the 'Server Name' from the Amazon SES SMTP Settings. For the port, use one of the 'Ports' from the Amazon SES SMTP Settings.
8. Click 'Add Account'.
9. If you want to be able to send mail as this address, enable 'Yes' and click 'Next'.
10. Enter your name and click 'Next Step'.
11. Enter the 'Server Name' from the Amazon SES SMTP Settings for the SMTP Server field. For the port, you can use '587' with TLS, or '465' with SSL. Enter your email address in the 'Username' field and your password in the 'Password' field.
12. Click 'Add Account'.
13. Google will send a confirmation code to your email address. Enter this confirmation code and click 'Verify'.
