import mimetypes
import os
import time
import speech_recognition as sr
import shutil
import subprocess  #import libraries

#print (os.getcwd())
#print (os.listdir())

r = sr.Recognizer() #define speech recognition variable
from pathlib import Path

[f.unlink() for f in Path("splitaudio").glob("*") if
 f.is_file()]  # clear out old segmented files
#Text color
W = '\033[0m'  # white
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
from pathlib import Path

[f.unlink() for f in Path("conversion/storing").glob("*") if
 f.is_file()]  # clear out old converted files
# file_name

start_time = 0

max_time = 10

block_num = 0


def importfiles(): #import files from input directory

    print("Processing files" + R + "." + G + "." + B + ".")
    print("\n" + G + "File imported successfuly")


# Read file names and extensions


def count_files(dir):
    return len([1 for x in list(os.scandir('inputFiles')) if x.is_file()])


def transcript_to_srt(current_time, block):
    if current_time >= max_time:

        return "time limit reached"
    else:
        import os
        import time
        from pydub import AudioSegment
        import os
        source = os.listdir('inputFiles')
        for files in source:
            fileName, fileExtension = os.path.splitext(files)
        fileName, fileExtension = os.path.splitext(files)
        yourFile = 'inputFiles/' + fileName + fileExtension
        converted = 'conversion/storing/' + fileName + '.wav'
        audio = AudioSegment.from_file(yourFile)
        lengthaudio = len(audio)
        str_lengthaudio = str(lengthaudio)
        lengthaudio_minus3 = (str_lengthaudio[: -3])
        str_lengthaudio = int(lengthaudio_minus3)

        def convert(seconds):
            return time.strftime("%H: hours, %M minutes, %S seconds", time.gmtime(n))

        n = str_lengthaudio
        hms_length = convert(n)

        print("\n")
        print(P + "Length of Audio File:", W, hms_length)

        start = 0
        # In Milliseconds, this will cut 9 Sec of audio
        if lengthaudio > 120000:
            threshold = 10000
        else:
            threshold = 5000
        end = 0
        counter = 0

        while start < lengthaudio:
            end += threshold
            audio = AudioSegment.from_file(yourFile)
            chunk_silent = AudioSegment.silent(duration=500)
            chunk = chunk_silent + audio[start:end] + chunk_silent

            filename = f'splitaudio/chunk{counter}.wav'
            counter_str = str(counter)  # convert to string
            parts = 'splitaudio/chunk' + counter_str + '.wav'

            chunk.export(filename, format="wav")

            with sr.AudioFile(parts) as source:
                r = sr.Recognizer()
                audio = r.listen(source)  # read the entire audio file
                try:
                    text = (r.recognize_google(audio))
                except sr.UnknownValueError:
                    text = "No speech detected in audio segment"
                    pass

                block += 1  # append each sentence
                block_str_ = str(block)  # convert to string

                start_str_ = str(start)  # convert to string
                if start_str_ == "0":
                    start_str = "0"
                    start_num = int(start_str)
                    s = int(start_str)

                else:
                    start_str = int(start_str_[:-3])
                    start_num = int(start_str)
                    s = start_num

            end_str_ = str(end)  # convert to string
            end_str = (end_str_[:-3])
            end_num = int(end_str)

            def convertt(seconds):
                return time.strftime("%H:%M:%S", time.gmtime(s))

            def converttt(seconds):
                return time.strftime("%H:%M:%S", time.gmtime(e))

            e = end_num

            started = convertt(e)
            finished = converttt(s)

            if start_num < 1:
                print("\n")
                print(B + "00:00:00", " --> ", finished)
                print(W + text)
                with open('Transcriptions/' + fileName + "_transcript.txt", "a") as f:
                    f.write(block_str_)
                    f.write("\n")
                    f.write("00:00:00" + "-->" + finished)
                    f.write("\n")
                    f.write(text)
                    f.write("\n")
                    f.write("\n")
            else:
                print("\n")
                print(B + started, " --> ", finished)
                print(W + text)
                with open('Transcriptions/' + fileName + "_transcript.txt", "a") as f:
                    f.write(block_str_)
                    f.write("\n")
                    f.write(started + "-->" + finished)
                    f.write("\n")
                    f.write(text)
                    f.write("\n")
                    f.write("\n")

            counter += 1

            start += threshold



def convert_to_srt(current_time, block):

    if current_time >= max_time:

        return "time limit reached"
    else:

        from pydub import AudioSegment
        import os
        source = os.listdir('inputFiles')
        for files in source:
            fileName, fileExtension = os.path.splitext(files)
        yourFile = 'inputFiles/' + fileName + fileExtension
        converted = 'conversion/storing/' + fileName + '.wav'
        audio = AudioSegment.from_file(converted)
        lengthaudio = len(audio)
        str_lengthaudio = str(lengthaudio)
        lengthaudio_minus3 = (str_lengthaudio[: -3])
        str_lengthaudio = int(lengthaudio_minus3)

        def convert(seconds):
            return time.strftime("%H hours, %M minutes, %S seconds", time.gmtime(n))

        n = str_lengthaudio
        hms_length = convert(n)

        print("\n")
        print(P + "Length of Audio File:", W, hms_length)

        start = 0
        # In Milliseconds, this will cut 12 Sec of audio
        if lengthaudio > 120000:
            threshold = 12000
        else:
            threshold = 5000
        end = 0
        counter = 0

        while start < lengthaudio:

            end += threshold
            audio = AudioSegment.from_file(converted)
            chunk_silent = AudioSegment.silent(duration=900)
            chunk = chunk_silent + audio[start:end] + chunk_silent

            filename = f'splitaudio/converted_chunk{counter}.wav'
            counter_str = str(counter)  # convert to string
            parts = 'splitaudio/converted_chunk' + counter_str + '.wav'

            chunk.export(filename, format="wav")

            with sr.AudioFile(parts) as source:
                r = sr.Recognizer()
                # remove this if it is not working
                # correctly.
                audio = r.listen(source)  # read the entire audio file
                try:
                    text = (r.recognize_google(audio))
                except sr.UnknownValueError:
                    text = "No speech detected in audio segment"
                    pass

                block += 1  # append each sentence
                block_str_ = str(block)  # convert to string

                start_str_ = str(start)  # convert to string
                if start_str_ == "0":
                    start_str = "0"
                    start_num = int(start_str)
                    s = int(start_str)

                else:
                    start_str = int(start_str_[:-3])
                    start_num = int(start_str)
                    s = start_num

            end_str_ = str(end)  # convert to string
            end_str = (end_str_[:-3])
            end_num = int(end_str)

            def convertt(seconds):
                return time.strftime("%H:%M:%S", time.gmtime(s))

            def converttt(seconds):
                return time.strftime("%H:%M:%S", time.gmtime(e))

            e = end_num

            started = convertt(e)
            finished = converttt(s)
            if start_num < 1:
                print("\n")
                print(B + "00:00:00", " --> ", finished)
                print(W + text)
                with open('Transcriptions/' + fileName + "_transcript.txt", "a") as f:
                    f.write(block_str_)
                    f.write("\n")
                    f.write("00:00:00" + "-->" + finished)
                    f.write("\n")
                    f.write(text)
                    f.write("\n")
                    f.write("\n")
            else:
                print("\n")
                print(B + started, " --> ", finished)
                print(W + text)
                with open('Transcriptions/' + fileName + "_transcript.txt", "a") as f:
                    f.write(block_str_)
                    f.write("\n")
                    f.write(started + "-->" + finished)
                    f.write("\n")
                    f.write(text)
                    f.write("\n")
                    f.write("\n")

            counter += 1
            #change start to the last end value
            start += threshold


def scandirectory():
    while True:
        from time import ctime

        count_files(
            'inputFiles')  # count number of files in input directory
        number_countfiles = int(
            count_files('inputFiles'))  # convert to integer
        # print("Number of Files awaiting proccessing", number_countfiles)

        if number_countfiles < 1:
                print(R + "No new files")
                print("\n")
                print("\n" + B + "Last checked at: " + ctime())
                time.sleep(5)
                return scandirectory()

        if number_countfiles >= 1:
            str_number_of_files = str(number_countfiles)
            print("\n" + R + "Number of files awaiting processing: " + str_number_of_files)
            print("\n" + B + "Last checked at: " + ctime())
            importfiles()
            checkmime()


def checkmime():
    def checkextension():

        if not fileExtension == '.wav':
            # convert any non '.wav' file
            # ^The Speech Recognition library can only process '.wav' files
            print("Converting " + fileName + fileExtension + " to .wav")
            print("\n")
            #use ffmpeg to convert the inputed file into a .wav
            subprocess.call(['ffmpeg', '-i', yourFile, converted])
            # Use Speech Recognition library to transcribe the outputted '.wav' files
            convert_to_srt(start_time, block_num)
            print("\n" + G + "Transcription Complete")
            shutil.move(yourFile, "storageDirectory")
            if count_files(dir) < 1:
                scandirectory()

            # delete the created .wav file(s) as it is no longer needed

            # if the file within the source directory is a .wav, simply transcribe using the Speech Recognition module
        if fileExtension == '.wav':
            print(G + "\nSelected File: " + fileName + fileExtension)
            transcript_to_srt(start_time, block_num)
            print("\n" + G + "Transcription Complete")
            shutil.move(yourFile, "storageDirectory")
            if count_files(dir) < 1:
                scandirectory()


    #open("Transcripts/transcript.txt", "w").close()
    source = os.listdir('inputFiles')
    for files in source:
        fileName, fileExtension = os.path.splitext(files)
    yourFile = 'inputFiles/' + fileName + fileExtension
    converted = 'conversion/storing/' + fileName + '.wav'
    unsupported = 'Returned_files/' + fileName + fileExtension
    mime = str(mimetypes.MimeTypes().guess_type(yourFile)[0])
    video = "video"
    audio = "audio"
    print("File Mime Type: " + B + mime)
    print("\n")

    while True:

        if video in mime or audio in mime:

            if video in mime:
                print(G + "The imported file contains video")
            if audio in mime:
                print(P + "The imported file contains audio")
                print("\n")
            checkextension()

        else:
            shutil.move(yourFile, unsupported)
            print(
                R + "The uploaded file contains no audio or video. " + fileName + " was moved to [Returned_files] directory.")
            return


while True:
    scandirectory()























