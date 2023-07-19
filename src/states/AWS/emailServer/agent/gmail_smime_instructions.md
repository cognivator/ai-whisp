
# Configuring S/MIME in Gmail

Gmail supports S/MIME (Secure/Multipurpose Internet Mail Extensions), a protocol used to encrypt emails and digitally sign them. Here are the instructions to enable and use S/MIME in Gmail:

1. **Enable S/MIME in Gmail**
   - You need to be using Gmail in a web browser to enable S/MIME. It's not currently possible to enable S/MIME from the Gmail app.
   - In Gmail, at the top right, click Settings (the gear icon) and then click "See all settings".
   - Click the "Accounts and Import" or "Accounts" tab.
   - In the "Send mail as" section, to the right of the address you want to use, click "Edit Info".
   - In the "Email Security" section, select "Sign outgoing messages" and "Encrypt all outgoing messages".
   - Click "Save Changes".

2. **Add a digital signature**
   - When you compose a new email, click the lock icon to the right of the recipient's email address. Note: if the lock is green and unlocked, the recipient doesn’t have S/MIME encryption.
   - The lock will turn gray and locked, meaning the email is signed.

3. **Check if an email you received is encrypted**
   - Open the email.
   - Check the icon next to the sender's name. If it's a closed padlock, the email was encrypted.

Please note that to use S/MIME, both the sender and the receiver must have S/MIME enabled. If the recipient doesn't have S/MIME enabled, you won't be able to send encrypted emails to them.
