#%%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

driver.get('https://b2b.10086.cn/b2b/main/listVendorNotice.html?noticeType=2#this')
ele = driver.find_elements_by_xpath("// td[@style]")
for ii in ele:
    print(ii.text.split('\n'))
# %%

nextbtn = driver.find_element_by_xpath("//tr/td[4]/a")
nextbtn.click()
ele = driver.find_elements_by_xpath("// td[@style]")
for ii in ele:
    print(ii.text.split('\n'))

# %%
