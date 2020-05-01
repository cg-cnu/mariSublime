<p align="center">
  <img src="https://user-images.githubusercontent.com/2767425/80055943-2313a280-8562-11ea-874f-5060dcbe45a0.png" height="100px"/>
  <h1 align="center">Mari Sublime</h1>
  <h4 align="center">Send code to mari from Sublime Text using command port</h4>
  <br>
</p>

_Sublime 2 & 3 compatible_

## Installation

### PackageControl

- In Sublime Text, _ctrl+shit+p_ > _Package Control: Install Package_
- Search for _Mari_

### Manual

- Download the zip file, extract the archive and rename the folder to
  `mariSublime`.
- In sublime _ctrl+shift+p_ > _Browse Packages_.
- Place the extracted `mariSublime` folder in the `packages` folder.

## Setup

### Enable Command Port in mari

- Use `mari.app.enableCommandPort( not ( mari.app.commandPortEnabled() ) )` to
  toggle command port in mari
- You should see a plug icon
  ![CommandPort
icon](https://user-images.githubusercontent.com/2767425/80058701-22323f00-8569-11ea-9da2-43586931d9e2.png)
  enabled in the lower left corner.

### In sublime

- Select a code snippet and press "ctrl+enter". Selected snippet will be executed in Mari.
- _ctrl+enter_ with out selection will execute the whole file.

## Acknowledgements

- https://github.com/justinfx/MayaSublime
- https://github.com/svenfraeys/SublimeBlender

### Issue/Feedback

log them in the [github
issues](https://github.com/cg-cnu/vscode-codetags/issues) or hit me on
[twitter](https://twitter.com/CgCnu).

### Like it?

:star: this repo.
