from base.base_test import BaseTest


class TestPost(BaseTest):

    def test_publish_post(self):
        post_text = "Случайный текст"
        self.login_page.open()
        self.login_page.input_username("administrator")
        self.login_page.input_password("administrator")
        self.login_page.click_login_button()
        self.home_page.wait_load_page()
        self.home_page.create_post(post_text)
        posts = self.home_page.find_published_posts()
        posts_with_text = [post for post in posts
                           if post_text in post.text]
        assert posts_with_text, f"Any posts with text {post_text} are not published"