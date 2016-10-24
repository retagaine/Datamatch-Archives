import smtplib
import json
from pprint import pprint

def results(user):
	# find id of user with user's email
	with open('data2015csv.json') as data_file:
		data = json.load(data_file)

		persona = None
		for person in data:
			if person["FIELD6"] == user:
				persona = person["FIELD1"]
				print persona

	# find matches using is found above
	with open('matches2015csv.json') as match_file:
		match = json.load(match_file)

		matches = None

		if persona != None:
			person1 = [item for item in match
					  if item["FIELD1"] == persona][0]
			matches = []
			matches.append(person1["FIELD6"])
			matches.append(person1["FIELD7"])
			matches.append(person1["FIELD8"])
			matches.append(person1["FIELD9"])
			matches.append(person1["FIELD10"])
			matches.append(person1["FIELD11"])
			matches.append(person1["FIELD12"])
			matches.append(person1["FIELD13"])
			matches.append(person1["FIELD14"])
			matches.append(person1["FIELD15"])
			if person1["FIELD16"] != "null":
				matches.append(person1["FIELD16"])
			if person1["FIELD17"] != "null":
				matches.append(person1["FIELD17"])

	# find all matches' names
	if matches != None:
		names = []
		for match in matches:
			name = [item for item in data
				if item["FIELD1"] == match][0]["FIELD2"]
			names.append(name)
			
		myString = "\n".join(names)
		return myString

# for every email from the Datamatch 2015 feedback (Responses).xlsx
sender = 'hcsdatamatch@gmail.com'
receiver = 'raynorkuang@gmail.com'

# Credentials (if needed)
username = 'hcsdatamatch@gmail.com'
password = 'i_heart_waffles'

# The actual mail send
with open('2015feedback.json') as data_file:

		users = json.load(data_file)

		for user in users:
			if user["FIELD21"] == "Yes.":
				if user["FIELD32"] != "No":
					server = smtplib.SMTP('smtp.gmail.com:587')
					server.starttls()
					server.login(username,password)

					# receiver = user["FIELD2"]
					
					SUBJECT = "Your Datamatch 2015 Results <3"
					TEXT =  "Dear Datamatch User, \n\n" \
						"You are receiving this email because you responded to a Datamatch research survey this past winter, " \
						"and showed interest in receiving your old matches from Datamatch 2015.\n\n" \
						"Without further ado, here's the list of your matches! (in no particular order) : \n\n" + results(user["FIELD2"]) + "\n\nThe 2016 edition of Datamatch is out now!" \
						" Presenting a new, sleeker, sexier website and " \
						"partnering with Satire V to release the most uproarious questions yet, " \
						"we've used feedback from Johnstone Family Professor of Psychology Steven Pinker and " \
						"the Harvard community for even better matches.\n\n" \
						"The 21st Datamatch could be the best yet.\n\n" \
						"Sign up now at http://datamatch.hcs.harvard.edu !\n\n" \
						"Love, \n\nThe 2016 Datamatch Team" \
						"PS. If you have any questions, feel free to email us back at this address."
					msg = 'Subject: %s\n\n%s' % (SUBJECT, TEXT)
					# server.sendmail(sender, receiver, msg)

					if ("alexanderyoung" in user["FIELD2"] or "rkoreh" in user["FIELD2"]):
						print results(user["FIELD2"])
					server.quit()
