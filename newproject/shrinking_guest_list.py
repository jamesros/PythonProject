guest_list = ['Kelly', 'Josh', 'Faith']
greeting = "Dear "
invitation = "\n\n\tYou are cordially invited to a grand dinner at my house.\n\nBYOB\n"
cancellation = "\n\n\tI Regret to inform you that you are no longer invited, as I ran out of chairs."
message = greeting + guest_list[0] + "," + invitation
print(message)
message = greeting + guest_list[1] + "," + invitation
print(message)
message = greeting + guest_list[2] + "," + invitation
print(message)

print(guest_list[1] + " Cannot make it, so now I gotta make a NEW list")
guest_list.remove('Josh')
guest_list.append('Kevin')

message = greeting + guest_list[0] + "," + invitation
print(message)
message = greeting + guest_list[1] + "," + invitation
print(message)
message = greeting + guest_list[2] + "," + invitation
print(message)

print("I have found a bigger table, so Now I am inviting more People")
guest_list.insert(0, 'Justin')
guest_list.insert(2, 'Julio')
guest_list.append('Louise')

message = greeting + guest_list[0] + "," + invitation
print(message)
message = greeting + guest_list[1] + "," + invitation
print(message)
message = greeting + guest_list[2] + "," + invitation
print(message)
message = greeting + guest_list[3] + "," + invitation
print(message)
message = greeting + guest_list[4] + "," + invitation
print(message)
message = greeting + guest_list[5] + "," + invitation
print(message)

print("Turns out, I can only invite 2 people")
cxl_guest = []
cxl_guest.append(guest_list.pop(1))
cxl_guest.append(guest_list.pop(2))
cxl_guest.append(guest_list.pop(3))
cxl_guest.append(guest_list.pop(0))

message = greeting + cxl_guest[0] + "," + cancellation
print(message)
message = greeting + cxl_guest[1] + "," + cancellation
print(message)
message = greeting + cxl_guest[2] + "," + cancellation
print(message)
message = greeting + cxl_guest[3] + "," + cancellation
print(message)

message = greeting + guest_list[0] + "," + invitation
print(message)
message = greeting + guest_list[1] + "," + invitation
print(message)

del guest_list[0]
del guest_list[0]

print(guest_list)