import pytest
from collections import *
from fixtures.data import *


@pytest.mark.parametrize(
    'mentors_', 'expected', [
        [mentors, 'Уникальные имена преподавателей: Адилет, Азамат, Александр, Алексей, Алена, Анатолий, '
                  'Анна, Антон, Вадим, Валерий, Владимир, Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, '
                  'Константин, Максим, Михаил, Никита, Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, '
                  'Филипп, Эдгар, Юрий']
    ]
)
def test_uniq_names(mentors_, expected):
    result = uniq_names(mentors)
    assert result == expected


@pytest.mark.parametrize(
    'mentors_', 'expected', [
        [mentors, 'Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)']
    ]
)
def test_top3_uniq_names(mentors_, expected):
    result = top3_uniq_names(mentors)
    assert result == expected


@pytest.mark.parametrize(
    'mentors_', 'expected', [
        [mentors, "На курсах 'Python-разработчик с нуля' и 'Java-разработчик с нуля' преподают: Антон, Евгений, Максим"
                  "На курсах 'Python-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Александр, "
                  "Евгений, Елена, Кирилл, Максим, Олег, Роман"
                  "На курсах 'Python-разработчик с нуля' и 'Frontend-разработчик с нуля' преподают: Александр, Евгений"
                  "На курсах 'Java-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Денис, Евгений, "
                  "Максим"
                  "На курсах 'Java-разработчик с нуля' и 'Frontend-разработчик с нуля' преподают: Денис, Евгений"
                  "На курсах 'Fullstack-разработчик на Python' и 'Frontend-разработчик с нуля' преподают: Александр, "
                  "Алена, Владимир, Денис, Евгений, Эдгар"]
    ]
)
def test_sup_names(mentors_, expected):
    result = sup_names(mentors)
    assert result == expected