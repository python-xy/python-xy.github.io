# -*- coding: utf-8 -*-

import os, os.path as osp

GOOGLE_CODE_FILES = "http://pythonxy.googlecode.com/files/"
SF_FILES = "https://sourceforge.net/projects/python-xy/files/plugins/"
DOWNLOAD_ICON = "http://www.gstatic.com/codesite/ph/images/dl_arrow.gif"

def is_wiki_name(name):
    """Return True is *name* is a Wiki name"""
    import string
    if name[0] in string.lowercase:
        return False
    up = True
    count = 0
    for index in range(len(name))[1:]:
        if name[index] in string.uppercase:
            if up:
                return False
            else:
                up = True
                count += 1
        elif up:
            up = False
    else:
        return count > 0
        
def ignore_wiki_name(name):
    if is_wiki_name(name):
        return "!"+name
    else:
        return name

def convert_size(size):
    for char in size[:]:
        if not char.isdigit():
            size = size.replace(char, '')
    unit = "KB"
    size = float(size)/1024
    if size > 1024*2:
        unit = "MB"
        size /= 1024
    if size:
        return "%d %s" % (size, unit)
    else:
        return "-"

PYTHON_MODS = set()

class XYModule(object):
    def __init__(self, lines):
        self.name = None
        self.version = None
        self.comment = None
        self.comment_fr = None
        self.url = None
        self.size = None
        self.internal_name = None
        self.dependencies = None
        self.recommended = None
        
        if len(lines) == 9:
            (self.name, self.version, self.comment_fr, self.comment, self.url,
             self.internal_name, recommended, size, dependencies) = lines
            self.recommended = recommended == "1 2"
            self.size = convert_size(size)
#            print self.name, ':', self.size
        else:
            (self.name, self.version, self.comment_fr, self.comment, self.url,
             self.internal_name, dependencies) = lines
        if dependencies == '-':
            self.dependencies = []
        else:
            self.dependencies = dependencies.replace(" ", "").split(",")
            
    def get_dl_link(self, suffix):
        global PYTHON_MODS
        if suffix:
            PYTHON_MODS.add(self.internal_name)
        if self.name == "Python":
            return ""
        strf = (SF_FILES, self.internal_name, self.version, suffix)
        return "%s%s-%s%s.exe" % strf


def get_contents(fname):
    return file(fname).read().decode('iso8859-1').encode('utf-8')
    
def get_modules(fname):
    contents = get_contents(fname)
    return [ XYModule(text.strip().splitlines())
             for text in contents.split('%')[1:] ]


def make_plugin_list(title, source, lang=None, suffix="_py27"):
    global PYTHON_MODS
    if title:
        wiki = "\n=== %s ===\n\n" % title
    else:
        wiki = ""
    for mod in get_modules(source):
        is_python = "python" in source or mod.internal_name in PYTHON_MODS
        l_suffix = suffix if is_python else ""
        link = mod.get_dl_link(l_suffix)
        if link:
            link = "[%s %s]" % (link, DOWNLOAD_ICON)
        if lang == "fr":
            comment = mod.comment_fr
            dep_str = "Dépendances :"
        else:
            comment = mod.comment
            dep_str = "Dependencies:"
        if mod.dependencies:
            dep = [ignore_wiki_name(_d) for _d in mod.dependencies]
            comment = "%s<br>_%s %s_" % (comment, dep_str, ", ".join(dep))
        strf = (mod.url, mod.name, mod.version, link, comment)
        wiki += "|| [%s %s] || %s || %s || %s ||\n" % strf
    return wiki


def create_header(summary):
    return """#summary %s.
#labels Featured
#sidebar TOC

""" % summary


def make_standard_plugin_pages():
    text = """%s
== Installation notes ==

Plugins available on this page are already included in Python(x,y) *%s* Full Edition. 

All these plugins are available outside of the main installer program for the following reasons:
  * each Python(x,y) plugin is compatible with a standard Python installation (i.e. you may install them on top of any Python installation, even without installing Python(x,y) - this is not the recommended way though, because the individual plugins do not handle dependencies)
  * customize your Python(x,y) installation (note: silent install is supported):
    * download the Python(x,y) installation
    * download the missing packages on this page (Python(x,y) plugins) or download any other Python modules: distutils (.exe) files and setuptools Python eggs (.egg) files are supported
    * copy all these installers in a subdirectory named "plugins" that you have created in the same folder as the Python(x,y) installer program
    * execute the Python(x,y) installer, then you will see on the bottom of the component list that a section called "Plugins" is available: tick this section to install automatically all the packages that you have previously copied in "plugins" subdirectory
  * custom update of Python(x,y):
    * update anytime some of the installed plugins by downloading the new versions available on this page (note: the plugins are updated more frequently than the distribution)
    * from time to time, upgrade your distribution with the update patches available on the download page (i.e. updating individual plugins does not interfere with the distribution update patches)

== Plugins ==
""" % (create_header("Python(x,y) standard plugins "
                     "(Python plugins and other)"),
       get_current_version())
    text += make_plugin_list("Python packages", "p_python.txt")
    text += make_plugin_list("Other packages", "p_other.txt")
    with open('../StandardPlugins.wiki', 'wb') as wikifile:
        wikifile.write(text)
    
    text_fr = """%s
== Notes d'installation ==

Toutes les extensions disponibles sur cette page sont incluses dans l'édition complète de Python(x,y) *%s*. 

Ces extensions sont proposées indépendamment de l'installeur principal pour les raisons suivantes :
  * chacune d'entre-elles est compatible avec une installation standard de Python (i.e. sans avoir préalablement installé Python(x,y) - auquel cas il est important de noter que les dépendances ne sont pas gérées par les installeurs individuels des extensions) ;
  * personnalisation de l'installation de Python(x,y) (méthode compatible avec une installation silencieuse) :
    * téléchargez l'édition de Python(x,y) (Custom, Light, Basic ou Full) qui correspond le mieux à votre besoin, même si certains modules sont manquants ;
    * téléchargez les modules manquants sous la forme d'extensions Python(x,y) - officielles ou développées par des tiers, de modules Python distutils (.exe) ou encore d'oeufs Python (.egg) ;
    * copiez tous ces installeurs dans un sous-répertoire nommé "plugins" que vous placerez dans le même dossier que l'installeur de Python(x,y) ;
    * exécutez l'installeur de Python(x,y), vous verrez qu'une section appelée "Plugins" est disponible dans la liste des composants : cocher ce composant permettra d'installer automatiquement tous les modules que vous avez copié dans le sous-répertoire "plugins" ;
  * mise à jour à la carte de Python(x,y) :
    * mettez à jour les extensions de votre choix en téléchargeant les nouvelles versions disponibles sur cette page (remarque : les extensions sont mises à jour plus fréquemment que la distribution) ;
    * de temps en temps, mettez à jour votre distribution avec les mises à jour disponibles sur la page de téléchargement (i.e. avoir mis à jour chaque extension n'interfère pas avec les mises à jour de la distribution).

== Extensions ==
""" % (create_header("Composants standard de Python(x,y) "
                     "(extensions Python et autres)"),
       get_current_version())
    text_fr += make_plugin_list("Extensions Python", "p_python.txt", lang="fr")
    text_fr += make_plugin_list("Autres extensions", "p_other.txt", lang="fr")
    with open('../fr/StandardPlugins.wiki', 'wb') as wikifile:
        wikifile.write(text_fr)


def make_additional_plugin_pages():
    text = """%s
== Installation notes ==

Plugins available on this page are *not* included in _Python(x,y)_ distributions. 

Note that each _Python(x,y)_ plugin is compatible with a standard Python 
installation (i.e. you may install them on top of any Python installation, 
even without installing _Python(x,y)_).

== Additional Plugins ==
""" % create_header("Python(x,y) additional plugins "
                    "(Python plugins and other)")
    text += make_plugin_list("Python packages", "p_add_python.txt")
    text += make_plugin_list("Other packages", "p_add_other.txt")    
    with open('../AdditionalPlugins.wiki', 'wb') as wikifile:
        wikifile.write(text)
    
    text_fr = """%s
== Notes d'installation ==

Les extensions disponibles sur cette page *ne sont pas* incluses dans les 
distributions _Python(x,y)_. 

Notez que chacune de ces extensions est compatible avec une installation 
standard de Python (i.e. sans avoir préalablement installé Python(x,y) - 
auquel cas il est important de noter que les dépendances ne sont pas gérées 
par les installeurs individuels des composants).

== Extensions ==
""" % create_header("Composants additionnels de Python(x,y) "
                    "(extensions Python et autres)")
    text_fr += make_plugin_list("Extensions Python", "p_add_python.txt", lang="fr")
    text_fr += make_plugin_list("Autres extensions", "p_add_other.txt", lang="fr")
    
    with open('../fr/AdditionalPlugins.wiki', 'wb') as wikifile:
        wikifile.write(text_fr)


def get_current_version(path=None):
    if path is None:
        path = os.getcwdu()
    contents = get_contents(osp.join(path, "changes.txt"))
    for text in contents.split('%'):
        lines = text.strip().splitlines()
        if lines:
            return lines[3]            

def get_top_version(path=None, changes="changes.txt"):
    if path is None:
        path = os.getcwdu()
    contents = get_contents(osp.join(path, changes))
    for text in contents.split('%'):
        lines = text.strip().splitlines()
        if lines:
            return lines[3]            

def make_changelog(path=None, lang=None, changes="changes.txt" ):
    if path is None:
        path = os.getcwdu()
    contents = get_contents(osp.join(path, changes))
    changes = "\n"
    for text in contents.split('%'):
        lines = text.strip().splitlines()
        # if changes != "changes.txt":
            # print lines
        if lines:
            yr = lines[0]
            mth = lines[1]
            day = lines[2]
            ver = lines[3]            
            if lang == "fr":
                changes += "=== Version %s (%s/%s/%s) ===\n" % (ver, day, mth, yr)
            else:
                changes += "=== Version %s (%s/%s/%s) ===\n" % (ver, mth, day, yr)
            chg = lines[4:]
            french = True
            skip = False
            for line in chg:
                if line.startswith('~'):
                    skip = False
                    if line[1] == "C":
                        if lang == "fr":
                            changes += "==== Correctifs ====\n"
                        else:
                            changes += "==== Fixed ====\n"
                    elif line[1] == "A":
                        if lang == "fr":
                            changes += "==== Ajouts ====\n"
                        else:
                            changes += "==== Added ====\n"
                    elif line[1] == "U":
                        if lang == "fr":
                            changes += "==== Mises à jour ====\n"
                        else:
                            changes += "==== Updated ====\n"
                    elif line[1] == "R":
                        if lang == "fr":
                            changes += "==== Removed ====\n"
                        else:
                            changes += "==== Removed ====\n"
                    elif line[1] == "L":
                        skip = True
                    continue
                elif skip == True:
                    continue
                elif lang == "fr":
                    if french:
                        changes += "  * %s\n" % line
                else:
                    if not french:
                        changes += "  * %s\n" % line
                french = not french
    return changes


def make_update_list(path=None, lang=None):
    if path is None:
        path = os.getcwdu()
    contents = get_contents(osp.join(path, "updates.txt"))
    if lang == "fr":
        updates = "\n|| *Installeur* || *Taille* || *Version requise* ||\n"
    else:
        updates = "\n|| *Installer* || *Size* || *Required version* ||\n"
    for text in contents.split('%')[1:]:
        name, ver, size = text.strip().splitlines()
        link = GOOGLE_CODE_FILES + name
        updates += "|| [%s %s] || %s || %s ||\n" % (link, name,
                                                    convert_size(size), ver)
    return updates


def make_download_list(path=None, lang=None):
    version = get_current_version(path)
    win = "Windows XP/Vista/7"
    ntua_mirror = "http://ftp.ntua.gr/pub/devel/pythonxy/"
    ntua_website = "http://www.ntua.gr/index_en.html"
    cmv_mirror = "http://pythonxy.connectmv.com/"
    cmv_website = "http://www.connectmv.com"
    kent_mirror = "http://www.mirrorservice.org/sites/pythonxy.com/"
    kent_website = "http://www.cs.kent.ac.uk/"
    if lang == "fr":
        dlist = "\n|| *Lien(s)* || *Site* ||\n"
    else:
        dlist = "\n|| *Link(s)* || *Location* ||\n"
    fname = "Python(x,y)-%s.exe" % version
    if lang == "fr":
        full_edition = "Complète"
        mirror1 = "[%s Mirroir] - fourni par [%s NTUA]" % (ntua_mirror,
                                                             ntua_website)
        mirror2 = "[%s Mirroir] - fourni par [%s ConnectMV]" % (cmv_mirror,
                                                             cmv_website)
        mirror3 = "[%s Mirroir] - fourni par [%s Université de Kent]" % (kent_mirror,
                                                             kent_website)
    else:
        full_edition = "Full"
        mirror1 = "[%s Mirror] - provided by [%s NTUA]" % (ntua_mirror,
                                                             ntua_website)
        mirror2 = "[%s Mirror] - provided by [%s ConnectMV]" % (cmv_mirror,
                                                             cmv_website)
        mirror3 = "[%s Mirror] - provided by [%s University of Kent]" % (kent_mirror,
                                                             kent_website)


    # GoogleCode links:
    # ----------------
    # Python(x,y)-2.7.2.0.zip, Python(x,y)-2.7.2.0.z01, ...
    # links = " ".join(["[%sPython(x,y)-%s.%s Part %d]"
                      # % (SF_FILES, version,
                         # "zip" if index == 1 else "z%02d" % (index-1), index)
                      # for index in range(1, 4)])
    # dlist += "|| %s || %s || %s || %s ||\n" % (win, full_edition,
                                               # '!GoogleCode', links)

    # DropBox link:
    # ---------
#    dropbox_dl_path = "https://www.dropbox.com/sh/tjzhpr7oowlv60o/uuNnG_sLF1/"
#    dlist += "|| %s || [%s %s] ||\n" % ( mirror3, dropbox_dl_path+fname, fname)
    
    # NTUA link:
    # ---------
    mirror_line_format = "|| [{1} {2}] || {0} ||\n"
    dlist += mirror_line_format.format(mirror1, ntua_mirror+fname, fname)

    # University of Kent link:
    # -----------------------
    dlist += mirror_line_format.format(mirror3, kent_mirror+fname, fname)

    # ConnectMV link:
    # --------------
    dlist += mirror_line_format.format(mirror2, cmv_mirror+fname, fname)

    return dlist


def make_download_pages():
    text = """%s
== Current release ==
Python(x,y) current version is *%s* ([License]):
%s

== Installation notes ==
  * It is recommended to uninstall any other Python distribution before installing Python(x,y)
  * You may update your Python(x,y) installation via individual package installers which are updated more frequently -- see the plugins page
  * Please use the Issues page to request new features or report unknown bugs
  * Python(x,y) can be easily extended with other Python libraries because Python(x,y) is compatible with all Python modules installers: distutils installers (.exe), Python eggs (.egg), and all other NSIS (.exe) or MSI (.msi) setups which were built for Python 2.7 official distribution - see the plugins page for customizing options
  * Another Python(x,y) exclusive feature: *all packages are optional* (i.e. install only what you need)
  * Basemap users (data plotting on map projections): please see the AdditionalPlugins

== Updates ==

The following installers will help you keep your Python(x,y) installation up-to-date: only installed plugin will be updated according to the change log.
%s

== Unstable release ==
Python(x,y) latest unstable release is *%s*

%s

== Plugin updates ==

The following plugins will certainly be included in Python(x,y) next release:
(maybe they are already included in current release and this page hasn't been refreshed yet, please check on standard plugins page)
%s

== Changes history ==
%s
""" % (create_header("Download page with changelog"),
       get_current_version(),
       make_download_list(),
       make_update_list(),
       get_top_version( changes='changes_beta.txt' ),
       make_changelog( changes='changes_beta.txt' ),
       make_plugin_list(None, "p_next.txt"),
       make_changelog())
    with open('../Downloads.wiki', 'wb') as wikifile:
        wikifile.write(text)

    '''
    [http://ftp.ntua.gr/pub/devel/pythonxy/beta/Python(x,y)-2.7.3.0-b1.exe Mirror1 - NTUA]
    [http://www.mirrorservice.org/sites/pythonxy.com/beta/Python(x,y)-2.7.3.0-b1.exe Mirror2 - University of Kent]
    '''
    
    text_fr = """%s
== Version actuelle ==
La version actuelle de Python(x,y) est la version *%s* ([License]) :
%s

== Notes d'installation ==
  * Nous recommandons de désinstaller toute autre distribution Python avant d'installer Python(x,y)
  * Merci d'utiliser la page Issues pour suggérer une nouvelle fonctionnalité ou signaler une anomalie inconnue
  * Vous pouvez facilement personnaliser Python(x,y) avec des bibliothèques de votre choix car Python(x,y) est compatible avec tous les installeurs de modules Python: installeurs distutils (.exe), oeufs Python (.egg), et tous les autres installeurs NSIS (.exe) ou MSI (.msi) qui ont été conçus pour la distribution officielle de Python 2.7 - voir la page des extensions pour plus d'informations sur la personnalisation de l'installation
  * Vous pouvez mettre à jour votre version de Python(x,y) :
    * soit via les installeurs individuelles des modules qui vous intéressent dont les versions les plus récentes sont sur la page des extensions
  * Encore une fonctionnalité exclusive de Python(x,y) : tous les composants inclus sont optionnels (n'installez que ce dont vous avez besoin)
  * Utilisateurs de Basemap (affichage de données cartographiques) : merci de visiter la page AdditionalPlugins

== Mises à jour ==

Les installeurs ci-dessous permettent de mettre à jour votre installation de Python(x,y) : seuls les composants que vous avez choisi lors de l'installation de Python(x,y) seront mis à jour.
%s

== Unstable release ==
Python(x,y) latest unstable release is *%s*
%s

== Mises à jour des extensions ==

Les composants suivants seront probablement inclus dans une version future de Python(x,y) : 
(peut-être sont-ils déjà inclus dans la version actuelle, merci de vérifier sur la page des composants standard)
%s

== Historique des changements ==
%s
""" % (create_header("Téléchargement et historique"),
       get_current_version(),
       make_download_list(lang="fr"),
       make_update_list(lang="fr"),
       get_top_version( changes='changes_beta.txt' ),
       make_changelog( lang="fr",changes='changes_beta.txt' ),
       make_plugin_list(None, "p_next.txt", lang="fr"),
       make_changelog(lang="fr"))
    with open('../fr/Downloads.wiki', 'wb') as wikifile:
        wikifile.write(text_fr)


if __name__ == "__main__":
    make_standard_plugin_pages()
    make_additional_plugin_pages()
    make_download_pages()
