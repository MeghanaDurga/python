#palindrome
st=input("enter a string:")
space=st.replace(" " ," ").lower()
if space==space[::-1]:
    print("palindrome")
else:
    print("not palindrome")
