# Link Tracker

### problem 

- links are the key element of the internet.
- it's hard to keep track of what's happening.
- there's many integrations, but never an integration for all the services. Better use the existing API - the browser agent which can access everything you can access.

### solution

- create the first link-only productivity app
- in this app you can add links to be tracked, and you get visual alerts for changes in what you're tracking.

### use cases

- investors 
    - an investor has a portfolio. the investor wants to know if the company hired more people, or if someone left. the investor wants to know if the homepage has been upgraded, or the pricing changed, or testimonials. the investor wants to know if the homepage of the product changed. the investor adds a link to the app, selects what part they want to check for changes (maybe there's a preset per domain). the investor adds them in a colection. the app periodically refreshes that url and tells the investor if something changed in a nice little indicator. 
- companies
    - a business manager wants to know if their competitor changed something in the website. if a certain github card has been closed. if a powerpoint is completed or some analytics property changed. you add those links to the app and voilá.
- hiring
    - you want to check if a person changed their status on linkedin. you add the link.
- fans
    - keep track of when Apple releases new products, when your team scores a goal, when a product is back in stock.

### approach

- the app uses the local context (local machine, IP, local browser sessions etc) to refresh links and tell you what's changed.
- each link has an object type - what are you tracking? a company/ webpage/ project/ social media profile? type tag (social, etc) custom config.
- the app let's you create several items of the same type.
- people will want a table view.
- there's user collaboration: you invite other users, and whomever contributes with links also needs to access links (?).
- maybe server side isn't a bad idea, BUT in that case we'd have to implement SSOs for services (which we don't want), the best thing is either fully local or a "local-like" server-side session.
