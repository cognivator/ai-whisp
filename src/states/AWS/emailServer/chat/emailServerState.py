State = {
  "project": {
    "name": "Email Server Deployment",
    "goals": ["Deploy an Email Server"],
    "constraints": [
      "Support Gmail as primary email client that sends and receives email.",
      "Support up to 5 domain names.",
      "Support up to 10 addresses per domain.",
      "Control spam.",
      "Support message encryption at rest and in transit.",
      "Manage addresses (add, remove, etc.) using admin processes without requiring redeployment, if possible."
    ],
    "services": {
      "AmazonSES": "Email sending and receiving",
      "AWSRoute53": "DNS management",
      "AWSIAM": "Manage addresses and admin processes",
      "AWSKMS": "Encrypt data at rest and in transit",
      "AmazonS3": "Store and retrieve mail data",
      "AWSLambda": "Automate email processing and address management",
      "AmazonWorkMail": "Managed email solution (optional)"
    },
    "codes": {
      "AmazonSES": '''
      import boto3
      ses = boto3.client('ses', region_name='us-west-2')
      response = ses.verify_email_identity(EmailAddress='user@domain.com')
      ''',

      "AWSRoute53": '''
      import boto3
      route53 = boto3.client('route53')
      response = route53.create_hosted_zone(
        Name='domain.com',
        CallerReference='2023-07-09',
        HostedZoneConfig={'Comment': 'Hosted zone for domain.com','PrivateZone': False})
      ''',

      "AWSIAM": '''
      import boto3
      import json
      iam = boto3.client('iam')
      with open('mypolicy.json', 'r') as file:
        policy_document = json.loads(file.read())
      response = iam.create_policy(PolicyName='MySamplePolicy',PolicyDocument=json.dumps(policy_document))
      ''',

      "AWSKMS": '''
      import boto3
      kms = boto3.client('kms', region_name='us-west-2')
      response = kms.create_key(Description='Key for encrypting emails',KeyUsage='ENCRYPT_DECRYPT',CustomerMasterKeySpec='SYMMETRIC_DEFAULT',Origin='AWS_KMS')
      ''',

      "AmazonS3": '''
      import boto3
      s3 = boto3.client('s3', region_name='us-west-2')
      response = s3.create_bucket(Bucket='my-email-bucket',CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})
      ''',

      "AWSLambda": '''
      import boto3
      import zipfile
      import io
      lambda_client = boto3.client('lambda', region_name='us-west-2')
      iam_client = boto3.client('iam')
      with zipfile.ZipFile(io.BytesIO(), 'w') as z:
        z.writestr('index.py', '''
            import json
            import boto3
            def lambda_handler(event, context):
                ses = boto3.client('ses', region_name='us-west-2')
                if event['operation'] == 'add':
                    response = ses.verify_email_identity(EmailAddress=event['email'])
                elif event['operation'] == 'remove':
                    response = ses.delete_identity(Identity=event['email'])
                return {
                    'statusCode': 200,
                    'body': json.dumps('Hello from Lambda!')
                }
            ''')
        z.close()
        function_data = io.BytesIO(z.read())
      role = iam_client.get_role(RoleName='my-iam-role')
      response = lambda_client.create_function(FunctionName='my-function',Runtime='python3.8',Role=role['Role']['Arn'],Handler='index.lambda_handler',Code={'ZipFile': function_data.read()})
      '''
    }
  }
}
