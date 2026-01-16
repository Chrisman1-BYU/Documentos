#Enhancement:
#This program was enhanced by adding a descriptive password strength label
#(Very Weak, Weak, Fair, Good, Strong, Very strong) in addition to the numeric
#strength score to improve user understanding and feedback.

LOWER = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
UPPER = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
DIGITS = ["0","1","2","3","4","5","6","7","8","9"]
SPECIAL = [
    "!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","}","|",";",":","'","/",",",".","<",">","?","\"","~","\\","~","`"]

#-------------------------------
#Function Definitions
#-------------------------------

def word_in_file(word, filename, case_sensitive=False):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            file_word= line.strip()

            if case_sensitive:
                if word == file_word:
                    return True
            else:
                if word.lower() == file.lower():
                    return True   
    return False             

def word_has_character(word, character_list):
    for char in word:
        if char in character_list:
            return True
        return False

def word_complexity(word):
    complexity = 0

    if word_has_character(word, LOWER):
        complexity += 1

    if word_has_character(word, UPPER):
        complexity += 1

    if word_has_character(word, DIGITS):
        complexity += 1    

    if word_has_character(word, SPECIAL):
        complexity += 1 

    return complexity
    
def password_strength(password, min_length=10, strong_length=16):
    #check dictionary words (case-insensitive)
    if word_in_file(password, "wordlist.txt", case_sensitive=False):  
        print("Password is a dictionary word and is not secure.")
        return 0

    #check top passwords (case-sensitivity)  
    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0
    
    #check length < min_length
    if len(password) <min_length:
        print("Password is too short and is not secure.")
        return 1
    
    #check strong length
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5
    
    #otherwise, calculate complexity
    complexity = word_complexity(password)
    return 1 + complexity

def strength_label(score):
    labels = {
        0: "very weak",
        1: "Weak",
        2: "Fair",
        3: "Fair",
        4: "Strong",
        5: "Very Strong"
    }
    return labels.get(score, "Unknown")

def main():
    while True: 
        password = input("Enter a password to test(or q to quit): ")

        if password.lower() == "q": #works for 'q' or 'Q'
            print("Goodbye!")
            break

    #call the password_strength function
    strength = password_strength(password)
    lable = strength_label(strength) 

    #Display the score to the user
    print(f"Password'{password}' has a strength score of: {strength} ({lable})\n")   

if __name__== "__main__":
    main()