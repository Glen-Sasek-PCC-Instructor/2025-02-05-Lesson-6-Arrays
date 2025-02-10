#reads colors from the user and appends to a list
#until the user presses the Enter key.
def main():
  colors = []
  #notice how we read one time outside the loop
  #check and then enter the loop
  aColor = input("Enter a color: ")
  while (aColor != ''):
    colors.append(aColor)
    aColor = input("Enter a color: ")

  print('')
  print('')
  index = 0;
  while(index < len(colors) - 1):
    print(colors[index], ", ", sep = '', end = '')
    index = index + 1
  else:
    print("and ", colors[index], ".", sep = '')

#call main
main()