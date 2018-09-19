#these exercises abuse the fact that false = 0 and true = 1
print(0 == (1 == 2))
print(2 + (3 == 4) + 5 == 7)
print((1 < -1) == (3 > 4))

# 0 == false --> 0 == 0 --> true
# 2 + false + 5 == 7 --> 2 + 0 + 5 = 7 --> true
# (false) == (false) --> true