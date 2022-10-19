from RPA.Browser.Selenium import Selenium
import pathlib
from RPA.Excel.Files import Files

CURRENT_PATH = pathlib.Path(__file__).parent.resolve()
PONumber = []
data_find = []
username = 'admin@procurementanywhere.com'
password = 'paypacksh!p'

file = Files()
driver = Selenium()
driver.set_download_directory(CURRENT_PATH)

driver.open_chrome_browser(
    'https://developer.automationanywhere.com/challenges/automationanywherelabs-supplychainmanagement.html')
# driver.click_element('//a[@type="button"]')

for i in range(1, 8):
    PONumber.append(driver.get_value('id:PONumber'+str(i)))
driver.click_link('//a[text()="Procurement Anywhere"]')


driver.switch_window('Automation Anywhere - PO Tracking Login')
driver.wait_until_element_is_visible(
    '//button[text()="Accept All Cookies"]', 10)
driver.click_element('//button[text()="Accept All Cookies"]')
driver.input_text('id:inputEmail', username, True)
driver.input_text('id:inputPassword', password, True)
driver.click_button('//button[@type="button"]')

for po_number in PONumber:
    item = []
    driver.input_text('//input[@type="search"]', po_number, True)
    item.append(driver.get_text('(//td)[7]'))
    item.append(driver.get_text('(//td)[8]'))
    item.append(driver.get_text('(//td)[5]'))
    data_find.append(item)


driver.switch_window('Automation Anywhere Labs - Supply Chain Management')

excel = file.open_workbook('./StateAssignments.xlsx')
ex_data_find = excel.read_worksheet()

for i in range(1, 8):
    index = i-1
    driver.input_text('id:shipDate'+str(i), data_find[index][0])
    driver.input_text('id:orderTotal'+str(i), data_find[index][1].strip('$'))
    for row in ex_data_find:
        if data_find[index][2] == row['A']:
            driver.select_from_list_by_value('agent'+str(i), row['B'])

driver.click_button('id:submitbutton')

input()
driver.close_all_browsers()
