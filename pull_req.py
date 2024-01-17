import requests
url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"
responce = requests.get(url)
check = responce.status_code
pr_user = {}
if check == 200:
    print("Request is successful")
    complete_output = responce.json()
    for i in complete_output:
        user = i["user"]["login"]
        if user in pr_user:
            pr_user[user]+=1
        else:
            pr_user[user]=1
    for user, count in pr_user.items():
        print(f"{user} : {count}")
else:
    print("Request is unsuccessfull ")