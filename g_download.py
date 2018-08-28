from google_drive_downloader import GoogleDriveDownloader as gdd

gdd.download_file_from_google_drive(file_id='1zIX4oGCNY_1YZjXOM068b7ghekuSmXCo',
                                    dest_path='./data/mnist.zip',
                                    unzip=True)
#https://drive.google.com/open?id=1zIX4oGCNY_1YZjXOM068b7ghekuSmXCo