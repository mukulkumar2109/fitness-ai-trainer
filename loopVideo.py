import cv2
import numpy as np 
import time
import pose_module as pm


x = input("Enter the exercise: ")
x=x.lower()
y = input("Enter the body part: ")
y=y.lower()

detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0
kTime=time.time()

while True:
    isclosed=0
    cap = cv2.VideoCapture(1)
    while True:
        result, img = cap.read()
        img = cv2.resize(img, (1200,720))
        if result==True:
            img = detector.findPose(img, False)
            lmList = detector.findPosition(img, False)
            if len(lmList)!=0 :

                match(x):
                    case "bicep curls":
                        match(y):
                            case "right arm":
                                angle = detector.findAngle(img,12,14,16)
                            case "left arm":
                                angle = detector.findAngle(img,11,13,15)
                        if(angle>180):
                            per = np.interp(angle, (210,310),(0,100))
                            bar = np.interp(angle, (210,310), (650,100))
                        else:
                            per = np.interp(angle, (60,165),(100,0))
                            bar = np.interp(angle, (60,165), (100,650))

                    case "squats":
                        match(y):
                            case "right leg":
                                angle = detector.findAngle(img, 24,26,28)
                            case "left leg":
                                angle = detector.findAngle(img, 23,25,27)
                        if(angle>180):
                            per = np.interp(angle, (195,290),(0,100))
                            bar = np.interp(angle, (195,290), (650,100))
                        else:
                            per = np.interp(angle, (60,160),(100,0))
                            bar = np.interp(angle, (60,160), (100,650))

                    case "pushups":
                        match(y):
                            case "right arm":
                                angle = detector.findAngle(img,12,14,16)
                            case "left arm":
                                angle = detector.findAngle(img,11,13,15)
                        if(angle>180):
                            per = np.interp(angle, (195,285),(0,100))
                            bar = np.interp(angle, (195,285), (650,100))
                        else:
                            per = np.interp(angle, (65,155),(0,100))
                            bar = np.interp(angle, (65,155), (650,100))

                    case "bench press":
                        match(y):
                            case "right arm":
                                angle = detector.findAngle(img,12,14,16)
                            case "left arm":
                                angle = detector.findAngle(img,11,13,15)
                        if(angle>160):
                            per = np.interp(angle, (185,330),(0,100))
                            bar = np.interp(angle, (185,330), (650,100))
                        else:
                            per = np.interp(angle, (50,150),(0,100))
                            bar = np.interp(angle, (50,150), (650,100))


                # print(angle,per)

                # check for curls
                color = (0,0,255)
                if per == 100:
                    color = (0,255,0)
                    if dir == 0:
                        count += 0.5
                        dir = 1
                if per == 0:
                    
                    if dir == 1:
                        count +=0.5
                        dir = 0

                cv2.rectangle(img,(1100,100),(1175,650),(255,255,255),5)
                cv2.rectangle(img,(1100,int(bar)),(1175,650),color,cv2.FILLED)
                cv2.putText(img, f'{int(per)}%', (1080,75), cv2.FONT_HERSHEY_PLAIN, 4, (255,0,0), 4)

                cv2.rectangle(img,(0,500),(200,720),(0,255,0),cv2.FILLED)
                cv2.putText(img, str(int(count)), (45,670), cv2.FONT_HERSHEY_PLAIN, 10, (0,0,255), 15)

                
                cTime = time.time()

                #Timer
                cv2.putText(img,f'Time: {int(cTime-kTime)}s', (60,140), cv2.FONT_HERSHEY_DUPLEX, 1, (255,255,255), 2)

                fps = 1/(cTime-pTime)
                pTime=cTime
                cv2.putText(img, "fps: "+ str(int(fps)), (55,90), cv2.FONT_HERSHEY_PLAIN, 3, (250,0,0), 2)

            cv2.imshow("Image",img)
            # cv2.waitKey(1)
            if (cv2.waitKey(1)==27):
                isclosed=1
                break
        else:
            break
    # To break the loop if it is closed manually
    if isclosed:
        break



cap.release()
cv2.destroyAllWindows()
