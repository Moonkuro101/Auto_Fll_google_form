# โปรเจคนี้เกี่ยวกับการทำการเติม google form อัติโนมัติโดยการใช้ selenium สำหรับ class CSD3101
  ![image](https://github.com/user-attachments/assets/f15bc1b5-15e7-49e7-8130-2d120bbb0bee)


  
## ติดตั้ง Selenium Framework
```
  pip install selenium
```
### module ที่ใช้สำหรับ Project  
```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
```

