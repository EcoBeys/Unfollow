import instaloader
import time
import sys
sys.path.insert(0,"./İnstagram Takip Etmeyenler/")
instagram = instaloader.Instaloader()

print("""
      |\     /|( (    /|(  ____ \(  ___  )( \      ( \      (  ___  )|\     /|
      | )   ( ||  \  ( || (    \/| (   ) || (      | (      | (   ) || )   ( |
      | |   | ||   \ | || (__    | |   | || |      | |      | |   | || | _ | |
      | |   | || (\ \) ||  __)   | |   | || |      | |      | |   | || |( )| |
      | |   | || | \   || (      | |   | || |      | |      | |   | || || || |
      | (___) || )  \  || )      | (___) || (____/\| (____/\| (___) || () () |
      (_______)|/    )_)|/       (_______)(_______/(_______/(_______)(_______)
      
                                                    
Kod Sahibi : Enes Cört
Python Version: 3.8.5
Sosyal Medya:https://linktr.ee/EcoBeys
NOT: KULLANICININ NE KADAR ÇOK TAKİPÇİ VE TAKİP EDENİ OLURSA UYGULAMA YAVAŞLAYABİLİR                                              
                                                    
    """)
username =input("Kullanıcı Adınızı Giriniz: ")
password = input("Şifrenizi Giriniz: ")
instagram.login(username,password)
print("""
1)Kendi Hesabınızda sizi takip etmeyen kullanıcıları bulma
2)Başka hesapların takip etmeyenlerini bulma
Not: 2.işlemde gizli hesaplarda ya da login yaptığınız kullanıcı takip etmiyorsa uygulama düzgün çalışmaz                                                    """)
secenek = input("Hangi işlemi yapmak istiyorsunuz: ")
def job1():
    
    profile = instaloader.Profile.from_username(instagram.context,username)
    
    followers = profile.get_followers()
    following = profile.get_followees()
    followers_list = list()
    following_list = list()
    
    for follower in followers:
        followers_list.append(follower.username)
    
    for followee in following:
        following_list.append(followee.username)
    
    
    for following in following_list:
        if following not in followers_list:
           print(following," kullanicisi seni takip etmiyor")
           count = +1
           time.sleep(1)
           with open(username + " Takip etmeyenler.txt", "a") as file:
                    file.write(following +"\n")
                    file.close() 
    fhand = open(username + " Takip Etmeyenler.txt")
    count=0
    for line in fhand:
        count=count+1
    print(count)
    
    
def job2():    
    
    secenek2 = input("Kullanıcı Adını Girin: ")
    profile = instaloader.Profile.from_username(instagram.context,secenek2)
    
    followers = profile.get_followers()
    following = profile.get_followees()
    followers_list = list()
    following_list = list()
    
    for follower in followers:
        followers_list.append(follower.username)
    
    for followee in following:
        following_list.append(followee.username)
    
    
    for following in following_list:
        if following not in followers_list:
           print(following," kullanicisi seni takip etmiyor")
           count = +1
           time.sleep(1)
           with open(secenek2 + " Takip etmeyenler.txt", "a") as file:
                    file.write(following +"\n")
                    file.close() 
    fhand = open(secenek2 + " Takip Etmeyenler.txt")
    count=0
    for line in fhand:
        count=count+1
    print(count)
    
    
    
if secenek == "1":
    job1()
elif secenek == "2":
    job2()
else:
    print("Lütfen Doğru Bir Seçenek Giriniz")    

    