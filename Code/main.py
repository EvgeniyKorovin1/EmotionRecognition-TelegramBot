import requests
import telebot
import face_recognition
import tensorflow as tf
import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt 
import json
import os

from tensorflow import keras
from PIL import Image, ImageDraw

def load_count(filename='Data\ImageFiles_All\ImagesNumber_Info.json', key = 'photos_number'):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return data[key]
    except FileNotFoundError:
        return 1  # Возвращает значения по умолчанию, если файл не найден

def save_count(photos_number, filename='Data\ImageFiles_All\ImagesNumber_Info.json'):
    data = {'photos_number': photos_number}
    with open(filename, 'w') as f:
        json.dump(data, f)

def TelegramBot_Live(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id,"Привет! Я Эмо-Бот! Не то что ты подумал - я в эмоциях разбираюсь! Отправь мне фото и я скажу кто и что там испытывает!")

    @bot.message_handler(content_types=["photo"]) #Функция, которая реагирует на получение фото
    def photo_work(message):
        
        photos_number = load_count()
        photos_number += 1
        fileID = message.photo[-1].file_id   
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(f"Data\ImageFiles_All\images\image_{photos_number}.jpg", 'wb') as new_file:#фото загрузилось в папку с указанным именем
            new_file.write(downloaded_file)

        #дальше работа с полученной картинкой 
        image = face_recognition.load_image_file(f"Data\ImageFiles_All\images\image_{photos_number}.jpg")
        face_locations = face_recognition.face_locations(image)

        if (len(face_locations) > 0):
            print(f"Я нашел аж {len(face_locations)} мордашек на твоей фотке!")
            bot.send_message(message.chat.id,f"Количество лиц, которое я нашел на фотографии - {len(face_locations)}!")
            bot.send_message(message.chat.id,"Я обвел все лица которые нашел! Вот они - смотри!")

            pil_image = Image.fromarray(image)
            draw1 = ImageDraw.Draw(pil_image)

            for(top, right, bottom, left) in face_locations:
                draw1.rectangle(((left, top),(right, bottom)), outline = (255,0,0), width= 4)
            del draw1

            pil_image.save(f"Data\ImageFiles_All\images_CircledFaces\image_{photos_number}_CircledFaces.jpg")
            with open(f'Data\ImageFiles_All\images_CircledFaces\image_{photos_number}_CircledFaces.jpg', 'rb') as photo_square:
                bot.send_photo(message.chat.id, photo_square) #Отправляет фото с обводкой в чат

            bot.send_message(message.chat.id,"А теперь каждое в отдельности!")

            faces_number = 1
            for(top, right, bottom, left) in face_locations:
                face_img = image[top:bottom, left:right]
                pil_face_image = Image.fromarray(face_img)
                pil_face_image.save(f"Data\ImageFiles_All\images_FacesSquare\image_{photos_number}_face_{faces_number}.jpg")

                with open(f"Data\ImageFiles_All\images_FacesSquare\image_{photos_number}_face_{faces_number}.jpg", 'rb') as photo_face:
                    bot.send_photo(message.chat.id, photo_face) #Отправляет фото лиц в чат

                img = cv2.imread(f"Data\ImageFiles_All\images_FacesSquare\image_{photos_number}_face_{faces_number}.jpg", cv2.IMREAD_GRAYSCALE)
                img = cv2.resize(img, (48,48))
                cv2.imwrite(f"Data\ImageFiles_All\images_FacesSquareGray\image_{photos_number}_face_gray_{faces_number}.jpg", img)

                img_gr = keras.utils.load_img(f"Data\ImageFiles_All\images_FacesSquareGray\image_{photos_number}_face_gray_{faces_number}.jpg", color_mode='grayscale')
                img_array = keras.utils.img_to_array(img_gr)
                img_array = tf.expand_dims(img_array, axis=0)
                img_array.shape

                predict = model.predict(img_array)

                for i in range(len(predict[0])):
                    if predict[0][i] >= 0.51:
                        bot.send_message(message.chat.id,f"Я думаю, что человек на фотографии - {emotions[i]}!")
                        break
                faces_number += 1
            save_count(photos_number)
        else:
            print(f"Я не нашел здесь лиц - попробуй ещё раз!")
            bot.send_message(message.chat.id,f"Я не нашел здесь лиц - попробуй ещё раз!")
            os.remove(f"Data\ImageFiles_All\images\image_{photos_number}.jpg")




    bot.infinity_polling()

if __name__ == '__main__':
    model = keras.models.load_model('model\model.h5') 
    model.inputs
    emotions = {0:'anger', 1:'disgust', 2:'fear', 3:'happiness', 4: 'sadness', 5: 'surprise', 6: 'neutral'}

    TelegramBot_Live(load_count('Data\TelegramBot_Token.json', 'token'))