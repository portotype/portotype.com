# The UPS of the Internet

I think AI will spawn a world's first UPS of data. 

Imagine a global, publicly accessible message queue between apps. 

That is, any app can call a central service and say "leave this message for that user of that app". And then any user can go that central service and ask "are there messages for me from that app?". 

# Why this is important

This is important because AI and collaborative workflows are the norm, and both of them are async. 

I will explain. So, most apps are a database + interface. 

The exception to that is the connection beween different users and between different apps. That requires another service to be available to connect users and applications. And if you want to connect users in different apps, then this becomes far more problematic.

Some of the users and apps are available, others aren't. Some speak the same language, some don't.

Examples: 
- you want to implement real-time chat on your platform. You need another service to store messages, store relationships between them, etc.
- you have an AI agent executing a task that requires hand-off to other agents and APIs. 

# Solution 

Implement a message queue with just 2 calls:
- send message to user U1 on app A1.
- read messages for user U1 on app A1.

Message properties 
- can be encrypted or public.
- if they require auth, messages can be accessed with a master publisher key; an app maker key; a user key; a self-registered user key (like validate this is your domain and you can read it). 
- can have file attached, probably start with simpler stuff.
- can expire after a while.

More
- Step 2 is to create actions on top of messages for processing.
- You can have this service be replicable across locations.

# Inspiration

- CoreFlux.org, which provides a MQTT service for IOT.
- UPS, where packages get delivered irrespective of who the sender is, what is inside the package, where the destination is. Address, message, send.
- HTTP, which is a protocol for the web, but this would be like ASYNC HTTP, no matter who is on the other side, even if they're not online, you drop a message.. someone will get it.

# Business

- First x messages free, then pay per message a super ultra small amount.
- Transformation on top.
