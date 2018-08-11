# return masked string
def maskify(cc):
	return "{:#>{}}".format("", len(cc) - 4) + cc[-4:]


print(maskify("SF$SDfgsd2eA"))
