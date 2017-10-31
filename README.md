<h1 align="center">BogoSearch </h1>
<p align="center">Search Algorithm inspired by the infamous BogoSort</p>

<img src = "https://i.imgur.com/MwGHU6a.png" style="min-width:100%; min-height:100%" />
<p align="center">BogoSort Running</p>

## Way it works
* Select a random number (let's call it x) between 0 and len of list
* Get element at position x in the list (let's call it k)
* Check if element we are searching for is equal to k
* IF TRUE - Return position of element(x) and additional data
* IF FALSE - Repeat steps
