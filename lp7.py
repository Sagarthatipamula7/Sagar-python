list=[12,75,150,180,145,525,50]
for i in range(len(list)):
    if list[i]%5==0 and list[i]<=150:
        print(list[i])
    elif list[i]>150 and list[i]<=500:
        continue
    elif list[i]>500:
        break
    else:
        print("none of the above")