from spy_details import spy
from start_chat import start_chat


print "Hello! Let\'s get started"

question = "Do you want to continue as " + spy['salutation'] + " " + spy['name'] + " (Y/N)? "
existing = raw_input(question)

if existing == "Y":
    start_chat(spy)
else:

    spy = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'is_online': False
    }

    spy['name'] = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy['name']) > 0:
        spy['salutation'] = raw_input("Should I call you Mr. or Ms.?: ")

        spy['age'] = raw_input("What is your age?")
        spy['age'] = int(spy['age'])

        spy['rating'] = raw_input("What is your spy rating?")
        spy['rating'] = float(spy['rating'])

        spy['is_online'] = True

        start_chat(spy)
    else:
        print 'Please add a valid spy name'




