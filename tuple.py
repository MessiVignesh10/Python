staff = ("Mala","Mathi","lakshmi")
(English,*Maths)=staff
maths = (2,3,4,5,6,7,5,4,3,2,3,4,5,5,5,6,7,3,5)
print(English)
print(Maths)
print(len(staff))
print(type(staff))
print(maths.count(5))
print(maths.count(3))

if (maths.count(3)>maths.count(5)):
    print("3 is the no which is printed most no of times")

else:
    print("5 is the no which is mostly used")