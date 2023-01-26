## Origin

In 2019, after 2 years working in the Rows.com platform (then dashdash.com), I realized that we were building more than a spreadsheet. **We're building a translator.** 

Our Rows editor is, essentially, just a bunch of rectangles (cells). Users can write a language into them, which is the spreadsheet language. This language includes values and formulas, and other visual notations like data formats and colors. When users write stuff into the cells, we automatically generate a code representation of the user's input in the front end, in the back end, and we also have a method to keep both ends synchronized. Our computation engine consumes this technical notation and performs any necessary calculations, sending results back to update what the user sees on the editor.

In reality, it's a bit more complicated than that. Behind the user input, there is an amalgamation of code, structures, and applications. Some of them exist locally in the browser and app, whereas others work in the cloud. It's hard to separate what belongs to a particular spreadsheet and a particular computation from what is shared between spreadsheets and belongs to the platform as a whole. This is because the platform was designed to provide a service to the user, without any particular belief on wether the architecture of our systems can provide value. 

But then I thought: what if we generated a human-readable representation of the spreadsheet, sitting between the grid interface of the editor and the several layers of technical code? We were already using some of it to describe bugs. `A1: 5` can represent a cell with a literal of value 5. `A1: =2+2 =>5` is a cell with a formula that results in the same value, 5. With such a notation we no longer force the user to interact with our spreadsheet language via only our interface, instead we create a contract for interactions. Human readable. Human editable. We would keep the table interface, but we'd also offer the human-readable representation of the spreadsheet. At a minimum, I thought, this would allow the spreadsheet community to create scripts that generate all kinds of spreadsheets.

So now we would have separated 3 layers: UI, human-readable code, and the all the technical stuff translated from the human-readable code. But we could take it one step further. Having the 3 layers meant that we would need an engine to translate this human notation into the actual code that executes for that particular spreadsheet. The engine that translates between the layers is the interesting piece. We could open it to the world. 

In a way, all of this isn't that different from Markdown, or other tools like Excalidraw and Mermaid. A class of programming languages for end-users. So I started generating all kinds of human-notation languages on my mind. 

## The goal of Full-Stack Markdowns

To build systems where human readable notations get translated into code.

## The Problem

- coding is hard. coding is getting more complex by the day, with multiple layers of OS, frameworks, libraries, APIs, conventions, best practices, etc.
- most Low-code-No-code platforms are very proprietary and that will mean trouble.
    - few to no programming languages were ever successful while being closed/ proprietary.
    - while having an API counts as being "open", APIs often mean a gatekeeper that will issue you keys, keep rate limits, security etc.
    - furtgerm the market for solutions moves in unforeseen ways, which makes it hard to keep pace with verticals needs unless you're investing a f- lot.
    - even with large enough investments, a platform must also keep pace with the underlying paradigms, OSes, devices and form-factors, which introduce new problems and opportunities. Examples: mobile, tablets, responsive, cloud, watch, lambda, VR, AR, crypto.
    - experimentation and adaptation is best provided by the community of pros.
- pure UI drag and drop frameworks hide the logic and expressiveness of the underlying domain language (which maps to a problem space).. With the pressure to ship, this creates wrong incentives for engineering teams, who have poorly defined or hidden contracts between the Creators and the actual Code.
    - Visual development is still very interesting, but it should neither negate a tangible artifact (the markdown) nor imply being proprietary. 

## The Solution

- just as markdown translates between text and html+css, I propose that there can be N textual languages that codify a whole stack: FE (code and style)+BE+Data+comms+infra. A full-stack-markdown or human-readable-everything-as-code.
- I think that more than the particular FSMD (full stack markdown language), we need to create the software where the FSMDs are used. Think of a VSCode or Github for business people.
- In the FSMD software, there are 4 separated layers:
    1. the human readable code.
    2. the code translated from of 1.  
    3. The visual rendering of 2.
    4. Navigation, settings, etc.
- All layers should be interpreted in real-time, editing should be possible on any. (I assume this is a very hard challenge). That means, the creator should be able to change code, change the programming language translation, and/or change the visual rendering, all at once.
- Our software should be an editor which, for each folder or group of folders executes a certain script (the FSMD parser).
- FSMDs should reuse as much pre-existing code as possible. The core of this business is to create the platform, not the individual FSMDs. 

## Use cases

FSMDs should allow for many solutions. 

- creating a personal blog from markdown files.
- creating a website for a company.
- rendering a gallery of photos from a folder with image files.
- rendering vanilla markdown within a folder.
- rendering excalidraw files within a folder.
- rendering code for a wiki (Notion-like).
- creating a workflow (Zapper-like).
- creating a drive of mixed blocks that are files and links and comments that are navigable and downloadable.
- do a small mathematical model and represent it live.
- create a visual interface for a MySQL/ SQLite database.
- create a simple shopping cart for sales.
- store and read (and share) passwords as encrypted files.

# Concepts

- [Todo.kanban](https://github.com/jessmartin/todo.kanban) turn a a markdown file into an interface.


