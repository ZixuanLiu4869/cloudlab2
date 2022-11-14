# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

def main(words: list) -> list:
    word_count = {}
    for word in words:
        for w in word:
            if w[0] not in word_count.keys():
                word_count[w[0]] = [1]
            else:
                word_count[w[0]].append(1)
    word_count = list(zip(word_count.keys(), word_count.values()))
    print(word_count)
    return word_count