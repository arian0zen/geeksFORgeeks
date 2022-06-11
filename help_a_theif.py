'''You have to help a thief to steal as many as GoldCoins as possible from a GoldMine. There he saw N Gold Boxes an each Gold Boxes consists of Ai Plates each plates consists of Bi Gold Coins. Your task is to print the maximum gold coins theif can steal if he can take a maximum of T plates. '''

from unittest.util import sorted_list_difference


A = [1, 2, 3]
B = [3, 2, 1]
T = 3
N = 3
#index_plate =list(range(N))
# max_coins = 0
# max = max(B)
# max_A_index = B.index(max)
# print (max_A_index)
#print ("the plate that have most amount of coins is: ", A[max_A_index])


#sorted_B = sorted(B, reverse=True)

#print (max)
#index_plate.sort(key=lambda i: sorted_B[i])
#print (index_plate)
if T == 0:
    print (0)
else:
    max_coins = 0
    while T:
        gold = max(B)
        max_A = A.index
        max_A_index = B.index(gold)
        if A[max_A_index] <= T and A[max_A_index] != 0:
            max_coins += gold*A[max_A_index]
            T -= A[max_A_index]
            A[max_A_index] = 0
            B[max_A_index] = 0
            
            
        else:
            max_coins += T * gold
            #T = 0
            
    print (max_coins)
            
        
        