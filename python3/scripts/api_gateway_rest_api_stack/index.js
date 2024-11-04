const crypto = require('crypto');

exports.handler = async (event) => {
    console.log('>> Handler', JSON.stringify(event, null, 4));

    const clientCertPem = event.requestContext.identity.clientCert.clientCertPem;
    const clientCert = new crypto.X509Certificate(clientCertPem);
    const memberId = clientCert.subject.split("\n").filter((element) => element.startsWith('CN='))[0].split("=")[1];

    const response = {
        principalId: memberId,
        context: {
            memberId
        },
        policyDocument: {
            Version: '2012-10-17',
            Statement: [{
                Action: 'execute-api:Invoke',
                Effect: 'allow',
                Resource: event.methodArn
            }]
        }
    };

    console.log('Authorizer Response', JSON.stringify(response, null, 4));

    return response;
};

