mkdir Umbraco.Framework
cd Umbraco.SourceFiles
mkdir images
mkdir usercontrols
mkdir xslt
mkdir _db
mkdir _media

set targetdir=../Umbraco.Framework/
set sourcedir=./

::_Media (include subfolders)
ROBOCOPY %sourcedir%_media %targetdir%media /MIR /XO /E