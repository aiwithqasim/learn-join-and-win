def id_card(sid, name, fname, course, time):
    print(
        """
    --->SAYLANI<---
    student id : {}
    student name : {}
    student father name : {}
    course : {}
    time : {}""".format(sid, name,fname, course,time)
    )

l1 = [0,'Faizan', 'ahmed', '033', 'AI&ML']
id_card(*l1) #starik out all the values onne by one we call the lsit in function.
#===========================================================================
def add(name,fname,*z):
    print(name)
    print(fname)
    print(sum(z))
add('Faizan', 'Ahmed', 2,3,4,5,6,7)