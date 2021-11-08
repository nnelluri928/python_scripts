def groups_per_user(group_dictionary):
	user_groups = {}
	for group,users in group_dictionary.items():
		for item in users:
			print(group,item)
			if item not in user_groups:
				user_groups[item] = []
			if item in user_groups:
				user_groups[item].append(group)
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],	
		 }))

