letter=input("Enter the charcter to find vowel or const\n")
if(not letter.isalpha()):
    print("Not letter")
else:
 match letter :
    case "A" | "a" | "E" | "e" | "I" | "i" | "O" | "o" |"U" |"u":
        print("vowel")
    case _ :
        print("Consnsont")
