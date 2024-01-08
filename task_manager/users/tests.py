from django.test import TestCase
from django.test import Client
from django.urls import reverse
from task_manager.users.models import User


class UsersTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin = User.objects.create(**{
            'username': 'admin',
            'first_name': 'admin',
            'last_name': 'admin',
            'password': 'admin'
        })

        self.admin.save()
        # print(get_user_model().objects.all().count())

    def login(self):
        self.client.force_login(self.admin)
        res = self.client.get(reverse('users:list'))
        self.assertContains(res, 'Задачи')

    def user_test(self):
        return User.objects.get(username='admin')

    def test_user_create(self):
        res = self.client.get(reverse('users:create'))
        self.assertEqual(200, res.status_code)

        reg_res = self.client.post(reverse('users:create'), {
            'username': 'test',
            'first_name': 'test',
            'last_name': 'test',
            'password1': 'test',
            'password2': 'test',
        }, follow=True)

        self.assertEqual(200, reg_res.status_code)
        self.assertContains(reg_res, 'Пользователь успешно зарегистрирован')

    def test_user_delete(self):
        res = self.client.get(
            reverse('users:delete', kwargs={'pk': self.user_test().pk}), follow=True)

        self.assertEqual(200, res.status_code)

        res_delete = self.client.post(
            reverse('users:delete', kwargs={'pk': self.user_test().pk}), follow=True)

        self.assertEqual(200, res_delete.status_code)
        # print(res_delete.content.decode('utf-8'))
        self.assertContains(res_delete, "You cannot change not yourself! Please sign in.")

    def test_user_list(self):
        self.client.logout()
        res = self.client.get(reverse('users:list'))
        # print(res.content.decode('utf-8'))
        self.assertEqual(200, res.status_code)
        self.assertContains(res, 'Регистрация')
        self.assertContains(res, 'Вход')
        self.assertNotContains(res, 'Статусы')

        self.login()

        res = self.client.get(reverse('users:list'))
        # print(res.content.decode('utf-8'))
        self.assertNotContains(res, 'Регистрация')
        self.assertNotContains(res, 'Вход')
        self.assertContains(res, 'Выход')

    def test_user_logout(self):
        self.client.logout()
        res = self.client.get(reverse('index'))
        self.assertEqual(200, res.status_code)
        # print(res.content.decode('utf-8'))
        self.assertContains(res, 'Вход')
        self.assertNotContains(res, 'Выход')
