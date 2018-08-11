def alphabet_position(text):
    return "".join([str(ord(x) - 96) + " " if x >= 'a' and x <='z' else "" for x in text.lower()]).rstrip().lstrip()

print(alphabet_position("The sunset sets at twelve o' clock."))
