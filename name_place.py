file=open("nameplace.txt","r")
for data in file:
    # print(data)
    if "delhi" in data:
        print(data)
        f=open("delhi.txt","a")
        write_content=f.write(data)
    elif "shimla" in data:
        d=open("simla.txt","a")
        simla_content=d.write(data)
        
    elif "shimla" not in data and "delhi" not in data:
        e=open("other.text","a")
        other_content=e.write(data)
    
