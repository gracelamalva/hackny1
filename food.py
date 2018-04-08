
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
    if (response['status']['code'] == 10000):
        #print("respinsemaha")
        for i in response['outputs']:
            for j in i['data']['concepts']:
                if j['value'] > .5:
                    ingredients.append(j['name'])
        return ingredients

def main():
    #l = get_ingredients('http://onelittleproject.com/wp-content/uploads/2016/07/DSC_9218.jpg')
    l = get_ingredients('https://images-na.ssl-images-amazon.com/images/I/512l5vJviXL._SY450_.jpg')
    ing = ",".join(l)
    #print(ing)
    url = "http://food2fork.com/api/search?key=17cd86aba7a553f7a8bb972f8066bafc&q=shrimp,mushroom"
    url_req = urllib2.Request(url, headers={ 'User-Agent': 'Safari/537.36', 'Content-Type': 'application/json'} , method='GET')
    response = urllib2.urlopen(url_req).read().decode('utf8')
    response_json = json.loads(response) 
    #print(response_json['recipes'])
    print(response_json['recipes'][0]['title'], response_json['recipes'][0]['source_url'])
    # for i in response_json['recipes']:
    #     print(i['title'],i['source_url'])
    #print(response_json)
    #soup.body.findAll(text='Python')



if __name__ == "__main__":
    main()