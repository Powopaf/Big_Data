    #!/bin/bash
    wget $@ 2>&1 | tee /dev/stderr | sed -u "s/^ *[0-9]*K[ .]*\([0-9]*%\) *\([0-9,]*[A-Z]\) *\([0-9a-z]*\).*/\1\n#Téléchargement ... \3 restant à \2\/s/" | zenity --title="Wget Gui" --text="Connexion..." --progress --auto-close --auto-kill 2> /dev/null
    echo


