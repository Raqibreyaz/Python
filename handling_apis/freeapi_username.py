import requests


def fetch_user_data():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    res = requests.get(url)
    data =  res.json()
    if(data["success"] and "data" in data):
        user_data = data['data']
        username = user_data["name"].values().join(" ")
        country = user_data["location"]['country']
        return username,country
    else:
        raise Exception("failed to fetch user data")
    
def main():
    try:
        username,country = fetch_user_data()
        print(f"Username: {username}, Country: {country}")
    except Exception as e:
        print(str(e))
        
if(__name__ == "__main__"):
    main()