st=input("Enter your words: ")
def revers(st):
    st=st.split()
    st.reverse()
    return " ".join(st)
print(revers(st))   
    