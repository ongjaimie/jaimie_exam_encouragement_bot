print("Title of program: Exam Period bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "stressed":
      feelings_list.append("stressed")
      encouragement_list.append("you can take a break and relax! You deserve it!")
      counter += 1
    if each_word == "worried":
      feelings_list.append("worried")
      encouragement_list.append("dont worry, you've got this!")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("you should take a short nap to recharge!")
      counter += 1
    if each_word == "burnt out":
      feelings_list.append("burnt out")
      encouragement_list.append("take a break, don't worry")
      counter += 1
      if each_word == "depressed":
      feelings_list.append("depressed")
      encouragement_list.append("don't feel too sad! study hard and you'll do just fine!")
      counter += 1
      if each_word == "confident":
      feelings_list.append("confident")
      encouragement_list.append("that's great! good luck for your exams!")
      counter += 1

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
