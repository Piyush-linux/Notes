### Linux Command
## file manipulation


---

<content> __>__ <file> : to store the content in taht file
__which__ <program> : return path of program
__pwd__ : Current path
__clear__ : Clear view of terminal
__exit__ : exit current session
__-v__ : Display process

__ls__ => To list sub-directory
	-a : hidden files
	-l : long format
	-t : sort modify time
	-S : list in size
	-d : list dir
	-<dir>
	-*.ext : extensin
	-al : Nested

__cd__ => To change directory
	-path/dir1
	--.. : get back
	-~ : Home dir
	-/ : Root dir
	-"space name"

__mkdir__=> Make dir
	-dir_name : dir name
	--p dir1/dir2/ : inside dir
	-{dir1,dir2,dir3} : multiple dir

__cat__ <opt> -/- <dir> => To Display & Manipulate content
	-<file> > <file> : to copy & paste from one file to another
	-<file> >> <file> : To append content 
	-b : add number
	-h : add number to all
	-S : sequeze blank line
	-E : To show end of line

__rmdir__ <dir> => To delete dir
	-dir1/dir2 : delete bottom once
	--p dir1/dir2 : Delete completly

__rm__ <file/dir> => To remove file/dir
	-r : Remove recursively
	-f1 f2 : Remove multiple

__cp__ => To copy file
	-<f1>-<f2/dir> : copy from one to another
	-<f1-f2>-<dir> : copy multiple file
	-R <dir>-<dir> : copy from one dir to another
	-i : override if file name is same

__mv__ => move or rename file
	-<f1>-<f2> : rename that file
	-<f1>-<dir> : move from one to other dir

__less__ <file> => Display large File
	-`space` -> next pg / `G` -> last pg /`g` -> First pg
	-`/txt` -> search txt / `n` -> next / `b` -> back
	-q : to quit session

__touch__ <file.ext> => make file
	-f1 f2 : Create multiple file

__nano__ <file> => Text Editor
	 	-o : write out (file_naming)
	 	-x : Exit editor
	 	-<f> : To edit 

__sudo__ => Super-User-Do
	-s : Get into root user

__top__ => Real-Time view
	-i : working process || PID : process

__kill__ => Kill process
	-pid <program> : Kill process
	-ps -ux : list of running program pid
	-ps -aux : list of all program pid
	-ps -c <progarm> : no. of instance

__echo__<string> => Display whats written
	-var=value : echo $var

__chmod__









