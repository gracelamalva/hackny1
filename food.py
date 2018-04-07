
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

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
    print(get_ingredients('http://onelittleproject.com/wp-content/uploads/2016/07/DSC_9218.jpg'))
    

if __name__ == "__main__":
    main()