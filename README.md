<a><img src="Data/poster.jpg"></a>
# EmotionRecognition-TelegramBot
This project was developed a telegram bot for emotion recognition. The recognition process is designed so that the bot expects an image as input, which may contain several people or no people at all. Then, the search for faces in the image is carried out and a photo is displayed in the chat to the user, where all found faces are highlighted. After that, for each found face, the predicted emotion is displayed in the chat, which corresponds to one of the 7 emotion classes. The approach to distributing emotions into groups and the dataset for training the recognition model were taken from the Kaggle platform ([“FER-2013”](https://www.kaggle.com/datasets/msambare/fer2013)).

## Сontents
- [Technologies](#technologies)
- [Using](#using)
- [Documentation](#documentation)
- [Distribute](#distribute)
- [Developers](#developers)
- [Contributing](#contributing)
- [License](#license)

## Technologies
- [Python](https://www.python.org/)
- [PyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/)
- [Tensorflow](https://www.tensorflow.org/)
- [Keras](https://keras.io/)
- [Face-recognition](https://pypi.org/project/face-recognition/)
- [OpenCV](https://pypi.org/project/opencv-python/)
- ...

## Using
To reproduce the results, test and run this project, you need to:
* Clone the repository, after which I recommend creating a virtual environment for the project ([video guide on working with a virtual environment](https://www.youtube.com/watch?v=rsG1Y5k-9jo)).

* The project has a [requirements.txt](requirements.txt) file containing information about all the libraries and their dependencies - use it to fill the virtual environment of your interpreter.

* To interact with Telegram, namely to launch a Telegram bot, you need a token, which can be created using the [Bot Father](https://t.me/botfathermeb). Add your token to the [TelegramBot_Token.json](Data/TelegramBot_Token.json) file as a text string, as a value for the "token" key.

After completing these steps, there should be no difficulties with launching the project! 🤩

If problems arise, try changing the version of the language you are using, the working assembly was tested on Python 3.10. 🦾

## Documentation
To get acquainted with additional information on the project - you can open the [Report](Report/Report.docx), it contains information on the architecture of the trained emotion recognition model, comparative analysis with another emotion recognition solution, a block diagram of the recognition algorithm and many other additional details.

The [Model](Model) folder contains a trained emotion recognition model file with the .h5 extension.

Additional information about the structure of the [Data](Data) folder. The directory contains: the [ImageFiles_All](Data/ImageFiles_All) folder and two files, one of which is a project poster, and the second is a storage for recording the telegram bot token. The "ImageFiles_All" directory has 4 folders and one file in its structure. Folders are used to accumulate images that can then be used to form new datasets, each directory stores its own image format, to navigate them, use the names of these folders and the examples of content loaded into them, the file accumulates information about how many user images were saved by the bot.


## Distribute
- [GitHub repository](https://github.com/EvgeniyKorovin1/EmotionRecognition-TelegramBot)

## Developers
- [Evgeniy Korovin](https://github.com/EvgeniyKorovin1) — ML-Engineer

## Contributing
To send feedback on the project or other interaction that can be associated with it, please use [email](https://mail.google.com/mail/?view=cm&fs=1&to=korovinevgeniyalexeyevich@gmail.com&su=EmotionRecognition-TelegramBot), indicating the [repository](https://github.com/EvgeniyKorovin1/EmotionRecognition-TelegramBot) as the subject of the letter.

## License
The license for the use of materials from this project can be viewed - [LICENSE](LICENSE).
