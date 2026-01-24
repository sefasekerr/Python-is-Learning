# import time
# import asyncio

# async def fetch_data(delay):
#     print("veri alınıyor...")
#     await asyncio.sleep(delay)
#     print("veri alındı...")
#     return {"data":"bazı veriler"}



# async def main():
#     print("start")
#     task = fetch_data(2)
#     result = await task
#     print(f"alınan veri : {result}")
#     print("end")    

# asyncio.run(main())



# ------------------
# Create a campaign\
# ------------------
# Include the Brevo library\
from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

from pprint import pprint
# Instantiate the client\
sib_api_v3_sdk.configuration.api_key['api-key'] = key
api_instance = sib_api_v3_sdk.EmailCampaignsApi()
# Define the campaign settings\
email_campaigns = sib_api_v3_sdk.CreateEmailCampaign(
name= "Campaign sent via the API",
subject= "My subject",
sender= { "name": "sefa şeker", "email": "sefaseker92@gmail.com"},
type= "classic",
# Content that will be sent\
html_content= "Congratulations! You successfully sent this example campaign via the Brevo API.",
# Select the recipients\
recipients= {"listIds": [2, 7]},
# Schedule the sending in one hour\
scheduled_at= "2018-01-01 00:00:01"
)
# Make the call to the client\
try:
    api_response = api_instance.create_email_campaign(email_campaigns)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailCampaignsApi->create_email_campaign: %s\n" % e)