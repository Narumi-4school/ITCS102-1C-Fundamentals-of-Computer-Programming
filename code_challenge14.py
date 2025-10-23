anime_list = [ ]

arayko = True
while arayko == True:
    a_list = input("Enter an anime (or type \"exit\" to stop): ")

    if a_list == "Exit":
        print("You have exited the anime entry program")
        break
    else:
        anime_list.append(a_list)
        continue
print("Here is the list of animes you typed: ")
for a in anime_list:
    print(f"-{a}")