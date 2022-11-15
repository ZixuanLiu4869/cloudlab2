# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

def main(line: tuple) -> list:
    word_list = []
    words = line[1].strip().split(' ')
    for word in words:
        word_list.append((word, 1))
    
    print(word_list)

    return word_list