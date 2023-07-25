Sure, here are the general steps to transfer a domain registration to AWS using Amazon Route 53:

## Prepare to Transfer the Domain

1. Unlock the domain with the current registrar. This process varies by registrar.
2. Disable privacy for the domain. This allows AWS to send an email to confirm the transfer.
3. Obtain an authorization code (also known as EPP code or transfer code) from the current registrar.

## Submit a Transfer Request to Route 53

1. Open the Route 53 console in AWS.
2. In the navigation pane, choose "Domain Registration", then choose "Transfer Domain".
3. Enter the domain name that you want to transfer to Route 53, without www (e.g., example.com).
4. Choose "Add to cart", review your request, then choose "Continue".
5. Enter the authorization code you obtained from the current registrar, and choose "Add to cart".

## Specify Contact Information

1. Choose the "Specify different contacts" option (unless you wish to use the same contact information for all aspects of the domain), and enter the contact information for the domain.
2. Review and edit the contact information for the domain, and choose "Add to cart".

## Choose Route 53 DNS Settings and Add to Shopping Cart

1. Choose whether you want to use Route 53 as the DNS service for the domain.
2. Choose "Add to cart".

## Enable or Disable Domain Auto-Renew

1. By default, Route 53 automatically renews domain registrations each year. You can choose to disable auto-renew if you prefer.

## Request the Transfer

1. Review the request and choose "Checkout".
2. Read the terms and conditions, select the acknowledgement check box, and then choose "Purchase".

## Authorize the Transfer

1. After you submit the transfer request, AWS sends an email to the domain registrant contact's email address.
2. Follow the instructions in the email to authorize the transfer.

## Confirm the Transfer with the Current Registrar

1. Most registrars send a second email to the registrant contact's email address to confirm the transfer.
2. Follow the instructions in that email as well.

Please note that the entire process can take some time to complete due to ICANN rules and procedures set by individual registrars. If everything goes smoothly, the domain should be transferred to AWS in a few days up to a week.