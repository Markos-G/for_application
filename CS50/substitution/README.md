### Substitution
In a substitution cipher, we “encrypt” a message by replacing every letter with another letter. To do so, we use a key: in this case, a mapping of each of the letters of the alphabet to the letter it should correspond to when we encrypt it. To “decrypt” the message, the receiver of the message would need to know the key, so that they can reverse the process. The key is a 26-character long.

The time the user executes the program, they should decide, by providing a command-line argument, on what the key should be in the secret message they’ll provide at runtime. Neither the comma nor the space will be substituted by the cipher. Only substitute alphabetical characters. Lowercase letters remain lowercase, and uppercase letters remain uppercase.
 
Also beside decrypting the message, the program deals with:

- an invalid key, explaining the error.
- no command-line argument at all, reminding the user how to use the program.
- too many command-line argument, reminding the user how to use the program.
