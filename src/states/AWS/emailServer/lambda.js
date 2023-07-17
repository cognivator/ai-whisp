const AWS = require('aws-sdk');
const ses = new AWS.SES({ region: 'us-west-2' });

exports.handler = async (event) => {
    const { operation, emailAddress } = event;

    if (operation === 'add') {
        await ses.verifyEmailIdentity({ EmailAddress: emailAddress }).promise();
        return `Email ${emailAddress} added successfully.`;
    }

    if (operation === 'remove') {
        await ses.deleteIdentity({ Identity: emailAddress }).promise();
        return `Email ${emailAddress} removed successfully.`;
    }

    return `Invalid operation. Please specify "add" or "remove".`;
};
