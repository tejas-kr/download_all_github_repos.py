from github import Github as gb
import urllib.request
import shutil
from pathlib import Path
import os
import getpass

user_name = input("Enter Username: ")
password = getpass.getpass()

g = gb(user_name, password)

g = gb("Auth_token_here")

def download_repo(repo):
	print(repo.name)
	usr_resp = input("Wanna download this repo? [Y/N]: ")
	if(usr_resp.lower() == "y" or usr_resp.lower() == "yes"):
		url = "https://api.github.com/repos/%s/%s/zipball"
		
		if(not os.path.isdir(str(Path.home()) + "/" + str(repo.owner.login))):
			os.mkdir(str(Path.home()) + "/" + str(repo.owner.login))
		
		file_name = str(Path.home()) + "/" + str(repo.owner.login) + "/" + str(repo.name)
		
		with urllib.request.urlopen(url % (repo.owner.login, repo.name)) as response, open(file_name, 'wb') as out_file:
			shutil.copyfileobj(response, out_file)
	
	elif(usr_resp.lower() == "n" or usr_resp.lower() == "no"):
		pass
	
	else:
		print("please choose a correct option!")



for repo in g.get_user().get_repos():
	download_repo(repo)


