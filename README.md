# Ideascale importer

```
Usage: main.py [OPTIONS]                                                                                                                                          

╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --api-token            TEXT       Ideascale API token.                                                             │
│ --fund                 INTEGER    Fund number. [default: 8]                                                        │
│ --fund-group-id        INTEGER    Ideascale Campaigns group id [default: 1]                                        │
│ --chain-vote-type      TEXT       Chain vote type [default: private]                                               │
│ --threshold            INTEGER    Voting threshold [default: 450]                                                  │
│ --fund-goal            TEXT       Fund goal [default: Lorem ipsum]                                                 │
│ --stages               INTEGER    List of stages ids that will be pulled from Ideascale                            │
│ --assessments          TEXT       Valid assessments CSV file                                                       │
│ --withdrawn            TEXT       Withdrawn proposals CSV file                                                     │
│ --proposals-map        TEXT       Mapping for proposals [default: templates/tags.json]                             │
│ --funds-format         TEXT       Mapping for funds transformation. [default: templates/funds_format.json]         │
│ --challenges-format    TEXT       Mapping for challenges export. [default: templates/challenges_format.json]       │
│ --proposals-format     TEXT       Mapping for proposals [default: templates/proposals_format.json]                 |
│ --reviews-format       TEXT       Mapping for assessments transformation. [default: templates/reviews_format.json] |
│ --output-dir           TEXT       Output dir for results [default: meta/fund9]                                     │
│ --help                            Show this message and exit.                                                      │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

For `--assessments` the example file can be found in `examples/assessments.csv`

For `--withdrawn` the example file can be found in `examples/withdrawn.csv`
