link_state_message = {'fromNode':'Justin', 'toNode':'Bowen', 'expiration':'1492052'}

print(link_state_message)
print(link_state_message['fromNode'])

lsm = link_state_message.copy()
print('copy: ', lsm)


print('fromNode' in link_state_message)