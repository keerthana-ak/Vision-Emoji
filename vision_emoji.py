import tensorflow as tf
import numpy as np
import sys
import cv2
from keras import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D
from keras.optimizers import Adam
from keras.layers import MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator

'''train_dir = 'C:/Users/chitt/Downloads/FER/train'
val_dir = 'C:/Users/chitt/Downloads/FER/test'
train_datagen = ImageDataGenerator(rescale=1./255)
val_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(48,48),
        batch_size=64,
        color_mode="grayscale",
        class_mode='categorical')

validation_generator = val_datagen.flow_from_directory(
        val_dir,
        target_size=(48,48),
        batch_size=64,
        color_mode="grayscale",
        class_mode='categorical')

emotion_model = Sequential()

emotion_model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48,48,1)))
emotion_model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout(0.25))

emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout(0.25))

emotion_model.add(Flatten())
emotion_model.add(Dense(1024, activation='relu'))
emotion_model.add(Dropout(0.5))
emotion_model.add(Dense(7, activation='softmax'))
# 

cv2.ocl.setUseOpenCL(False)

emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}


emotion_model.compile(loss='categorical_crossentropy',optimizer=Adam(lr=0.0001, decay=1e-6),metrics=['accuracy'])
emotion_model_info = emotion_model.fit_generator(
        train_generator,
        steps_per_epoch=28709 // 64,
        epochs=50,
        validation_data=validation_generator,
        validation_steps=7178 // 64)
emotion_model.save_weights('emotion_model.h5')
'''

# start the webcam feed
from time import sleep
emotion_model = Sequential()

emotion_model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48,48,1)))
emotion_model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout(0.25))

emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout(0.25))

emotion_model.add(Flatten())
emotion_model.add(Dense(1024, activation='relu'))
emotion_model.add(Dropout(0.5))
emotion_model.add(Dense(7, activation='softmax'))
emotion_model.load_weights('emotion_model.h5')
emotion_dict = {0: "   Angry   ", 1: "Disgusted", 2: "  Fearful  ", 3: "   Happy   ", 4: "  Neutral  ", 5: "    Sad    ", 6: "Surprised"}
emoji_dist={0:r"C:\Users\91984\OneDrive\Documents\Emoji_project\Emojis\Neutral\angry.png",
            1:r"C:\Users\91984\OneDrive\Documents\Emoji_project\Emojis\Neutral\disgusted.png",
            2:r"C:\Users\91984\OneDrive\Documents\Emoji_project\Emojis\Neutral\fearful.png",
            3:r"C:\Users\91984\OneDrive\Documents\Emoji_project\Emojis\Neutral\happy.png",
            4:r"C:\Users\91984\OneDrive\Documents\Emoji_project\Emojis\Neutral\neutral.png",
            5:r"C:\Users\91984\OneDrive\Documents\Emoji_project\Emojis\Neutral\sad.png",
            6:r"C:\Users\91984\OneDrive\Documents\Emoji_project\Emojis\Neutral\surprised.png"}
emoji_distb={0:r"C:\Users\91984\OneDrive\Documents\Emoji_project\Emojis\Boy\angry.png",
             1:r"C:\Users\91984\OneDrive\Documents\Emoji_project\Emojis\Boy\disgusted.png",
             2:r"C:\Users\91984\OneDrive\Documents\Emoji_project\Emojis\Boy\fearful.png",
             3:r"C:\Users\91984\OneDrive\Documents\Emoji_project\Emojis\Boy\happy.png",
             4:r"C:\Users\91984\OneDrive\Documents\Emoji_project\Emojis\Boy\neutral.png",
             5:r"C:\Users\91984\OneDrive\Documents\Emoji_project\Emojis\Boy\sad.png",
             6:r"C:\Users\91984\OneDrive\Documents\Emoji_project\Emojis\Boy\surprised.png"}
emoji_distg={0:r"C:\Users\91984\OneDrive\Documents\Emoji_project\Emojis\Girl\angry.png",
             1:r"C:\Users\91984\OneDrive\Documents\Emoji_project\Emojis\Girl\disgusted.png",
             2:r"C:\Users\91984\OneDrive\Documents\Emoji_project\Emojis\Girl\fearful.png",
             3:r"C:\Users\91984\OneDrive\Documents\Emoji_project\Emojis\Girl\happy.png",
             4:r"C:\Users\91984\OneDrive\Documents\Emoji_project\Emojis\Girl\neutral.png",
             5:r"C:\Users\91984\OneDrive\Documents\Emoji_project\Emojis\Girl\sad.png",
             6:r"C:\Users\91984\OneDrive\Documents\Emoji_project\Emojis\Girl\surprised.png"}

print_emo={0:"\U0001F620",1:"\U0001F616",2:"\U0001F628",3:"\U0001F601",4:"\U0001F610",5:"\U0001F61E",6:"\U0001F632"}

print_emog={0:"\U0001F926",1:"\U0001F926",2:"\U0001F645",3:"\U0001F469",4:"\U0001F64D",5:"\U0001F64D",6:"\U0001F64E"}

print_emob={0:"\U0001F926",1:"\U0001F926",2:"\U0001F645",3:"\U0001F9D1",4:"\U0001F64D",5:"\U0001F64D",6:"\U0001F64E"}
cap = cv2.VideoCapture(0)
while True:
    # Find haar cascade to draw bounding box around face
    ret, frame = cap.read()
    if not ret:
        break
    bounding_box = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    num_faces = bounding_box.detectMultiScale(gray_frame,scaleFactor=1.3, minNeighbors=5)
    cv2.putText(frame, 'Girl:G  Boy:B   Neutral:N   Quit:Q',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2,cv2.LINE_AA)
    for (x, y, w, h) in num_faces:
        cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2)
        roi_gray_frame = gray_frame[y:y + h, x:x + w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)
        emotion_prediction = emotion_model.predict(cropped_img)
        maxindex = int(np.argmax(emotion_prediction))
        if cv2.waitKey(1) & 0xFF == ord('N'):
            imgemo=cv2.imread(emoji_dist[maxindex])
            cv2.imshow('',imgemo)
            print(print_emo[maxindex])
        if cv2.waitKey(1) & 0xFF == ord('G'):
            imgemo=cv2.imread(emoji_distg[maxindex])
            cv2.imshow('',imgemo)
            print(print_emog[maxindex])
        if cv2.waitKey(1) & 0xFF == ord('B'):
            imgemo=cv2.imread(emoji_distb[maxindex])
            cv2.imshow('',imgemo)
            print(print_emob[maxindex])
        if cv2.waitKey(1) & 0xFF == ord('Q'):
            sys.exit()
        cv2.putText(frame, emotion_dict[maxindex], (x+20, y-60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('Video', cv2.resize(frame,(1200,860),interpolation = cv2.INTER_CUBIC))

cap.release()
cv2.destroyAllWindows()

