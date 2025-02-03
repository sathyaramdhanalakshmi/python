def take_input():
    str=input("enter a string: ")
    return str
def string_analysis(str):
    vowels="aeiouAEIOU"
    digits="0123456789"
    cntvowels=0
    cntconso=0
    cntdigits=0
    cntspecialchar=0
    for char in str:
        if char in vowels:
            cntvowels+=1
        elif char in digits:
            cntdigits+=1
        elif char.isalpha():
            cntconso+=1
        else:
            cntspecialchar+=1
            
    reversedstring= str[::-1]
    
    return(cntvowels,cntconso,cntdigits,cntspecialchar,reversedstring)
           
def display(v,c,d,s,r):
    print(f"no of vowels: {v} \n no of consonents: {c} \n no of digits: {d} \n no.of special charecters: {s} \n reversed string is {r}") 
    
def main():
    str=take_input()
    vowelcnt,consonentcnt,digitscnt,specialcharcnt,reversedstring=string_analysis(str)
    
    display(vowelcnt,consonentcnt,digitscnt,specialcharcnt,reversedstring)
main()
    
    
    