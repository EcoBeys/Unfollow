import instaloader
import time
import sys
import colorama
from colorama import Fore,Back,Style
from getpass import getpass
import os 
from os import system


colorama.init(autoreset=True)

sys.path.insert(0,"./Unfollow_Bot/")
instagram = instaloader.Instaloader()

print(Fore.CYAN + """
      
      |\     /|( (    /|(  ____ \(  ___  )( \      ( \      (  ___  )|\     /|
      | )   ( ||  \  ( || (    \/| (   ) || (      | (      | (   ) || )   ( |
      | |   | ||   \ | || (__    | |   | || |      | |      | |   | || | _ | |
      | |   | || (\ \) ||  __)   | |   | || |      | |      | |   | || |( )| |
      | |   | || | \   || (      | |   | || |      | |      | |   | || || || |
      | (___) || )  \  || )      | (___) || (____/\| (____/\| (___) || () () |
      (_______)|/    )_)|/       (_______)(_______/(_______/(_______)(_______)
      


""")
                                                    
print(Fore.CYAN+""" 
Kod Sahibi : Enes Cört
Python Version: 3.8.5
Sosyal Medya: https://linktr.ee/EcoBeys
                                             
                                                    
    """)


# Function for implementing the loading animation 
def load_animation(): 

	# String to be displayed when the application is loading 
	load_str = "konsol uygulamasi basliyor..."
	ls_len = len(load_str) 


	# String for creating the rotating line 
	animation = "|/-\\"
	anicount = 0
	
	# used to keep the track of 
	# the duration of animation 
	counttime = 0		
	
	# pointer for travelling the loading string 
	i = 0					

	while (counttime != 100): 
		
		# used to change the animation speed 
		# smaller the value, faster will be the animation 
		time.sleep(0.090) 
							
		# converting the string to list 
		# as string is immutable 
		load_str_list = list(load_str) 
		
		# x->obtaining the ASCII code 
		x = ord(load_str_list[i]) 
		
		# y->for storing altered ASCII code 
		y = 0							

		# if the character is "." or " ", keep it unaltered 
		# switch uppercase to lowercase and vice-versa 
		if x != 32 and x != 46:			 
			if x>90: 
				y = x-32
			else: 
				y = x + 32
			load_str_list[i]= chr(y) 
		
		# for storing the resultant string 
		res =''			 
		for j in range(ls_len): 
			res = res + load_str_list[j] 
			
		# displaying the resultant string 
		sys.stdout.write("\r"+res + animation[anicount]) 
		sys.stdout.flush() 

		# Assigning loading string 
		# to the resultant string 
		load_str = res 

		
		anicount = (anicount + 1)% 4
		i =(i + 1)% ls_len 
		counttime = counttime + 1
	
 

# Driver program 
if __name__ == '__main__': 
	load_animation() 

	# Your desired code continues from here 
	# s = input("Enter your name: ") 
	s ="Şanslı kişi"
	sys.stdout.write("Merhaba "+str(s)+"\n") 
time.sleep(1)

print(Back.RED +  "NOT: KULLANICININ NE KADAR ÇOK TAKİPÇİ VE TAKİP EDENİ OLURSA UYGULAMA YAVAŞLAYABİLİR ")    
print(Back.RED+"Not: Kullanıcı adınızı ve şifrenizi düzgün yazdığınızdan emin olun yanlış yazarsanız uygulama kendini otomatik kapatacaktır")
    
username =input("Kullanıcı Adınızı Giriniz: ")
print(Back.RED + "Şifreniz Güvenlik amacıyla gizlenmektedir")
password = getpass('Şifrenizi giriniz: ')
instagram.login(username,password)

def yoyo():
    print("""
1)Kendi Hesabınızda sizi takip etmeyen kullanıcıları bulma
2)Başka hesapların takip etmeyenlerini bulma
3)Bir Kullanıcının takip ettiklerini dosyaya yazdırma
4)Bir Kullanıcının takipçilerini dosyaya yazdırma
'exit' yazarak çıkabilirsiniz                                                     """)
    print(Back.RED+ "Not: 2.işlemde gizli hesaplarda ya da giriş yaptığınızda kullanıcı takip etmiyorsa uygulama düzgün çalışmaz")                                                    

    secenek = input("Hangi işlemi yapmak istiyorsunuz: ")
    def job1():
        
                profile = instaloader.Profile.from_username(instagram.context,username)
                
                followers = profile.get_followers()
                following = profile.get_followees()

                print("Yükleniyor:")


                #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
                animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

                for i in range(len(animation)):
                        time.sleep(3)
                        sys.stdout.write("\r" + animation[i % len(animation)])
                        sys.stdout.flush()

                print("\n")
                print("Başarıyla Yüklendi...") 
                time.sleep(1)
              
            
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
                        with open(username + " Takip Etmeyenler.txt", "a") as file:
                                file.write(following +"\n")
                                file.close() 
                
        
        
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
        
                print("Yükleniyor:")


#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
                animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

                for i in range(len(animation)):
                    time.sleep(3)
                    sys.stdout.write("\r" + animation[i % len(animation)])
                    sys.stdout.flush()

                print("\n")
                print("Başarıyla Yüklendi...") 
                time.sleep(1)
                
                for following in following_list:
                    if following not in followers_list:
                        print(following," kullanicisi seni takip etmiyor")
                        count = +1
                        time.sleep(1)
                        with open(secenek2 + " Takip Etmeyenler.txt", "a") as file:
                                file.write(following +"\n")
                                file.close() 
                
    
    def job3():
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
                
                print("Yükleniyor:")


#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
                animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

                for i in range(len(animation)):
                    time.sleep(3)
                    sys.stdout.write("\r" + animation[i % len(animation)])
                    sys.stdout.flush()

                print("\n")
                print("Başarıyla Yüklendi...") 
                time.sleep(1)
                
                for following_list in following_list:
                        if following not in followers_list:
                            print(following_list + " Takip ediyorsun")
                            count = +1
                            time.sleep(1)
                   
                        with open(secenek2 +" Takip ettikleri.txt", "a") as file:
                            file.write(following_list +"\n")
                            file.close()    
                            
                
    
    def job4():
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
                print("Yükleniyor:")


#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
                animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

                for i in range(len(animation)):
                    time.sleep(3)
                    sys.stdout.write("\r" + animation[i % len(animation)])
                    sys.stdout.flush()

                print("\n")
                print("Başarıyla Yüklendi...")
                time.sleep(1)
                
                for followers_list in followers_list:
                        if followers_list in followers_list:
                            print(followers_list +  " seni takip ediyor")
                            count = +1
                            time.sleep(1)
                            
                            with open(secenek2 + " Takipçileri.txt", "a") as file:
                                file.write(followers_list +"\n")
                                file.close() 
                
                
    
    if secenek == "1":
        job1()
            
    elif secenek == "2":
        job2()
            
    elif secenek == "3":
        job3()  
                
    elif secenek == "4":
        job4()
                
    elif secenek == "exit":
            print("çıkılıyor...")
            time.sleep(2)
            quit()
            
            
    else:
             print("Lütfen Doğru Bir Seçenek Giriniz")    
             yoyo()                            
        

yoyo()
        
