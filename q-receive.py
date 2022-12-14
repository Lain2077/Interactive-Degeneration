#DATA RECEPTION + TRANSLATED // PROOF OF CONCEPT

with open("RESULTATS.txt") as file:
    lines = file.readlines()

prompt = ""


def Q(line_num):
    return(lines[line_num - 1])

#QUESTION 1
Q1 = Q(1)

Q1A = (int(Q1) - 1) * 10 + 1

prompt += " Deforestation [" + str(Q1A) + "%],"
  
    
#QUESTION 2

Q2 = Q(2)

Q2A = (int(Q2) - 1) * 10 + 1

prompt += " Heavy clouds [" + str(Q2A) + "%],"
   
   
#QUESTION 3

Q3 = Q(3)

Q3A = (int(Q3) - 1) * 10 + 1

prompt += " Dry [" + str(Q3A) + "%],"
  
  
print("Alter this image with the help of these datas. Ignore data without concerned elements in the image:" + prompt)