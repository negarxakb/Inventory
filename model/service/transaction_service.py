from controller.exception.exception import TransactionNotFoundError
from model.da.da import *
from model.entity.transaction import Transaction

class LessonService:
    @staticmethod
    def save(lesson):
        lesson_da = DataAccess(Transaction)
        lesson_da.save(lesson)
        return lesson

    @staticmethod
    def edit(lesson):
        lesson_da = DataAccess(lesson)
        if lesson_da.find_by_id(lesson.id):
            lesson_da.edit(lesson)
            return lesson
        else:
            raise TransactionNotFoundError()

    @staticmethod
    def remove(id):
        lesson_da = DataAccess(Lesson)
        if lesson_da.find_by_id(id):
            return lesson_da.remove(id)
        else:
            raise TransactionNotFoundError()

    @staticmethod
    def find_all():
        lesson_da = DataAccess(Lesson)
        return lesson_da.find_all()

    @staticmethod
    def find_by_id(id):
        lesson_da = DataAccess(Lesson)
        return lesson_da.find_by_id(id)

    # todo : group, department, title, code

    @staticmethod
    def find_by_lesson_group(lesson_group):
        lesson_da = DataAccess(Lesson)
        return lesson_da.find_by(Lesson.lesson_group == lesson_group)

    @staticmethod
    def find_by_department(department):
        lesson_da = DataAccess(Lesson)
        return lesson_da.find_by(Lesson.department == department)

    @staticmethod
    def find_by_title(title):
        lesson_da = DataAccess(Lesson)
        return lesson_da.find_by(Lesson.title == title)

    @staticmethod
    def find_by_code(code):
        lesson_da = DataAccess(Lesson)
        return lesson_da.find_by(Lesson.code == code)