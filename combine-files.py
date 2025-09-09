# to run:
# open terminal and navigate to directory containing combine-files.py
# be sure file_1.txt, file_2.txt, and output.txt (or any named text files) are in the same directory as combine-files.py
# run this command below:
# python combine-files.py file_1.txt file_2.txt output.txt
# feel free to alter the sums to test different cases
import argparse

# create Argument Parser object
parser = argparse.ArgumentParser()
parser.add_argument("file_1")
parser.add_argument("file_2")
parser.add_argument("output_file")

# save arguments to object args
args = parser.parse_args()

print(f"1: {args.file_1} 2: {args.file_2} 3: {args.output_file}")

# variable that will store contents of first file
file_1 = []

# append contents of first file into list
with open(args.file_1) as file:
  while line := file.readline():
    file_1.append(int(line))

# variable that will store contents of second file
file_2 = []

# append contents of second file into list
with open(args.file_2) as file:
  while line := file.readline():
    file_2.append(int(line))

# variable that will store result list
result = []

# if sum of file_1 is larger than sum of file_2
if(sum(file_1) > sum(file_2)):
  # set result to combined list with second file in front of first file
  result =  file_2 + file_1
  # print("case 1, file 1 sum is bigger than file 2")
else:
  # set result to combined list with first file in front of second file
  result = file_1 + file_2
  # print("case 2, file 2 sum is bigger than file 2")

# write result as list of strings seperated by '\n' to file
with open(args.output_file, "w") as file:
  file.write("\n".join(list(map(str, result))))
