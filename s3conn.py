import boto3 

def handle_upload_mp4(f): # f = 파일명
    data = open('./videos/'+f+'.mp4', 'rb')
    # '로컬의 해당파일경로'+ 파일명 + 확장자
    
    s3 = boto3.resource('s3') 
    s3.Bucket('baedalgeek-team3').put_object(
        Key=f, Body=data, ContentType='video/mp4')

for i in range(1,4):
    handle_upload_mp4(str(i))

def handle_download_mp4(f):
    client = boto3.client('s3')
    client.download_file('baedalgeek-team3', f, "./downloadvideo/"+f+".mp4")

for i in range(1,4):
    handle_download_mp4(str(i))
