::##############################################################
::MADE BY ENOME!
::This file can be used to deploy your sourcecode to an Umbraco instance
::USE AT OWN RISK /MIR will delete files to keep both folders in sync

::ROBOCOPY INFO
::/xo - exclude file if the destination already exists and is newer.
::/S : Copy Subfolders.
::/E : Copy Subfolders, including Empty Subfolders.
::/MIR : MIRror a directory tree - equivalent to /PURGE plus all subfolders (/E)
::##############################################################

set targetdir=../Umbraco.Framework/
set sourcedir=./

::BIN
ROBOCOPY %sourcedir%bin %targetdir%bin /XO

::CSS (include subfolders)
ROBOCOPY %sourcedir%css %targetdir%css /MIR /XO /E

::IMAGES (include subfolders)
ROBOCOPY %sourcedir%images %targetdir%images /MIR /XO /E

::PYTHON (include subfolders)
ROBOCOPY %sourcedir%python %targetdir%python /MIR /XO /E

::SCRIPTS (include subfolders)
ROBOCOPY %sourcedir%scripts %targetdir%scripts /MIR /XO /E

::MASTERPAGES
ROBOCOPY %sourcedir%masterpages %targetdir%masterpages *.master /MIR /XO

::USERCONTROLS (should only copy the *.ascx files)
ROBOCOPY %sourcedir%usercontrols %targetdir%usercontrols *.ascx /MIR /XO

::XSLT
ROBOCOPY %sourcedir%xslt %targetdir%xslt /MIR /XO