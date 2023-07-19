
# Instructions for setting up IAM for the CloudFormation Stack Builder

To enable your Lambda function to interact with AWS CloudFormation and create stacks, you need to create an IAM role with the necessary permissions and assign it to your Lambda function.

Here are the steps to do that:

## Step 1: Open the IAM console

Sign in to the AWS Management Console and open the IAM console at https://console.aws.amazon.com/iam/.

## Step 2: Create a new role

In the navigation pane, choose **Roles**, and then choose **Create role**.

## Step 3: Choose AWS service as the trusted entity

On the **Create role** page, choose **AWS service**. Then, choose **Lambda** and click **Next: Permissions**.

## Step 4: Attach policies

On the **Attach permissions policies** page, search for and select the `AWSLambdaExecute` policy. This policy provides the permissions necessary for a Lambda function to execute and create logs.

Next, search for and select the `AWSCloudFormationFullAccess` policy. This policy provides full access to AWS CloudFormation, which allows your Lambda function to create, update, and delete CloudFormation stacks.

Once you've selected these policies, click **Next: Tags**.

## Step 5: Add tags (Optional)

On the **Add tags** page, you can add key-value pairs to categorize and manage your IAM role. This step is optional and you can choose **Next: Review** if you do not wish to add any tags.

## Step 6: Review and create the role

On the **Review** page, give your role a name and description. Then, choose **Create role**.

## Step 7: Assign the role to your Lambda function

Once the role is created, you can assign it to your Lambda function via the AWS Lambda console. In your function's **Execution role** settings, select **Use an existing role** and choose the role you just created.

After setting up the IAM role, your Lambda function should have the necessary permissions to create CloudFormation stacks.
