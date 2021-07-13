import requests
import json
import pyfiglet,sys,time
rs = requests.session()
print("""
		
░█████╗░██████╗░███╗░░░███╗
██╔══██╗██╔══██╗████╗░████║
███████║██║░░██║██╔████╔██║
██╔══██║██║░░██║██║╚██╔╝██║
██║░░██║██████╔╝██║░╚═╝░██║
╚═╝░░╚═╝╚═════╝░╚═╝░░░░░╚═╝
""")
print("Log in to your Instagram account:")
print("")     
username = input("username :")
password = input("password :")
Target = input("Target :")
url = 'https://www.instagram.com/accounts/login/ajax/'
headers = {
     'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '275',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'csrftoken=DqBQgbH1p7xEAaettRA0nmApvVJTi1mR; ig_did=C3F0FA00-E82D-41C4-99E9-19345C41EEF2; mid=X8DW0gALAAEmlgpqxmIc4sSTEXE3; ig_nrcb=1',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
    'x-csrftoken': 'DqBQgbH1p7xEAaettRA0nmApvVJTi1mR',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': 'bc3d5af829ea',
    'x-requested-with': 'XMLHttpRequest'
    }
data = {
         'username': f'{username}',
         'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
         'queryParams': '{}',
         'optIntoOneTap': 'false'
    }    
r = rs.post(url, headers=headers, data=data)
if  'authenticated":true' in r.text:
    print("")
    print("-"*25)	
    print("")
    print("Login :"+username)
    try:
        u = rs.get(f"https://www.instagram.com/{Target}/?__a=1")
        id =  str(u.json()["graphql"]["user"]["id"])
        print(f"{Target} : {id}")
        print("")
        print("-"*25)
    except:
    	print("Sent too many requests, try later")
    	exit()	
    s =rs.get('https://www.instagram.com/graphql/query/?query_hash=303a4ae99711322310f25250d988f3b7&variables={"reel_ids":["%s"],"tag_names":[],"location_ids":[],"highlight_reel_ids":[],"precomposed_overlay":false,"show_story_viewer_list":true,"story_viewer_fetch_count":50}'%(id))
    ss = json.loads(s.content.decode())
    if len(ss['data']['reels_media'])>0:
        print("")
        print("Usernames hidden in the story :")
        print("")
        for i in ss['data']['reels_media']:
            da = i['items']
            if len(da)>0:
                for ii in da:
                    if len(ii['tappable_objects'])>0:
                        for iii in ii['tappable_objects']:
                            user = iii['username']   
                            print(f"username :{user}")       
    else:
    	print("There are no hidden usernames")   	
elif '{"message":"checkpoint_required"' in r.text:
	print("Checkpoint")
else:
    print("Error, Try again")
