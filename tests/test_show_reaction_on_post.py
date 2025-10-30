import time

from base.base_test import BaseTest


class TestShowReactionOnPost(BaseTest):

    def test_show_reaction_on_post(self):
        self.login_page().open()
        self.login_page().login_as_user(username=self.data.LOGIN,
                                      password=self.data.PASSWORD)
        self.home_page().wait_load_page()
        self.home_page().post_block.find_published_posts()
        self.home_page().post_block.show_reaction_on_post()
        self.home_page().post_block.scroll_to_emoji_panel()
        emoji_panel = self.home_page().post_block.emoji_panel()
        assert emoji_panel.is_displayed()