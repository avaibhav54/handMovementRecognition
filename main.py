import cv2
import mediapipe as mp
import time
cap=cv2.VideoCapture(0)
mphands=mp.solutions.hands
hands=mphands.Hands()
mpdraw=mp.solutions.drawing_utils
fingercordinate=[(8,6),(12,10),(16,14),(20,18)]
thumbcordinate=(4,2)

while True:
   success, img= cap.read()
   imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
   results=hands.process(imgrgb)
   multilandmarks=results.multi_hand_landmarks
   #print(multilandmarks)
  # print(success)
   t = time.time()
   if multilandmarks:
       handpoints=[]
       for handLms in multilandmarks:
           mpdraw.draw_landmarks(img,handLms,mphands.HAND_CONNECTIONS)

           intialpoints = []
           for idx,lm in enumerate(handLms.landmark):
               h,w,c=img.shape
               cx,cy=int(lm.x*w),int(lm.y*h)
               handpoints.append((cx,cy))
               

       for point in handpoints:

           cv2.circle(img, point, 5, (0,0,255), cv2.FILLED)

       upcount=0
       for cordinates in fingercordinate:
           if(handpoints[cordinates[0]][1]<handpoints[cordinates[1]][1]):
               upcount+=1

       if (handpoints[thumbcordinate[0]][0] < handpoints[thumbcordinate[1]][0]):
               upcount+=1
       if(upcount<5):
            cv2.putText(img,"warning",(150,150),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),12)
            print(str(time.time()-t))
   cv2.imshow("Finger counter",img)
   cv2.waitKey(2)