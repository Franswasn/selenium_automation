import time
from selenium import webdriver
from bs4 import BeautifulSoup


def main():
    link_list = []
    j = 10
    driver = webdriver.Chrome()
    url = 'https://unsplash.com/wallpapers/desktop/laptop'
    driver.get(url)
    time.sleep(2)
    driver.maximize_window()
    time.sleep(2)
    for i in range(60):
        strn = 'window.scrollBy(0,{})'.format(j)
        driver.execute_script(strn, "")
        time.sleep(2)
        i += 1
        j += 75
    soup = BeautifulSoup(driver.page_source, 'lxml')
    links = soup.find_all('a', class_='_2Mc8_')

    for link in links:
        newlink = str(link)
        link_start = newlink.find('photos/')
        link_end = newlink.find('" itemprop')
        linkonly = ('https://unsplash.com/{}/download?force=true'.format(newlink[link_start:link_end]))
        if linkonly not in link_list:
            link_list.append(linkonly)
    print("Number of links scrapped: ",len(link_list))
    return link_list


def get_pics(link_list):
    driver = webdriver.Chrome()
    driver.set_window_position(-2000, 0)
    num = len(link_list)
    for urls in link_list:
        print("Remaining: ",num)
        driver.get(urls)
        num = num - 1
        time.sleep(5)
    print("\nDownload completed successfully.............")


if __name__ == '__main__':
    get_pics(main())
