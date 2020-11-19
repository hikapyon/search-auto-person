from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/Users/okafujihikaru/Documents/python/driver/chromedriver")
person = input("検索したい人を入力")

def run(p,i,n):#人を検索。pはサイトのURL,iはタブの順番、nはsearch_boxの要素名
    if i != 0:#1番目のタブ以降新しいタブを開く
        driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[i])
    driver.get(p)
    search_box = driver.find_element_by_name(n)
    search_words = person
    search_box.send_keys("".join(search_words))
    search_box.send_keys(Keys.RETURN)


 

run("https://www.google.co.jp",0,"q")
run("https://www.google.co.jp/imghp?hl=ja",1,"q")
run("https://www.wikipedia.org/",2,"search")
run("https://www.youtube.com/?gl=JP&hl=ja",3,"search_query")