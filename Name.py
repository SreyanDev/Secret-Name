try:
    name = input("Enter your name: ")


    def huh(name):

        x=name[-1:] + name[2:]
        y=f"gffgd{x + name[-1:-3] +name[9:13]+ name[-2:3] + name[1:-3]}rjskd"
        print(y)

    huh(name)

    debug = input("Type yes for debugging: ")

    if debug.lower()=="yes":
        print(name)

except:
    print("Enter only characters!")
