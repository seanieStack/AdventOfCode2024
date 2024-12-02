from Day5.helper import parse_input

rule_dict, updates = parse_input()

valid_updates = []

for update in updates: #loop over all updates
    valid_update = True

    for i, page in enumerate(update): # loop over all pages in update
        rules_for_page = rule_dict[page] # get the rules for the current update

        for later_page in update[i + 1:]: # loop over pages after the current page
            if later_page not in rules_for_page: #if a future page is not in the list of rules set flag and break
                valid_update = False
                break

        if not valid_update:
            break

    if valid_update:
        valid_updates.append(update)


total = 0
for valid_update in valid_updates:
    total += int(valid_update[len(valid_update) // 2])

print(total)

