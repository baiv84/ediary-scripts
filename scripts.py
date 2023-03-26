import random
from datacenter.models import Mark
from datacenter.models import Lesson
from datacenter.models import Schoolkid
from datacenter.models import Chastisement
from datacenter.models import Commendation


def get_child_by_name(name):
    """Return child entity by 'name' field from the database"""
    """(only 1 record or None in case of exception)"""
    child = None
    name = name.strip()
    if not len(name):
        raise SystemExit("""Empty child names are not allowed!\n"""
                         """Exit from program!""")
    try:
        child = Schoolkid.objects.filter(full_name__contains=name).get()
    except Schoolkid.MultipleObjectsReturned:
        print(f'Oops, more than 1 child with name "{name}" in database')
    except Schoolkid.DoesNotExist:
        print(f'Oops, there is no child with name "{name}" in database')
    return child


def fix_marks(child_name='Фролов Иван'):
    """Fix bad marks of particular child - replace bad mark with '5'"""
    corrected_marks_count = -1
    child = get_child_by_name(child_name)
    if child:
        bad_marks = Mark.objects.filter(schoolkid=child, points__lte=3)
        for mark in bad_marks:
            print(f'Fix bad mark, child - {child_name}, "{mark.points}" -->> replace with "5"')
            mark.points = 5
            mark.save()
        corrected_marks_count = len(bad_marks)
    return corrected_marks_count


def remove_chastisements(child_name='Фролов Иван'):
    """Delete particular child's chastisements from the diary"""
    removed_chastisements_count = -1
    child = get_child_by_name(child_name)
    if child:
        chastisements = Chastisement.objects.filter(schoolkid=child)
        removed_chastisements_count = len(list(map(lambda chastisement: chastisement.delete(), chastisements)))
    return removed_chastisements_count


def create_commendation(child_name='Фролов Иван', subject_title='Математика'):
    """Make random commendation to some schoolkid"""
    messages = [
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
    ]
    error_code = -1

    child = get_child_by_name(child_name)
    if child:
        year = child.year_of_study
        letter = child.group_letter
        lessons = Lesson.objects.filter(subject__title__contains=subject_title,
                                        year_of_study=year,
                                        group_letter=letter).order_by('-date')
        if not lessons:
            print(f"""Error occured - check subject title name, """
                  f"""may be title "{subject_title}" is incorrect!""")
            return error_code

        while True:
            lesson = random.choice(lessons)
            subject = lesson.subject
            teacher = lesson.teacher
            created = lesson.date
            check_lesson = Commendation.objects.filter(schoolkid=child, subject=subject,
                                                       teacher=teacher, created=created).count()
            if not check_lesson:
                print(f"""Lesson - {lesson.subject.title}, """
                      f"""child - {child_name}, """
                      f"""teacher - {lesson.teacher.full_name}, """
                      f"""date - {lesson.date} -> Make new Commendation""")
                text = random.choice(messages)
                Commendation.objects.create(text=text, created=lesson.date,
                                            schoolkid=child, subject=lesson.subject,
                                            teacher=lesson.teacher
                                            )
                error_code = 0
                break
    else:
        print('No commendation done...')
    return error_code
