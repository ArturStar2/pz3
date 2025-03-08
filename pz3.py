class Result:
    def __init__(self, student, semester, subjects, attestations):
        self.student = student
        self.semester = semester
        self.subjects = subjects
        self.attestations = attestations

    def get_student(self):
        return self.student

    def set_student(self, value):
        self.student = value

    def get_semester(self):
        return self.semester

    def set_semester(self, value):
        self.semester = value

    def get_subjects(self):
        return self.subjects

    def set_subjects(self, value):
        self.subjects = value

    def get_attestations(self):
        return self.attestations

    def set_attestations(self, value):
        self.attestations = value

    def no_attestations(self):
        return self.attestations.count(False)

    def __str__(self):
        return f"Студент: {self.student}, Семестр: {self.semester}, Не аттестаций: {self.no_attestations()}"


student1 = Result("Краснова София Викторовна", 1, ["Математика", "Физика", "Информатика"], [True, False, True])
student2 = Result("Орлов Тимур Романович", 2, ["Химия", "Биология", "География"], [False, False, True])

print(student1)
print(student2)
