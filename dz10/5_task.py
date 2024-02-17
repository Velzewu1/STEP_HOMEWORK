"""Task 3"""

def election_votes(candidates, electors):
    """Counts all votes"""
    votes = []
    for i in range(electors):
        print(", ".join(candidates))
        vote = input("За кого вы голосуете: ")
        for candidate in candidates:
            if candidate.lower() == vote.lower():
                votes.append(candidate)
    return votes

def count_votes(total_votes):
    """Choose winner"""
    votes_count = {}
    leaders_list = []
    winner = 0

    for vote in total_votes:
        votes_count[vote] = total_votes.count(vote)
    winner_votes = sorted(votes_count.values())[-1]
    for k, v in votes_count.items():
        if v == winner_votes:
            leaders_list.append(k)

    if len(leaders_list) > 1:
        winner = sorted(leaders_list, key=len)[0]
    return f"Победил: {winner}"

if __name__ == "__main__":
    CANDIDATE_LIST = ["Аскаров", "Бекмуханов", "Ернур", "Пешая", "Карим", "Шаримазданов"]

    elector_count = int(input("Введите кол-во выборщиков: "))
    print(count_votes(election_votes(CANDIDATE_LIST, elector_count)))
    