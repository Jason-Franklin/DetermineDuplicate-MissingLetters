#Start with the following Python code.

alphabet = "abcdefghijklmnopqrstuvwxyz"

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"]

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"]

def histogram(s):

   d = dict()

   for c in s:

        if c not in d:

            d[c] = 1

        else:

            d[c] += 1

   return d

#Part 1

#Write a function called has_duplicates()
#that takes a string parameter and returns True
#if the string has any repeated characters

def has_duplicates(s):

    #Call the function histogram and store the resultant

    #dictionary in a variable letter_count.

    letter_count = histogram(s)

    #Run the loop to access each letter present in 'letter_count'.

    for letter in letter_count:

        #If the count of the current letter is

        #greater than 1 then, return True.

        if letter_count[letter] > 1:

            return True



    #Otherwise, return False.

    return False

#Run the loop to access each string in test_dups.

for curr_string in test_dups:

   #Call the function has_duplicates() and print the duplicate information

   #for the current string.

    if(has_duplicates(curr_string)):

        print(curr_string + " has duplicates")

    else:

        print(curr_string + " has no duplicates")

#Part 2

#Define the function missing letters().

def missing_letters(s):

    #Use the global variable alphabet.

    global alphabet

    #Define a variable to store the missing letters.

    new_string = ""

    #Get the histogram of the string 's'.

    letter_count = histogram(s)

    #Run the loop to access each alphabet one by one.

    for curr_letter in alphabet:



        #If the current letter is not present in

        #the histogram then, add it to the string

        #containing the missing letters.

        if curr_letter not in letter_count:

            new_string += curr_letter



    #Return the string containing the missing letters.

    return new_string

#Run the loop to access each string in test_miss.

for curr_string in test_miss:

    #Call the function() missing_letters to get

    #the letters that are missing from the current string.

    miss_letters = missing_letters(curr_string)

    #If there are no missing letters in the current string then, print the

    #required information.

    if miss_letters == "":

        print(curr_string + " uses all the letters")



    #Otherwise, output the missing letters

    #for the current string.

    else:



        print(curr_string +" is missing "+ miss_letters)


