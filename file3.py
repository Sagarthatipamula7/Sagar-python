def counting_even():
    with open("practice.txt","r")as f:
        data=f.read()

    new_data=data.split(",")
    count=1
    for value in new_data:
        if(int(value)%2==0):
            count+=1
        
    print(count)

counting_even()