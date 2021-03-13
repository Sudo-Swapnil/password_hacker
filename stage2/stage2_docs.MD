This stage we try simple brute force method to "guess" the password which a user might have set. 
Here we assume the password may contain combination of only small latin characters (a-z) and any digit (0-9). 

The algorithm is the following:

1. Using itertools.product() function, we create a generator function which yields every possible permutation of all lengths, in a step by step manner, 
   i.e. first we create password strings of length 1, then 2 and so on. 
2. On generating each password string, send the password to the server using socket.
3. If generated password is not the user password, we continue generating next passward until we guess the password correctly.
4. On getting success message from the server, we print the guessed password and terminate