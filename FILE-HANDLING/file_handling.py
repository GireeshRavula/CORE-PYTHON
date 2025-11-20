# name = input("Enter a Name:")
# ptr = open("Gireesh.txt",'w')
# ptr.write(name)
# ptr.close()


# => To add new data to existing data without deleting :


name = input("Enter a Name:")
ptr = open("Gireesh.txt",'a')
ptr.write(name)
ptr.close()

