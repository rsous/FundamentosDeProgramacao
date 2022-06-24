def getNames(num):
  output = ''
  for i in range(num):
    temp = input()
    temp = temp.split(" ")
    output += f'{temp[0]} {temp[-1]}\n'
  print(output)

getNames(int(input()))