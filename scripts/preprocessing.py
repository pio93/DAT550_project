from tqdm import tqdm
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, RegexpTokenizer

def pre_proc(df):
    df.drop(['title1_zh', 'title2_zh'], axis=1, inplace=True)
    df.replace(['agreed', 'disagreed'], 'related', inplace=True)

    # Convert text to lower case
    title1_en = [c.lower() for c in tqdm(title1_en)]
    title2_en = [c.lower() for c in tqdm(title2_en)]

    tokens1 = [word_tokenize(c) for c in tqdm(title1_en)]
    tokens2 = [word_tokenize(c) for c in tqdm(title2_en)]

    #Remove stop words
    sw = stopwords.words("english")
    tokens1 = [[word for word in t if word not in sw] for t in tqdm(tokens1)]
    tokens2 = [[word for word in t if word not in sw] for t in tqdm(tokens2)]

    tokenizer = RegexpTokenizer(r'\w+')
    tokens1 = [["".join(tokenizer.tokenize(word)) for word in t 
          if len(tokenizer.tokenize(word)) > 0] for t in tqdm(tokens1)]
    tokens2 = [["".join(tokenizer.tokenize(word)) for word in t 
          if len(tokenizer.tokenize(word)) > 0] for t in tqdm(tokens2)]