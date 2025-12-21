# How Language Models Work

When LLM recieves input prompt from user, the LLM tokenizer converts the prompt into tokens along with token-IDs. These IDs are mapped to embedding vectors, which are processed through the LLM layers to produce a probability distribution over the vocabulary for the next token. The selected token IDs are then decoded by the tokenizer into text, producing the final response for the user.

## LLM Tokenization

It can be defined as process of breaking down text into manageale units called tokens. These are words, subwords or characters. Tokenization helps the LLM to reduce complexity of text data for making it faster.
Token is a unique identifier represented as an integer in model's vocabulary, making model to efficiently manipulate and process text.

## Importance of Tokenization

Tokenization affects:

- vocabulary size
- representation efficiency
- context length / sequence length
- handling of rare / unseen words
- model performance and computational cost
  If tokenization is not performed then for rich languages like English there can be vocabulary explosion problem.

## Types of Tokenization

### Character level

Each character is treated as token.

#### Advantages:

- No vocabulary explosion problems as limited number of tokens possible.
- Tiny vocabulary size

#### Disadvantages:

- Very long sequences
- Weak semantics per token
- Slower training/inference for long sequences

### Word level

Tokens correspond to complete words.

#### Advantages:

- Intuitive segmentation
- Shorter sequences than character-level

#### Disadvantages:

- Requires very large vocabulary
- Fails on unseen or rare words (vocabulary exploaion problem)
- Language-dependent rules

### Subword level

Subword methods split text into fragments smaller than words but larger than characters. They balance vocabulary size and sequence length. They are the most used in GPT, BERT, T5 and LLaMA etc.

#### Advantages:

- avoid OOV failures
- share fragments across related words
- handle rare words efficiently
- compress vocabulary

#### Disadvantages:

Subword tokenization improves vocabulary efficiency and reduces vocabulary issues, but segmentation remains statistical rather than semantic. It can fragment rare or domain-specific words, produces inconsistent boundaries across models, inherits corpus bias, struggles with morphologically rich languages, and creates interoperability challenges due to fixed vocabularies.

#### Byte Pair Encoding (BPE)

BPE merges frequently most occurring token pairs to create subword units. So it has fixed vocabulary size and a deterministic segmentation given merge rules.
its advantages are :-

- Can decompose unfamiliar text into subwords.
- Prevents scaling to huge lexicons.
- Fewer tokens per input.
- Reuses common prefixes/suffixes.
- Efficient for long variable names.
- Minimal computation required.
  its disadvantages are :-
- Breaks words in unintuitive places.
- Purely frequency-driven merges.
- Cannot add new atomic tokens later.
- Rare concepts fragment heavily.
- Merge rules reflect distributional bias.
- Agglutinative languages suffer.

#### WordPiece

Similar to BPE, used in BERTs and related models. It has a difference that it chooses the merge which maximizes the language likelihood.
its advantages are :-

- Subwords allow decomposition of rare tokens.
- Likelihood-based merges smooth boundaries.
- Reduces memory usage.
- Merge choices reflect conditional probabilities.
- Tokens cover longer spans.
  its disadvantages are :-
- Likelihood calculation increases cost.
- Must split unknown tokens.
- Not fully linguistically aware.
- Generates long subword chains.
- Splits technical terms inefficiently.

####

## Embeddings

In Machine Learning, Embedding is a learnable mapping from discrete objects to continuous numeric vectors in a low-dimensional space.

### Why Embedding

Most ML methods expect numerical, continuous inputs. However real world problems have discrete objects like words, sentences, documents, images referenced as discrete objects, tokens in source code, etc. Encoding these in Integers or one-hot-encoding is problematic. Embeddings solve the problems.
A Embedding is a learned mapping from a discrete set to a continuous vector space. eg. word, item, categorical feature and user embeddings in various fields which is implemented through a _Embedding Matrix_

### Embedding Space

A good Embedding space shows the following properties:

- More similar meaning vectors are kept close in vicinity.
- Unrelated vectors are kept distant.
- Small movement yields smooth semantic transition.
- Encodes all essential information in few dimensions.
- linearly regular if sufficiently semantic.

### Learning Mechanism

Embeddings are constructed as trainable parameters in the form of an embedding matrix whose rows correspond to vector representations of discrete objects such as tokens, categories, or items. During model training, this matrix is initialized randomly and refined through gradient descent as the network optimizes its loss function. Each forward pass performs a lookup for relevant indices rather than matrix multiplication, selecting the corresponding vectors to feed into the model. Backpropagation then updates only the embedding vectors participating in the batch, gradually shaping the geometry of the embedding space to encode semantic similarity or task-specific relationships. Consequently, the embedding’s structure emerges implicitly from the learning objective, data distribution, and optimization process rather than from explicit manual design.

### Types of Embedding

#### Word Embedding

1. Word2Vec:
   It is a word embedding technique which converts words in a vector as a collection of numbers, developed by google engineers. Word2Vec can capture semantic meaning of words over BOW and TFIDF, vectors converted have a lower dimension as compared to BOW and TFIDF, It is dense vector as compared to previous techniques.
   There are 2 ways to use this - eighter use pretrained model on your dataset or train your model on dataset and use it.
   Word2Vec uses the intuition - we give features to all the training words and numbers are given from a scale of -1 to 1 or 0 to 1 to each word for each feature. these features make up the vector of dimension d, in real systems these features are created with neural networks (which give the problem that we dont know the meaning of feature).
   Assumption of Word2Vec is that two words sharing similar contexts also share a similar meaning and consequently similar vectors.
   Types of Word2Vec:

- CBOW(Continuous Bag of Words) :- It is to predict central words from contextual words. CBOW trains embeddings by taking multiple context words, averaging their embeddings, and predicting the target word. Embeddings are learned because weight updates push similar contexts to share similar vectors. It is efficient and forms the basis for many deep NLP architectures.
- Skip-gram :- It is reverse of CBOW, formally to predict the surrounding words from central words. The embedding matrix is optimized such that co-occurring words have high dot product similarity. Techniques like negative sampling make training scalable. The resulting vectors capture semantic and syntactic structures learned from distributional patterns.
  [Word2Vec Practice Jupyter Notebook (externel)](https://colab.research.google.com/drive/1uva1YrnxJPBW6mcPswRuZvMLQ1xi56Rd#scrollTo=bb830a41)

2. GloVe:
   GloVe (Global Vectors for Word Representation) is an unsupervised learning algorithm designed to generate dense word embeddings by leveraging global statistical information from a corpus. Unlike Word2Vec’s local context prediction objectives, GloVe is based on factorizing a word–word co-occurrence matrix, ensuring that embeddings encode ratios of co-occurrence probabilities across the entire vocabulary. It constructs word vectors such that meaningful semantic relationships emerge through linear regularities, where vector offsets correspond to relationships like gender or analogies between capitals and countries. The model combines the benefits of matrix factorization and predictive approaches, using weighted least squares optimization to emphasize informative co-occurrence pairs while de-emphasizing extremely frequent, uninformative pairs. The result is an embedding space that captures both global corpus structure and fine-grained semantic similarity, making GloVe highly effective for downstream NLP tasks such as semantic similarity, analogy reasoning, and feature enrichment in machine learning models.

3. and many more like - BERT, GPT token embeddings, ELMo, etc.

#### Sentence and Document Embedding

These encode entire text sequences into fixed vector:

- Sentence-BERT
- Universal Sentence Encoder

#### Graph Embedding

Maps graph vertices to vector space:

- DeepWalk
- Node2Vec
- Graph NN Encoder

#### Recommender Embedding

#### Tabular Embedding

### Evaluating Embeddings

Qualitative evaluation includes:

- _Nearest Neighbour Inspection_ :- observe the closest vectors in embedding space for selected target words or token. It assess semantic similarity preservation and detect contextual embeddings. so, check if a word has semantically related words near it.
- _Word Analogy Resoning_ :- check if embedding support analogies like if 'king' returns 'queen' so what 'man' returns (must return 'woman'). Static embeddings use linear offsets; contextual embeddings require contextual embedding extraction first.
- _Semantic Clustering Visualization_ :- Use dimensionality reduction techniques like PCA, UMAP, t-SNE for visualizing clusters, check if similar semantics group appear together, synonyms appear together.
- _Sentence Embedding Coherence_ :- When sentence are embedded as a whole similar sentences should cluster, paraphases should be close and unrelated sentences should be far apart.

### Advantages and Disadvantages

Advantages:

- compact representation of discrete tokens
- capture semantic structure
- learnable jointly with model
- support differentiable learning
  Disadvantages:
- require large data to learn high-quality embeddings
- interpretability is limited
- embedding space meaning depends on objective
- transferability across domains may fail

## Transformers

## Autoregressive Generation

# Hallucintion in LLMs
