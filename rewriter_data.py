import re
from rouge import Rouge 
def _extraction_start_ngram(triples, s2, alpha = 0, alpha2 = 0.25):
    aa=[]
    l = len(triples) 
    i = 1
    s2 = s2.split(' ')
    a=0
    ans=[]
    for i in triples:
        s1=i[0]+' '+i[1]+' '+i[2]
        s1 = s1.split(' ')
        l1 = len(s1)
        i12 = 0
        for a1 in s1:
            if a1 in s2:
                i12 += 1
        a12 = i12 / l1
        if a12 > a and a12 > 0:
            ans=[]
            ans.append(i)
            a=a12
        elif a12 == a and a12 > 0:
            ans.append(i)
        if a12>=alpha:
            aa.append(i)
    if len(aa)==0 and a >= alpha2:
        aa=ans
    
    return aa
    



def _extraction_start_rouge(triples, s2, alpha = 0.4, alpha2 = 0, alpha3=0):
    rouge = Rouge()
    aa=[]
    l = len(triples) 
    i = 1
    a=0
    ans=[]
    for i in triples:
        s1=i[0]+' '+i[1]+' '+i[2]
        scores = rouge.get_scores(s1, s2)
        if scores[0]['rouge-1']["r"] > alpha and scores[0]['rouge-2']["r"] > alpha2 and scores[0]['rouge-l']["r"] > alpha3:
            aa.append(i)
        elif  scores[0]['rouge-1']["p"] > alpha and scores[0]['rouge-2']["p"] > alpha2 and scores[0]['rouge-l']["p"] > alpha3:
            aa.append(i)
            
    return aa
def _extraction_start2(triples_, alpha = 0.7):
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
                        triples.pop(i)
                        if i > 0:
                            i-=1
                    except:
                        pass
                else:
                    try:
                        triples.pop(ii)
                        if ii > 0:
                            ii-=1
                        if i > 0:
                            i-=1
                    except:
                        pass
                        
            ii+=1
        i+=1

# a = open('1234567','w', encoding='utf-8')
# aaa=0
# with open('1234' , 'r' , encoding='utf-8') as f:
    # for line in f:
        # line=line.strip()
        # if line=='':
            # continue
        # if line=='No extractions found.':
            # a.write(line+"\n\n")
            # continue
        # line=re.findall(r'[(](.*?)[)]', line) 
        # if len(line)==0:
            # aaa+=1
            # a.write("\n")
            # continue
        # a.write(line[0]+"\n")
        
        # if aaa % 10000 == 0:
            # print(aaa)
        # if aaa == 500000:
            # break
aaa=0
aaa2=0
a1=open('triples_ollie' , 'r' , encoding='utf-8')
a2=open('triples_openie' , 'r' , encoding='utf-8')
a3=open('summary' , 'r' , encoding='utf-8')
aa1=open('_summary' , 'w' , encoding='utf-8')
aa2=open('triples' , 'w' , encoding='utf-8')
triples1=[]
triples2=[]
while True:
    triple1=a1.readline()
    while triple1 != triple1.strip() and len(triple1.strip()) == 0:
        triple1=a1.readline()
    if triple1.strip() == 'No extractions found.':
        triples1=[]
        triple1=a1.readline()
    else:    
        while len(triple1.strip()) > 0:
            triple1=triple1.strip().split(';')
            triples1.append(triple1)
            triple1=a1.readline()
    if not triple1:
        break
    
    triple2=a2.readline()
    while triple2 != triple2.strip() and len(triple2.strip()) == 0:
        triple2=a2.readline()
    if triple2.strip() == '12345':###
        triples2=[]
        triple2=a2.readline()
    else:    
        while len(triple2.strip()) > 0:
            triple2=triple2.strip().split(';')
            triples2.append(triple2)
            triple2=a2.readline()
    if not triple2:
        break
    
    triples=triples1+triples2
    _extraction_start2(triples)
    summary=a3.readline().strip()
    triples_=_extraction_start_rouge(triples,summary)
    aaa2+=1
    if len(triples_)>0:
        aa1.write(summary+"\n")
        triple_index=[]
        for index, i in enumerate(triples_):
            triple_index.append((index, summary.find(i[0])+summary.find(i[1])+summary.find(i[2])))
        triple_index=sorted(triple_index, key=lambda x: x[1])
        for i in triple_index:
            aa2.write(triples_[i[0]][0]+' '+triples_[i[0]][1]+' '+triples_[i[0]][2]+' ')
        aa2.write("\n")    
        aaa+=1
        if aaa % 1000 == 0:
            print(aaa)
            print(aaa2)
        if aaa == 300000:
            break
            
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    