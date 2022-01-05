sample_instructions = "8-sample.TXT"
real_instructions = "8.TXT"

which_instructions = real_instructions

instruction_list = []
register_dictionary = {}


for this_line in open(which_instructions):
    this_register = this_line.split()[0]
    if this_register not in register_dictionary:
        register_dictionary[this_register] = 0
    instruction_list.append(this_line.strip())


def do_instruction(this_instruction, reg_dict):
    parsed_instruction = this_instruction.split()
    reg_to_modify = parsed_instruction[0]
    inc_or_dec = parsed_instruction[1]
    modification = int(parsed_instruction[2])
    reg_to_compare = parsed_instruction[4]
    comparison_type = parsed_instruction[5]
    comparison_number = int(parsed_instruction[6])
    inc_dec_toggle = 0

    condition_met = False

    if inc_or_dec == "inc":
        inc_dec_toggle = 1
    else:
        inc_dec_toggle = -1

    if comparison_type == "==":
        if reg_dict[reg_to_compare] == comparison_number:
            condition_met = True
    if comparison_type == "<":
        if reg_dict[reg_to_compare] < comparison_number:
            condition_met = True
    if comparison_type == ">":
        if reg_dict[reg_to_compare] > comparison_number:
            condition_met = True
    if comparison_type == "!=":
        if reg_dict[reg_to_compare] != comparison_number:
            condition_met = True
    if comparison_type == "<=":
        if reg_dict[reg_to_compare] <= comparison_number:
            condition_met = True
    if comparison_type == ">=":
        if reg_dict[reg_to_compare] >= comparison_number:
            condition_met = True

    if condition_met:
        reg_dict[reg_to_modify] += inc_dec_toggle * modification

max_value = max(register_dictionary.values())

for instruction in instruction_list:
    do_instruction(instruction, register_dictionary)
    this_max = max(register_dictionary.values())
    if this_max > max_value:
        max_value = this_max


print("Part 1: " + str(max(register_dictionary.values())))
print("Part 2: " + str(max_value))
