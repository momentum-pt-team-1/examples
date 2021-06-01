def return_phrases():
    return "More organized", "More readable", "Easier reuse", "Share and connect"

def build_sentence(banana):
    return "%s is a benefit of functions!" % banana

def name_benefits_of_functions():
    all_the_phrases = return_phrases()
    print("all_the_phrases: ", all_the_phrases)
    for item in all_the_phrases:
        print("The current item is: ", item, "index:", all_the_phrases.index(item))
        print(build_sentence(item))

name_benefits_of_functions()