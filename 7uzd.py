from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

words = ['māja', 'dzīvoklis', 'jūra']

vectors = [model[word] for word in words if word in model]

similarity_matrix = {}

for i in range(len(vectors)):
    for j in range(i+1, len(vectors)):
        similarity = model.cosine_similarities(vectors[i], [vectors[j]])[0]
        similarity_matrix[(words[i], words[j])] = similarity

for word_pair, similarity in similarity_matrix.items():
    print(f"Semantisks līdzīgums starp '{word_pair[0]}' un '{word_pair[1]}': {similarity:.4f}")
