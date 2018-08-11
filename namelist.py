def namelist(names):
	if len(names) < 3:
		if len(names) == 2:
			return "{} & {}".format(names[0]['name'], names[1]['name'])

		elif len(names) == 0:
			return ""

		else:
			return names[0]['name']

	result = "".join([x['name'] + ", " for x in names[:-2]])
	result += "{} & {}".format(names[-2]['name'], names[-1]['name'])
	return result
