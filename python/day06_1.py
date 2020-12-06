def main(txt):
    groups = txt.split('\n\n')
    pos_questions = [set(group.replace('\n', '')) for group in groups]
    num_pos_questions = [len(pq) for pq in pos_questions]
    return sum(num_pos_questions)


if __name__ == '__main__':
    with open('../data/input06.txt') as f:
        txt = f.read()

    print(main(txt))
