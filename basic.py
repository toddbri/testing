class Person(object):

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count =0
        self.met = []

    def greet(self, other_person):
        self.greeting_count +=1
        if not other_person in self.met:
            self.met.append(other_person)
            other_person.met.append(self)
        print 'Hello %s, I am %s!' % (other_person.name, self.name)

    def print_contact_info(self):
        print "%s's email: %s, %s's phone number: %s" % (self.name,self.email,self.name,self.phone)

    def __repr__(self):
        return 'Person(%s, %s)' % (self.name, self.email)

    def add_friend(self, new_friend):
        self.friends.append(new_friend)

    def num_friends(self):
        return len(self.friends)

if __name__ == "__main__":
    sonny = Person("Sonny","sonny@gmail.com","483-485-4948")
    jordan = Person("Jordan","jordan@aol.com","495-586-3456")
    dee_ann = Person("Dee Ann","deeann@live.com","555-1212")
    sonny.greet(jordan)
    jordan.greet(sonny)

    print "%s %s" % (sonny.email,sonny.phone)
    print "%s %s" % (jordan.email,jordan.phone)

    sonny.print_contact_info()
    jordan.print_contact_info()
    jordan.add_friend(sonny)
    sonny.add_friend(jordan)
    # print jordan.friends.__len__()
    print jordan.num_friends()
    print jordan.greeting_count

    print "_"*10

# print jordan.friends
