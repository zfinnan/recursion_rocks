# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨`

# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer 
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"

def coin_flips(n):
    heads_or_tails = ['H', 'T']
    results = []
    for i in heads_or_tails:
        for result in coin_flips(n-1):
            results.append(i + result)
        return results


print(coinFlips(2)) 
=> ["HH", "HT", "TH", "TT"]