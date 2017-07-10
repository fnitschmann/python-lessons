# variables and strings exercise 7
name_with_whitespaces = "   Max "

without_at_beginning = name_with_whitespaces.lstrip()
without_at_end = name_with_whitespaces.rstrip()
without_any = name_with_whitespaces.strip()

print("Without spaces at the beginning: '{}'".format(without_at_beginning))
print("Without spaces at the end: '{}'".format(without_at_end))
print("Without any spaces : '{}'".format(without_any))
