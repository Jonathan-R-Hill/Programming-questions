score = {'e' : 1, 'a' : 1, 'i' : 1, 'o' : 1 , 'n' : 1, 'r' : 1, 't' : 1, 'l' : 1, 's' : 1, 'u' : 1, 
'd' : 2, 'g' : 2, 
'b' : 3, 'c' : 3 , 'm' : 3, 'p' : 3, 
'f' : 4, 'h' : 4, 'v' : 4, 'w' : 4, 'y' : 4, 
'k' : 5, 
'j' : 8, 'x' : 8, 
'q' : 10, 'z' : 10
}

# List and variable storage
n = int(input())            # Number of words

my_words = []
my_letters = []

stored_letters = []

answer = ("", 0)

# Loops adding to the starting lists
for _ in range(n):
    w = input().lower()            # Adding Words to my_words list to check
    my_words.append(w)


letters = input()           # String of letters 
for i in letters:           # Adding Letters to storage as a list for {new_letters} function to work
    stored_letters.append(i)


def new_letters():
    # Deletes any letters left over from the last word
    for _ in range(len(my_letters)):
        my_letters.pop()
    
    # Adds the starting letters back to the list from the stored_letters for the new word to use
    for letter in stored_letters:
        my_letters.append(letter)

    
def word_score():
    # Looping through each word and totaling the value of each word sets value to 0 if a letter isn't in my_letters
    global answer
    for word in my_words:
        # Reseting letters and total
        total = 0
        new_letters() 

        for i in range(len(word)):
            if word[i] in my_letters:
                total += score[word[i]]     # Adds the points based on the letter
                my_letters.remove(word[i])  # remove the letter used from my_letters for next loop
            
            else:
                total = 0
                break

        # Updates the answer if it has a better score than the current answer
        if total >  answer[1]:
            answer = (word, total)
    
    print(answer[0])    # Prints the word from {answer}


word_score()
