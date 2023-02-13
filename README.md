you can create a stack using the AWS CLI with the following command:
`aws cloudformation create-stack --stack-name my-stack --template-body file://my-template.yaml --parameters ParameterKey=BucketName,ParameterValue=my-bucket-name
`

 If you need to update:
 `aws cloudformation update-stack --stack-name my-app-stack --template-body file://my-updated-template.yaml
`
Delete the Stack: Using the AWS CLI, you can delete a CloudFormation stack using the `aws cloudformation delete-stack --stack-name my-stack`

Monitor the Deletion Progress: After running the delete command, you can monitor the progress of the stack deletion using the `aws cloudformation describe-stacks` command. This command will show you the current status of the stack, as well as any events that occur during the deletion process. You can run the command like this:
`aws cloudformation describe-stacks --stack-name my-stack`