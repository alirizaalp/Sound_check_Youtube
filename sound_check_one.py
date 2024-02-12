from youtubesearchpython import VideosSearch
import speech_recognition as sr
import webbrowser

def search_youtube(query):
    videos_search = VideosSearch(query, limit=1)
    
    results = videos_search.result()

    
    return results["result"][0]["link"] if results["result"] else None

def play_youtube(video_url):
   
    webbrowser.open(video_url)

def recognize_speech():
   
    recognizer = sr.Recognizer()

   
    with sr.Microphone() as source:
        print("Sesinizi bekliyorum...")

       
        recognizer.adjust_for_ambient_noise(source, duration=1)

     
        audio = recognizer.listen(source, timeout=5)

    try:
     
        return recognizer.recognize_google(audio, language="tr-TR").lower()
    except sr.UnknownValueError:
        print("Komut anlaşılamadı.")
        return None

if __name__ == "__main__":
    
    song_found = False

    while not song_found:
       
        command = recognize_speech()

        if command:
          
            if "watch" in command:
                print("Hangi şarkıyı aramamı istersiniz?")
                
              
                search_query = recognize_speech()

                if search_query:
                   
                    video_url = search_youtube(search_query)

                    if video_url:
                        print(f"{search_query} için bulunan video: {video_url}")
                        
                       
                        play_youtube(video_url)
                        
                        
                        song_found = True
                    else:
                        print("Video bulunamadı.")
            elif "çıkış" in command:
              
                print("Programdan çıkılıyor.")
                break
            else:
                
                print("Geçersiz komut. Tekrar deneyiniz lütfen.")
    

    print("Teşekkürler! Aramayı durdurdum.")




