# 2017-12-03. Trouble ahead for SaaS

From a user demand angle, the SaaS business model is built on a **simplification** advantage: A SaaS tool gives you the functionality you need to do your job, ready to use and hassle-free. In return, they charge a monthly (or yearly) fee. The per person logic is a favorite, but other tiered pricing models exist that scale with usage or features.

From a supply angle, it seems like SaaS proliferated because of how easy and inexpensive it has become to create them:
- Inexpensive infrastructure (IaaS and PaaS) offered by the likes of Amazon, Google, Heroku, etc. 
- Containers (VMs, containers) that offer convenient abstraction of infrastructure.
- Automated development operations with infrastructure as code.
- Open Source software, libraries and API integration code in abundance.

I believe that these forces will also ultimately be the demise of SaaS as the king of B2B pricing models for software. 

- Open source automation will evolve deep into the harder parts of software management: configuring, monitoring, updating, scaling, security. Infrastructure as code keeps things predictable, modular, and easy to migrate. We will get "everything as code".
- This will open up the abstraction provided by saas companies. Today the saas players offer it all on a UX level. "click a button and get an account/server/email and don't worry about managing it". Then you will be able to DIY "import a configuration, everything is setup, now you get the buttons for whatever you need".
- This will, in turn, empty up a significant part of the value. Because the "as code" oferring will be open, new players will be able to match the experience faster, and the heavy premium will come down.
- I think this will mimic the first push of automated software installs, life Wordpress, Magento and Drupal of the 2000s. Just this time, instead of a deploy of a single software in a single server, you'll be deploying a whole setup that is ready to scale and easy to manage and update.

SaaS may fight back and replicate pricing models that are tuned to infrastructure usage. Like charging per actual days used or just for active users instead of charging for everyday and every user. They can and will keep investing in differentiating functionality that is hard to replicate under a distributed model, especially for niches. Machine learning models will also bring advantages to the players controlling most of the data when these times arrive. 

Complex models may survive in SaaS, but the future clearly will bring a lot of hardship to this model.

IaaS + Containers + Automation + Open Source > SaaS.
  
