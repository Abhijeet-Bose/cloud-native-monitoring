import boto3


kms = boto3.client('kms', region_name='us-west-2')

ecr_client = boto3.client('ecr')

repository_name = 'my-cloud-native-repo'

response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']

print(repository_uri)