'''
860. Lemonade Change

At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). 
Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. 
You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, 
or false otherwise.
'''


class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if bills[0] == 10 or bills[0] == 20 or bills[1] == 20:
            return False

        dollar = {
            "5": 0,
            "10": 0,
            "20": 0
        }

        for i in bills:
            if i == 5:
                dollar["5"] += 1
            elif i == 10:
                if dollar["5"] >= 1:
                    dollar["10"] += 1
                    dollar["5"] -= 1
                else:
                    return False
            elif i == 20:
                if dollar["10"] >= 1 and dollar["5"] >= 1:
                    dollar["20"] += 1
                    dollar["5"] -= 1
                    dollar["10"] -= 1
                elif dollar["5"] >= 3:
                    dollar["20"] += 1
                    dollar["5"] -= 3
                else:
                    return False
            # cash = i

            # if not cash == 5 :
            #     return False
            # elif not (cash == 10 and dollar["5"] >=1)  :
            #     return False
            # elif not  (cash == 20 and (dollar["5"] >= 3 or ( dollar["5"] >= 1 and dollar["10"] >= 1))):
            #     return False

        return True
