# Guide to using Linux 

## Commands (known as hotkeys) with Terminal:
1. CTRL+ALT+T – New Terminal window from File System
   (type "clear" to clear the terminal instance)
3. CTRL+ALT+N – New Terminal window from another window
4. CTRL+ALT+T – New Terminal tab
5. CTRL+ALT+W – Close current Terminal tab
6. CTRL+ALT+Q – Close current Terminal window

## Navigating your file system:
To investigate further just where we are in the file structure, let’s use the pwd command:
1. In your terminal type: pwd
2. Press Enter
### How to see what kind of files are in the folder:
1. In your terminal type: ls
2. Press Enter
### List the contents of a folder by typing: 
ls -hal ... You will then see only the self and parent directory listings
### To add a new directory type: 
mkdir newDir ... then ls -hal to see that new directory 

### Jump into the new directory --> "cd" command
### To create a file, type: 
touch newFile.txt
### To append something into the file, type: 
echo “Hello!” >> newFile.txt
### To verify that it worked, you will want to print it out, type: 
cat newFile.txt
### List the directory contents --> "ls"
### To delete the file, type: 
rm newFile.txt
### To delete a directory, type: 
rm -r [newDirName]
### To change directory / get out of a directory, type:
cd ... then you can list with ls

## man command
The man command provides the details of whichever command is passed into the function as an argument.
The man command will list the "name", "synopsis", "description", and further details of how the specific command can be used.

## the - (known as the 'tac') symbol
The '-' symbol allows us to combine options 

## Filtering 
When using Linux, you will often need to find or sort through listings and files on the operating system.
In general, the two most common filtering functions you will use in Linux will be sort and grep. 
Filtering commands tend to be used with the pipe "|" character. The pipe character means the output of some other function will feed the input of the filter. 

### 'sort' for example can be used to sort a file's contents in alphabetical order. (ex command: textFile.txt | sort OR cat words.txt | sort)

### 'grep' stands for “Global Regular Expression Print”. 
### While grep sounds complex, the grep command simply searches for strings and prints the results. (ex command: cat words.txt | sort | grep "alpaca")





