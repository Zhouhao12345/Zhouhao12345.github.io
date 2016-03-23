from django.test import TestCase
from teambuilder.models import Team, Course
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

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

    def test_slug_line_creation(self):

        user = User(username='jeff')
        user.set_password('jeff')
        user.save()

        course = Course(name='Algorithms and Data Structures', creator=user, team_size=1, code='COMP01234', course_password='ALGO2016')
        course.save()

        self.assertEqual(course.slug, 'algorithms-and-data-structures')

class IndexViewTests(TestCase):

    def test_index_with_no_teams(self):

        response = self.client.get(reverse('teambuilder:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No teams have been built')
        self.assertContains(response, 'No courses have been added')
        self.assertQuerysetEqual(response.context['teams'], [])


    def test_index_view_with_team(self):

        user = User(username='jeff')
        user.set_password('jeff')
        user.save()

        course = Course(name='big data', creator=user, team_size=4, code='COMP01234', course_password='BIGDATA')
        course.save()
        team = Team(name='awesome', course=course, creator=user, required_skills='java', description='team for big data')
        team.save()

        response = self.client.get(reverse('teambuilder:index'))
        self.assertContains(response, 'awesome')
        self.assertEqual(len(response.context['teams']), 1)
