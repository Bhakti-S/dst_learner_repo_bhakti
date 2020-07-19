# --------------
#Code starts here
#Function to read file
def read_file(path):
    file = open(path, 'r')
    sentence = file.readline()
    file.close()
    return sentence
sample_message = read_file(file_path)    
print (sample_message)   

#Calling the function to read file
message_1 = read_file(file_path_1)
message_2 = read_file(file_path_2)
print(message_1)
print(message_2)
#Printing the line of the file
#Function to fuse message
def fuse_msg(message_a,message_b):
    quotient = int(message_b)//int(message_a)
    #Integer division of two numbers
    return str(quotient)
    #Returning the quotient in string format
secret_msg_1 = fuse_msg(message_1,message_2)   
print(secret_msg_1) 

message_3 = read_file(file_path_3)
print(message_3)

def substitute_msg(message_c):
    if message_c == "Red":
        sub = 'Army General'
    elif message_c == "Green":    
        sub = 'Data Scientist'
    elif message_c == 'Blue':
        sub = 'Marine Biologist'  
    else:
        sub = ''    
    return sub      
    
secret_msg_2 = substitute_msg(message_3)    
message_4 = read_file(file_path_4)
message_5 = read_file(file_path_5)  
print("sm 2 ", secret_msg_2)  
print(message_4)
print(message_5)
    
def compare_msg(message_d,message_e):   
    a_list = message_d.split()
    b_list = message_e.split()
    c_list = list([char for char in a_list if char not in b_list])
    final_msg = " ".join(c_list)
    return final_msg
    
secret_msg_3 = compare_msg(message_4, message_5) 
 
#Function to filter message
message_6 = read_file(file_path_6)
print(message_6)

def extract_msg(message_f):
    a_list = message_f.split()
    print ("alist is ", a_list)
    b_list = list(filter(lambda x : len(x)%2==0, a_list))
    print ("blsit is ",b_list)
    final_msg = " ".join(b_list)
    print("final msg is ",final_msg)
    return final_msg
    #Splitting the message into a list
secret_msg_4 = extract_msg(message_6)
print(secret_msg_4)    
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]

secret_msg = " ".join(message_parts)
# define the path where you 
final_path= user_data_dir + '/secret_message.txt'

#Combine the secret message parts into a single complete secret message
#Function to write inside a file
def write_file(secret_msg,path):
    file2 = open(path, 'a+')
    file2.write(secret_msg)  
    file2.close() 
    #Opening a file named 'secret_message' in 'write' mode

write_file(secret_msg,final_path)
print(secret_msg)
    #Writing to the file


    #Closing the file


#Calling the function to write inside the file    


#Printing the entire secret message


#Code ends here


