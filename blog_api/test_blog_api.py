from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from blog.models import Post, Category
from django.contrib.auth.models import User


class PostTestsAnyClassNameWillWork(APITestCase):

    def test_view_posts_and_any_function_name_will_work(self):
        url = reverse('blog_api:listcreate')  # blog_api from urls.py app_name
        #print(url, "========url===========")
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        self.test_category = Category.objects.create(name='test_category')
        self.testuser1 = User.objects.create_superuser(
            username='testuser1', password='testpassword1')
        self.client.login(username=self.testuser1.username,
                          password='testpassword1')
        data = {
            "category": 1,
            "title": 'testpost',
            "excerpt": 'test',
            "content": 'test content',
            "slug": 'test-post',
            "auther": 1,
            "status": 'published'
        }
        # blog_api from urls.py app_name & listcreate from correcponding url name
        url = reverse('blog_api:listcreate')
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # blog_api from urls.py app_name & detailcreate from correcponding url name
        url = reverse('blog_api:detailcreate', kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_update(self):
        client = APIClient()
        self.test_category = Category.objects.create(name='test_category')
        self.testuser1 = User.objects.create_user(
            username='testuser1', password='testpassword1')
        self.testuser2 = User.objects.create_user(
            username='testuser2', password='testpassword2')
        testPost = Post.objects.create(category_id=1, title='testpost', excerpt='test',
                                       content='test content', slug='test-post', auther_id=1, status='published')
        self.client.login(username=self.testuser1.username,
                          password='testpassword1')
        # blog_api from urls.py app_name & detailcreate from correcponding url name
        url = reverse('blog_api:detailcreate', kwargs={'pk': 1})
        data = {
            "title": 'testpostfdfdfdf',
            "content": 'test',
            "auther": 1,
        }
        response = self.client.put(url, data=data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
