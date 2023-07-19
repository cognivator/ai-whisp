
import boto3

# AWS clients
route53 = boto3.client('route53')
acm = boto3.client('acm')

# Constants
DOMAIN_NAME = 'example.com'  # Replace with your domain name
EMAIL_ADDRESS = 'admin@example.com'  # Replace with your email address

# Create Hosted Zone in Route 53
response = route53.create_hosted_zone(
    Name=DOMAIN_NAME,
    CallerReference='myUniqueIdentifier',
    HostedZoneConfig={
        'Comment': 'Hosted zone for ' + DOMAIN_NAME,
        'PrivateZone': False
    }
)

# Output the hosted zone ID
print('Hosted Zone ID:', response['HostedZone']['Id'])

# Request a certificate in ACM
response = acm.request_certificate(
    DomainName=DOMAIN_NAME,
    ValidationMethod='EMAIL',
    IdempotencyToken='myUniqueIdentifier',
    Options={
        'CertificateTransparencyLoggingPreference': 'ENABLED'
    },
    DomainValidationOptions=[
        {
            'DomainName': DOMAIN_NAME,
            'ValidationDomain': DOMAIN_NAME
        },
    ],
    SubjectAlternativeNames=[
        '*.' + DOMAIN_NAME,
    ],
    Tags=[
        {
            'Key': 'Purpose',
            'Value': 'SSL/TSL for ' + DOMAIN_NAME
        },
    ]
)

# Output the Certificate ARN
print('Certificate ARN:', response['CertificateArn'])
