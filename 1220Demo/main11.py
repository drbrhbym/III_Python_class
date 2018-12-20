f = open("vote.json", "r", encoding="utf-8")

article = f.read()
f.close

import json

vote = json.loads(article)
print(vote[123]['CandidateName'])

