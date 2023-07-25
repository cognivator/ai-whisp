
# Setting Up AWS Credentials

Setting up AWS credentials involves configuring your access keys, which consist of an Access Key ID and a Secret Access Key. These keys are used to sign programmatic requests to AWS.

Here are the steps to set up AWS credentials:

1. **Create an IAM user in your AWS account**: 

   - Sign in to the AWS Management Console and open the IAM console at https://console.aws.amazon.com/iam/.
   
   - In the navigation pane, choose Users and then choose Add user.
   
   - For User name, enter a name (for example, `myIAMUser`). 
   
   - Select the checkbox for Programmatic access, and then choose Next: Permissions.

   - Choose Attach existing policies directly.
   
   - In the policy list, select the checkbox for `AdministratorAccess`, then choose Next: Tags.
   
   - (Optional) Add metadata to the user by attaching tags as key-value pairs. Then choose Next: Review.
   
   - Review the user and permissions, then choose Create user.

2. **Download .csv file containing your new access keys**:

   - After you choose Create user in the previous step, the final page shows the user's access key ID and secret access key. 
   
   - Choose Download .csv to save the access keys to a CSV file on your computer. Store the file in a secure location.

3. **Configure your AWS credentials**: 

   You can configure your AWS credentials in several ways, but here is how to do it using the AWS CLI:
   
   - Open the Terminal.
   
   - Enter `aws configure` and press Enter.
   
   - When prompted, enter your Access Key ID and Secret Access Key from the .csv file you downloaded earlier.
   
   - For Default region name, enter the region you want to use (for example, `us-west-2` for the US West (Oregon) region).
   
   - For Default output format, enter `json`.

Your AWS credentials are now set up and ready to use with AWS CLI, Boto3, and other AWS SDKs.
