import requests
from osuAPI.key import KEY
def getUser(user):
    response = requests.get("https://osu.ppy.sh/api/get_user?u="+user+"&k="+KEY)
    user = response.json()[0]
    return user