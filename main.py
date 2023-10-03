person1BusySchedule = []
person1WorkHours = []
person2BusySchedule = []
person2WorkHours = []
meetingDurationPersons1and2 = None
person3BusySchedule = []
person3WorkHours = []
person4BusySchedule = []
person4WorkHours = []
meetingDurationPersons3and4 = None
person5BusySchedule = []
person5WorkHours = []
person6BusySchedule = []
person6WorkHours = []
meetingDurationPersons5and6 = None
person7BusySchedule = []
person7WorkHours = []
person8BusySchedule = []
person8WorkHours = []
meetingDurationPersons7and8 = None
person9BusySchedule = []
person9WorkHours = []
person10BusySchedule = []
person10WorkHours = []
meetingDurationPersons9and10 = None
person11BusySchedule = []
person11WorkHours = []
person12BusySchedule = []
person12WorkHours = []
meetingDurationPersons11and12 = None
person13BusySchedule = []
person13WorkHours = []
person14BusySchedule = []
person14WorkHours = []
meetingDurationPersons13and14 = None
person15BusySchedule = []
person15WorkHours = []
person16BusySchedule = []
person16WorkHours = []
meetingDurationPersons15and16 = None
person17BusySchedule = []
person17WorkHours = []
person18BusySchedule = []
person18WorkHours = []
meetingDurationPersons17and18 = None
person19BusySchedule = []
person19WorkHours = []
person20BusySchedule = []
person20WorkHours = []
meetingDurationPersons19and20 = None

with open('Input.txt', 'r') as file:
	lines = file.readlines()
	person1BusySchedule = eval(lines[0])
	person1WorkHours = eval(lines[1])
	person2BusySchedule = eval(lines[2])
	person2WorkHours = eval(lines[3])
	meetingDurationPersons1and2 = int(lines[4])
	
	person3BusySchedule = eval(lines[6])
	person3WorkHours = eval(lines[7])
	person4BusySchedule = eval(lines[8])
	person4WorkHours = eval(lines[9])
	meetingDurationPersons3and4 = int(lines[10])

	person5BusySchedule = eval(lines[12])
	person5WorkHours = eval(lines[13])
	person6BusySchedule = eval(lines[14])
	person6WorkHours = eval(lines[15])
	meetingDurationPersons5and6 = int(lines[16])

	person7BusySchedule = eval(lines[18])
	person7WorkHours = eval(lines[19])
	person8BusySchedule = eval(lines[20])
	person8WorkHours = eval(lines[21])
	meetingDurationPersons7and8 = int(lines[22])

	person9BusySchedule = eval(lines[24])
	person9WorkHours = eval(lines[25])
	person10WorkHoursBusySchedule = eval(lines[26])
	person10WorkHours = eval(lines[27])
	meetingDurationPersons9and10 = int(lines[28])

	person11BusySchedule = eval(lines[30])
	person11WorkHours = eval(lines[31])
	person12BusySchedule = eval(lines[32])
	person12WorkHours = eval(lines[33])
	meetingDurationPersons11and12 = int(lines[34])

	person13BusySchedule = eval(lines[36])
	person13WorkHours = eval(lines[37])
	person14BusySchedule = eval(lines[38])
	person14WorkHours = eval(lines[39])
	meetingDurationPersons13and14 = int(lines[40])

	person15BusySchedule = eval(lines[42])
	person15WorkHours = eval(lines[43])
	person16BusySchedule = eval(lines[44])
	person16WorkHours = eval(lines[45])
	meetingDurationPersons15and16 = int(lines[46])

	person17BusySchedule = eval(lines[48])
	person17WorkHours = eval(lines[49])
	person18BusySchedule = eval(lines[50])
	person18WorkHours = eval(lines[51])
	meetingDurationPersons17and18 = int(lines[52])

	person19BusySchedule = eval(lines[54])
	person19WorkHours = eval(lines[55])
	person20BusySchedule = eval(lines[56])
	person20WorkHours = eval(lines[57])
	meetingDurationPersons19and20 = int(lines[58])


def TimeToMinutes(time_str):
  hours, minutes = map(int, time_str.split(':'))
  return hours * 60 + minutes


def MinutesToTime(minutes):
  return f"{minutes // 60:02d}:{minutes % 60:02d}"


def AvailableTimeSlots(busy_schedule, work_hours):
  slots = []
  current_time = work_hours[0]
  for start, end in busy_schedule:
    if current_time < start:
      slots.append((current_time, start))
    current_time = max(current_time, end)
  if current_time < work_hours[1]:
    slots.append((current_time, work_hours[1]))
  return slots


def AvailableTimeSlotsInCommon(slots1, slots2, duration):
  common = []
  i, j = 0, 0
  while i < len(slots1) and j < len(slots2):
    start = max(slots1[i][0], slots2[j][0])
    end = min(slots1[i][1], slots2[j][1])
    if end - start >= duration:
      common.append((start, end))
    if slots1[i][1] < slots2[j][1]:
      i += 1
    else:
      j += 1
  return common


# Convert to minutes
person1BusySchedule = [(TimeToMinutes(start), TimeToMinutes(end))
                       for start, end in person1BusySchedule]
person1WorkHours = [
    TimeToMinutes(person1WorkHours[0]),
    TimeToMinutes(person1WorkHours[1])
]
person2BusySchedule = [(TimeToMinutes(start), TimeToMinutes(end))
                       for start, end in person2BusySchedule]
person2WorkHours = [
    TimeToMinutes(person2WorkHours[0]),
    TimeToMinutes(person2WorkHours[1])
]

person3BusySchedule = [(TimeToMinutes(start), TimeToMinutes(end))
                       for start, end in person3BusySchedule]
person3WorkHours = [
    TimeToMinutes(person3WorkHours[0]),
    TimeToMinutes(person3WorkHours[1])
]
person4BusySchedule = [(TimeToMinutes(start), TimeToMinutes(end))
                       for start, end in person4BusySchedule]
person4WorkHours = [
    TimeToMinutes(person4WorkHours[0]),
    TimeToMinutes(person4WorkHours[1])
]

person5BusySchedule = [(TimeToMinutes(start), TimeToMinutes(end))
                       for start, end in person5BusySchedule]
person5WorkHours = [
    TimeToMinutes(person5WorkHours[0]),
    TimeToMinutes(person5WorkHours[1])
]
person6BusySchedule = [(TimeToMinutes(start), TimeToMinutes(end))
                       for start, end in person6BusySchedule]
person6WorkHours = [
    TimeToMinutes(person6WorkHours[0]),
    TimeToMinutes(person6WorkHours[1])
]

person7BusySchedule = [(TimeToMinutes(start), TimeToMinutes(end))
                       for start, end in person7BusySchedule]
person7WorkHours = [
    TimeToMinutes(person7WorkHours[0]),
    TimeToMinutes(person7WorkHours[1])
]
person8BusySchedule = [(TimeToMinutes(start), TimeToMinutes(end))
                       for start, end in person8BusySchedule]
person8WorkHours = [
    TimeToMinutes(person8WorkHours[0]),
    TimeToMinutes(person8WorkHours[1])
]

person9BusySchedule = [(TimeToMinutes(start), TimeToMinutes(end))
                       for start, end in person9BusySchedule]
person9WorkHours = [
    TimeToMinutes(person9WorkHours[0]),
    TimeToMinutes(person9WorkHours[1])
]
person10BusySchedule = [(TimeToMinutes(start), TimeToMinutes(end))
                       for start, end in person10BusySchedule]
person10WorkHours = [
    TimeToMinutes(person10WorkHours[0]),
    TimeToMinutes(person10WorkHours[1])
]

person11BusySchedule = [(TimeToMinutes(start), TimeToMinutes(end))
                       for start, end in person11BusySchedule]
person11WorkHours = [
    TimeToMinutes(person11WorkHours[0]),
    TimeToMinutes(person11WorkHours[1])
]
person12BusySchedule = [(TimeToMinutes(start), TimeToMinutes(end))
                       for start, end in person12BusySchedule]
person12WorkHours = [
    TimeToMinutes(person12WorkHours[0]),
    TimeToMinutes(person12WorkHours[1])
]

person13BusySchedule = [(TimeToMinutes(start), TimeToMinutes(end))
                       for start, end in person13BusySchedule]
person13WorkHours = [
    TimeToMinutes(person13WorkHours[0]),
    TimeToMinutes(person13WorkHours[1])
]
person14BusySchedule = [(TimeToMinutes(start), TimeToMinutes(end))
                       for start, end in person14BusySchedule]
person14WorkHours = [
    TimeToMinutes(person14WorkHours[0]),
    TimeToMinutes(person14WorkHours[1])
]

person15BusySchedule = [(TimeToMinutes(start), TimeToMinutes(end))
                       for start, end in person15BusySchedule]
person15WorkHours = [
    TimeToMinutes(person15WorkHours[0]),
    TimeToMinutes(person15WorkHours[1])
]
person16BusySchedule = [(TimeToMinutes(start), TimeToMinutes(end))
                       for start, end in person16BusySchedule]
person16WorkHours = [
    TimeToMinutes(person16WorkHours[0]),
    TimeToMinutes(person16WorkHours[1])
]

person17BusySchedule = [(TimeToMinutes(start), TimeToMinutes(end))
                       for start, end in person17BusySchedule]
person17WorkHours = [
    TimeToMinutes(person17WorkHours[0]),
    TimeToMinutes(person17WorkHours[1])
]
person18BusySchedule = [(TimeToMinutes(start), TimeToMinutes(end))
                       for start, end in person18BusySchedule]
person18WorkHours = [
    TimeToMinutes(person18WorkHours[0]),
    TimeToMinutes(person18WorkHours[1])
]

person19BusySchedule = [(TimeToMinutes(start), TimeToMinutes(end))
                       for start, end in person19BusySchedule]
person19WorkHours = [
    TimeToMinutes(person19WorkHours[0]),
    TimeToMinutes(person19WorkHours[1])
]
person20BusySchedule = [(TimeToMinutes(start), TimeToMinutes(end))
                       for start, end in person20BusySchedule]
person20WorkHours = [
    TimeToMinutes(person20WorkHours[0]),
    TimeToMinutes(person20WorkHours[1])
]

# Find available slots	
person1_available = AvailableTimeSlots(person1BusySchedule, person1WorkHours)
person2_available = AvailableTimeSlots(person2BusySchedule, person2WorkHours)
person3_available = AvailableTimeSlots(person3BusySchedule, person3WorkHours)
person4_available = AvailableTimeSlots(person4BusySchedule, person4WorkHours)
person5_available = AvailableTimeSlots(person5BusySchedule, person5WorkHours)
person6_available = AvailableTimeSlots(person6BusySchedule, person6WorkHours)
person7_available = AvailableTimeSlots(person7BusySchedule, person7WorkHours)
person8_available = AvailableTimeSlots(person8BusySchedule, person8WorkHours)
person9_available = AvailableTimeSlots(person9BusySchedule, person9WorkHours)
person10_available = AvailableTimeSlots(person10BusySchedule, person10WorkHours)
person11_available = AvailableTimeSlots(person11BusySchedule, person11WorkHours)
person12_available = AvailableTimeSlots(person12BusySchedule, person12WorkHours)
person13_available = AvailableTimeSlots(person13BusySchedule, person13WorkHours)
person14_available = AvailableTimeSlots(person14BusySchedule, person14WorkHours)
person15_available = AvailableTimeSlots(person15BusySchedule, person15WorkHours)
person16_available = AvailableTimeSlots(person16BusySchedule, person16WorkHours)
person17_available = AvailableTimeSlots(person17BusySchedule, person17WorkHours)
person18_available = AvailableTimeSlots(person18BusySchedule, person18WorkHours)
person19_available = AvailableTimeSlots(person19BusySchedule, person19WorkHours)
person20_available = AvailableTimeSlots(person20BusySchedule, person20WorkHours)

combined = []

# Find common available slots
common_available1 = AvailableTimeSlotsInCommon(person1_available,
																						person2_available,
																						meetingDurationPersons1and2)
# Convert back to time strings
common_available1 = [(MinutesToTime(start), MinutesToTime(end))
										for start, end in common_available1]
combined.append(common_available1)


common_available2 = AvailableTimeSlotsInCommon(person3_available,
																						person4_available,
																						meetingDurationPersons3and4)
# Convert back to time strings
common_available2 = [(MinutesToTime(start), MinutesToTime(end))
										for start, end in common_available2]
combined.append(common_available2)


common_available3 = AvailableTimeSlotsInCommon(person5_available,
																						person6_available,
																						meetingDurationPersons5and6)
# Convert back to time strings
common_available3 = [(MinutesToTime(start), MinutesToTime(end))
										for start, end in common_available3]
combined.append(common_available3)


common_available4 = AvailableTimeSlotsInCommon(person7_available,
																						person8_available,
																						meetingDurationPersons7and8)
# Convert back to time strings
common_available4 = [(MinutesToTime(start), MinutesToTime(end))
										for start, end in common_available4]
combined.append(common_available4)


common_available5 = AvailableTimeSlotsInCommon(person9_available,
																						person10_available,
																						meetingDurationPersons9and10)
# Convert back to time strings
common_available5 = [(MinutesToTime(start), MinutesToTime(end))
										for start, end in common_available5]
combined.append(common_available5)


common_available6 = AvailableTimeSlotsInCommon(person11_available,
																						person12_available,
																						meetingDurationPersons11and12)
# Convert back to time strings
common_available6 = [(MinutesToTime(start), MinutesToTime(end))
										for start, end in common_available6]
combined.append(common_available6)


common_available7 = AvailableTimeSlotsInCommon(person13_available,
																						person14_available,
																						meetingDurationPersons13and14)
# Convert back to time strings
common_available7 = [(MinutesToTime(start), MinutesToTime(end))
										for start, end in common_available7]
combined.append(common_available7)


common_available8 = AvailableTimeSlotsInCommon(person15_available,
																						person16_available,
																						meetingDurationPersons15and16)
# Convert back to time strings
common_available8 = [(MinutesToTime(start), MinutesToTime(end))
										for start, end in common_available8]
combined.append(common_available8)


common_available9 = AvailableTimeSlotsInCommon(person17_available,
																						person18_available,
																						meetingDurationPersons17and18)
# Convert back to time strings
common_available9 = [(MinutesToTime(start), MinutesToTime(end))
										for start, end in common_available9]
combined.append(common_available9)


common_available10 = AvailableTimeSlotsInCommon(person19_available,
																						person20_available,
																						meetingDurationPersons19and20)
# Convert back to time strings
common_available10 = [(MinutesToTime(start), MinutesToTime(end))
										for start, end in common_available10]
combined.append(common_available10)


with open('Output.txt', 'w') as output_file:
	output_file.write("These are the available time slots in common for persons 1 and 2: " + 
										str(common_available1) + "\n")
	output_file.write("These are the available time slots in common for persons 3 and 4: " + 
										str(common_available2) + "\n")
	output_file.write("These are the available time slots in common for persons 5 and 6: " + 
										str(common_available3) + "\n")
	output_file.write("These are the available time slots in common for persons 7 and 8: " + 
										str(common_available4) + "\n")
	output_file.write("These are the available time slots in common for persons 9 and 10: " + 
										str(common_available5) + "\n")
	output_file.write("These are the available time slots in common for persons 11 and 12: " + 
										str(common_available6) + "\n")
	output_file.write("These are the available time slots in common for persons 13 and 14: " + 
										str(common_available7) + "\n")
	output_file.write("These are the available time slots in common for persons 15 and 16: " + 
										str(common_available8) + "\n")
	output_file.write("These are the available time slots in common for persons 17 and 18: " + 
										str(common_available9) + "\n")
	output_file.write("These are the available time slots in common for persons 19 and 20: " + 
										str(common_available10) + "\n")