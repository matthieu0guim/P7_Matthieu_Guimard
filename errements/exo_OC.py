# -*- coding: utf-8 -*-
import random

# Initialize seed so we always get the same result between two runs.
# Comment this out if you want to change results between two runs.
# More on this here: http://stackoverflow.com/questions/22639587/random-seed-what-does-it-do
random.seed(0)

##################################################
#################### VOTES SETUP #################
##################################################

VOTES = 100000
MEDIAN = VOTES/2
CANDIDATES = {
    "hermione": "Hermione Granger",
    "balou": "Balou",
    "chuck-norris": "Chuck Norris",
    "elsa": "Elsa",
    "gandalf": "Gandalf",
    "beyonce": "Beyoncé"
}

MENTIONS = [
    "A rejeter",
    "Insuffisant",
    "Passable",
    "Assez Bien",
    "Bien",
    "Très bien",
    "Excellent"
]

def create_votes():
    return [
        {
            "hermione": random.randint(3, 6),
            "balou": random.randint(0, 6),
            "chuck-norris": random.randint(0, 2),
            "elsa": random.randint(1, 2),
            "gandalf": random.randint(3, 6),
            "beyonce": random.randint(2, 6)
        } for _ in range(0, VOTES)
    ]

##################################################
#################### FUNCTIONS ###################
##################################################

candidates = {
    "hermione": [0, 0, 0, 0, 0, 0, 0],
    "balou": [0, 0, 0, 0, 0, 0, 0],
    "chuck-norris": [0, 0, 0, 0, 0, 0, 0],
    "elsa": [0, 0, 0, 0, 0, 0, 0],
    "gandalf": [0, 0, 0, 0, 0, 0, 0],
    "beyonce": [0, 0, 0, 0, 0, 0, 0]
}

def results_hash(votes):
    candidates_results = {
        candidate: [0]*len(MENTIONS)
        for candidate in CANDIDATES.keys()
    }
    for vote in votes:
        for candidate, mention in vote.items():
            candidates_results[candidate][mention] += 1
    return candidates_results

def majoritary_mention_hash(candidates_results):
    cumulated_votes = 0
    r = {}
    for candidate, candidate_result in candidates_results.items():
        for mention, vote_count in enumerate(candidate_result):
            cumulated_votes += vote_count
            if MEDIAN < cumulated_votes:
                r[candidate] = {
                    'mention': mention,
                    'score': cumulated_votes
                }
                break
    return r

def sort_candidate_by(mentions):
    unsorted = [(key, (mention["mention"], mention["score"])) for key, mention in mentions.items()]
    swapped = True
    while swapped:
        swapped = False
        for j in range(0, len(unsorted) - 1):
            if unsorted[j+1][1] > unsorted[j][1]:
                unsorted[j+1], unsorted[j] = unsorted[j], unsorted[j+1]
                swapped = True
    return [
        {
            "name": candidate[0],
            "mention": candidate[1][0],
            "score": candidate[1][1]
        }
        for candidate in unsorted
    ]

def print_results(results):
    for i, result in enumerate(results):
        name = CANDIDATES[result["name"]]
        mention = MENTIONS[result["mention"]]
        score = result["score"] * 100 / VOTES
        if i == 0:
            print(f"Gagnant: {name} avec {score}% de mention {mention}")
            continue
        else:
            print(f"-{name} avec {score}% de mention {mention}")
##################################################
#################### MAIN FUNCTION ###############
##################################################

def main():
    votes = create_votes()
    results = results_hash(votes)
    majority_mentions = majoritary_mention_hash(results)
    sorted_candidate = sort_candidate_by(majority_mentions)
    print_results(sorted_candidate)

if __name__ == '__main__':
    main()
