# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")

# greet_with("Bot", "New York")

def calculate_love_score(name1, name2):
    true_score = 0
    love_score = 0
    love = ["l","o","v","e"]
    true = ["t","r","u","e"]
    all_characters = (name1 + name2).lower()
    for l in love:
        love_score += all_characters.count(l)
    
    for t in true:
        true_score += all_characters.count(t)
        
    print(f"{true_score}{love_score}")


calculate_love_score("Kanye West", "Kim Kardashian")