# To get the proposals-slugs.json file
# If you run this graphql query you can access the necessary data to build the URL
# https://projectcatalyst.io/funds/${fund._id}/${challenge.slug}/${project.projectSlug}
# https://projectcatalyst.io/api/v1/graphql?explorerURLState=N4IgJg9gxgrgtgUwHYBcQC4QEcYIE4CeABMADpJFEBmMSYAFAPoCWY6RpIAjAAycCUJcpUoAHPBABWCKCgDOQiiMosww5UXFSZKAMoAbGAHN1yqAAsAhvv3IjCRRpFzDJpcoC%2Bpol6W%2BPIB5AA
# the project._id is the ideascale id
# The project.slug for the most part is a staight up slugification of the project name, but there are some exceptions worth noting:
# If there is a name collision or if the resultant name is too long, then the slug is shortened and a unique short hash is added

import json

with open("proposals.json") as proposals_file:
    proposals = json.load(proposals_file)

with open("slug-urls.json") as urls_file:
    urls = json.load(urls_file)

for proposal in proposals:
    found = False
    for row in urls["data"]["fund"]["projects"]:
        if row["_id"] == proposal["proposal_id"]:
            found = True
            proposal["proposal_url"] = (
                "https://projectcatalyst.io/funds/10/"
                + row["challenge"]["slug"]
                + "/"
                + row["projectSlug"]
            )

    if not found:
        print("Not found for proposal id: " + proposal["proposal_id"])

json_object = json.dumps(proposals, indent=4)
with open("proposals-slugs.json", "w") as outfile:
    outfile.write(json_object)
