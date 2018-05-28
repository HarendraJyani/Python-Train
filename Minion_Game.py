def minion_game(string):
    v = 'AEIOU'
    pos = 0
    neg = 0
    for i in range(len(string)):
        if string[i] in v:
            pos += len(string) - i
        else:
            neg += len(string) - i
    if pos > neg:
        print("Kevin", pos)
    elif pos < neg:
        print("Stuart", neg)
    else:
        print("Draw")
    
