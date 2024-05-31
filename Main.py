import yaml
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import AddChatUserRequest
import time
from cfonts import render

# Load configuration from config.yaml
with open('config.yaml', 'r', encoding='utf-8') as file:
    config = yaml.safe_load(file)

api_id = config['telegram']['api_id']
api_hash = config['telegram']['api_hash']
source_group = config['telegram']['source_group']
destination_group = config['telegram']['destination_group']
time_between_each_member = config['telegram']['time_between_each_member']
members_before_wait = config['telegram']['members_before_wait']
wait_time = config['telegram']['wait_time']

outputx = render('Dev : Ghalwash', colors=['white', 'blue'], align='center')
print(outputx)
print('')
print('''
transfare teleram Group member
Coded By ghalwash @Mrfa0gh
But Your Data into config.yanml''')
print()
# Connect to Telegram
with TelegramClient('session_name', api_id, api_hash) as client:
    # Get the ID of the source group
    source_entity = client.get_entity(source_group)
    
    # Get the ID of the destination group
    destination_entity = client.get_entity(destination_group)
    
    # Get all the members from the source group
    members = client.get_participants(source_entity)
    
    count = 0  # Count of added members
    
    # Invite each member to the destination group
    for member in members:
        try:
            client(AddChatUserRequest(destination_entity.id, member.id, fwd_limit=100))
            print(f"Invited {member.username} to {destination_group}")
            count += 1  # Increase the count of added members
            
            # Wait between adding each member
            time.sleep(time_between_each_member)
            
            # Additional wait after adding a specific number of members
            if count % members_before_wait == 0:
                print(f"Waiting for {wait_time} seconds...")
                time.sleep(wait_time)
            
        except Exception as e:
            print(f"Failed to invite {member.username} to {destination_group}: {e}")
