import unittest

from project.student import Student


class StudentTests(unittest.TestCase):
    """
    This class tests the Student class.
    """

    def setUp(self) -> None:
        self.student = Student(name='John')

    def test_constructor_initializes_name_and_empty_courses_when_no_courses_given(self):
        self.assertEqual(self.student.name, 'John')
        self.assertEqual(self.student.courses, {})

    def test_constructor_initializes_name_and_courses_when_given(self):
        courses = {'Math': ['note1']}
        student = Student(name='Alice', courses=courses)
        self.assertEqual(student.name, 'Alice')
        self.assertEqual(student.courses, courses)

    def test_enroll_existing_course_adds_notes_and_returns_message(self):
        self.student.courses = {'Math': ['note1']}
        result = self.student.enroll('Math', ['note2'])
        self.assertEqual(result, 'Course already added. Notes have been updated.')
        self.assertEqual(self.student.courses['Math'], ['note1', 'note2'])

    def test_enroll_new_course_with_Y_adds_course_with_notes(self):
        result = self.student.enroll('Physics', ['note1'], add_course_notes='Y')
        self.assertEqual(result, 'Course and course notes have been added.')
        self.assertIn('Physics', self.student.courses)
        self.assertEqual(self.student.courses['Physics'], ['note1'])

    def test_enroll_new_course_with_empty_string_adds_course_with_notes(self):
        result = self.student.enroll('Chemistry', ['note1'])
        self.assertEqual(result, 'Course and course notes have been added.')
        self.assertIn('Chemistry', self.student.courses)
        self.assertEqual(self.student.courses['Chemistry'], ['note1'])

    def test_enroll_new_course_with_N_adds_course_without_notes(self):
        result = self.student.enroll('Biology', ['note1'], add_course_notes='N')
        self.assertEqual(result, 'Course has been added.')
        self.assertIn('Biology', self.student.courses)
        self.assertEqual(self.student.courses['Biology'], [])

    def test_add_notes_to_existing_course_updates_notes(self):
        self.student.courses = {'Math': ['note1']}
        result = self.student.add_notes('Math', 'note2')
        self.assertEqual(result, 'Notes have been updated')
        self.assertEqual(self.student.courses['Math'], ['note1', 'note2'])

    def test_add_notes_to_non_existing_course_raises_exception(self):
        with self.assertRaises(Exception) as context:
            self.student.add_notes('Physics', 'note1')
        self.assertEqual(str(context.exception), 'Cannot add notes. Course not found.')

    def test_leave_existing_course_removes_course_and_returns_message(self):
        self.student.courses = {'Math': ['note1']}
        result = self.student.leave_course('Math')
        self.assertEqual(result, 'Course has been removed')
        self.assertNotIn('Math', self.student.courses)

    def test_leave_non_existing_course_raises_exception(self):
        with self.assertRaises(Exception) as context:
            self.student.leave_course('History')
        self.assertEqual(str(context.exception), 'Cannot remove course. Course not found.')


if __name__ == '__main__':
    unittest.main()
