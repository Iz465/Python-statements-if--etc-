

def substring(string, name_list):
    emma = string.count("Emma")
    john = string.count("John")
    jack = string.count("Jack")
    
    name_list.append(emma)
    name_list.append(john)
    name_list.append(jack)



name_list = []
sentence1 = "Emma is a good developer. Emma is a writer" # Emma = 2 John = 0 Jack = 0
sentence2 = "Emma has a  Father named John, John is old. John is smart. John raised Emma at his house." # Emma = 2 John = 4 Jack = 0
sentence3 = "Emma has a son named Jack. Jack is agile. Jack plays sports. Jack, John and Emma live together. Emma takes Jack to school." # Emma = 3 John = 1 Jack = 5

result1 = substring(sentence1, name_list)
result2 = substring(sentence2, name_list)
result3 = substring(sentence3, name_list)

print("\t\tEmma\tJohn\tJack")
num = 0
sentence_num = 1
for name in name_list:
    if num == 0:
        print(f"Sentence {sentence_num}: ", end = "\t")
        sentence_num += 1
    print(f"  {name}", end = "\t")
    num += 1
 
    if num == 3:
        print("\n")
        num = 0
    

 



