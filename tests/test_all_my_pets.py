import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_my_pets_count(my_pets):
   """Проверяется, что в таблице есть все питомцы пользователя"""

   element = WebDriverWait(pytest.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                            '//div[@class=".col-sm-4 left"]')))
   # Статистика
   user_statistics_str = pytest.driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text
   user_statistics_list = user_statistics_str.split('\n')
   my_pets_count_statistics = None

   for i in user_statistics_list:
      if 'Питомцев' in i:
         my_pets_count_statistics = int(i.split(': ')[1])

   element = WebDriverWait(pytest.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//tbody/tr')))
   # Данные питомцев в таблице
   my_pets = pytest.driver.find_elements(By.XPATH, '//tbody/tr')
   my_pets_count_table = len(my_pets)
   assert my_pets_count_statistics == my_pets_count_table


def test_images_my_pets(my_pets):
   """Проверяется, что хотя бы у половины питомцев есть фото"""

   element = WebDriverWait(pytest.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//tbody/tr')))
   # Данные питомцев в таблице
   my_pets = pytest.driver.find_elements(By.XPATH, '//tbody/tr')
   my_pets_count_table = len(my_pets)

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//tbody/tr/th/img')))
   # Данные питомцев в таблице
   images_my_pets = pytest.driver.find_elements(By.XPATH, '//tbody/tr/th/img')
   images_my_pets_count = 0

   for i in range(my_pets_count_table):
      if images_my_pets[i].get_attribute('src') != '':
         images_my_pets_count += 1

   assert images_my_pets_count >= my_pets_count_table / 2


def test_names_species_ages_my_pets(my_pets):
   """Проверяется, что у всех питомцев есть имя, возраст и порода"""

   WebDriverWait(pytest.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//tbody/tr')))
   # Данные питомцев в таблице
   my_pets = pytest.driver.find_elements(By.XPATH, '//tbody/tr')
   my_pets_count_table = len(my_pets)

   element = WebDriverWait(pytest.driver, 10).until(
      EC.visibility_of_all_elements_located((By.XPATH, '//tbody/tr/td[1]')))
   element = WebDriverWait(pytest.driver, 10).until(
      EC.visibility_of_all_elements_located((By.XPATH, '//tbody/tr/td[2]')))
   element = WebDriverWait(pytest.driver, 10).until(
      EC.visibility_of_all_elements_located((By.XPATH, '//tbody/tr/td[3]')))
   # Имена, порода и возраст питомцев
   names_my_pets = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[1]')
   species_my_pets = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[2]')
   ages_my_pets = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[3]')

   for i in range(my_pets_count_table):
      assert names_my_pets[i].text != ''
      assert species_my_pets[i].text != ''
      assert ages_my_pets[i].text != ''


def test_pets_difference_my_pets(my_pets):
   """Проверяется, что в списке нет повторяющихся питомцев"""

   element = WebDriverWait(pytest.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//tbody/tr')))
   # Данные питомцев в таблице
   my_pets = pytest.driver.find_elements(By.XPATH, '//tbody/tr')
   my_pets_count_table = len(my_pets)
   my_pets_list = [my_pets[i].text for i in range(my_pets_count_table)]
   my_pets_set = set(my_pets_list)
   assert len(my_pets_list) == len(my_pets_set)


def test_names_difference_my_pets(my_pets):
   """Проверяется, что у всех питомцев разные имена"""

   element = WebDriverWait(pytest.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//tbody/tr')))
   # Данные питомцев в таблице
   my_pets = pytest.driver.find_elements(By.XPATH, '//tbody/tr')
   my_pets_count_table = len(my_pets)

   element = WebDriverWait(pytest.driver, 10).until(
      EC.visibility_of_all_elements_located((By.XPATH, '//tbody/tr/td[1]')))
   # Имена питомцев
   names_my_pets = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[1]')
   names_my_pets_list = [names_my_pets[i].text for i in range(my_pets_count_table)]
   names_my_pets_set = set(names_my_pets_list)
   assert len(names_my_pets_list) == len(names_my_pets_set)
