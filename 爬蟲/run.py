from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# 提供你的 ChromeDriver 可執行檔案路徑
driver_path = "C:\chromedriver\chromedriver.exe"

# 創建 ChromeDriver 的 Service
chrome_service = ChromeService(executable_path=driver_path)

# 使用 ChromeService 初始化 WebDriver
driver = webdriver.Chrome(service=chrome_service)

# 以下是你的原始程式碼
title = []
updt = []
view = []



driver.get("https://www.tc.edu.tw/page/78f8e2b3-e309-4bb1-b8e1-4fd7a9d0af83")
for i in range(1,9+1):
    updt.append(driver.find_element(By.XPATH, f'//*[@id="main"]/section/div/div/div[2]/div[1]/div[2]/div[{i}]/div[4]/span').text)

    title.append(driver.find_element(By.XPATH, f'/html/body/main/section/div/div/div[2]/div[1]/div[2]/div[{i}]/div[3]/span/a/span[2]').text)
    view.append(driver.find_element(By.XPATH, f'//*[@id="main"]/section/div/div/div[2]/div[1]/div[2]/div[{i}]/div[5]/span').text)


print(title)
print(updt)
print(view)

import csv

# 開啟輸出的 CSV 檔案
with open('output.csv', 'w', newline='') as csvfile:
  # 建立 CSV 檔寫入器
  writer = csv.writer(csvfile)


  writer.writerow(['標題', '更新日期', '點閱數'])
  for i in range(9):
     writer.writerow([title[i], updt[i], view[i]])
 