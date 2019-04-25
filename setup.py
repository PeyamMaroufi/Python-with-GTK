# Here we imported the 'setup' module which allows us to install Python scripts to the local system beside performing some other tasks, you can find the documentation here: https://docs.python.org/2/distutils/apiref.html 
from distutils.core import setup 

setup(name = "Youtube Downloader GTK", # Name of the program. 
      version = "0.1", # Version of the program. 
      description = "A simple GTK application to download songs and videos from Youtube.", # You don't need any help here. 
      author = "Payam M", # Nor here. 
      author_email = " You don't need it",# Nor here :D 
      url = "https://github.com/PeyamMaroufi/", # If you have a website for you program.. put it here. 
      license='Mozilla Public License 2.0', # The license of the program. 
      scripts=['YoutubeDownloader'], # This is the name of the main Python script file, in our case it's "myprogram", it's the file that we added under the "myprogram" folder. 

# Here you can choose where do you want to install your files on the local system, the "myprogram" file will be automatically installed in its correct place later, so you have only to choose where do you want to install the optional files that you shape with the Python script 
      data_files = [ ("lib/YoutubeDownloaderGTK", ["Settings.py", "Downloader.py"]), # This is going to install the "ui.glade" file under the /usr/lib/myprogram path. 
                     ("share/applications", ["myprogram.desktop"]) ] ) # And this is going to install the .desktop file under the /usr/share/applications folder, all the folder are automatically installed under the /usr folder in your root partition, you don't need to add "/usr/ to the path.


# NOT DONE YET