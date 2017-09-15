from globals import friends

def add_friend():
    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0
    }
    new_friend['name'] = raw_input("Please add your friend's name: ")
    new_friend['salutation'] = raw_input("Are they Mr. or Ms.?: ")

    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']

    new_friend['age'] = raw_input("Age?")
    new_friend['age'] = int(new_friend['age'])

    new_friend['rating'] = raw_input("Spy rating?")
    new_friend['rating'] = float(new_friend['rating'])

    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['rating'] >= new_friend['rating']:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)


