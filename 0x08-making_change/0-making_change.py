#!/usr/bin/python3
"""Determine the fewest number of coins needed
to meet a given amount total"""


def makeChange(coins, total):
    '''This function takes in a list(coins) and counts it off of total'''
    if total <= 0:
        return 0

    else:
        count = 0
        sorted_coin = sorted(coins)
        sorted_coin.reverse()
        for coin in sorted_coin:
            while (total >= coin):
                total -= coin
                count += 1
        if total == 0:
            return count
        return -1
