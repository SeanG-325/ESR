import gensim.downloader as api
from gensim.models import TfidfModel
from gensim.corpora import Dictionary
from openie import StanfordOpenIE
dataset = api.load("wiki-english-20171001")
dct = Dictionary(dataset)  # fit dictionary
corpus = [dct.doc2bow(line) for line in dataset]  # convert corpus to BoW format
model = TfidfModel(corpus)  # fit model

client=StanfordOpenIE()
s = "the internet 's most popular capybara enjoyed some downtime in the bath with its duckling friends . capybara joejoe who lives in las vegas with his owner cody kennedy , has almost 60,000 followers on instagram . add that to his near 5,000 facebook likes and his twitter account that boasts over 1,000 twitter followers and you have yourself one popular rodent . the capybara called joejoe has near 60,000 instagram followers and lives in las vegas with his owner cody kennedy . the fuss surrounding the capybara is perhaps at first hard to understand -- until you see the various pictures and videos he is featured in on his various social media accounts . sat in a shallow bath , the large rodent sits perfectly still while three energetic ducklings stand on its head and body . one falls from joejoe 's head -- hitting him in the eye on the way down , before splashing into the water -- but the capybara remains calm . the rodent then begins flicking its ears as another duckling jumps from its back -- the original duck swims around him in the water . the large rodent sits perfectly still in the bath while three energetic ducklings stand on its head and body . a duckling falls from joejoe 's head and hits him in the eye on the way down , before splashing into the water and swimming around him . helping the second duckling -- or deciding he wants to relax in the water a bit more , joejoe crouches slightly to allow it to jump back onto his back . he then submerges his head in the water , which causes a duckling to slide off him . the video concludes with one duckling , who manages to maintain its balance twice when the rodent makes a dive , standing on its back . the giant rodent submerges his head in the water , which causes a duckling to slide off him ."


def _extraction_start(text, model, alpha1 = 0.15, alpha2 = 0.4):
    triples_ = []
    a = client.annotate(text)
    triples = []
    for i in a:
        triples.append(list(i.values()))
    text_ = text.split(' ')
    s = dct.doc2bow(text_)
    s_ = model[s]
    d = {}
    for i in s_:
        d[i[0]] = i[1]
    for i in triples:
        index = 0
        s1 = i[0] + ' ' + i[1] + ' ' + i[2] 
        s1 = s1.split(' ')
        s1_ = dct.doc2bow(s1)
        for item in s1_:
            if item[0] not in d.keys() or d[item[0]] > alpha2:
                index += 1
        if index / len(s1_) > alpha1:
            triples_.append(i)
    for i in triples_:
        print(i)
    return triples_

a = _extraction_start(s, model)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


