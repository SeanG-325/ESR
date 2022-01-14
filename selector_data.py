import re
from rouge import Rouge 
import random
random.seed(123)
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
    
def _extraction_start_rouge_label(triples, s2, p_alpha = 0.35, alpha2 = 0, alpha3=0, n_alpha=0.2):
    rouge = Rouge()
    p=[]
    n=[]
    l = len(triples) 
    i = 1
    a=0
    ans=[]
    for i in triples:
        s1=i[0]+' '+i[1]+' '+i[2]
        scores = rouge.get_scores(s1, s2)
        if scores[0]['rouge-1']["r"] > p_alpha:# and scores[0]['rouge-2']["r"] > alpha2 and scores[0]['rouge-l']["r"] > alpha3:
            p.append(i)
        elif  scores[0]['rouge-1']["p"] > p_alpha:# and scores[0]['rouge-2']["p"] > alpha2 and scores[0]['rouge-l']["p"] > alpha3:
            p.append(i)
        else:#  scores[0]['rouge-1']["p"] < n_alpha and scores[0]['rouge-1']["r"] < n_alpha:# and scores[0]['rouge-2']["p"] > alpha2 and scores[0]['rouge-l']["p"] > alpha3:
            n.append(i)
            
    return p, n


def _extraction_start2(triples_, alpha = 0.6):
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
a4=open('article1' , 'r' , encoding='utf-8')
input1=open('_triple' , 'w' , encoding='utf-8')
input2=open('_article' , 'w' , encoding='utf-8')
label=open('_label' , 'w' , encoding='utf-8')
triples1=[]
triples2=[]
while True:
    triples1=[]
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
    triples2=[]
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
    article=a4.readline().strip()
    triples_p, triples_n=_extraction_start_rouge_label(triples,summary)
    aaa2+=1
    
    
    #print(triples_n)
    #print("\n\n")
    for i in triples_p:
        input1.write(i[0]+' '+i[1]+' '+i[2]+"\n")
        input2.write(article+"\n")
        label.write("1\n")
    
    for i in triples_n:
        a = random.random()
        if a > 0.75:
            input1.write(i[0]+' '+i[1]+' '+i[2]+"\n")
            input2.write(article+"\n")
            label.write("0\n")
    
    
   
    
    