import random

while True:
    if ((input("Play the game: (yes/no) ")) == "no"):
        print("Thank you")
        break;
    else:
        attempts = 0;
        x = random.randint(1,100);
        while True:
            attempts +=1;
            y = int(input("Guess the number: "));
            if x == y :
                print("Congratulations, you guessed it in ", attempts, "attempts.");
                break
            elif x > y :
                print("Too Low, try again");
            else:
                print("Too high, try again");
        
