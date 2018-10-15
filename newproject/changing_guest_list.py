guest_list = ['Kelly', 'Josh', 'Faith']
greeting = "Dear "
invitation = "\n\n\tYou are cordially invited to a grand dinner at my house.\n\nBYOB\n"
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

