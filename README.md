# Setter Generation for List items in included service code

1. Clone the file [AddingListSertter.py](http://192.168.4.55/sunkuet02/Utilities/blob/master/AddingListSetter.py)
2. Run it. 
3. Insert the path of the generated-sources you want to generate the setters.
4. Click on the `Generate List Setter` Button to generate the setters.

`Please don't give the path to your source code. This may change your source code.`


# Migration of repository from svn to git

1. Create a file users.txt where all authorized users whose data needs to face. if not possible then run : 
    ````bash
	svn log --xml | grep author | sort -u | perl -pe 's/.*>(.*?)<.*/$1 = /' | tee users.txt
	````
	The file should be like : 
	````bash
	alsun = alsun <sun@tigerit.com>
	username = FullName <name@email.com>
    ````    

2. Then fetch file link of subversion: 
    ````bash
	git svn clone --stdlayout --no-metadata --authors-file=users.txt http://192.168.1.173/path-to-repo/
	````
	you may get few warnings if you didn't put the correct url. You don't need to give trunk folder path or branch folder path.
	
3. Go to the cloned folder : 
    ````bash
    cd your-repo
	````
4. If project is huge then run the below command multiple times : 
    ````bash
	git svn fetch
	````
5. Then add the remote URL of git by using : 
    ````bash
	git remote add origin git@192.168.4.55:user/group/remote-repo.git
	````
6. Then push the repo to upstream(e.g. gitlab) using 
    ````bash
	git push origin master
	````
7. Then see the changes to the remote. 
