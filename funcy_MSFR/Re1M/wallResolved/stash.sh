if [ -d $1 ]; then
   echo "Folder $1/ already exists, stashing aborted!"
else
   case=msfr
   mkdir $1
   mv "$case"0.*  $1
   mv logfile $case.log.* $1
   cp $case.par  SIZE $case.usr $1
fi

