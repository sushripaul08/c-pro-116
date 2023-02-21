import cv2

image= cv2.imshow("assests/solar-system.jpg")



cv2.putText(image,"Sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(image,"Mercury",(30,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(image,"Venus",(40,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(image,"Earth",(50,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(image,"Jupiter",(60,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(image,"Saturn",(70,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(image,"Euranus",(80,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(image,"Neptune",(90,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.imwrite("Solar_systemwithname.jpg",image)

cv2.imshow("output",image)


cv2.waitKey(0)