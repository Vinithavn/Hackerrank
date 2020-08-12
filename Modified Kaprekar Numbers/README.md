A modified Kaprekar number is a positive whole number with a special property. 
If you square it, then split the number into two integers and sum those integers, you have the same value you started with.

Consider a positive whole number n with d digits. We square n to arrive at a number that is either 2d digits long or 2d-1 digits long.
Split the string representation of the square into two parts, l and r. The right hand part, r must be d digits long. 
The left is the remaining substring. Convert those two substrings back to integers, add them and see if you get n.

Function Description:
Complete the kaprekarNumbers function in the editor below. It should print the list of modified Kaprekar numbers in ascending order.

kaprekarNumbers has the following parameter(s):

p: an integer
q: an integer

Input Format:
The first line contains the lower integer limit p.
The second line contains the upper integer limit q.

Note: Your range should be inclusive of the limits

Constraints:
1<p<q<100000
