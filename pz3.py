class Result:
    def __init__(self, student, semester, subjects, attestations):
        self._student = student
        self._semester = semester
        self._subjects = subjects
        self._attestations = attestations

    def get_student(self):
        return self._student

    def set_student(self, value):
        self._student = value

    def get_semester(self):
        return self._semester

    def set_semester(self, value):
        self._semester = value

    def get_subjects(self):
        return self._subjects

    def set_subjects(self, value):
        self._subjects = value

    def get_attestations(self):
        return self._attestations

    def set_attestations(self, value):
        self._attestations = value

    def count_non_attestations(self):
        return self._attestations.count(False)

    def __str__(self):
        return f"Студент: {self._student}, Семестр: {self._semester}, Не аттестаций: {self.count_non_attestations()}"


# Пример использования
student1 = Result("Иванов Иван", 3, ["Математика", "Физика", "Информатика"], [True, False, True])
student2 = Result("Петрова Анна", 5, ["Химия", "Биология", "География"], [False, False, True])

print(student1)
print(student2)
