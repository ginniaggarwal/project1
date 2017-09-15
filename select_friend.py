from globals import friends

def select_friend():
        item_number = 0

        for friend in friends:
            print '%d, %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,
                                                                    friend.age,
                                                                    friend.raitng)

            item_number = item_number + 1



