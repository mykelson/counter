import os
import pathlib
import unittest

from selenium import webdriver

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome('C:\\Users\\mykeltuz\\Downloads\\Programs\\chromedriver') # change this path to run this test on your device.

class WebpageTests(unittest.TestCase):

    def test_title(self):
        driver.get(file_uri("counter.html"))
        self.assertEqual(driver.title, "Counter")

    def test_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element_by_tag_name("button")
        increase.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "1")

    def test_multiple_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element_by_tag_name("button")
        for i in range(3):
            increase.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "4")

if __name__ == "__main__":
    unittest.main()