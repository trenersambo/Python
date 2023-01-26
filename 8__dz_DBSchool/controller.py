"""Модуль взаимодействия пользователя с базой данных"""
import sys

import model
import view

PATH_FILE = ''
TEXT_INFO = '\nИнформация не найдена.\nУбедитесь в правильности ввода данных.'


def input_parents(command: int):
    """Обработка запросов родителей"""
    match command:
        case 1:
            name = view.get_name()
            if model.check_name(model.get_journal(), name):
                view.show_pupil_lessons(model.get_journal(), name)
            else:
                view.show_message(TEXT_INFO)
        case 2:
            name, lesson = view.get_name(), view.get_lesson()
            if model.check_info(model.get_journal(), lesson, name):
                view.show_pupil_lesson(model.get_journal(), name, lesson)
            else:
                view.show_message(TEXT_INFO)
        case 3:
            sys.exit()


def input_teacher(command: int):
    """Обработка запросов учителя"""
    match command:
        case 1:
            view.show_list_pupils(model.get_journal())
        case 2:
            view.show_journal(model.get_journal())
        case 3:
            lesson = view.get_lesson()
            if model.check_lesson(model.get_journal(), lesson):
                view.show_progress_lesson(model.get_journal(), lesson)
            else:
                view.show_message(TEXT_INFO)
        case 4:
            control_knowledge()
        case 5:
            sys.exit()


def start():
    """Запуск программы"""
    global PATH_FILE
    view.main_menu()
    access = view.choice_access()
    PATH_FILE = view.choice_class()
    model.read_db(PATH_FILE)
    if access != 1:
        while True:
            command = view.command_teacher()
            input_teacher(command)
    else:
        while True:
            command = view.command_parents()
            input_parents(command)


def control_knowledge():
    """Контроль знаний ученика"""
    lesson = view.get_lesson()
    if model.check_lesson(model.get_journal(), lesson):
        view.show_message('Кто будет отвечать?')
        name = view.get_name()
        if model.check_name(model.get_journal(), name):
            mark = view.control()
            model.add_mark(model.get_journal(), mark, lesson, name, PATH_FILE)
            view.show_pupil_lesson(model.get_journal(), name, lesson)
        else:
            view.show_message(TEXT_INFO)
    else:
        view.show_message(TEXT_INFO)
