def remove_fourth_character(word: str) -> str:
    newword1 = word[:3]
    newword2 = word[4:]

    new = newword1 + newword2

    return new


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
