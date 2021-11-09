# Importing flask
from flask import *

# Importing necesary libraries
import os
import time
import pathlib
from zipfile import ZipFile
from pytube import YouTube, Playlist
import re
import platform

sistema = platform.system()
if sistema == "Windows":
    spliters = "\\"
else:
    spliters = "/"

app = Flask(__name__)

# Function for mp3 converter in "/"
# Returns a static html file "mp3.html"
@app.route("/")
def mp3():
    return app.send_static_file("mp3.html")

# Function for mp4 converter in "/mp4"
# Returns a static html file "mp4.html"
@app.route("/mp4")
def mp4():
    return app.send_static_file("mp4.html")

# Returns a static html file "about.html"
@app.route("/about")
def about():
    return app.send_static_file("about.html")

# Returns a static html file "contact.html"
@app.route("/contact")
def contact():
    return app.send_static_file("contact.html")

# Function for mp3 processing, accepts http GET and POST
@app.route("/processUrlMP3", methods=["GET", "POST"])
def processUrlMP3():
    '''
    url_input, request the url from the html form
    values[0] = url_input
    values[1] = "download" (the downloads directory)
    '''
    url_input = request.form.get("url")
    values = [url_input, "download"]

    try:
        # detects if you're trying to download a playlist
        if "playlist" in str(values[0]):

            file_names = []

            playlist = Playlist(str(values[0]))

            playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

            for url in playlist.video_urls:
                yt = YouTube(url)
                video = yt.streams.filter(only_audio=True).first()
                destination = str((values[1]))
                out_file = video.download(output_path=destination)

                base, ext = os.path.splitext(out_file)
                new_file = base + ".mp3"

                # try to rename the file, .mp4 -> .mp3
                # if the file already exits in the directory, remove the .mp4 file
                try:
                    os.rename(out_file, new_file)

                except:
                    os.remove(out_file)
                    exit

                # saving our file name into a variable file_name
                # adding file_name into file_names list
                file_name = new_file.split(spliters)
                file_name = file_name[-1]
                file_names.append(file_name)

            # creating a zip file
            myzip = ZipFile('./download/prueba.zip', 'w')
            for file in file_names:
                myzip.write("./download/"+file)
                print(file)
            myzip.close()

            return render_template("download_mp3_template.html", file_name="prueba.zip")

        # if trying to download a single video
        else:
            yt = YouTube(str(values[0]))
            video = yt.streams.filter(only_audio=True).first()
            destination = str((values[1]))
            out_file = video.download(output_path=destination)

            base, ext = os.path.splitext(out_file)
            new_file = base + ".mp3"

            # try to rename the file, .mp4 -> .mp3
            # if the file already exits in the directory, remove the .mp4 file
            try:
                os.rename(out_file, new_file)

            except:
                os.remove(out_file)
                exit

            # saving our file name into a variable file_name
            file_name = new_file.split("spliters)
            file_name = file_name[-1]

            return render_template("download_mp3_template.html", file_name=file_name)

    # if there's no url in the form input, or the url isn't valid, return a error
    except:
        return render_template("error_template.html", processUrl="/processUrlMP3", MPx="MP3")

# Function for mp4 processing, accepts http GET and POST
@app.route("/processUrlMP4", methods=["GET", "POST"])
def processUrlMP4():
    url_input = request.form.get("url")
    
    try:
        yt = YouTube(url_input)
        file_name=(yt.title + ".mp4")
        stream = yt.streams.get_highest_resolution()
        stream.download("./download")

        return render_template("download_mp4_template.html", file_name=file_name)

    except:
        return render_template("error_template.html", processUrl="/processUrlMP4", MPx="MP4")

'''@app.route("/contactForm", methods=["GET", "POST"])
def contactForm():
    name = request.form.get("name")
    print (name)'''

# Function for downloading
@app.route("/download/<path:filename>", methods=["GET", "POST"])
def download(filename):
    return send_from_directory(directory="download", path=filename)


# Running the app in a non-privilege computer
app.run()

# Running the app in a admin-privilege computer
#app.run(host="0.0.0.0", port=80)
