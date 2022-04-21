import boto3
def lambda_handler(event, context): 
    message = event['Records'][0]['Sns']['Message']
    email = message.split(':')[1]
    token = message.split(':')[3]
    # dynamodb = boto3.resource('dynamodb')
    # table = dynamodb.Table('EmailValidTable')
    # item = table.get_item(
    #     Key={
    #         'EmailAddress': email
    #     }
    # )
    # if item == None:
    #     return
    # let's see if its working
    link = "https://demo.zhenluo.me/v1/verifyUserEmail?email=" + email + '&token=' + token
    # Replace sender@example.com with your "From" address.
    # This address must be verified with Amazon SES.
    SENDER = "no-reply@demo.zhenluo.me"

    # Replace recipient@example.com with a "To" address. If your account 
    # is still in the sandbox, this address must be verified.
    RECIPIENT = email

    # Specify a configuration set. If you do not want to use a configuration
    # set, comment the following variable, and the 
    # ConfigurationSetName=CONFIGURATION_SET argument below.
    # CONFIGURATION_SET = "ConfigSet"

    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
    AWS_REGION = "us-east-1"

    # The subject line for the email.
    SUBJECT = "Varify your email with demo.zhenluo.me"

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("Verify link:\r\n" + link)

    # The HTML body of the email.
    BODY_HTML = """<html>
    <head></head>
    <body>
      <h1>Vrify your email via link</h1>
      <p>
        <a href=""" + link + """>verify link</a>
        </p>
    </body>
    </html>
                """            

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    ses = boto3.client('ses',region_name=AWS_REGION)

    #Provide the contents of the email.
    response = ses.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_HTML,
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=SENDER,
        # If you are not using a configuration set, comment or delete the
        # following line
        # ConfigurationSetName=CONFIGURATION_SET,
    )
    return
