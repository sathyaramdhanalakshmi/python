def display(data):
    print(f"the area is {data}")
    
def get_input():
    received_length=input("length: ")
    received_width=input("width: ")
        
    return (received_length,received_width)
    
def compute_area(length,width):
    area=int(length)*int(width)
    return area
    
def main():
    (length,width)=get_input()
    area=compute_area(length,width)
    display(area)
    
main()