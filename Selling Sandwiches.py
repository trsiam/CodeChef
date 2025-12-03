#https://www.codechef.com/problems/SANDWSHOP

"""Chef sells sandwiches for a living. Each sandwich is sold for 
A
A rupees.

Chef also needs to buy the ingredients to make a sandwich. The sandwich buns cost 
B
B rupees, and the vegetables cost 
C
C rupees. Let us assume that there are no other costs for Chef right now.

What is the profit Chef makes in selling one sandwich? It may be possible that the answer is negative to indicate that Chef makes a loss instead."""

A,B,C = map(int,input().split())
cost=B+C
print(A-cost)