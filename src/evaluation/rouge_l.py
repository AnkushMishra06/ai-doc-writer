from typing import Tuple, List

def tokenize(text: str) -> List[str]:
    """
    Tokenize the text in words.
    """
    return text.lower().split()

def lcs_length(x: List[str], y: List[str]) -> int:
    """
    compute the length of longest common subsequence in both tokenized sequences.
    """
    m, n = len(x), len(y)
    table = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                table[i][j] = table[i-1][j-1]+1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])

    return table[m][n]

def rouge_l_score(candidate : str, reference : str) -> float:
    """
    compute ROUGE-L score between candidate and reference strings.
    """
    candidate_tokens = tokenize(candidate)
    reference_tokens = tokenize(reference)

    if not candidate_tokens or not reference_tokens:
        return 0.0

    lcs = lcs_length(candidate_tokens, reference_tokens)

    precision = lcs/len(candidate_tokens)
    recall = lcs/len(reference_tokens)

    if precision + recall == 0:
        return 0.0

    f1 = 2*precision*recall/(precision+recall)

    return f1