# What

Web Worker AI Model.
An AI LLM that you can easily spawn as a web-worker to use in your web-apps.

# Why

Because you want full control of your AI.

You need a javascript package READY to run on a web worker so that web apps can run local algos:
- avoid having to call cloud apis (cost, availability). call the web-worker.
- ⁠avoid having to target different local OS APIs: Apple Intelligence, Chrome gemini, Microsoft OS Copilot AI thing dark side.
- part of your web-app, test = production.

# how

1. Start by shipping a simple NPM repo simple that is your LLM. Model, weights, calling classes, the full thing. Ship with an opensource LLM, small one. 
2. Then move that code to a Web Worker (i think its the best approach) bc web workers function like a background app in the browser.

Why web workers make sense
-	Web Workers run javascript.
-	WWs run in a separate thread from the main JavaScript thread.
- WWs have their own execution context, making them independent your main app. Don't have to manage that if you don't want to.
- WWs do asynchronous processing, they won't block the main thread. (this is good bc AI is expensive).
- WWs cannot render UI, but you don't need that.

You could take it up a notch with a full virtual apps, using WebAssembly. 

# business model

This saves companies lots of money and hassle, mostly through saved engineering time and AI cost. Maybe offer smaller models for free and more complex models for a price. Maybe it's support. 

You can go "fixed price".
You can also offer per-use-case models. One just to parse SQL/Python (data applications), another just for image generation, etc.
