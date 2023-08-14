# Authors and Contributions
# Date: 2023-08-14 14:25:59
# -----------------------------------
# Steve Henty - DevOps, AIWhisperer
# ChatGPT-4 - AWS Solutions Architect
# Transferring Domain from Name.com to AWS

Follow these steps to transfer your domain registration from Name.com to AWS Route 53:

## At Name.com
1. **Log in to Name.com Account**: Access your Name.com account and navigate to the domain you want to transfer.
2. **Unlock the Domain**: Locate the "Domain Locking" option and disable it. This allows the domain to be transferred.
3. **Request Authorization Code**: Request the EPP authorization code (also known as the transfer code). This code is required to verify the transfer with AWS.

## At AWS Route 53
4. **Log in to AWS Console**: Open your AWS Management Console and navigate to Route 53.
5. **Initiate Domain Transfer**: Select "Registered domains," then click "Transfer Domain."
6. **Enter Domain Name**: Provide the domain name you want to transfer and click "Check."
7. **Provide Authorization Code**: Enter the EPP authorization code obtained from Name.com.
8. **Configure DNS Settings**: Follow the prompts to configure DNS settings, contact information, and any other required details.
9. **Complete Transfer**: Review the information and complete the transfer process.

## Final Steps
10. **Confirm Email**: AWS will send a confirmation email to the registered contact email address. Confirm the transfer by following the instructions in the email.
11. **Monitor Transfer Status**: Monitor the transfer status within Route 53. The transfer may take up to 7 days to complete.
12. **Secure Name.com Account**: It's advisable to re-enable the domain lock at Name.com once the transfer is confirmed.

**Note**: Transferring a domain may impact existing DNS configurations, email setups, and other services linked to the domain. Carefully review and plan the transfer to minimize disruptions.

**Important**: Ensure that the email address associated with the domain at Name.com is accessible, as it will be used for transfer confirmation.