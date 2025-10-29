import allure
from base.base_test import BaseTest

@allure.epic("Administrator")
@allure.feature("Login and Post")
class TestPost(BaseTest):

    @allure.story("Check login as admin and make post")
    def test_publish_post(self):
        post_text = "Случайный текст"
        self.login_page.open()
        self.login_page.login_as_user(username=self.data.LOGIN,
                                      password=self.data.PASSWORD)
        self.home_page.wait_load_page()
        self.home_page.create_post(post_text)
        posts = self.home_page.find_published_posts()
        posts_with_text = [post for post in posts
                           if post_text in post.text]
        assert posts_with_text, f"Any posts with text {post_text} are not published"

