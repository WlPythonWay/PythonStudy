#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


class Manager:
    """
    管理员
    """
    def __init__(self, username, password):
        """
        初始化
        """
        self.admin_username = username
        self.admin_password = password
        self.menu_dict = {
            '1': self.create_school,
            '2': self.create_lesson,
            '3': self.create_classes,
            '4': self.create_manager,
            '5': self.create_teacher,
            '6': self.create_student
        }

    def menu(self):
        while True:
            action.is_exist()
            info = '''            1、创建学校
            2、创建课程
            3、创建班级
            4、创建管理员
            5、创建老师
            6、创建学生
            7、退出登录'''
            print(info)
            choice = input('请输入选项：')
            if choice in self.menu_dict:
                self.menu_dict[choice]()
            elif choice == '7':
                action.logout()
                return
            else:
                print('输入错误')

    def create_school(self):
        name = input('请输入学校名字：')
        if name in action.role_content['school']:
            print('学校已存在')
            return
        addr = input('请输入学校地址：')
        school = School(name, addr)
        action.save(school)

    def create_lesson(self):
        name = input('请输入课程名字：')
        if name in action.role_content['lesson']:
            print('课程已存在')
            return
        school = input('请输入课程所在学校：')
        if school not in action.role_content['school']:
            print('学校不存在')
            return
        cycle = input('请输入课程周期：')
        fee = input('请输入课程费用：')
        lesson = Lesson(name, school, cycle, fee)
        action.save(lesson)

    def create_classes(self):
        name = input('请输入班级名字：')
        if name in action.role_content['classes']:
            print('班级已存在')
            return
        lesson = input('请输入班级课程：')
        if lesson not in action.role_content['lesson']:
            print('课程不存在')
            return
        teacher = input('请输入班级老师：')
        # if teacher not in action.role_content['teacher']:
        #     print('老师不存在')
        #     return
        classes = Classes(name, lesson, teacher)
        action.save(classes)

    def create_manager(self):
        username = input('请输入用户名：')
        if username in action.role_content['teacher']:
            print('管理员已存在')
            return
        password = input('请输入密码：')
        manager = Manager(username, password)
        action.save(manager)

    def create_teacher(self):
        name = input('请输入用户名：')
        if name in action.role_content['teacher']:
            print('老师已存在')
            return
        password = input('请输入密码：')
        school = input('请输入学校：')
        if school not in action.role_content['school']:
            print('学校不存在')
            return
        classes = input('请输入班级：')
        if classes not in action.role_content['classes']:
            print('班级不存在')
            return
        teacher = Teacher(name, password, school, classes)
        action.save(teacher)

    def create_student(self):
        name = input('请输入学生姓名：')
        if name in action.role_content['student']:
            print('学生已存在')
            return
        password = input('请输入密码：')
        classes = input('请输入班级：')
        if classes not in action.role_content['classes']:
            print('班级不存在')
            return
        teacher = input('请输入老师姓名：')
        if teacher not in action.role_content['teacher']:
            print('老师不存在')
            return
        student = Student(name, password, classes, teacher)
        action.save(student)


class School:
    """
    学校
    """
    def __init__(self, name, addr):
        """
        初始化
        :param name: 学校名称
        :param addr: 学校地址
        """
        self.school_name = name
        self.school_addr = addr


class Lesson:
    """
    课程
    """
    def __init__(self, name, school, cycle, fee):
        """
        初始化
        """
        self.lesson_name = name
        self.lesson_school = school
        self.lesson_cycle = cycle
        self.lesson_fee = fee


class Classes:
    """
    班级
    """
    def __init__(self, name, lesson, teacher):
        """
        初始化
        """
        self.class_name = name
        self.class_lesson = lesson
        self.class_teacher = teacher


class Teacher:
    """
    老师
    """
    def __init__(self, name, password, school, classes):
        """
        初始化
        """
        self.teacher_name = name
        self.teacher_password = password
        self.teacher_school = school
        self.teacher_classes = classes
        self.menu_dict = {
            '1': self.view_classes,
            '2': self.view_lesson
        }

    def menu(self):
        while True:
            info = '''            1、查看班级
            2、查看课程
            3、退出登录'''
            print(info)
            choice = input('请输入选项：')
            if choice in self.menu_dict:
                self.menu_dict[choice]()
            elif choice == '3':
                action.logout()
                return
            else:
                print('输入错误')

    def view_classes(self):
        print('所教班级：%s' % self.teacher_classes)

    def view_lesson(self):
        teacher_lesson = None
        with open('data/classes', encoding='utf-8') as f:
            for i in f:
                if self.teacher_classes == i.split('|')[0]:
                    teacher_lesson = i.split('|')[1]

            if not teacher_lesson:
                print('老师所属班级不存在')
                return
        print('所教课程：%s' % teacher_lesson)


class Student:
    """
    学生
    """
    def __init__(self, name, password, classes, teacher):
        """
        初始化
        """
        self.student_name = name
        self.student_password = password
        self.student_classes = classes
        self.student_teacher = teacher
        self.menu_dict = {
            '1': self.view_classes,
            '2': self.view_lesson
        }

    def menu(self):
        while True:
            info = '''            1、查看班级
            2、查看课程
            3、退出登录'''
            print(info)
            choice = input('请输入选项：')
            if choice in self.menu_dict:
                self.menu_dict[choice]()
            elif choice == '3':
                action.logout()
                return
            else:
                print('输入错误')

    def view_classes(self):
        print('所在班级：%s' % self.student_classes)

    def view_lesson(self):
        print('授课老师：%s' % self.student_teacher)


class Action:
    """
    运行
    """
    def __init__(self):
        """
        初始化
        """
        self.login_status = False
        self.role_content = {
            'school': [],
            'lesson': [],
            'classes': [],
            'student': [],
            'teacher': [],
            'admin': []
        }
        self.file_name_list = ['school', 'lesson', 'classes', 'user']

    def create_file(self):
        """
        创建文件夹和文件
        :return:
        """
        dir_name = 'data'
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        for file_name in self.file_name_list:
            file_name = dir_name + '/' + file_name
            if not os.path.exists(file_name):
                file = open(file_name, 'w', encoding='utf-8')
                if 'user' in file_name:
                    file.write('admin|123456|admin\n')
                file.close()

    def login(self, username, password):
        """
        登录
        :return:
        """
        with open('data/user', encoding='utf-8') as file_read:
            for line in file_read:
                info = line.split('|')
                if username == info[0] and password == info[1]:
                    if self.login_status:
                        print('Already login, Please Logout !')
                        return
                    self.login_status = True
                    print('Login Success !')
                    return info[-1].strip()

            if not self.login_status:
                print('Username or password incorrect, Login fail ! ')
                return

    def logout(self):
        """
        登出
        :return:
        """
        if not self.login_status:
            print('Not logged in, Please Login !')
            return
        self.login_status = False
        print('Logout Success !')

    def save(self, obj):
        """
        保存信息
        :return:
        """
        if 'school_name' in obj.__dict__:
            with open('data/school', 'a', encoding='utf-8') as f:
                f.write('%s|%s\n' % (obj.school_name, obj.school_addr))
        elif 'lesson_name' in obj.__dict__:
            with open('data/lesson', 'a', encoding='utf-8') as f:
                f.write('%s|%s|%s|%s\n' % (obj.lesson_name, obj.lesson_school, obj.lesson_cycle, obj.lesson_fee))
        elif 'class_name' in obj.__dict__:
            with open('data/classes', 'a', encoding='utf-8') as f:
                f.write('%s|%s|%s\n' % (obj.class_name, obj.class_lesson, obj.class_teacher))
        elif 'admin_name' in obj.__dict__:
            with open('data/user', 'a', encoding='utf-8') as f:
                f.write('%s|%s|%s\n' % (obj.admin_username, obj.admin_password, 'admin'))
        elif 'teacher_name' in obj.__dict__:
            with open('data/user', 'a', encoding='utf-8') as f:
                f.write('%s|%s|%s|%s|%s\n' % (obj.teacher_name, obj.teacher_password, obj.teacher_school, obj.teacher_classes, 'teacher'))
        elif 'student_name' in obj.__dict__:
            with open('data/user', 'a', encoding='utf-8') as f:
                f.write('%s|%s|%s|%s|%s\n' % (obj.student_name, obj.student_password, obj.student_classes, obj.student_teacher, 'student'))

    def is_exist(self):
        """
        判断是否存在
        :return:
        """
        for file_name in self.file_name_list:
            with open('data/%s' % file_name, encoding='utf-8') as fr:
                for line in fr:
                    if file_name == 'user':
                        role = line.split('|')[-1].strip()
                        file_name = role
                    self.role_content[file_name].append(line.split('|')[0])


if __name__ == '__main__':
    action = Action()
    action.create_file()

    while not action.login_status:
        print('欢迎登录老男孩学员管理系统(初始管理员：admin/123456)')
        print('1、登录\n2、退出')
        choice = input('请输入选项：')
        if choice == '1':
            username = input('用户名：')
            password = input('密码：')
            role = action.login(username, password)
            if role == 'admin':
                obj = Manager(username, password)
                obj.menu()

            elif role == 'student':
                with open('data/user', encoding='utf-8') as f:
                    for i in f:
                        if username == i.split('|')[0] and password == i.split('|')[1] and role == i.split('|')[-1].strip():
                            student_classes = i.split('|')[2]
                            student_teacher = i.split('|')[3]
                            break
                obj = Student(username, password, student_classes, student_teacher)
                obj.menu()
            elif role == 'teacher':
                with open('data/user', encoding='utf-8') as f:
                    for i in f:
                        if username == i.split('|')[0] and password == i.split('|')[1] and role == i.split('|')[-1].strip():
                            teacher_school = i.split('|')[2]
                            teacher_classes = i.split('|')[3]
                            break
                obj = Teacher(username, password, teacher_school, teacher_classes)
                obj.menu()
        elif choice == '2':
            break
        else:
            print('输入错误')

