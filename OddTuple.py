def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''

    mnoznik = 0
    newTup = ()
    for i in aTup:
        if mnoznik%2==0:
            newTup = newTup+(i,)
        mnoznik+=1    
    return newTup        

    