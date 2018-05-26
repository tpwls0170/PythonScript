import Job

print("============ Main =============")
print("1. 회사명")
print("2. 직종")
print("3. 지역")
print("4. 학력")
print("==============================")
number = eval(input("selete menu : "))

if(number == 1):
    Job.ConnectServer(1)
if(number == 2):
    Job.ConnectServer(2)
if(number == 3):
    Job.ConnectServer(3)
if(number == 4):
    Job.ConnectServer(4)
