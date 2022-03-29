# Do not modify this list
phone_list = ["98-777-653", "98-742-644", "34-855-326", "34-25-629", "34-489-115", "72-999-563", "9-321-459",
              "72-654-121", "72-4-694", "72-255-313", "98-111-323", "98-433-14", "34-577-342", "98-323-000",
              "98-202-666", "34-5435-454", "34-515-633"]

ugly_phone_list = ["98-333-111", "12--323-566", "123-34-221", "99-948-321", "-12-123-346",
                     "894-58438-543", "85-234-222",
                     "12-333-444-", "99-888--433", "15-465-876", "98-555-22", "-3-355-333", "3--344-53", "--2--45---",
                     "11-111-222", "12#22$34$222", "98 223 555"]
phone_list1 = []
phone_list2 = []
for item in phone_list:
    if len(item) == 10:
        phone_list1.append(item)
    else:
        phone_list2.append(item)
print("These are the valid phone numbers in your phonebook:" + str(phone_list1))
print("and these are the wrong ones:" + str(phone_list2))

area_codes = []
for item in phone_list1:
    area_codes.append(item[0]+item[1])
print("The area codes:" + str(area_codes))

phone_list3 = []
for i in phone_list1:
    phone_list3.append(i[2:])
print("and the numbers without the area codes:" + str(phone_list3))

unic_areacodes = []
for i in area_codes:
    if i not in unic_areacodes:
        unic_areacodes.append(i)
print("The unique area codes:" + str(unic_areacodes))

countx = sum(1 for i in phone_list1 if "98" in i)
print("Phone numbers for area code 98: " + str(countx))

county = sum(1 for i in phone_list1 if '34' in i)
print("Phone numbers for area code 34: " + str(county))

countz = sum(1 for i in phone_list1 if '72' in i)
print("Phone numbers for area code 72: " + str(countz))






# "These are the valid phone numbers in your phonebook:"
# "and these are the wrong ones:"


# "The area codes:"
# "and the numbers without the area codes:"


# "The unique area codes:"


# "You have X numbers from area 98, Y numbers from area 34, and Z numbers from area 72."


# "These are the pretty phone numbers:"
# "and these are the ugly ones:"
