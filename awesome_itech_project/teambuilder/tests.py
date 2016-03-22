from django.test import TestCase
from teambuilder.models import Team, Course
from django.contrib.auth.models import User

class TeamAttributesTest(TestCase):

    def test_ensure_team_size_is_greater_than_zero(self):

        user = User(username='jeff')
        user.set_password('jeff')
        user.save()

        course = Course(name='big data', creator=user, team_size=4, code='COMP01234', course_password='BIGDATA')
        course.save()
        team = Team(name='awesome',course=course,creator=user,required_skills='java', description='team for big data')
        team.save()

        self.assertEqual((team.current_size == 1), True)

    def test_ensure_team_size_entered_for_course_is_greater_than_one(self):

        user = User(username='jeff')
        user.set_password('jeff')
        user.save()

        course = Course(name='big data', creator=user, team_size=1, code='COMP01234', course_password='BIGDATA')
        course.save()

        self.assertEqual((course.team_size > 1), False)

