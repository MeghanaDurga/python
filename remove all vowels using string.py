st="mango"
char=list(st)
vowels="aeiouAEIOU"
for vowel in vowels:
    while vowel in char:
        char.remove(vowel)
result=" ".join(char)
print("string without vowels:",result)
