def anagram(s1,s2):
    # Replaces spaces with non-spaces and changes it to lower.
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    # Checks if the first string is the same length than s2
    if len(s1) != len(s2):
        return False
    # Dictionary to be able to count the length.
    count = {}

    #For loop to check for repition of number
    for letter in s1:
        if letter in count:
        # Adds number to the count and keeps the repetion of letters in the dictionary
            count[letter] += 1
        else:
            count[letter] = 1

    # Reverse the first for loop.
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for i in count:
        if count[i] != 0:
            return False
    return True

user_input_s1 = input()
user_input_s2 = input()

anagram(user_input_s1,user_input_s2)
