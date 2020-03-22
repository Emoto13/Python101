import os
import sys
   
def reduce_file_path(file_path): 
    while "//" in file_path:
        file_path = file_path.replace("//", "/")

    if '../' in file_path:
        file_path = file_path[0 : file_path.index('../')]
        n = len(file_path) - 2
        

        while n >= 0:
            if file_path[n] == "/":
                break
            n -= 1

        if n >= 0:    
            file_path = file_path[0:n + 1]    

    file_path = file_path.replace("./", "")


    if len(file_path) > 1 and file_path[-1] == "/":
        file_path = file_path[0:len(file_path) - 1]
        

    print(file_path)

def main():
    reduce_file_path("/")
    reduce_file_path("/srv/../")
    reduce_file_path("/srv/www/htdocs/wtf/")
    reduce_file_path("/srv/www/htdocs/wtf")
    reduce_file_path("/srv/./././././")
    reduce_file_path("/etc//wtf/")
    reduce_file_path("/etc/../etc/../etc/../")
    reduce_file_path("//////////////")
    reduce_file_path("/../../")
    reduce_file_path("/etc////0ssfa////wtf/")


if __name__ == '__main__':
    main()