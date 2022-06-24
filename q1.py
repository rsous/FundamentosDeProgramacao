def sortNums(userInput):
  allNums = []

  if userInput:
    while userInput:
      arr = userInput.split(" ")
      for i in range(len(arr)):
        arr[i] = float(arr[i])
      arr.sort()
      for i in arr:
        allNums.append(i)
      print(f'Menor: {arr[0]} Maior: {arr[-1]}')
      userInput = input()
    average(allNums)
    
  else:
    print('Nenhum número foi lido. Portanto, não existe média!')

def average(nums):
  total = 0
  for i in nums:
    total += i
  total = total / len(nums)
  print(f'Quantidade de Números Lidos: {len(nums)}')
  print(f'Média dos Números Lidos: {total:.2f}')      

sortNums(input())