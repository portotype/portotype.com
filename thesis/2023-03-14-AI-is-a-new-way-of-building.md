# Thesis: AI is a new way of building startups

## The thesis

I think AI will spawn a new way of building applications. 

- the best-in-class AIs (OpenAI) are pre-trained on the whole of open-source and open-solutions (stack overflow, API documentation).
- This means that out of the box, you can ask AI to generate code from these open sources.
- This means that companies will have an incentive to:
    - choose open-source libraries and components / APIs, as its faster to build in them;
    - keep the connection to these as abstracted and pure as possible, so that it's easier to plug them in, upgrade them etc, and connect them with other components. (The connections between components themselves can be a component).
- This means that companies will also have an incentive to:
    - provide open-source libraries and components / APIs to their services, as its faster to build with them;
    - keep their products open and free to extend.
- This will lead to an explosion of solutions, and a far lower cost in building.
- This will benefit:
    - components that are easy to use an integrate (APIs) with few complexities (e.g. rate limiting).
    - companies that are a free canvas where you can add all these building blocks;

## Example

At Rows.com, we built a Charts solution using an open-source Charts library. We integrated it by integrating the library deep with Rows platform: schema, persistence, FE app framework. We surely kept appropriate structures and abstractions for our technology process _at the time_, which was "designers and engineers build the simplest UX possible for the user, which is a polished UI, and maintain it". For our solution to cover the most common chart types, it took us many many months and several engineers.

The problem is that the technology process above did not include the possibility that a prompt could translate fuzzy to syntax (human text to code). If that UX becomes possible, then you can offer a new, faster experience. You have a generic html component, and when the user asks to do a Chart of XY dataset, with such and such property, you ask your ML to render that as a Chart of library X. And "that's it". Adding new Charts is faster, and you can always later push the syntax into a generic visual UI too.

## Key benefit

- faster code development.
- infinite extensibility.
- user-generated "code" or "configs" in a markdown matter with simple syntaxes.
