from fixtures.data import *


def uniq_names(mentors):
    # Добавляем в список всех преподавателей со всех курсов
    all_list = []
    for m in mentors:
        all_list.extend(m)
    # Код, который заполнит all_list.

    # Делаем список all_names_list, состоящий только из имён, и заполняем его
    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)
    # Делаем так, чтобы остались только уникальные имена (без повторений)
    unique_names = list(set(all_names_list))

    # Теперь необходимо отсортировать имена в алфавитном порядке, используя sorted() для списка
    all_names_sorted = sorted(unique_names)
    # Результат будет в all_names_sorted
    return f'Уникальные имена преподавателей: {", ".join(all_names_sorted)}'

def top3_uniq_names(mentors):
    all_list = []
    for m in mentors:
        all_list.extend(m)

    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)

    # Уникальные имена будут в unique_names
    unique_names = list(set(all_names_list))

    # Подсчёт встречаемости каждого имени через list.count()
    popular = []
    for name in unique_names:
        popular.append([name, all_names_list.count(name)])  # Добавить подсчёт имён
    # Это код для сортировки списка с элементами вида [имя, количество] по убыванию встречаемости
    popular.sort(key=lambda x: x[1], reverse=True)

    # Получаем топ-3 часто встречающихся имён из списка popular
    top_3 = popular[0:3]
    for top_3_final in top_3:
        top_ = [(f"{top_3_final[0]}: {top_3_final[1]} раз(а)") for top_3_final in top_3]
    return ", ".join(top_)


def sup_names(mentors):
    # Делаем список списков имён
    mentors_names = []
    for m in mentors:
        course_names = []
        for name in m:
            course_names.append(name.split()[0])
        # Код, который добавляет списки имён в общий список mentors_names:
        mentors_names.append(sorted(course_names))

    # Храним здесь пары курсов, в которых есть совпавшие имена
    pairs = []
    list_mentors = []
    # # Попарное сравнение "наборов" преподавателей на курсах. Каждую новую пару запоминаем для исключения повторов.
    for id1 in range(len(mentors_names)):
        for id2 in range(len(mentors_names)):
            # Проверяем, что мы не сравниваем список сам с собой:
            if id1 == id2:
                continue
            # Код для сравнения двух "наборов" преподавателей, используя множества
            intersection_set = set(mentors_names[id1]).intersection(set(mentors_names[id2]))
            if len(intersection_set) > 0:  # Допишите проверку, что результат не пустой, имена есть
                # Код, который проверяет, что эта пара еще не встречалась
                pair = {courses[id1], courses[id2]}
                # Если pair еще не встречалась, то выведем на экран два курса и список преподавателей, которые есть
                # на обоих курсах
                if pair not in pairs:
                    pairs.append(pair)
                    # Отсортируем имена по алфавиту, используя sorted() для списка
                    all_names_sorted = sorted(intersection_set)
                    # Конструкция вывода результата, используя string.join()
                    list_mentors.append(f"На курсах '{courses[id1]}' и '{courses[id2]}' преподают: {', '.join(str(i) for i in all_names_sorted)}\n")
    return f'{list_mentors[0]}{list_mentors[1]}{list_mentors[2]}{list_mentors[3]}'


# res1 = top3_uniq_names(mentors)
# res2 = sup_names(mentors)
# res3 = uniq_names(mentors)
#
# print(res1)
# print(res2)
# print(res3)