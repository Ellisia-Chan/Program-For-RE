import re

class Selection:
    def __init__(self):
        pass
    def str_scanner(self):
        string = input("Enter a String: ")
        pattern = r'^[a-z].*[^\w\d]$'
        
        if re.search(pattern, string):
            print("\n Valid String \n")
        else:
            print("\n Invalid String \n")
            
    def rem_nega(self):
        n_words = ["hate", "angry", "bully", "punch", "rant"]
        
        paragh = input("Enter a Paragraph: ")
        pattern = r'\b(?:' + '|'.join(map(re.escape, n_words)) + r')\b'
        
        result = re.sub(pattern,'-', paragh)
        print("\n" + result + "\n")
        
    def sub_string(self):
        a = input("Enter String a: ")
        b = input("Enter String b: ")
        
        if re.search(b, a):
            print(f"\n {b} found in {a}! \n")
        else:
            print(f"\n {b} not found in {a} \n")

if __name__ == "__main__":
    while True:
        option = input("Choose Options: \n > a) utilize a string scanner \n > b) eliminate negativity from strings \n > c) extract substrings \n > d) Exit \n > ").lower()
        
        checker = Selection()
        
        if option == "a":
            checker.str_scanner()
            continue
        elif option == "b":
            checker.rem_nega()
            continue
        elif option == "c":
            checker.sub_string()
            continue
        elif option == "d":
            break
        else:
            print("Invalid Input")
            continue




