import boto3
REGION = "us-west-2"
sesion_origen = boto3.Session(region_name=REGION)
s3_client = sesion_origen.client("s3")


try:
    print("Intentando crear bucket")
    bucket_tfstate = "terraform-tfstate-sps-demo"

    response = s3_client.create_bucket(
        Bucket=bucket_tfstate,
        CreateBucketConfiguration={
            'LocationConstraint': REGION,
    },
    )    
except Exception as e:
    print(e)
    print("No fue posible crear bucket.")

try:
    print("Habilitando versionado...")
    response = s3_client.put_bucket_versioning(
        Bucket=bucket_tfstate,
        VersioningConfiguration={
            'Status': 'Enabled'
        }
    )
except Exception as e:
    print(e)
    print("No fue posible habilitar versionado")