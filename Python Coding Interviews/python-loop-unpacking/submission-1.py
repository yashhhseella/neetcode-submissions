from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    realName = ""
    currentMax = 0
    for scoress in scores:
        name, score = scoress
        if score > currentMax:
            currentMax = score
            realName = name
    return realName


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
