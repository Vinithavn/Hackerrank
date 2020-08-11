An English text needs to be encrypted using the following encryption scheme.
First, the spaces are removed from the text. Let L be the length of this text.
Then, characters are written into a grid, whose rows and columns have the following constraints:

sqrt(L)<=row<=column<=sqrt(L)

For example, the sentence , "if man was meant to stay on the ground god would have given us roots",
after removing spaces is 54 characters long. sqrt(54) is between 7 and 8 , so it is written in the form of a grid with 7 rows and 8 columns.


ifmanwas  
meanttos          
tayonthe  
groundgo  
dwouldha  
vegivenu  
sroots

The encoded message is obtained by displaying the characters in a column, inserting a space, and then displaying the next column and inserting a space, and so on. For example, the encoded message for the above rectangle is:

imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau

You will be given a message to encode and print.

Function Description

Complete the encryption function in the editor below. It should return a single string composed as described.

encryption has the following parameter(s):
s: a string to encrypt

Input Format:
One line of text, the string s

Constraints:
1<=|s|<81
s is comprised only of characters in the range ascii[a-z]

Output Format:
Print the encoded message on one line as described.

