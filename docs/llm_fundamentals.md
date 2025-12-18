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