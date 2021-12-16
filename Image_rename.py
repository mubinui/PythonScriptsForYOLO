
import os

# Function to rename multiple files
def main():
   i = 61
   path = "D:/Datasets/Rock_Dataset_New/Sedimentary_Sandstone/"
   for filename in os.listdir(path):
      my_dest ="rock" + str(i) + ".jpg"
      my_source =path + filename
      my_dest =path + my_dest

      os.rename(my_source, my_dest)
      i += 1
# Driver Code
if __name__ == '__main__':
   # Calling main() function
   main()