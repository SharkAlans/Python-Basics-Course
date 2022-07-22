

class Student:

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def study(self):
        print(f'{self.name} is learning...')

    def sawatdee():
        if self.gender == 'ชาย':
            tail = 'ครับ'
            callme = 'ผม'
        else:
            tail = 'ค่ะ'
            callme = 'หนู'
        print('สวัสดี{tail} {callme}ซี่อ{self.name}')

class SpecialStudent(Student):

    def __init__(self,name,age,gender,parent):
        super().__init__(name,age,gender)
        self.parent = parent

    def hello(self, person='เพื่อน'):
        if person == 'เพื่อน':
            print('เฮัย! ว่าไง? สบายดีไหม?')
        else:
            print('ไม่รู้ว่าเขาคือใครเดินออกดีกว่า')
            
    def sawatdee(self):
        print('สวัสดี ซี่อ{self.name}')

    def myfather(self):
        print('รู้ไหม? ผมลูกใคร')
        print(f'ผมลูก{self.parent}')



class Teacher:

    def __init__(self,name,gender,subject):
        self.name = name
        self.gender = gender
        self.subject = subject

    def teach(self):
        print(' {} is teaching {}'.format(self.name,self.subject))


if __name__ == '__main__':
    student1 = Student('Sam',9,'ชาย')
    student2 = Student('May',9,'หญิง')
    special_student = SpecialStudent('George',9,'ซาย','นายกอบต.เจท')

    teacher1 = Teacher('Teacher John','Men','Teaches English')
    print(teacher1.name)
    print(teacher1.subject)

    print('---08.30----')
    # student1.sawatdee()
    # student2.sawatdee()
    teacher1.teach()
    student1.study()
    student2.study()
    print('---08.45---')
    special_student.sawatdee()
    print('George walk to his own desk')
    special_student.hello('เพื่อน')
    print(f'{teacher1.name}! Can I have good grades')
    special_student.myfather()


