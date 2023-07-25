
# Domain Transfer to AWS Route 53

Transferring a domain registration to AWS involves several steps and requires coordination with your current domain registrar. Here are the general steps to transfer a domain registration to AWS Route 53:

1. **Verify that the domain is eligible for transfer**: To transfer a domain, the domain must be registered with another registrar, the domain must be unlocked, and you must have access to the domain's admin contact.

2. **Disable WHOIS privacy for the domain**: If you have enabled WHOIS privacy, disable it. If WHOIS privacy is enabled, the registrar can't see your admin email address, which prevents them from sending you the transfer authorization code.

3. **Get an authorization code (also known as an EPP code or transfer code)**: You get this code from the current registrar for the domain.

4. **Transfer the domain to Route 53**: 

   - Open the Route 53 console at https://console.aws.amazon.com/route53/.
   
   - In the navigation pane, choose "Domain Registration", "Transfer Domain".
   
   - Follow the prompts to specify the domain that you want to transfer to Route 53.

5. **Wait for email from Route 53**: Route 53 sends an email to the admin contact for the domain. The email includes a link and instructions about how to approve the transfer.

6. **Approve the transfer**: Follow the instructions in the email to approve the transfer. If you don't receive the email, check the spam or junk mail folder.

7. **Wait for the transfer to complete**: It can take 5 to 7 days for a domain transfer to complete.

For more detailed instructions, please refer to the [AWS documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-to-route-53.html).
