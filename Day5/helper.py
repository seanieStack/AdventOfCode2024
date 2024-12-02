def parse_input():
    with open("input.txt", "r") as f:
        data = f.read()

    rules, updates = (temp := data.split("\n\n"))[0].split("\n"), [x.split(",") for x in temp[1][:-1].split("\n")]

    rule_dict = dict()
    for rule in rules:
        rule_parts = rule.strip().split("|")
        if rule_parts[0] in rule_dict.keys():
            rule_dict.get(rule_parts[0]).append(rule_parts[1])
        else:
            rule_dict[rule_parts[0]] = [rule_parts[1]]

    return rule_dict, updates