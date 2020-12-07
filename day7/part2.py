class Bag:


    def __init__(self, color):
        self.color = color
        self.children = []
        self.children_num = {}
        self.parents = []

    def add_child(self, child, num):
        self.children.append(child)
        self.children_num[child.color] = num

    def add_children(self, children: list):
        self.children = children

    def add_parent(self, parent):
        self.parents.append(parent)

    def __str__(self):
        return self.color


def traverse_children(curr: Bag, been: dict, num: int, been_list: list, level=0):
    been_list.append((num, level))
    been[curr.color] = num
    if not curr.children:
        return 1
    c_count = 0
    for p in curr.children:
        num = curr.children_num[p.color]
        c_count += num * (traverse_children(p, been, num, been_list, level=level + 1))

    return c_count + 1


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
        if child_bag_color != "no other":
            num = int(el.split()[-3])
            if child_bag_color in bag_dict:
                child_bag = bag_dict[child_bag_color]
            else:
                child_bag = Bag(child_bag_color)
                bag_dict[child_bag_color] = child_bag
            super_bag.add_child(child_bag, num)
            child_bag.add_parent(super_bag)


curr_bag = bag_dict['shiny gold']
count = 1
been = {}

been_list = []
print(traverse_children(curr_bag, been, 1, been_list)-1)




