# Introduction

This guide details the steps needed to setup a Python(x, y) build environment and creating/updating packages.

# Building Python(x, y) from source

  1. Clone the Mercurial repository.
  1. Install latest AutoIt version - http://www.autoitscript.com/site/autoit/downloads .
  1. Install [NSIS ANSI 2.46.4](http://unsis.googlecode.com/files/nsis-2.46.4-Unicode-setup.exe).
  1. Download the official 32bit Python Distribution supported by Python(x, y) - currently 2.7.2: http://www.python.org/ftp/python/2.7.2/python-2.7.2.msi and place it under `%PXYSRC%\bin\python` (create the missing directories manually).
  1. Execute `%PXYSRC%\src\Python(x,y)\Build_All.au3` and build all packages. This takes a long time.
  1. The Python(x, y) distribution is found under `%PXYSRC%\bin`.

# Building Individual Packages

# Adding New Packages

# Install Templates Guide

## Adding Environment Variables

`$XY.RegistryRootKey` holds the target registry hierarchy - HKLM for all users or HKCU for the current user. It should used for updating environment variables (PATH or other package specific ).
for example, under the `Installer Sections`
```NSIS

!define XY_ENABLE_ENVIRONMENT_VARIABLE_MANIPULATION
!insertmacro xyDefs


;---------------------
; customization start

${XYAddToPath} "$INSTDIR"
${EnvVarUpdate} $0 "VTK_DATA_ROOT" "A" $XY.RegistryRootKey "$ReqPath\VTKData"

;------------------
; customization end
```
Followed by matching entries under the `Uninstaller Section`:

```NSIS

Section "Uninstall"

!insertmacro xy_sec_uninstall_pre

;---------------------
; customization start

# get the contents of our variables
ReadEnvStr $0 VTK_DATA_ROOT
${un.EnvVarUpdate} $0 "VTK_DATA_ROOT" "R" $XY.RegistryRootKey "$0"
${un.XYDeleteFromPath} "$INSTDIR"

!insertmacro xy_sec_uninstall_post

```

## Adding File Associations

```NSIS

!define XY_ENABLE_ENVIRONMENT_VARIABLE_MANIPULATION
!insertmacro xyDefs

Section "!${ID}" SecXY
...
;---------------------
; customization start

${registerExtension} "$ReqPath\Lib\site-packages\PyQt4\designer.exe" ".ui" "QtDesigner File"
${registerExtension} "$ReqPath\Lib\site-packages\PyQt4\linguist.exe" ".ts" "QtLinguist File"

...

Section "-Cleanup" SecCleanUp

${RefreshShellIcons}

SectionEnd

...

Section "Uninstall"

;---------------------
; customization start

${unregisterExtension} ".ui" "QtDesigner File"
${unregisterExtension} ".ts" "QtLinguist File"

${RefreshShellIcons}
```

## Adding Start Menu Entries
```NSIS


Section "-Cleanup" SecCleanUp

${XYCreateStartEntry} "Veusz.lnk" "$ReqPath\Scripts\veusz.exe" "" \
"$INSTDIR\veusz.ico" "" "" "" "" "$ReqPath\Scripts"

SectionEnd

...

Section "Uninstall"

!insertmacro xy_sec_uninstall_post

...
${XYDeleteStartEntry} "Veusz.lnk"
...
!insertmacro xy_sec_uninstall_pre

SectionEnd

```