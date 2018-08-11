import re


def order(sentence):
	if len(sentence) == 0:
		return ""
	sentence = sentence.split(' ')
	word_order = {}
	for i in sentence:
		word_order[re.search("[1-9]", i).group(0)] = i
	return "".join([word_order[x] + " " for x in sorted(word_order.keys())]).rstrip()

