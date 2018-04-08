
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
#from BeautifulSoup import BeautifulSoup
#import unirest
import json
import urllib.request as urllib2

app = ClarifaiApp()
model = app.models.get('food-items-v1.0')

def get_ingredients(image_url):
    """returns the ingredients in a given food pic"""
    
    image = ClImage(url= image_url)
    response= model.predict([image])
    #print(response)
    ingredients = []
    cnt= 0 

    if (response['status']['code'] == 10000):
        #print("respinsemaha")
        for i in response['outputs']:
            for j in i['data']['concepts']:
                if j['value'] > .7 and cnt < 3:
                    ingredients.append(j['name'])
                    cnt += 1
                else:
                    return ingredients
                    
        return ingredients

def get_recipe(image_url):
    """ """
    ingredients = get_ingredients(image_url)
    ing = ",".join(ingredients)
    url = "http://food2fork.com/api/search?key=17cd86aba7a553f7a8bb972f8066bafc&q=" + ing
    url_req = urllib2.Request(url, headers={ 'User-Agent': 'Safari/537.36', 'Content-Type': 'application/json'} , method='GET')
    response = urllib2.urlopen(url_req).read().decode('utf8')
    response_json = json.loads(response) 
    if response_json['count'] == 0:
        return "No recipes found! "
    else:
        result = "\n  Yummy, with that ingredients you could make a delicious {} , here you can find the recipe to do that {} \n Bon Appetit! {} ".format(response_json['recipes'][0]['title'], response_json['recipes'][0]['source_url'], u"\U0001F60B")
        return str(result)

if __name__ == "__main__":
    main()