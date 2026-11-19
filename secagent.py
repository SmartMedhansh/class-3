# Part 1: Ask the Agent for thier Details
name = input("Enter your real name Agent: ")
gadget = input("Enter your favourite gadget: ")

# Part 2: Store the agent details, using different data types
agent_number = 7
speed_rating = 9.5
mission_count = 12
height_m = 1.65
is_active = True

# Part 3: print each detail with its data type

print("Name: ", name, "-> type:", type(name))
print("gadget:", gadget, "-> type:", type(gadget))
print("agent_number:", agent_number, "->type:", type(agent_number))
print("speed_rating:", speed_rating, "->type:", type(speed_rating))
print("height_m", height_m, "->type:", type(height_m))
print("is_active:", is_active, "->type:", type(is_active))

#Part 4: Typecaste the numbers and true/false value into text

agent_number_text = str(agent_number)
mission_count_text = str(mission_count)
speed_rating_text = str(speed_rating)
status_text = str(is_active)

# Part 5: Slice the name to create a secret code name
frist_three = name[0:3]
last_letter = name[-1:]
code_name = frist_three + last_letter
print("Frist 3 letters of name:, frist_three")
print("Last letter of name:", last_letter)
print("Secret Code Name:", code_name)

# Part 6: Reverse the gadget name using slicing
reversed_gadget = gadget[::-1]
print("Reversed Gadget Name:", reversed_gadget)

# Part 7: Join everything together to build the final badge
badge_line_1 = "AGENT" + code_name.upper()
badge_line_2 = "ID" + agent_number_text + " | MISSION: " + mission_count_text
badge_line_3 = "SPEED: " + speed_rating_text + " | ACTIVE: " + status_text
bagde_line_4 = "SECRET GADGET CODE" + reversed_gadget.upper()

#Part 8: Print the complete secret agent badge
print("")
print("===== SECRET AGENT BADGE =====")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(bagde_line_4)
print("==============================")