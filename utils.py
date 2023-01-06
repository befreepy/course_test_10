import json

"""
Получаем список студентов
"""

def load_candidates():
    with open('candidates.json', "r", encoding='utf8') as file:
        return json.load(file)


"""
Показываем всех кандидатов
"""

def get_all():
    return load_candidates()

"""
Возвращаем кандидата по pk
"""

def get_by_pk(pk):
    for candidate in load_candidates():
        if candidate['pk'] == pk:
            return candidate
    return

"""
Возвращаем кандидатов по навыку
"""


def get_by_skill(skill):
    candidates = []
    for candidate in load_candidates():
        if skill.lower() in candidate['skills'].lower().split(', '):
            candidates.append(candidate)
    return candidates


