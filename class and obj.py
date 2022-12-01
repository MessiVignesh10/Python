class cse :
    def add_name(self,start,end,middle):
       return start + end + middle

name = cse()
name.start = "Messi"
name.end = "Vignesh"
name.middle = "none"
print(name.add_name(name.start,name.end,name.middle))

name = cse()
name.start = "Lionel"
name.end = "Saravanan"
name.middle = "none"
print(name.add_name(name.start,name.end,name.middle))
