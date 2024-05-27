import os 
from django.conf import settings

import logging
logger = logging.getLogger(__name__)	


## Global AWS settings 
AWS_ACCESS_KEY_ID 			= os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY 		= os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_S3_OBJECT_PARAMETERS 	= {'CacheControl': 'max-age=86400'}

## S3 config
AWS_STORAGE_BUCKET_NAME 	= os.environ.get('MASTER_BUCKET_NAME')
AWS_S3_DOMAIN 				= os.environ.get('AWS_S3_DOMAIN_NAME')
AWS_S3_VERIFY 				= True
AWS_SERVER_PROTOCOL         = 'https'
AWS_DEFAULT_ACL 			= None

## Django
DEFAULT_FILE_STORAGE 		= 'systemops.my_storage.MediaStorage'
PUBLIC_MEDIA_LOCATION 		= os.environ.get('PUBLIC_MEDIA_LOCATION')
AWS_S3_CUSTOM_DOMAIN		= f'{AWS_STORAGE_BUCKET_NAME}.{AWS_S3_DOMAIN}'
MEDIA_ROOT 					= f'{AWS_SERVER_PROTOCOL}://{AWS_S3_CUSTOM_DOMAIN}/'
MEDIA_URL 					= f'{AWS_SERVER_PROTOCOL}://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'

# sample path of a file
# "https://cdr-108.s3.amazonaws.com/test-data/Screen-Shot-2023-03-06.png"
# "https"+ "://" + "cdr-108" + "." + "s3.amazonaws.com" + "/" + "test-data" + "/" + "Screen-Shot-2023-03-06.png"
# MEDIA_ROOT = "https://cdr-108.s3.amazonaws.com/test-data"
# MEDIA_ROOT = AWS_SERVER_PROTOCOL + "://" + BUCKET_NAME + "." + DOMAIN_NAME + "/" + FOLDER_NAME + "/"


######### local server 
# MEDIA_ROOT = '/Users/zoti01011989/Desktop/myfolder'
# MEDIA_URL = '/media/'
# print("MEDIA_ROOT ->>{}".format(MEDIA_ROOT))
# print("MEDIA_URL ->>{}".format(MEDIA_URL))
