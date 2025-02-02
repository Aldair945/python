def reverse_sentence(sentence):
    sentence = list(sentence.split())
    sentence.reverse()
    for i in sentence:
        print(i, end = " ")
sentence = input()
reverse_sentence(sentence)