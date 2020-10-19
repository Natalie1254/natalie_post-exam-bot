# natalie_post-exam-bot
print("Title of program: Activities to try")
print()
print("Please answer the following questions truthfully and we'll suggest an activity for you!")
print("Please respond with a number 1 - 5, where 1 is strongly disagree and 5 is strongly agree.")
print()

skill1 = input("I have a sense of rhythm.")

outdoor1 = input("I'll go crazy if I do not go out of the house for the whole day.")

game1 = input("I enjoy competitive acivities.")

skill2 = input("I have good coordination.")

outdoor2 = input("I enjoy physical activities.")

game2 = input("I enjoy being in the virtual world")


skill_final = int(skill1) + int(skill2)
outdoor_final = int(outdoor1) + int(outdoor2)
game_final = int(game1)+ int(game2)

print()

if skill_final > outdoor_final and skill_final > game_final:
  print("You might want to learn dance !")
elif outdoor_final > music_final:
  print("You might want to engage in sports with others!")
else:
  print("You might want to try a new online game!")

  
