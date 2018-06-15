parsed_form = {}
with open('input', 'r') as form:
	list_of_arguments = []
	for line in form:
		line = line.replace('\n', '')	
		argument = line.split(':')
		parsed_form[argument[0]] = argument[1]

print(parsed_form)
