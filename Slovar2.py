languages1 = {
    'jen': ['python', 'ruby'],
    'sarah': ['c','c++'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
     }
for name, languages in languages1.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())