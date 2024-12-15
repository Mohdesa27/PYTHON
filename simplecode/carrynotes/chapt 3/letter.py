#method one
n=input("enter the name")
data=input("enter the data")
letter=("dear,"+n.capitalize()+"\nyou are selected!\n as "+data.upper())
print(letter)

#method second
letter="Dear,{0}\n you are selected !\n as {1}"
print(letter.format(n.capitalize(),data.upper()))
