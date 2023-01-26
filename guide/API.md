### What is an API?

An API is a way for computer programs to receive and answer requests from other computer programs.

`API` means `Application Programming Interface`. 

> Let's say you call a restaurant to order a pizza. The service that consists of "a number" where you "place your order" and that results in a "confirmation" is your pizza "API". Because its a human conversation, the request will be slighyly different for every person who calls, but it will always have to involve the same convention: the pizzeria staff needs to know your name, address, pizza preference, and with that they'll be able to tell you an estimated delivery time.

> After selling 10'000 pizzas, the pizzeria gets tired of phone calls. They tell you to just visit https://www.thepizzeria.com/your-name/your-full-address/the-pizza-you-want-and-quantity/ and that's it. They will extract your details from that website link you entered in your browser and show you on the page whether they can deliver it or not. What they created is an API!

### What makes an API

* An API offers a method for a particular program to receive requests from another program. Its a convention of how any program can reach that particular program that has the API.
* You can say an API is made of 2 events: the `request` and the `response` to the request.
    * the `request` involves:
        * The target, frequently called an `endpoint`, is the entity responsible for processing the `request`, doing anything that's asked in it, and then responding. In web APIs, it involves a web address (an URL). 
        * the `content` of your message: this is a particular layout of the information to send in the request (a `schema`), plus the the actual `data` and other configurations like the `format` of the message.
    * the `response` can include `content` too, though some APIs respond with just an "OK".

### Common Types of APIs

* Web APIs. These are the APIs that let your application access the functionality provided by a another computer program accross the internet. The payment APIs of Paypal are Web APIs.
* Operating System APIs: operating systems like Windows and iOS provide APIs that let application creators execute common functions easily. Send alerts to the user, display a web page inside your application or doing complex mathematical computations - all of those things can be provided by Operating Systems APIs.

### Examples of APIs
* When you login in into your online bank account, the bank website logs you in by asking a central bank API to check if the username and password you provided are ok. The API returns something like "OK" or "Not OK", and it frequently also returns some basic info on your account.
* When you tell your bank app to transfer money to a friend, the bank app is sending an API request to the Bank server (which is another program) telling it that you want to move money to your friend's bank account. The bank will, then, send a separate API request to your friends bank (or a central authority) telling them that you moved money to your friends account. The APIs will respond with the status of those operations and other details.
* When you play a 3D game in your Phone, the game app will like be calling a system API to access the 3D potential of the graphics processor of the phone. 
