# idea

In **traditional apps**, you have a fixed data model → fixed API → fixed UI.

With the **AI-routed app**, a self-describing payload + optional ask → AI router → materialized data/actions/UI

# example

You start with an app that has only 2 AI routers/ interpreters, one in the BE and one in the FE. You say "store the financial data in these company reports / PDFs, saving the PDF for tracking". Then the BE router extracts data and PDF and saves it as lets say a CSV. When data is loaded, the FE router knows that it's got financial data and will guess an interface for that. Then user say: "now show me interactive charts for it" and the FE router creates it.

Importantly, the FE router doesn't need to know beforehand that this is a “financial dashboard.” It receives a payload whose semantics are already exposed, plus the ask, and can decide that charts, tables, filters, etc. are the appropriate representation.


                  ┌──────────────────────┐
                  │  SELF-DESCRIBING     │
                  │       PAYLOAD        │
                  └──────────┬───────────┘
                             │
                          + ASK
                             │
                             ▼
                 ┌────────────────────────┐
                 │     BACKEND AI ROUTER  │
                 └───────────┬────────────┘
                             │
                   ┌─────────┴─────────┐
                   ▼                   ▼
                DATA                 ACTIONS
                   │                   │
                   └─────────┬─────────┘
                             │
                             ▼
                 ┌────────────────────────┐
                 │    FRONTEND AI ROUTER  │
                 └───────────┬────────────┘
                             │
                   ┌─────────┴─────────┐
                   ▼                   ▼
                  UI              INTERACTIONS
