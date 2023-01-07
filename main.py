import boto3

boto3.setup_default_session(profile_name='iamadmin-production')
athena_client = boto3.client(service_name='athena')

#Code assumes you have uploaded your source datafile to a S3 bucket


DATABASE_NAME = "sacremento"  # Athen database and table name
TABLE_NAME = "sac_crime"
RESULT_OUTPUT_LOCATION = "s3://awsathenademo134/analysisoutput/"  #S3 bucket for stroing query results

def create_database():
    response = athena_client.start_query_execution(
        QueryString=f"create database if not exists {DATABASE_NAME}",
        ResultConfiguration={"OutputLocation": RESULT_OUTPUT_LOCATION}
    )

    return response["QueryExecutionId"]



def create_table():
    with open("sac_crime.ddl") as ddl:
        response = athena_client.start_query_execution(
            QueryString=ddl.read(),
            ResultConfiguration={"OutputLocation": RESULT_OUTPUT_LOCATION}
        )

        return response["QueryExecutionId"]

create_database()
create_table()

#Query for data for dsitrict 3 in sacremento
query_string = """   
SELECT * FROM sacremento.sac_crime
WHERE district= 3;
"""

response = athena_client.start_query_execution(QueryString=query_string,ResultConfiguration={ 'OutputLocation': "s3://awsathenademo134/analysisoutput/"})
query_execution_id = response['QueryExecutionId']




