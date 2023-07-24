from googleapiclient.discovery import build

YOUTUBE_API_KEY = 'AIzaSyAem-ptyr8RMcY3l-r2fnodMvQrnvlrwDI'

youtube = build('youtube','V3', developerKey=YOUTUBE_API_KEY)

search_response = youtube.serch().list(
    part='snippet',
    q='KOG',
    order='viewVount',
    type='video',
).execute()

