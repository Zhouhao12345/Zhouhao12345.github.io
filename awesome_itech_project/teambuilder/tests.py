from django.test import TestCase
from teambuilder.models import Team, Course
from django.contrib.auth.models import User

class TeamAttributesTest(TestCase):

    def Test_ensure_team_size_is_greater_than_zero(self):

        user = User(username='jeff')
        user.set_password('jeff')
        user.save();

        course = Course(name='big data', creator=user, team_size=4, code='COMP01234', course_password='BIGDATA')
        course.save()
        team = Team(name='awesome',course=course,creator=user,required_skills='java',description='team for big data')
        team.save()
        team2 = Team(name='awesome2',course=course,creator=user,required_skills='java',description='team for big data')
        team2.save()
        self.assertEqual((team.current_size == 1),True)

    def Test_ensure_team_name_are_positive(self):

        user = User(username='jeff')
        user.set_password('jeff')
        user.save();

        course = Course(name='big data', creator=user, team_size=4, code='COMP01234', course_password='BIGDATA')
        course.save()
        team = Team(name='awesome',course=course,creator=user,required_skills='java',description='team for big data')
        team.save()
        team2 = Team(name='awesome2',course=course,creator=user,required_skills='java',description='team for big data')
        team2.save()
        self.assertEqual((team.name >= 0),True)
