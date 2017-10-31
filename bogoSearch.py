import random
import time

#intiialzing a function that helps generating a cryptographically secure random number
secure_random = random.SystemRandom()

#function randomly picks an element and compares it to the element we are searching for, if found it returns or
#else it tries again -- timeout and noOfTries will be implemented in a future update to act as a mesasure to limit 
#number of tries and attempt time to find element
def bogoSearch (listOfElements, element, timeout = 0, noOfTries = 0):
  count = 0;
  start_time = time.time()
  while(True):
    count = count + 1;
    selectedIndex = secure_random.choice(range(len(listOfElements)));
    selectedElement = listOfElements[selectedIndex];
    if(selectedElement == element):
      elapsed_time = time.time() - start_time;
      print("ELEMENT HAS BEEN FOUND AT POSITION: " + str(selectedIndex));
      print("NUMBER OF TRIES TAKEN TO FIND ELEMENT: " + str(count));
      print("TIME ELAPSED: " + str(elapsed_time) + " seconds")
      return 0;

if __name__ == "__main__":
  #example
  listTemplate = ['Amazon','Chalk','Salesforce','BaazarVoice','Shippo','Twilio','LinkedIn','Twitter','Toast','Yelp ','Facebook','Google','Stripe','Airbnb','Apple','Redbooth','Addepar','Appian','Blend','Bloomberg','Capital One','DataDog','Dropbox','Fidelty','Couple','Galois','Goldman Sachs','GumGum','Intel','IMC','IXL Learning','Karat','Jane Street','Kayak','Khan Academy','Lucid','LiveRamp','Microsoft','Nvidia','AMD','OpenAI','Qualatrics','Roblox','Shogun Enterprises','SpaceX','Yahoo','Yelp ','WhatsApp','Walmart Labs','Yext','Two Sigma','Asana','BrainTree','Box','ShutterFly','Docker','Ebay','Figma','Evernote','Fitbit','Github','Frog','Houzz','JawBone','Lyft','Logitech','Medium','Lytx','Mozilla','Next','Paypal','Playstation','Quizlet','Quora','Ripple','Riot Games','Slack ','Square','Snap','Thumbstack','Twitch','HealthIQ','Milliman','PagerDuty','Coinbase','Optimizely','Uber','Pintrest','Spotify','Magic Leap','Unity','Zenefits','Sprinklr','MongoDB','RobinHood','Blizzard'];
  templateElement = "Coinbase";
  bogoSearch (listTemplate, templateElement);
