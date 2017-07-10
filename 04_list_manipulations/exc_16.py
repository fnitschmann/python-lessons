# list manipulations - exercise 16
invited_persons = ["Daniel", "Mark", "Hunter"]

for person in invited_persons:
    message = "Hey {}! You are invited to my dinner.".format(person)
    print(message)

print("\nA bigger table is available! I will invite a few more people!\n")

invited_persons.insert(0, "Claris")
invited_persons.insert(2, "Mandy")
invited_persons.append("Doris")

for person in invited_persons:
    message = "Hey {}! You are invited to my dinner.".format(person)
    print(message)
