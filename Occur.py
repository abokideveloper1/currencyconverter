sentence = str(input("Enter a sentence: ")).strip()
print("The word A is found {} times".format(sentence.upper().count("A")))
print("The word A is found for the first time at position {}".format(sentence.upper().find("A")+1))
print("The word A is found for the last time at position {}".format(sentence.upper().rfind("A")+1))