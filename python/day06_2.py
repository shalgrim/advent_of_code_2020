from collections import Counter


def main(txt):
    groups = txt.split('\n\n')
    lines_by_group = [group.split() for group in groups]
    num_people_by_group = [len(lbg) for lbg in lines_by_group]
    num_votes_by_group = [Counter(group.replace('\n', '')) for group in groups]

    qualifying_votes = []
    for voters, votes in zip(num_people_by_group, num_votes_by_group):
        qualifying_votes.append(len([v for v in votes.values() if v == voters]))

    return sum(qualifying_votes)


if __name__ == '__main__':
    with open('../data/input06.txt') as f:
        txt = f.read()

    print(main(txt))
