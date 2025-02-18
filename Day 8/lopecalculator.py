def calculate_love_score(name1,name2):
    true_letter = ["T","R","U","E"]
    love_letter = ["L","O","V","E"]
    
    word = list(name1.upper())
    word2 = list(name2.upper())
    
    word_combined = word + word2

    arr1 = str(sum(1 for item in word_combined if item in true_letter))
    arr2 = str(sum(1 for item in word_combined if item in love_letter))

    sumar = arr1 + arr2
    print(sumar)


calculate_love_score("Kanye West", "Kim Kardashian")
   