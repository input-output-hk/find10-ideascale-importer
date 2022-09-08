# Ideascale importer

```
Usage: main.py [OPTIONS]                                                                                                                                          

╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --api-token              TEXT       Ideascale API token.                                                             │
│ --fund                   INTEGER    Fund number. [default: 8]                                                        │
│ --fund-group-id          INTEGER    Ideascale Campaigns group id [default: 1]                                        │
│ --chain-vote-type        TEXT       Chain vote type [default: private]                                               │
│ --threshold              INTEGER    Voting threshold [default: 450]                                                  │
│ --fund-goal              TEXT       Fund goal [default: Lorem ipsum]                                                 │
│ --merge-multiple-authors            When active includes and merge contributors name in author field [default: False]│
│ --authors-as-list                   Export authors as a list of objects replacing the single author [default: False] │
│ --stages                 INTEGER    List of stages ids that will be pulled from Ideascale                            │
│ --assessments            TEXT       Valid assessments CSV file                                                       │
│ --withdrawn              TEXT       Withdrawn proposals CSV file                                                     │
│ --proposals-map          TEXT       Mapping for proposals [default: templates/tags.json]                             │
│ --funds-format           TEXT       Mapping for funds transformation. [default: templates/funds_format.json]         │
│ --challenges-format      TEXT       Mapping for challenges export. [default: templates/challenges_format.json]       │
│ --proposals-format       TEXT       Mapping for proposals [default: templates/proposals_format.json]                 |
│ --reviews-format         TEXT       Mapping for assessments transformation. [default: templates/reviews_format.json] |
│ --output-dir             TEXT       Output dir for results [default: meta/fund9]                                     │
│ --help                              Show this message and exit.                                                      │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

For `--assessments` the example file can be found in `examples/assessments.csv`.
It is possible to omit this param (scores will be at 0 and reviews empty).

For `--withdrawn` the example file can be found in `examples/withdrawn.csv`.
It is possible to omit this param (excluded proposals will be empty).

The `--proposals-format` map has a double function:
 - Only the keys of the `export_cols` field that are present in the proposals
 prepared by the script are exported and extra fields are filtered out.
 Having a field in `export_cols` doesn't guarantee that a field will be
 exported because it depends by its presence in the data (e.g. when
   `--merge_multiple_authors` the field `proposers` is not generate and not
   included in the export even if specified in this file).
- When a key is present it is exported after being cast with the data type
specified as values in the `export_cols` object.

The `--proposals-map` file is used to map the ideascale fields to local
proposal fields. It is possible to specify more than one ideascale field that
will be mapped to a local field.
