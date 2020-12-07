class Bag:


    def __init__(self, color):
        self.color = color
        self.children = []
        self.parents = []

    def add_child(self, child):
        self.children.append(child)

    def add_children(self, children: list):
        self.children = children

    def add_parent(self, parent):
        self.parents.append(parent)

    def __str__(self):
        return self.color


def traverse(curr: Bag, been: set):
    been.add(curr.color)
    if not curr.parents:
        return

    for p in curr.parents:
        if p.color not in been:
            traverse(p, been)
    return


with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

bag_dict = {}
for line in lines:
    str_list = line.split('bag')
    super_bag_color = str_list[0].strip()

    if super_bag_color in bag_dict:
        super_bag = bag_dict[super_bag_color]
    else:
        super_bag = Bag(super_bag_color)
        bag_dict[super_bag_color] = super_bag

    remain = str_list[1:-1]

    for el in remain:
        child_bag_color = ' '.join(el.split()[-2:])
        if child_bag_color == "no other":
            pass
        else:
            if child_bag_color in bag_dict:
                child_bag = bag_dict[child_bag_color]
            else:
                child_bag = Bag(child_bag_color)
                bag_dict[child_bag_color] = child_bag
            super_bag.add_child(child_bag)
            child_bag.add_parent(super_bag)


curr_bag = bag_dict['shiny gold']
count = 0
been = set()
traverse(curr_bag, been)

print(len(been)-1)








