import os
from google_drive_downloader import GoogleDriveDownloader as gdd

gdd.download_file_from_google_drive(file_id='1l0SsicIM9xhVy1C--PbwNfottKPfvfLg',
                                    dest_path='./mnist.zip',
                                    unzip=True)
os.remove('./mnist.zip')
#https://drive.google.com/open?id=1zIX4oGCNY_1YZjXOM068b7ghekuSmXCo
#https://drive.google.com/open?id=1wi-rN7-c6rNtw7ODoHrYJx2WJMFLYkRY
#https://drive.google.com/open?id=1l0SsicIM9xhVy1C--PbwNfottKPfvfLg