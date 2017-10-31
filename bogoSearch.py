import random
import time

#intiialzing a function that helps generating a cryptographically secure random number
secure_random = random.SystemRandom()

#function randomly picks an element and compares it to the element we are searching for, if found it returns or
#else it tries again -- timeout and noOfTries will be implemented in a future update to act as a mesasure to limit 
#number of tries and attempt time to find element
def bogoSearch (listOfElements, element, timeout = 0, noOfTries = 0):
  count = 0;
  while(True):
    start_time = time.time()
    count = count + 1;
    selectedIndex = secure_random.choice(range(len(listOfElements)));
    if(listOfElements[selectedIndex] == element):
      elapsed_time = time.time() - start_time;
      print("ELEMENT HAS BEEN FOUND AT POSITION: " + str(selectedIndex));
      print("NUMBER OF TRIES TAKEN TO FIND ELEMENT: " + str(count));
      print("TIME ELAPSED: " + str(elapsed_time) + " seconds")
      return 0;

if __name__ == "__main__":
  #example
  listTemplate = ["test", "test123"];
  templateElement = "test";
  bogoSearch (listTemplate, templateElement);
