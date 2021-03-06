# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from group import Group
import unittest


class test_group_creation(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_group_creation(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.create_group(Group(group_name="name", group_header="header", group_footer="footer"))
        self.return_to_groups_page()
        self.logout()

    def test_empty_group_creation(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_groups_page()
        self.create_group(Group(group_name="", group_header="", group_footer=""))
        self.logout()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_xpath("//input[@name='new'][1]").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.group_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.group_header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.group_footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
        wd = self.wd
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://addressbook/group.php")

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
