import cv2 ,imutils
import pytesseract

def read_txt(image,txt_type):
  text='non'
  if txt_type == 'num':
    text = pytesseract.image_to_string(image, lang='ara_number').replace(' ','')

  elif txt_type == 'char':
    text = pytesseract.image_to_string(image,lang='ara')

  elif txt_type == 'combined':
    text = pytesseract.image_to_string(image,lang='ara_combined')

  return text.replace('\n','').replace('\x0c','').replace('\u200e','').replace('\u200f','')

def scan(img, face,data):
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  if face == 'f':
    pic      = img[50:350,50:275]
    Name1    = img[150:225, 700:1000]
    Name2    = img[215:300, 400:1000]
    address1 = img[290:360, 400:1000]
    address2 = img[360:440, 400:1000]
    ID       = img[490:560,400:1000]

    cv2.imwrite('Result/pic.png',pic)
    cv2.imwrite('Result/Name1.png',Name1)
    cv2.imwrite('Result/Name2.png',Name2)
    cv2.imwrite('Result/address1.png',address1)
    cv2.imwrite('Result/address2.png',address2)
    cv2.imwrite('Result/ID.png',ID)

    data['Name'] = read_txt(Name1,'char') + " " + read_txt(Name2,'char')
    data['Address'] = read_txt(address1,'combined') + " " + read_txt(address2,'combined')
    data['ID '] = read_txt(ID,'num')

  if face == 'b':
    ID2      = img[30:80,430:820]
    job1     = img[70:140,230:820]
    job2     = img[125:185,230:820]
    gender   = img[175:260,700:820]
    religion = img[180:260,480:740]
    status   = img[180:260,220:570]
        
    cv2.imwrite('Result/ID2.png',ID2)
    cv2.imwrite('Result/job1.png',job1)
    cv2.imwrite('Result/job2.png',job2)
    cv2.imwrite('Result/gender.png',gender)
    cv2.imwrite('Result/religion.png',religion)
    cv2.imwrite('Result/status.png',status)

    data['ID2'] = read_txt(ID2,'num')
    data['job'] = read_txt(job1,'char') + " " + read_txt(job2,'char')
    data['gender'] = read_txt(gender,'char') 
    data['religion'] = read_txt(religion,'char') 
    data['status'] = read_txt(status,'char') 

  return data