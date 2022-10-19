from RPA.Desktop import Desktop
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
driver = Desktop()
driver.open_application(
    r'C:\Program Files\Google\Chrome\Application\chrome.exe')

driver.click('image:./instagram.png')

input()
driver.close_all_applications()
