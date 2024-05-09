# 13-2. Better Stars: 
You can make a more realistic star pattern by introducing randomness when you place each star. 

Recall from Chapter 9 that you can get a random number like this:

from random import randint
random_number = randint(-10, 10)

This code returns a random integer between −10 and 10. Using your code in Exercise 13-1, adjust each star’s position by a random amount.