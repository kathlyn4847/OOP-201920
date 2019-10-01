#course: Object-oriented programming, year 2, semester 1
#academic year: 201920
#author: B. Schoen-Phelan
#date: 29-09-2019
#purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your name: ")
        print("Originally entered: "+ message)

        # print only first and last of the sentence

        print (message[0] + message[-1])

        # use slice notation

        print (message [2:4])
        # escaping a character
        print("He said \"that\'s fantastic\"!")

        # find all a's in the input word and count how many there are
        result = message.find('a')

        print("A appears in position :",result)


        count = message.count('a')

        print("How many times is a in this string: ",count)

        amount = len(message)
        print("This string contains this many characters",amount)

        # replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace()

        print (message.replace("a","-"))






        # printing only characters at even index positions

        i = range(0, 10, 2)
        for n in i:
            print(message[n])

        # hand the input string to a list and print it out
        words = message.split()

        print(words)




        # append a new element to the list and print
        words.append("sup")

        print("New list", words)

        # remove from the list in 3 ways
        words.remove('hey')

        print("Updated list:", words)

        del words[3]

        print("Updated 2 list:", words)

        words.pop(0)

        print("Updated 3  list:", words)

        # check if the word cake is in your input list
        print('cake' in words)


        # reverse the items in the list and print
        words.reverse()

        print(words)

        # reverse the list with the slicing trick
        words[::-1]

        print(words)

        # print the list 3 times by using multiplication
        print(words)*3


tas = Types_and_Strings()
tas.play_with_strings()
tas.play_with_lists()