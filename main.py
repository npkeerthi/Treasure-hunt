print('''
*******************************************************************************
          |                   |                  |                    blue
					
					 |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("\nWelcome to Treasure Island.")
input("Your mission is to find the treasure.\nPress enter to continue after each statement.\n")
print("You are running from angry pirates, where you come across a cross road. Which way you go? Type 'left' or 'right'.")
way = input().lower()

if way == "right":
    print('''
**************************************************************************
             ______              ______              ______     
          ,-' ;  ! `-.        ,-' ;  ! `-.        ,-' ;  ! `-.  
         / :  !  :  . \      / :  !  :  . \      / :  !  :  . \ 
        |_ ;   __:  ;  |    |_ ;   __:  ;  |    |_ ;   __:  ;  |
        )| .  :)(.  !  |    )| .  :)(.  !  |    )| .  :)(.  !  |
        |"    (##)  _  |    |"    (##)  _  |    |"    (##)  _  |
        |  :  ;`'  (_) (    |  :  ;`'  (_) (    |  :  ;`'  (_) (
        |  :  :  .     |    |  :  :  .     |    |  :  :  .     |
        )_ !  ,  ;  ;  |    )_ !  ,  ;  ;  |    )_ !  ,  ;  ;  |
        || .  .  :  :  |    || .  .  :  :  |    || .  .  :  :  |
        |" .  |  :  .  |    |" .  |  :  .  |    |" .  |  :  .  |
        |mt-2_;----.___|    |mt-2_;----.___|    |mt-2_;----.___|
           = yellow =           = red =             = blue =         
***************************************************************************\n
    ''')
    print("You are safe for a while, but not for long. There are 3 doors ahead of you. Which one will you choose?")
    print("(Hint: Think about what the colors represent)")
    door = input("yellow, red or blue? ").lower()
    if door == "yellow":
        print("\nYou walk into a place like paradise. The sun is shining, birds are chirping.")
        print("You heard the roars of the pirates coming behind you. You start running towards the river.")
        print('''
****************************************    
                        _,._      
        .||,       /_ _\\     
        \.`',/      |'L'| |    
        = ,. =      | -,| L    
        / || \    ,-'\\"/,'`.   
        ||     ,'   `,,. `.  
        ,|____,' , ,;' \| |  
        (3|\    _/|/'   _| |  
        ||/,-''  | >-'' _,\\ 
        ||'      ==\ ,-'  ,' 
        ||       |  V \ ,|   
        ||       |    |` |   
        ||       |    |   \  
        ||       |    \    \ 
        ||       |     |    \\
        ||       |      \_,-'
        ||       |___,,--")_\\
        ||         |_|   ccc/
        ||        ccc/       
        ||                hjm
*****************************************
            ''')
        input("\nThere's a bridge ahead, you can quickly pass it to get rid of the pirates behind.\n...But who is that over there? A wizard?!")
        input("Wizard: 'Hello there mighty mortal. Before I let you through this bridge, you have to prove you're worthy by answering my questions correctly.'")
        print("Will you answer the questions or will you try to swim across the river? Type 'answer' or 'swim'")
        answer = input().lower()
        if answer == "answer":
            input("Wizard: 'Alright there, my first question for you is... '")
            print('''
**************************************************************************************
            .::.
            _::_
          _/____\_        ()
          \      /      <~~~~>
           \____/        \__/         <>_
           (____)       (____)      (\)  )                        __/"""\\
            |  |         |  |        \__/      WWWWWW            ]___ 0  }
            |__|         |  |       (____)      |  |       __        /   }
           /    \        |__|        |  |       |  |      (  )     /~    }
          (______)      /____\       |__|       |__|       ||      \____/
         (________)    (______)     /____\     /____\     /__\     /____\\
         /________\   (________)   (______)   (______)   (____)   (______)
            King        Queen       Bishop      Rook      Pawn     Knight
************************************************************************************** \n    
            ''')
            game = input("Wizard: 'What is the name of this game?' ").lower()
            if game == "chess":
                input("Wizard: 'Well this was easy. But I have another question for you, and it's more difficult.'")
                input("Wizard: 'Here is my second question... '")
                print('''
********************************************
                        __
                       / _)
              _.----._/ /
             /         /
          __/ (  | (  |
        /__.-'|_|--|_|

********************************************\n
                ''')
                print("Wizard: 'Now tell me... What is the name of this animal?'")
                animal = input().lower()
                if animal == "dinosaur":
                    input("Wizard: 'You are surprising me human. But I haven't yet done with you. You shall correctly answer my third and final question.'")
                    input("Wizard: 'And that is...'")
                    print('''
******************************************************************************
                                          .-.
                  ,                     .-' ,c'.
              __rK                    _)a  7  ;
              /  ~,)                  (_,      (
            _;   /a(                   |_.    :'\\
            L/\.'__/                   \       ' )nnnK-.
            S  / (_                  .- L,-'   .dHHHb   |
            S( '\_\\                / dHb'----'dHHHHb    \\
            S \  ,  )      _,-._   / dHHHb"x.dHHHHHHb     \\
            S |'. '.______/_U/_ '.-z/dHHHp   'dHHHHHb\     |
            [H |  '..___.--'._C__  ) |         dHHHHHHb\ _   \\
            /| |_  | \     L/'--._/_ ;                  k '  /
            |//- '-. ---.__         '|                 /     |
            (       '-.   '.        |               _'-.  _/
        .."' `.,  _ ,  :  | \      _\             ,/ ,  '/
        ."       ':   .     : |   .-' '',          : |/(/\]/
                \  /:  '  | :  /_      '...... .'/      |
                |     |  : / .' '--.__,     __.'\      /
                |   : ;  |/ |         '----'L,  |     /
                    \  : .   \  '-.________ /   ]  |____/
            snd     L_____'..'           _.7' _/  <,    >
                                        <___.'     /    \\
                                                \____/
                                                            ____     _____
******************************************************************************
                    ''')
                    print("Wizard: 'Tell me human... What is the name of this movie (1 word)?'")
                    movie = input().lower()
                    if movie == "shrek":
                        input("Wizard: 'You have proved yourself worthy. I have faith in you human. May all the gods be with you in your journey.'\n")
                        input("You passed the bridge. Now the pirates cannot come after you. You are safe.")
                        input("You see something shining ahead. You get closer and closer...")
                        input("And here it is! The treasure! You've found it!")
                        print("Congratulations human... Seems like you were the one all along.")
                    else:
                        print("Wizard: 'You came this far... Such a shame to see you gone.'")
                        print("Wizard: 'Pirates! The human is yours.'")
                        print("The answer was 'Shrek'.")
                        print("Game over.")
                else:
                    print("Wizard: 'Seems like you are not worthy of it after all.'")
                    print("Wizard: 'Pirates! The human is yours.'")
                    print("The answer was 'Dinosaur'.")
                    print("Game over.")
            else: 
                print("Wizard: 'You have failed me human.'")
                print("Wizard: 'Pirates! The human is yours.'")
                print("The answer was 'Chess'.")
                print("Game over.")
        elif answer == "swim":
            print("You are eaten by the wild piranhas in the river.")
            print( "Game over.")
        else:
            print("Wrong answer. Game over.")
    elif door == "blue":
        print("You fell down a cliff and drowned in the ocean.")
        print("Game over.")
    elif door == "red":
        print("You went into a room full of fire and burned to death.")
        print("Game over.")
    else:
        print("Wrong answer. Game over.")
else:
    print("Uh-oh! There's a wall ahead, you're stuck. The pirates have come to get you.")
    
    