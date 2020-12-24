from day23_1 import play_game


class Cup:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f'{self.value} -> {self.next}'


class Circle:
    def __init__(self, cup_list, current_cup_value):
        self.cups_by_value = {cup.value: cup for cup in cup_list}
        self.current_cup_value = current_cup_value
        self.size = len(cup_list)

    @property
    def current_cup(self):
        return self.cups_by_value[self.current_cup_value]

    def move(self):
        # Part 1
        picked_up = [self.current_cup.next]

        while len(picked_up) < 3:
            picked_up.append(picked_up[-1].next)

        self.current_cup.next = picked_up[-1].next

        # Part 2
        destination_cup_value = self.current_cup_value - 1
        while destination_cup_value in [cup.value for cup in picked_up]:
            destination_cup_value -= 1

        if destination_cup_value == 0:
            destination_cup_value = self.size

        # Part 3
        destination_cup = self.cups_by_value[destination_cup_value]
        destination_cup_next = destination_cup.next
        destination_cup.next = picked_up[0]
        picked_up[-1].next = destination_cup_next

        # Part 4
        self.current_cup_value = self.current_cup.next.value


def main(cupstring, moves):
    cups = [Cup(int(c)) for c in cupstring]
    max_cup = max(cup.value for cup in cups)
    cups += [Cup(i) for i in range(max_cup+1, 1_000_001)]

    for i, cup in enumerate(cups[:-1]):
        cup.next = cups[i+1]

    cups[-1].next = cups[0]

    circle = Circle(cups, cups[0].value)

    for i in range(moves):
        if i % 100000 == 0:
            print(f'turn {i+1}')
        circle.move()

    cup1 = circle.cups_by_value[1]
    next = cup1.next
    next2 = next.next

    return next.value * next2.value


if __name__ == '__main__':
    print(main('853192647', 10_000_000))
