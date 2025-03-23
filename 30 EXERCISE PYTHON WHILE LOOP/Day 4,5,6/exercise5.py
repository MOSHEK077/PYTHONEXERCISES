#Palindrome Check: Check if a number is a palindrome using a while loop.
def is_palindrome(n):
    orginal_number = n
    reversed_number = 0
    while n > 0 :
        digits = n % 10
        reversed_number = reversed_number * 10 + digits
        n = n // 10
    return orginal_number == reversed_number
number = 12321
if is_palindrome(number):
    print(number,"is a palindrome")
else:
    print(number,"is not a palindrome")
    
    """A palindrome is a word, phrase, number, or sequence of characters that reads the same forwards and backwards, ignoring spaces, punctuation, and capitalization.

Examples of Palindromes:
Words:

Civic

Radar

Level

Racecar

Phrases:

"A man, a plan, a canal, Panama!"

"Madam, in Eden, I’m Adam."

Numbers:

121

12321

4554

In the case of numbers, like we discussed earlier, if the number remains the same when its digits are reversed, then it’s considered a palindrome.

Would you like to explore more about palindromes or perhaps try some coding exercises related to them?

"""