from os import access
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.BJJuRwaDXBPiSws8Y3Ic5GaRN_UT5gEemY-sbSlsf9S1a-g7ehjwtqlcAwRHc8ifrcj2Cfj98hnZ9qeC45HZ4PTYp5MsVyt7p77kg-_jIec-JSgSi1zwHn4VlTvrcTVw8PB9E3o'
    transferData=TransferData(access_token)

    file_from=input('Enter the file path: ')
    file_to=input('Enter the full path to upload to dropbox: ')
    transferData.upload_file(file_from,file_to)
    print('File has been moved')

main()      