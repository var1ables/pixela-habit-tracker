import requests
import datetime


TOKEN = YOUR_TOKEN
USERNAME = YOUR_USER_NAME

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'


#parameters used to create the initial account
params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsofService': 'yes',
    'notMinor': 'yes'
}

#Creating a username and authentication token
#response = requests.post(url=PIXELA_ENDPOINT, json=params)
#print(response.text)

graph_endpoint= f'{PIXELA_ENDPOINT}/{USERNAME}/graphs'


#Graph name configuration
# graph_config = {
#     'id': 'graph1',
#     'name': 'study_graph',
#     'unit': 'hours',
#     'type': 'float',
#     'color': 'sora'
# }

#constant created from graph
GRAPH_ID = 'graph1'

#Header used for authentication
headers = {
    'X-USER-TOKEN': TOKEN
}

#To Create a Graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


#calling the datetime module to get the date info
now = datetime.datetime.now()

#creating parameters for the post data
post_data = {
    'date': f'{now.year}' + f'{now.strftime("%m")}' + f'{now.day}',
    'quantity': '4.0'
}

#creating the creation endpoint for the next post
creation_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}'

#creating the response variable and calling it
# response = requests.post(url=creation_endpoint, json=post_data, headers=headers)
# print(response)

#updating pixel from pixela
update_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/DATE_YOU_WANT_TO_EDIT'

new_pixel_data = {
    'quantity': YOUR_QUANTITY_STR
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response)


#removing pixel from pixela

remove_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/DATE_YOU_WANT_TO_REMOVE'
# response = requests.delete(url=remove_endpoint, headers=headers)
# print(response)