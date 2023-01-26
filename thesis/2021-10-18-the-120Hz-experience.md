# the 120Hz experience

_This article was first posted on our Rows.com "tech" Slack channel on 2021-10-19._

Today apple is announcing their next-gen laptops and chips. 

We will see, as it's expected, new Apple silicon with many important improvements over what was gen1 (Apple m1). We will also see other improvements: I think mostly focused on screens (ProMotion/ 120Hz?) and cameras, with at least 1080p with better FOV, head tracking, better light handling with ML. Battery bumps can be there or not, depending on how much power vs. weight they want - these are Pro machines anyway. A big question is how powerful gpus will be, and if apple will continue the tradition of custom graphics sw (like Metal) or if they'll support some other standards (DirectX OpenGL etc).

I think it's important to reflect on these announcements and general industry trends seriously. The following is my perspective.

As more power is given to the Front-End, I predict that we will be seeing more responsibilities being handed to local algorithms. 

- FrontEnds enable more fluid, richer experiences. Local is faster, at least in what concerns latency and the computing budget. It is also more reliable as there's no outages. It also poses significant challenges like data sync between different users working on the same project. Finally, on the FE you can do generally do better animations and richer multimedia.
- Local also gives more power to the users. Local-first software opens up the possibility of offline modes. In this context it's important to decouple convenient online benefits like cloud storage, synchronization and collaboration, from local benefits like allowing users to edit whenever & wherever, which are enabled by the local ownership (and portability) of your data.
- 3D, VR and AR are even more possible with extra computing power, though that's of limited interest to many B2B SaaS companies like our own, [Rows.com](rows.com). 
- Back-end can't match the "120Hz front-end experience" in real-time. For 120Hz experiences, you have to offer user actions that react under 10ms, and that includes the front-end part and back-end. And in 2021, cloud services for data and transformations don't operate at those speeds for any sufficently advanced computation. Probably they won't be able to do it for a long long time, given distances, network latency and unpredictable loads. 
- Candidates for local algorithms are search, computation, Image and Video processing and of course interface rendering. 
- Already we see an early indication that the industry is looking for those solutions, for example in the continued growth of productivity apps and services that are local-first or offer significant offline modes. Google Sheets offers it for the iPad and even in the browser; We know Notion is toying with the idea, and the upcoming SuperList app will be local-first.
- There's still the question of where in the FE we should bould our local app: natively, in the browser or hybrid. Having more powerful computers also bolsters the browsers case. Still, in my experience, web-development offers more compatibility at the expense of a worse user experience. In the browser, you have to compete for tab space; persistence and memory are limited and owned by the browser, which includes basic stuff like keeping you logged-in and downloading the "web app"; and if those weren't enough, web development is very fragmented, and you have to pick from a number of frameworks (e.g. react) that are all incomplete and offer less power (read, fps) and UI consistency than their native counterparts. All this makes the browser ok for simple apps or apps you use a few times per week, but if you’re spending many hours per day on them, the lesser experience usually shows. If your productivity app is especially demanding (as spreadsheets are), being web-only or web-most is hard to justify.
- I definitely recommend this terrific article that pushes for this view, [Local-first Software](https://www.inkandswitch.com/local-first.html), by the Ink & Switch collective. It covers much more ground, and is more technical than this opinion of mine. 

At the same time, the more FE evolves, the more innovation will come to the BE too. 

- Already on ARM architectures, novel Infrastructure providers such as Cloudflare are being joined by traditional ones (AWS, GCP) to offer computation that is closer to the FE (edge), more cost efficient (ARM), more powerful (ML), and scalable (lambdas). Cloud services offer literally any kind of pre-built component you could wish for - state, realtime comms, cms, queues, DBs, etc.. 
- Components that do persistence (DBs), sync for state managmeent, and collaboration seem like safe bets on critical components that will stay on the server/ cloud side.
- Novel things will continue to permeate into cloud systems, notably blockchains, as robust ways to own stuff and form consensus in a distributed world.

Some might think i'm relying too much on Apple for this view of the future. Quite the contrary. Apple rarely predicts the future. But more frequently than any other company, they are the creator of the conditions for that future. Mac GUIs, the mouse, ethernet, wifi, iPod, iTunes, iPhone, App Stores, iPads, Apple Watches are creations that apple developed or at least first unleashed at scale. And most of those became the basis of today's hardware and software economy. As an example, our company Rows can be traced to the iPhone: the iPhone => a bigger market for apps => popularization of Massive-scale Apps => cloud providers that support that scale (AWS) => faster creation of software and the SaaS model => SaaS VCs doing investment in new productivity concepts => Rows. 

In conclusion, I take from the Apple silicon efforts that that frontends are evolving to enable 120Hz experiences. That is spearheaded by native frameworks, and it will be impossible for apps to offer these new experiences while keeping tightly coupled FE-BE architectures. The most demanding and pleasant productivity systems should be the first to migrate to richer local experiences, keeping the cloud for storage, sync and collaboration. Within local-apps, It will make sense that a decent chunk will go the native route, to take advantage of platforms to offer multi-device, native-like experiences, while others will create hybrid apps ported from the web.

Let’s go!
