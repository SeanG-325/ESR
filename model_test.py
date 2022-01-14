from fairseq.models.roberta import RobertaModel
from fairseq.models.bart import BARTModel
from fairseq.data.data_utils import collate_tokens
from collections import defaultdict
import torch
import numpy as np

_triples = "fairseq/123/triples"


triples = open(_concat_triples, 'r', encoding='UTF-8')


# need to be changed before using
_summary = open('fairseq/123/_summary', 'r', encoding='UTF-8') # corresponding summary of the triple
concat_triples = open('fairseq/123/concat_triples', 'w', encoding='UTF-8') # directly concatenate the triples 
ref = open('fairseq/123/ref', 'w', encoding='UTF-8') # reference summary
rewrited = open('fairseq/123/rewrited', 'w', encoding='UTF-8') # rewrited summary

# selector and rewriter checkpoints paths need to be changed before using
roberta = RobertaModel.from_pretrained('/home/sg6063/fairseq/123/checkpoints/', checkpoint_file='checkpoint1.pt')
roberta.eval()
bart = BARTModel.from_pretrained('/home/sg6063/fairseq/123/bart/', checkpoint_file='checkpoint1.pt')
bart.eval()  # disable dropout (or leave in train mode to finetune)
KWARGS = dict(beam=5, lenpen=0.5, max_len_b=25, min_len=3, no_repeat_ngram_size=3)
bart = bart.cuda().half()
s1 = []
s2 = []
summ = []
s = ''
m = 0

# on Gigaword testset
dict = defaultdict(str)
a1 = open('fairseq/123/giga-input')
a2 = open('fairseq/123/giga-ref')
for i in range(1951):
    dict[a2.readline().strip()] = a1.readline().strip()

while True:
    s1 = []
    s1.append(triples.readline().strip())
    #print(s1)
    s1.append(_summary.readline().strip())
    #print(s2)
    summ.append(dict[s1[1]])
    #s1 = []
    
    if len(s1[0])==0 and len(s1[-1])==0 and len(s2) > 0:
        batch = collate_tokens([roberta.encode(pair[0], pair[1]) for pair in s2], pad_idx=1)
        logprobs = roberta.predict('sentence_classification_head', batch).detach().numpy()[:,1]
        #tokens = roberta.encode(s1,s2)
        #a = roberta.predict('sentence_classification_head',tokens).argmax().item()
        #print(a)
        #a = np.array(logprobs)
        a = np.argsort(logprobs).tolist()
        for i in a:
            #if len(s) < 0.5 * len(s2[1][1]) and logprobs[i] > np.log(0.5):
            if logprobs[i] > np.log(0.5):
                s += s2[i][0]
        concat_triples.write(s+"\n")
        s = bart.sample(s, **KWARGS).strip()
        rewrited.write(s+"\n")
        ref.write(summ[-1]+"\n")
        s = ''
        s2 = []
        summ = []
        m += 1
        if m==80:
            break
    else:
        s2.append(s1)
        
        
        
        
        
        
        
        
        
        
        
