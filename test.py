import json

pp = json.load(open(f"meta/fund9/proposals.json"))

maxlen = 0
for p in pp:
    if len(p['proposer_name']) > maxlen:
        maxlen = len(p['proposer_name'])
        print(f"New max {p['proposal_title']}")

print(maxlen)
print(f"Count {len(pp)}")
