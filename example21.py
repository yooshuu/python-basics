import random
# myList = ["하나", "둘", "셋", "넷", "다섯", "여섯"]
#
# while(True) :
#     response = input("주사위 던지기를 계속하시겠습니까? (yes, no)")
#     if  response == "yes" :
#         coin = random.choice(myList)
#         print(coin)
#     else :
#         break


myList2 = ["앞면", "뒷면"]

while(True) :
    response = input("동전을 던지시겠습니까?")
    if response == "yes" :
        coin = random.choice(myList2)
        print(coin)
    else :
        break
#