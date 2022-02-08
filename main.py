import.os

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
        
def main():
    secret_word = input("Enter secret word: ")
    clear_screen()
    lives = 5
    while lives > 3:    
        print("Heart" * lives)
        
        


if __name__ == "__main__"
    main()
