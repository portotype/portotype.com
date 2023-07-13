The problem

- product creators have little visibility on funnels of features

The solution
- ideally i’d add 2 lines of code to our software, and then an app woud guide me in visually picking which states or events map out to what (an open of a Chart is the id of the Chart when spreadsheet is loaded in editor OR in live OR in Embed).
- for the BE part, to know state (which Charts still exist), you'd have to probe the API or database, or do more events.

Example
- on a spreadsheet, how many people clicked Add Chart
    - of these, how many people successfully added a Chart
        - of these, how many Charts remain (not deleted Chart or spreadsheet)
            - of these, how many Charts are still used (opened, active)
                - of these, how many Charts have been updated.
- for each of these cuts, refine the analysis
    - the period (over the following x days, always);
    - for the base data (how many clicked add chart) you could also define for everyone or per cohort.
- replace Charts with Data Tables, Pivots, Spreadsheets, Integrations, and Embeds. (Maybe i’m missing something).
