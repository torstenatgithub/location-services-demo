# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import logging
import time
from geocode import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# ?address_line=willy-brandt-str.1&municipality_name=berlin&state_code=&post_code=10557&country_code=DEU

def lambda_handler(event, context):

    try:    
        logger.debug (event)
        
        t1 = time.time()
        response = geocode_address(event["address_line"], event["municipality_name"], event["state_code"], event["post_code"], event["country_code"])
        t2 = time.time()
        logger.debug ("Time: %.3f" % (t2 - t1))

    except Exception as e:
        logger.exception (e)
        response = {
            "Exception": str(e)
        }
    
    if "Longitude" in response:
        lambda_response = {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {},
            "multiValueHeaders": {},
            "body": response
        }
    else:
        lambda_response = {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {},
            "multiValueHeaders": {},
            "body": response
            #"body": {
            #    "message": "Invalid input or error while geocoding address."
            #}
        }

    return lambda_response