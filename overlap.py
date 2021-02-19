def _extraction_start(triples_, alpha = 0.75):
    triples = triples_
    l = len(triples)
    i = 1
    while i < len(triples):
        ii = 0
        while ii < i:
            s1 = triples[i][0] + ' ' + triples[i][1] + ' ' + triples[i][2] 
            s2 = triples[ii][0] + ' ' + triples[ii][1] + ' ' + triples[ii][2] 
            s1 = s1.split(' ')
            s2 = s2.split(' ')
            l1 = len(s1)
            l2 = len(s2)
            i12 = 0
            i21 = 0
            for a1 in s1:
                if a1 in s2:
                    i12 += 1
            for a2 in s2:
                if a2 in s1:
                    i21 += 1
            a12 = i12 / l1
            a21 = i21 / l2
            if a12 >= alpha or a21 >= alpha:# and a12 + a21 > 1.25:
                if a12 >= a21:
                    try:
                        triples.remove(triples[i])
                        i-=1
                    except:
                        pass
                else:
                    try:
                        triples.remove(triples[ii])
                        ii-=1
                    except:
                        pass
            ii+=1
        i+=1
    
    return triples
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
