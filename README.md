# Mari Sublime #
Execute selected code snippets or the whole .py file from sublime in mari.

<br> Sublime 2 & 3 compatible

## Installation ##
<br> Download the zip file, extract the archive and rename the folder to mariSublime.
<br> In sublime go to Preferences > Browse Packages.
<br> Place the extracted folder in the sublime packages folder.

## Enable Command Port in mari ##
<br> User this command to toggle command port in mari
<br> mari.app.enableCommandPort( not ( mari.app.commandPortEnabled() ) )
<br> you will see a plug icon enabled in the lower left corner.   ![CommadPort](/../master/examples/CommandPort.16x16.png?raw=true "CommandPort icon")

## Usage ##
* Select a code snippet and press ctrl + m. 
* Only the selected snippet will be executed in mari.
* Deselect everything and press ctrl + m.
* The whole file will be executed in mari. 

## Acknowledgements ##
<br> https://github.com/justinfx/MayaSublime
<br> https://github.com/svenfraeys/SublimeBlender
<br> http://net.tutsplus.com/tutorials/python-tutorials/how-to-create-a-sublime-text-2-plugin/

## Updates ##
<br> seperated logic in a module to use as a library
