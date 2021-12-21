# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from hashlib import new
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import date
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

#now full information
today = date.today()
daynow = today.strftime("%m/%d/%Y")
nama = "Rio Ricardo Siahaan"
nomor_karyawan= "10804"
gid = "Z0033N5Z"
division = "Smart Infrastructure"
businnes_unit = "SI DG"
lokasi = "Project Site"
suhu = str(round(random.uniform(35.5, 36.7), 1))
kondisi = "Sehat"
keluarga_covid = "Tidak"
keluar_rumah = "Tidak"
transport_umum = "Tidak"
kegiatan_umum = "Tidak"
kontak_covid = "Tidak"
gejala_klinis= "Tidak"
keluarga_gejala_klinis = "Tidak"
trip_negara_lain = "Tidak"
balik_perjalanan_bisnis = "Tidak"
sudah_melakukan_pcr = "Tidak"
sudah_vaksin = "Ya"
vaksin_ke_berapa = "Kedua"


questions={
    "QuestionId_r458f1ecadc1d46558815c0a26aa4d344 QuestionInfo_r458f1ecadc1d46558815c0a26aa4d344": daynow ,
    "QuestionId_r4ee7aba5fe9d4024833dfb154f6b05fb QuestionInfo_r4ee7aba5fe9d4024833dfb154f6b05fb": nama,
    "QuestionId_r4f5c512d8c6f4943b825a8d2fdc1cb1a QuestionInfo_r4f5c512d8c6f4943b825a8d2fdc1cb1a": nomor_karyawan,
    "QuestionId_ra4792b1130644f27b5f4b4e3fc2469a6 QuestionInfo_ra4792b1130644f27b5f4b4e3fc2469a6": gid ,
    "QuestionId_r8c6fdc39c34c498dadcb62eed78c373a QuestionInfo_r8c6fdc39c34c498dadcb62eed78c373a": division ,
    "QuestionId_r53a1e82a669f42b4a0fc9fbc2e54d5f5 QuestionInfo_r53a1e82a669f42b4a0fc9fbc2e54d5f5": businnes_unit,
    "QuestionId_r654457beb7cb43998f0868eddc6f9e03 QuestionInfo_r654457beb7cb43998f0868eddc6f9e03": lokasi ,
    "QuestionId_r9fccf1bdde2b40a386ffdca1fc0a4ef8 QuestionInfo_r9fccf1bdde2b40a386ffdca1fc0a4ef8": suhu ,
    "QuestionId_r4b41d58e0cd94e16a32f38fb878c5311 QuestionInfo_r4b41d58e0cd94e16a32f38fb878c5311": kondisi ,
    "QuestionId_r2eade824c9024391b1faf32e72954eb6 QuestionInfo_r2eade824c9024391b1faf32e72954eb6": keluarga_covid ,
    "QuestionId_re9223f4939a944b98662fcd8ed5a4cfc QuestionInfo_re9223f4939a944b98662fcd8ed5a4cfc": keluar_rumah ,
    "QuestionId_rd223cb6efdec4c498dce507fffe97fc3 QuestionInfo_rd223cb6efdec4c498dce507fffe97fc3": transport_umum ,
    "QuestionId_rf0933419ed984f73b3b22aad6d650365 QuestionInfo_rf0933419ed984f73b3b22aad6d650365": kegiatan_umum ,
    "QuestionId_r526a7a43276d467e9e4ed5881b7c84e8 QuestionInfo_r526a7a43276d467e9e4ed5881b7c84e8": kontak_covid ,
    "QuestionId_r7fc5f1dc14904c68b59aedc7dafe8ba8 QuestionInfo_r7fc5f1dc14904c68b59aedc7dafe8ba8": gejala_klinis ,
    "QuestionId_rddbbfba0700447a4be8a1c7572128e34 QuestionInfo_rddbbfba0700447a4be8a1c7572128e34": keluarga_gejala_klinis ,
    "QuestionId_r40fd0dedce2f467c81072c3c2fede001 QuestionInfo_r40fd0dedce2f467c81072c3c2fede001": trip_negara_lain ,
    "QuestionId_r64a94d24c21b413db8805e42e0dfc58d QuestionInfo_r64a94d24c21b413db8805e42e0dfc58d": balik_perjalanan_bisnis ,
    "QuestionId_r7a833e1aa9384c29905efd77b9c600a4 QuestionInfo_r7a833e1aa9384c29905efd77b9c600a4": sudah_melakukan_pcr,
    "QuestionId_r988c896b200f44a898ea880d2b1e909c QuestionInfo_r988c896b200f44a898ea880d2b1e909c": sudah_vaksin,
    "QuestionId_re57f4f5e64df4ce390ce65b0a5847809 QuestionInfo_re57f4f5e64df4ce390ce65b0a5847809": vaksin_ke_berapa
}

def asses_question(webelem):
    for q in questions.keys():
        try:
            #print(q)
            question = webelem.find_element(By.XPATH, ".//*[@aria-labelledby='" + q + "']")
            return question
        except:
            continue
        #return none if i don't find anything
        print("wrong question id")
        return None

def radioquestion(webelem, question_id):
    # find the dropdown button
    try:
        choice = webelem.find_element(By.XPATH, ".//*[contains(@aria-label,'" + questions[question_id] + "')]")
        choice.click()
    except:
        print("Invalid choice")

def dropdownquestion(webelem, question_id):
    #find the dropdown button
    try:
        dropdown_button = webelem.find_element(By.XPATH,".//i")
        dropdown_button.click()
        choice = webelem.find_element(By.XPATH,".//*[contains(@aria-label,'"+ questions[question_id] +"')]")
        choice.click()
    except:
        print("Invalid choice")

def answerquestion (webelem, question_id):
    match webelem.tag_name:
        case "input":
            webelem.send_keys(questions[question_id])
        case "div":
            #we found dropdown or radio button menu
            if(webelem.get_attribute("role") == "listbox"):
                dropdownquestion(webelem,question_id)
            elif (webelem.get_attribute("role") == "radiogroup"):
                radioquestion(webelem,question_id)
            else:
                print("unknown question")
        case _:
            print("wrong type of tags")

#not used because take too long
def readChildXPATH (ParentElem, ParentXPath):
    count = {}
    count_index = {}
    items = 0
    for i in ParentElem.find_elements(By.XPATH, ParentXPath + "/*"):
        try:
            count[i.tag_name] += 1
        except:
            count[i.tag_name] = 1
            count_index[i.tag_name] = 1
        finally:
            items += 1

    for i in ParentElem.find_elements(By.XPATH, ParentXPath + "/*"):
        #get my xpath
        #do something with me
        #if i am a listed input then send keys according to the my answers list
        if i.tag_name == "input":
            answerquestion(i, i.get_attribute("aria-labelledby"))

        if(count[i.tag_name] > 1):
            myxpath = ParentXPath + '/' + i.tag_name + '[' + str(count_index[i.tag_name]) + ']'
            count_index[i.tag_name] += 1
        else:
            myxpath = ParentXPath + '/' + i.tag_name
        #print(myxpath)
        readChildXPATH(i, myxpath)

#main program
#get services
s = Service('C:/Users/z0033n5z/Downloads/chromedriver/chromedriver.exe')
driver = webdriver.Chrome(service=s)

#open the web page
driver.get('https://forms.office.com/Pages/ResponsePage.aspx?id=zTuuOHmV1E-t2rQuFJXVWmneDwy0B39FkejzXOyEoMJUM1dBTUc5SFZPSU9OQU1XV0tTQk84UVBVRSQlQCN0PWcu')
#testing purpose
#driver.get("file:///C:/Users/z0033n5z/Desktop/tesuuu.html")

#wait until web page is loaded
tanggal  = '//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/input[1]'
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, tanggal)))

root_path= '//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]'

#testing purpose
#root_path = '/html/body/div'
root = driver.find_element(By.XPATH, root_path)

#check the first question
next_question = root.find_element(By.XPATH,".//div")
question = asses_question(next_question)
answerquestion(question, question.get_attribute("aria-labelledby"))

# now loop through siblings
while(True):
    try:
       next_question = next_question.find_element(By.XPATH, "./following-sibling::div")
       question = asses_question(next_question)
       answerquestion(question, question.get_attribute("aria-labelledby"))
    except:
       break
