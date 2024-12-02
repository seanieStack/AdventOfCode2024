from Day5.helper import parse_input

rule_dict, updates = parse_input()

def find_invalid(all_updates):
    first_invalid = []

    for update in all_updates: #loop over all updates
        valid_update = True

        for i, page in enumerate(update): # loop over all pages in update
            rules_for_page = rule_dict[page] # get the rules for the current update

            for later_page in update[i + 1:]: # loop over pages after the current page
                if later_page not in rules_for_page: #if a future page is not in the list of rules set flag and break
                    valid_update = False
                    break

            if not valid_update:
                break

        if not valid_update:
            first_invalid.append(update)

    return first_invalid

def check_valid(update):
    update_is_valid = True
    invalid_index = -1
    corresponding_invalid_rule_index = -1

    for i, page in enumerate(update):  # loop over all pages in update
        rules_for_page = rule_dict[page]  # get the rules for the current update

        for j, later_page in enumerate(update[i + 1:]):  # loop over pages after the current page
            if later_page not in rules_for_page:  # if a future page is not in the list of rules set flag and break
                update_is_valid = False
                invalid_index = i
                corresponding_invalid_rule_index = j + i + 1
                break

        if not update_is_valid:
            break

    if update_is_valid:
        return True
    else:
        return invalid_index, corresponding_invalid_rule_index

def correct_invalid(update):
    resp = check_valid(update)
    if isinstance(resp, bool):
        return update
    else:
        i, j = resp
        element = update.pop(j)
        update.insert(i, element)
        return correct_invalid(update)

invalid_updates = find_invalid(updates)

validated_updates = []
for invalid_update in invalid_updates:
    validated_updates.append(correct_invalid(invalid_update))

total = 0
for valid_update in validated_updates:
    total += int(valid_update[len(valid_update) // 2])

print(total)
