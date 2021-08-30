from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category


class Test_Create_Post(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='test_category')
        testuser1 = User.objects.create_user(
            username='testuser1', password='testpassword1')
        testPost = Post.objects.create(category_id=1, title='testpost', excerpt='test',
                                       content='test content', slug='test-post', auther_id=1, status='published')

    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        auther = f'{post.auther}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'

        self.assertEqual(auther, 'testuser1')
        self.assertEqual(excerpt, 'test')
        self.assertEqual(title, 'testpost')
        self.assertEqual(content, 'test content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), 'testpost')
        self.assertEqual(str(cat), 'test_category')
