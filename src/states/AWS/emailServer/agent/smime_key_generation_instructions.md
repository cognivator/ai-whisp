
# S/MIME Key Generation and Storage

S/MIME encryption relies on a system of digital certificates for public key infrastructure (PKI). These certificates include public keys and are issued by a certificate authority (CA). The corresponding private key is kept secure by the entity to whom the certificate was issued.

Here's a general overview of how S/MIME encryption keys are created and stored:

1. **Certificate Request**: To start, a certificate signing request (CSR) is generated. This request includes a newly generated public key and some identifying information about the entity requesting the certificate. The private key is also generated at this time but is not included in the CSR. The private key must be kept secure and private by the entity generating the CSR.

2. **Certificate Issuance**: The CSR is sent to a CA. The CA verifies the identity of the entity and, if everything checks out, creates a new digital certificate that includes the public key from the CSR and the identifying information. This certificate is digitally signed by the CA to ensure its authenticity and integrity.

3. **Certificate Distribution**: The new digital certificate is installed on the email server or client that generated the CSR. The certificate (including the public key) is also distributed to any entities that need to verify the digital signatures or encrypt data for the certificate owner. This could be other email servers, clients, or users.

4. **Private Key Storage**: The private key generated during the CSR is securely stored by the owner. In the case of an email client, the private key may be securely stored in the client application or the operating system's key store. The security of the private key is crucial; if it were to be exposed, an attacker could impersonate the certificate owner or decrypt any data that was encrypted with the owner's public key.

For S/MIME to work properly in an email system, both the sender and the recipient need to have their own certificate and private key. The sender uses the recipient's public key (from their certificate) to encrypt the email, and the recipient uses their private key to decrypt it. For digital signatures, the sender uses their private key to sign the email, and the recipient uses the sender's public key (from their certificate) to verify the signature.

Note: The process of requesting, issuing, and managing certificates can be complex and requires careful security measures. Many organizations use managed PKI services to handle these tasks. For individual users, there are also email services that provide built-in support for S/MIME certificates.
