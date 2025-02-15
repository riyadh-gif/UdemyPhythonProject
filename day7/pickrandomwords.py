import random

word_list = ["chicken","cow","camel"]
random_item = random.choice(word_list)

user_input = input("masukan karakter: ").strip()

result = [char == user_input for char in random_item]

print(random_item)

for res in result:
    print(res)
