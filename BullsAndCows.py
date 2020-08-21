'''
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
'''


def getHint(self, secret: str, guess: str) -> str:
    bull = cow = 0
    c = Counter(secret)
    for e, ch in enumerate(guess):
        if ch == secret[e]:
            bull += 1
            if c.get(ch) <= 0:
                cow -= 1
            else:
                c.subtract(ch)
        elif c.get(ch, 0) > 0:
            cow += 1
            c.subtract(ch)

    return f'{bull}A{cow}B'
