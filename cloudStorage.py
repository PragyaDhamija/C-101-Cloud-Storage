import dropbox

class TransferData: 
    def __init__(self, access_token):
        self.access_token = access_token
        
    def uploadFile(self, fileFrom, fileTo):
        # link the our dropbox account to the application
        dbx = dropbox.Dropbox(self.access_token)
        f = open(fileFrom, 'rb')
        #upload these contents to the dropbox using the files_upload() method
        dbx.files_upload(f.read(),fileTo)

def main():
    accessToken = 'sl.BCGCBoqmIHXOoXxfXqXNv_CBMtR3p_d6Whnazb-vsALkXGJYZtHRif2qnUNoS40lkgi5a2goX8NO9BHAuFn1BYau9F5l5eNCzOIbv9Nxxv5Lpwp1EJQHv30vN70jaCPjx05Z6q02qLs'
    # object for the class TransferData is being created here
    td = TransferData(accessToken)
    file_from = input("Enter the complete path of the file to be transfered:- ")
    file_to = input("Enter the complete path to upload to Dropbox:- ")
    
    # Using the object of the class, we are calling the function uploadFile
    td.uploadFile(file_from,file_to)
    print("The file has been moved successfully... :)")

main()