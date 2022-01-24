# class Student:
#
#     def __init__(self, name):
#         self.name = name
#
#     def print_info(self):
#         print(f'{self.name} => ', end='')
#
#     class Inner:
#         def __init__(self, mod, proc, memory):
#             self.mod = mod
#             self.proc = proc
#             self.memory = memory
#
#         def print_info_nout(self):
#             print(f'{self.mod}, {self.proc}, {self.memory}')
#
#
# s1 = Student('Roman')
# s2 = s1.Inner('WP', 16, 17)
# s1.print_info()
# s2.print_info_nout()
# s1 = Student('Vladimir')
# s2 = s1.Inner('WP', 17, 16)
# s1.print_info()
# s2.print_info_nout()
# ==========================================================


class Student:
    def __init__(self, name):
        self.name = name
        self.note = self.Notebook()

    def show(self):
        print(self.name, end='')
        self.note.show()

    class Notebook:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = '17'
            self.ram = 16

        def show(self):
            print(f'==>{self.brand}, {self.cpu}, {self.ram}')


s1 = Student('Vladimir')
s2 = Student('Roman')
# s3 = s1.Notebook()
s1.show()
s2.show()
