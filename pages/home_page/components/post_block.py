import allure
from base.base_page import BasePage


class PostBlock(BasePage):

    _NEWSFEED_BLOCK = ".newsfeed-middle"
    _ACTIVE_USER_POST = "[id^='activity-item']"
    _REACTION_TO_POST = "[id^='ossn-like']"
    _EMOJI_PANEL = ".comments-likes .ossn-like-reactions-panel"
    _POST_BLOCK = "#ossn-wall-form"
    _POST_TEXTAREA = "//*[@id='ossn-wall-form']/fieldset/div[2]/textarea"
    _POST_PUBLISH_BTN = "//input[@type='submit']"
    _PUBLISHED_POSTS = "//*[starts-with(@id,'activity-item')]"

    @allure.step("Input text and create post")
    def create_post(self, text: str):
        self.click_mouse(self._POST_TEXTAREA)
        self.enter_text(self._POST_TEXTAREA, text)
        self.click_mouse(self._POST_PUBLISH_BTN)

    @allure.step("Find all posts on hone page")
    def find_published_posts(self):
        elements = self.find_elements(self._PUBLISHED_POSTS)
        return elements

    def newsfeed_block(self):
        return self.find_element(self._NEWSFEED_BLOCK)

    def first_active_user_post(self):
        return self.find_element(self._ACTIVE_USER_POST)

    def show_reaction_on_post(self):
        return self.hover_mouse(self._REACTION_TO_POST)

    def scroll_to_emoji_panel(self):
        return self.scroll_to(self._EMOJI_PANEL)

    def emoji_panel(self):
        return self.find_element(self._EMOJI_PANEL)
