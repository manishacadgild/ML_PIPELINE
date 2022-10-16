
import os


SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"

API_KEY ="DHAL25T7ENPMJKBY" #os.getenv('API_KEY',None)
API_SECRET_KEY = "MfGy8j3ChacVcTB92nalWz0fuhSWs4VrklaAv2ntJk4Ee74oZxhvHtTiDg9M4Ow7"#os.getenv('API_SECRET_KEY',None)
BOOTSTRAP_SERVER ="pkc-6ojv2.us-west4.gcp.confluent.cloud:9092" #os.getenv('BOOTSTRAP_SERVER',None)
#SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
#SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)
## Schema details 
ENDPOINT_SCHEMA_URL  ="https://psrc-znpo0.ap-southeast-2.aws.confluent.cloud" #os.getenv('ENDPOINT_SCHEMA_URL',None)
SCHEMA_REGISTRY_API_KEY ="ZORR3I2IAN5ML7FJ" #os.getenv('SCHEMA_REGISTRY_API_KEY',None)
SCHEMA_REGISTRY_API_SECRET ="U5rdQ1v6EMGD0yTlE9INcpfQj/4jgicP/DcmIRPNMBRIeJDB1qOSQuNhhSv8Vtb+" #os.getenv('SCHEMA_REGISTRY_API_SECRET',None)


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    #print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

