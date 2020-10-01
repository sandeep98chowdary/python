secret_number = 777
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
a=int(input('enter your guessed number:'))
while a!=secret_number:
    print("Ha ha! You're stuck in my loop!")
    a=int(input('enter your guessed number:'))
    
print("Well done, muggle! You are free now.")   
exit(input('press enter to exit'))
