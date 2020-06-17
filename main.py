import requests

access_perm = 'stories,photos,app_widget,message,docs,manage,wall,stats,groups,offline'
app_id = ''

def get_token(app_id,access_perm,redirect_url='https://oauth.vk.com/blank.html'):
	url = 'https://oauth.vk.com/authorize?client_id=%s&display=page&redirect_url=%s&scope=%s&response_type=token&v=5.110&state=123456' % (app_id,redirect_url,access_perm)
	return url


#you need to get access token in vk 
access_token = ''


def post(method_name,parameters,access_token):
	url = 'https://api.vk.com/method/%s?%s&access_token=%s&v=5.110' % (method_name,parameters,access_token)
	return url


#----------------------------------------
group_id = '-'
friends_only = '0'
message = 'your message'
attachments = 'if needed'
signed = '1'
from_group = '1'

#publish_date = ''
#post_id = 
parameters = 'owner_id=%s&friends_only=%s&from_group=%s&message=%s&attachments=%s' % (group_id,friends_only,from_group,message,attachments)
#-----------------------------------------

r = requests.get(post('wall.post',parameters,access_token))
print(r.text)
print('---')

#get_token(app_id,access_perm)

