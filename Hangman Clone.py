#2022-11-27
dejected = {
    1: "Nice guess!",
    2: "Wow you're good!",
    3: "You got it again.",
    4: "How do you know what to guess?",
    5: "It's almost as if you know the answer.",
    6: "...you know the answer don't you"
}

answer = "Harmony"                                             #Generate keyword
lower_answer = answer.lower()                                               #Get lower-cased version to avoid problems with upper-case letters later
current_word = list(answer)                                                 #Generate dummy word for display purposes; starts as the keyword in asterisk form
i = 0
while i < len(answer):
    if current_word[i].isalpha() == True: current_word[i] = "_"             #Turn all the characters into undescores
    i += 1
counter = 1
chances = 3                                                                 #initialize number of chances remaining
hidden_chars = current_word.count("_")                                      #initialize number of hidden characters remaining
while hidden_chars > 0 and chances > 0:                                     #while "there are more than zero hidden characters remaining" and "there are more than zero lives remaining"
    print("The statement: " + "".join(current_word))                            #print the dummy word's current state
    print("Chances remaining: " + str(chances))                                 #print number of chances remaining
    guess = input("Guess a letter: ")                                           #let player input a guess
    if lower_answer.find(guess.lower()) != -1:                                  #if input letter in lower case is found in the keyword,
        print(dejected.get(counter, "I give up"))                                   #print "nice guess!" from dejected list (system gets more dejected as the correct guesses pile up)
        counter += 1
                                                                                    #convert the corresponding asterisks/characters in the dummy word into that letter
        indices = [pos for pos, char in enumerate(lower_answer) if char == guess]   #get the indices of the character
        num_indices = len(indices)                                                  #get the quantity of indices
        i = 0
        while i < num_indices:                                                      #while iteration step is less than the number of indices,
            current_word[indices[i]] = answer[indices[i]]                               #replace the dummy word's character with the corresponding character of the answer
            i += 1
    else:                                                                       #else (i.e. input letter is not found),
        counter = 1
        chances -= 1                                                                #remove 1 life
        print("The statement doesn't contain that letter.")                         #print "incorrect guess"
    hidden_chars = current_word.count("_")                                      #update number of hidden characters
    print("--------------------")                                               #separate turns with a line so it looks more organized
if hidden_chars == 0: print("Congratulations, you guessed the answer, \"" + answer + "\"!")     #if "there are zero hidden characters remaining" (i.e. the word is complete), congratulate the player
else: print("The answer was \"" + answer + "\". You can try again next time.")                  #else (i.e. "there are zero lives remaining"), reveal the answer and tell the player to try again
