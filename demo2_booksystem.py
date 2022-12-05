# example txt file
# <index> <bookname> <bookid> <Borrowed/NotBorrowed> <borrower name> <borrower id> <expected return time>

filename = "book_record.txt"
encoding="utf-8"

def search_book():
    name = input("Input searched book name:")
    file = open(filename,"r",encoding=encoding)
    read_data_all = []
    count = len(file.readlines())
    file.seek(0,0)
    for i in range(count):
        read_data = file.readline().strip('\n').split()
        read_data_all.append(read_data)
    for read_data in read_data_all:
        if(name==read_data[1]):
            if len(read_data)<7:
                print("Book Info：[",read_data[0]+","+read_data[1]+","+read_data[2]+","+read_data[3]+","+"''"+","+"''"+","+"'']")
    file.close()

def add_book():
    file = open(filename,"r+",encoding=encoding)
    print("Input added book info:")
    id = input("id:")
    bookname=input("bookname:")
    author=input("author:")
    
    read_data_all = []
    count = len(file.readlines())
    file.seek(0,0)
    for i in range(count):
        read_data = file.readline().strip('\n').split('\t')
        read_data_all.append(read_data)
    file.close()
    file = open(filename,"w+",encoding=encoding)
    for read_data in read_data_all:
        file.write("\t".join(read_data)+"\n")# avoid to cover already checked book
    file.write(id+"\t"+bookname+"\t"+author+"\t"+"NotBorrowed"+"\t"+"\t"+"\t"+"\n")
    print('Done!')
    file.close()


def borrow_book():
    file = open(filename,"r+",encoding=encoding)
    name = input("Input borrowed book name:")
    read_data_all = []
    count = len(file.readlines())
    file.seek(0,0)
    for i in range(count):
        read_data = file.readline().strip('\n').split()
        read_data_all.append(read_data)
    for read_data in read_data_all:
        if len(read_data)<7:
            read_data.append("")
            read_data.append("")
            read_data.append("")
            read_data.append("")
        if(name==read_data[1]):
            if read_data[3] == "Borrowed":
                print("borrower name:" + read_data[4])
                print("borrower id:" + read_data[5])
                print("expected return time:" + read_data[6])
            else:
                read_data[3] = "Borrowed"
                read_data[4] = input("borrower name:")
                read_data[5] = input("borrower id:")
                read_data[6] = input("expected return time:")
            break
    else:
        print("No book info!")
    file.close()
    file = open(filename,"w+",encoding=encoding)
    for read_data in read_data_all:
        if len(read_data)<7:
            read_data.append("")
            read_data.append("")
            read_data.append("")
            read_data.append("")
        file.write(read_data[0] + "\t" + read_data[1] + "\t" + read_data[2]+ "\t" + read_data[3]+ "\t" + read_data[4]+ "\t" + read_data[5]+ "\t" + read_data[6]+"\n")
    file.close()

def return_book():
    file = open(filename,"r+",encoding=encoding)
    name = input("Input returned book name:")
    read_data_all = []
    count = len(file.readlines())
    file.seek(0,0)
    for i in range(count):
        read_data = file.readline().strip('\n').split('\t')
        read_data_all.append(read_data)
    for read_data in read_data_all:
        if len(read_data)<7:
            read_data.append("")
            read_data.append("")
            read_data.append("")
            read_data.append("")
        if(name==read_data[1]):
            read_data[3] = "Not borrowed"
            read_data[4] = ""
            read_data[5] = ""
            read_data[6] = ""
            print("Done!")
            break
        else:
            print("No book info")
    file.close()
    file = open(filename,"w+",encoding=encoding)
    for read_data in read_data_all:
        file.write(read_data[0] + "\t" + read_data[1] + "\t" + read_data[2]+ "\t" + read_data[3]+"\n")
    file.close()

def search_borrower():
    name = input("Input borrower name:")
    file = open(filename,"r",encoding=encoding)
    read_data_all = []
    borrow_book_all = []
    count = len(file.readlines())
    file.seek(0,0)
    for i in range(count):
        read_data = file.readline().strip('\n').split('\t')
        read_data_all.append(read_data)
    for read_data in read_data_all:
        if len(read_data)<7:
            read_data.append("")
            read_data.append("")
            read_data.append("")
            read_data.append("")
        if(name==read_data[4]):
            borrow_book_all.append(read_data)
    file.close()
    if len(borrow_book_all) == 0:
        print("No borrowed record")
    else:
        print("borrower has borrowed "+str(len(borrow_book_all))+" books, book names are: ")
        for item in borrow_book_all:
            print(item[1])
if True:
    while(1):
        print("******Book borrow system****")
        print("******1.add books******")
        print("******2.search books******")
        print("******3.borrow books**********")
        print("******4.return books******")
        print("******5.search borrower**********")
        print("******6.exit**********")
        op = input("input index to choose :")
        if(op == "1"):
            add_book()
        elif(op == "2"):
            search_book()
        elif(op == "3"):
            borrow_book()
        elif(op == "4"):
            return_book()
        elif(op == "5"):
            search_borrower()
        else:
            break
