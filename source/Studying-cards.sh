#To make this file clickable : 

#Go to your Terminal or iTerm.

#Change to directory where this file is located.

#Type the following:

    #chmod a+x (yourscriptname)

#Right click on this file and select Open with and Other.

#Enable All Applications and choose Terminal.

#NOTE: If you always want to open that file with Terminal, then check Always Open With.

#Finally, double click on your file and it should work.

###################################
#To add an icon to this file : 
#Create a .desktop file like this and put it in /usr/share/applications/ :

    #[Desktop Entry]
    #Type=Application
    #Name=XChat Firefox
    #Exec=/usr/bin/your_script
    #Icon=/usr/share/icons/xchats_icon

#"XChat Firefox" will then be a launchable application with XChat's icon. Exec can also take a bash command (with arguments, optionally) as its value.

cd #enter folder (absolute) location of main.py here
python3 main.py  