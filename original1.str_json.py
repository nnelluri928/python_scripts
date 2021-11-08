''' converting json string in to python object'''

import json

people_string = '''
	{
	"people": [
		{
			"name": "john smith",
			"phone": "615-555-7164",
			"emails": ["johnsmith@bogusemail.com","john.smith@work-place.com"],
			"has_license": false
		},
		{
			"name": "john Doe",
                        "phone": "560-555-7164",
                        "emails": null,
                        "has_license": true
		}
	]
}
'''


data = json.loads(people_string)





for person in data['people']:
  del person['phone']


new_str = json.dumps(data,indent=2,sort_keys=True)

print(new_str)


