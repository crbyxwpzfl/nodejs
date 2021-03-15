# personal portable homebridge v1.1.7
#### start-homebridge
```powershell
cd $env:DESKTOP; node.exe .\nodejs\node_modules\homebridge\bin\homebridge homebridge -D -U .\nodejs\homebridge-dir
```
#### setup
add __DESKTOP__ environment variable<br/>
add __%DESKTOP%\path\to\nodejs-folder__ to PATH variable<br>
add __IP__, __USR__, __PW__ environment variable for ambilight.py<br/>
add __PLINK__ environment variable for bigSUR.py<br/>

#### nodejs portable
get binary zip from [nodejs](https://nodejs.org/en/download/)<br>
extract to folder<br>
make file .npmrc<br>
```
cache=cache-dir
prefix=
```
check everithing works and check dirs are correct with<br>
```
node -v
npm -v
npm config list
```

#### update npm
```
npm install npm@latest
```
when ERR run again but drag files causing the ERR out the dir while install is running

#### gerneral npm
```
npm list :list install packages in current dir
npm outdated :list outdated packages
npm uninstall :uninstall a package
npm install :install a package
npm update :to update outdated packages
```

# [homebridge source](https://github.com/homebridge/homebridge/)
# [cmd4 source](https://github.com/ztalbot2000/homebridge-cmd4)
# [ffmpeg source](https://github.com/Sunoo/homebridge-camera-ffmpeg)















