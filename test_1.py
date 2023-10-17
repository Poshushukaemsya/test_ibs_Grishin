

# с условием на не более чем 1 дубликат для каждого элемента
# достаточно проверить нет ли далее в списке такого же элемента
def duplicate_nums(lst):
    return sorted([n for i,n in enumerate(lst) if n in lst[i+1:]]) or None

