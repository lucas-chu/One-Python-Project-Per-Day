"""To-do list where you can chronologically add your tasks, modify them and mark if they have been completed.
  A cleanup feature enables you to delete completed tasks which are more than a week old - unless
  you have flagged them as 'protected'."""

import datetime
import os
#make a list to hold to new items
shopping_list = []

def show_help():
  print("\nSeperate each item with a comma.")
  print("Type DONE to quit, SHOW to see the current list, and HELP to get this message")

def show_list():
  count = 1
  for item in shopping_list:
    print("{}: {}".format(count, item))
    count += 1

print("Give me a list of things you want to shop for.")
show_help()

while True:
    new_stuff = input("> ")

    if new_stuff == "DONE":
        print("\nHere's your list:")
        break
    elif new_stuff == "HELP":
        show_help()
        continue
    elif new_stuff == "SHOW":
        show_list()
        continue
    else:
        new_list = new_stuff.split(",")
        index = input("Add this at a certain spot? Press enter for the end of the list, "
                      "or give me a number. Currently {} items in the list.".format(len(shopping_list)))
    if index:
        spot = int(index) - 1
        for item in new_list:
            shopping_list.insert(spot, item.strip())
            spot += 1
    else:
        for item in new_list:
            shopping_list.append(item.strip())

