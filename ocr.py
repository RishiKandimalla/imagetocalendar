import easyocr

reader = easyocr.Reader(['en'])
result=reader.readtext('images/spring2025.png')
for (bbox, text, prob) in result:
    print(text, bbox)

