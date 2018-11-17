#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
from datetime import datetime as dt


class Person:
    """
    >>> p = Person('Ivan', 'Ivanov', 'male', date(1989, 4, 26))
    >>> print(p)
    Ivan Ivanov, male, 29 years

    >>> p.full_ages()
    29
    >>> Person('Ivan', 'Ivanov', 'man', "1989.4.26")
    Traceback (most recent call last):
        ...
    ValueError: bday must be date type
    """

    def __init__(self, name, surname, sex, bday):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.bday = bday
        if not isinstance(bday, date):
            raise ValueError('bday must be date type')

    def __repr__(self):
        return f'Person({self.name} {self.surname}, ' + \
            f'{self.sex}, {self.full_ages()} years)'

    def set_bday(self, bday):
        self.bday

    def full_ages(self):
        now = dt.now()
        age = now.year - self.bday.year - 1
        if now.month > self.bday.month:
            age += 1
        elif now.month == self.bday.month and now.day >= self.bday.day:
            age += 1
        return age

    def __str__(self):
        return f'{self.name} {self.surname}, {self.sex}, ' + \
            f'{self.full_ages()} years'


class Student(Person):
    """
    >>> s = Student('Ivan', 'Ivanov', 'male', date(1989, 4, 26), 161, 9)
    >>> print(s)
    Ivan Ivanov, male, 29 years, 161 group, 9 skill
    """
    def __init__(self, name, surname, sex, bday, group, skill):
        Person.__init__(self, name, surname, sex, bday)
        self.group = group
        self.skill = skill

    def __str__(self):
        return f'{self.name} {self.surname}, {self.sex}, ' + \
            f'{self.full_ages()} years, {self.group} group, {self.skill} skill'

    def __repr__(self):
        return f'Student({self.name} {self.surname}, {self.sex},' + \
            'f{self.full_ages()} years, {self.group} group, ' + \
            'f{self.skill} skill)'


class Group():
    """
    Encapsulates list of students
    """

    def __init__(self, students_list):
        self.students_list = students_list

    def __str__(self):
        ans = [f"Student({s})" for s in self.students_list]
        ans = f"Group({ans})"
        return ans

    def __len__(self):
        return len(self.students_list)

    def __eq__(self, other):
        if not isinstance(other, Group):
            other = Group(other)
        self.students_list = \
            sorted(self.students_list, key=lambda x: (x.full_ages(), x.skill))
        other.students_list = \
            sorted(other.students_list, key=lambda x: (x.full_ages(), x.skill))
        if str(self) == str(other):
            return True
        else:
            return False

    def sort_by_age(self, reverse=False):
        self.students_list = \
            sorted(self.students_list,
                   key=lambda x: x.full_ages(), reverse=reverse)
        return self.students_list

    def sort_by_skill(self, reverse=False):
        self.students_list = sorted(self.students_list,
                                    key=lambda x: x.skill, reverse=reverse)
        return self.students_list

    def sort_by_age_and_skill(self, reverse=False):
        self.students_list = \
            sorted(self.students_list,
                   key=lambda x: (x.full_ages(), x.skill), reverse=reverse)
        return self.students_list


if __name__ == '__main__':
    import doctest
    doctest.testmod()
