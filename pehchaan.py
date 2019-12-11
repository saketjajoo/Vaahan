import cv2
import mechanize
from bs4 import BeautifulSoup as BS
from captcha import get_text_from_captcha
import os

def get_det(vno):
    url = "https://vahan.nic.in/nrservices/faces/user/searchstatus.xhtml"
    url_for_captcha = "https://vahan.nic.in/nrservices/cap_img.jsp"

    titles = ["Registering Authority :", "Registration Number :", "Registration Date :",
              "Chassis Number :", "Engine Number :", "Owner Name :", "Vehicle Class :",
              "Fuel Type :", "Vehicle Make / Model :", "Registration Upto :", "MV Tax Upto :",
              "Insurance Details :", "PUC Number :", "Emission Norms :", "RC Status :"]

    results = []
    main_list = []
    res_list = []

    br = mechanize.Browser()
    br.set_handle_robots(False)

    html = br.open(url)
    soup = BS(html, features="html5lib")
    image_tags = soup.findAll('img')
    for image in image_tags:
        filename = image['src'].lstrip('http://')
        data = br.open(url_for_captcha).read()
        br.back()
        save = open("captcha_img.jpg", 'wb')
        save.write(data)
        save.close()

    caps = get_text_from_captcha("captcha_img.jpg")
    caps.replace("O", "0")
    text_captcha = str(caps)
    #print(text_captcha)

    br.select_form(name="masterLayout")
    br["regn_no1_exact"] = vno
    br["txt_ALPHA_NUMERIC"] = text_captcha
    res = br.submit()
    content = res.read()
    soup = BS(str(content), features="html5lib")
    prettyHTML = soup.prettify()
    main_list = []
    result = soup.find("div", {"id": "rcDetailsPanel"})
    if result == None:
        #print(text_captcha)
        return titles, list()
    result = result.prettify()

    table = soup.find("table")
    for row in table.findAll("tr"):
        cells = row.findAll("td")
        main_list.append(str(cells))



    y = str(main_list[0]).split("1. Registering Authority: ")
    z = str(y[1]).split("\\n")
    z[0].strip()
    temp = z[0].split(",")
    temp[0].strip()
    temp[1].strip()

    reg_auth = (temp[0][:len(temp[0])]).strip() + ", " + (temp[1][1:len(temp[1])]).strip()
    results.append(reg_auth)

    indices = [1, 2, 4, 6, 9]
    for i in range(1, len(main_list) - 1):
        main_list[i] = main_list[i].split(",")
        if i in indices:
            res_list.append(main_list[i][1])
            res_list.append(main_list[i][3])
        else:
            res_list.append(main_list[i][1])

    results.append(res_list[0][11:21])

    indices = [4, 7, 10, 11]
    for i in range(1, len(res_list)):
        res_list[i] = str(res_list[i][5:])
        res_list[i] = res_list[i].replace("<td>", "")
        res_list[i] = res_list[i].replace("</td>", "")
        res_list[i] = res_list[i].replace("\\n", "")
        res_list[i] = res_list[i].replace("]", "")
        res_list[i] = res_list[i].replace(">", "")
        res_list[i] = res_list[i].replace("\"", "")
        res_list[i] = res_list[i].replace("colspan=", "")
        res_list[i] = res_list[i].replace("style=", "")
        res_list[i] = res_list[i].replace("color: ", "")
        res_list[i] = res_list[i].replace("blue", "")
        res_list[i] = res_list[i].replace("red", "")
        if i in indices:
            res_list[i] = str(res_list[i][1:].strip())
        results.append(res_list[i])

    ind = results[11].find('valid upto')
    if ind != -1:
        ind -= 1
    temp = results[11].split("            ")
    results[11] = str(temp[0]) + ", " + str(temp[-1]).lstrip()

    os.remove('captcha_img.jpg')

    #print("\n")
    #print("--------------------------------------------")
    #for i in range(len(titles)):
        #print(titles[i], end=" ")
        #print(results[i])
    #print("--------------------------------------------")
    return titles, results