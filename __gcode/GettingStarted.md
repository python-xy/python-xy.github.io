## Where to begin?

As a beginner, if I could buy only two books on Python, I would buy these two
(and, if I could buy only one, it would certainly be the second one because it
has a very well written introduction on Python language):
  * “[Python, Essential Reference](http://www.amazon.com/Python-Essential-Reference-Developers-Library/dp/0672328623)”, David M. Beazley, Ed.: Sams Publishing, ISBN-13: 978-0-672-32862-6 ;
  * “[Rapid GUI Programming with Python and Qt](http://www.qtrac.eu/pyqtbook.html)”, Mark Summerfield, Ed.: Prentice Hall, ISBN-13: 978-0-13-235418-9.

However, if you are interested in a scientific-oriented complete reference
with a lot of examples, I would strongly recommend this one:

> “[Python Scripting for Computational Science](http://www.springer.com/math/cse/book/978-3-540-73915-9)”, Hans Petter Langtangen, Ed.: Springer, ISBN-13: 978-3-540-73915-9.

See the [bibliography](Bibliography.md) page for more references.

Of course, it is possible to learn Python without buying anything: Python(x,y)
includes almost all freely available documentations, online books, examples and
tutorials that I could gather on the internet (please do not hesitate to
contact me if you wish to include your own findings).


## IDLE

For your first lines in Python, you won’t need any sophisticated IDE.
IDLE (**Figure 1**), that is the Python IDE written by Python creator himself
(Guido van Rossum), is powerful enough to edit and run short scripts. It also
provides a Python interpreter to run interactively your code (**Figure 2**).

Note that when one is used to MATLAB's IDE for example, IDLE may seems too much limited/simple in comparison. But that is its purpose: to provide a simple but efficient IDE to begin with Python programming language. If you are looking for something more powerful but easy-to-use as well, please go directly to next paragraph for a detailed description of the IDE that will probably fit all your needs (except write your programs), **Spyder**.

_**Figure 1** : IDLE editor window_<br>
<img src='http://pythonxy.googlecode.com/files/idle_editor.png' />

<i><b>Figure 2</b> : IDLE shell window</i><br>
<img src='http://pythonxy.googlecode.com/files/idle_shell.png' />

To begin with, you may run and then edit <i>matplotlib</i> examples in Python(x,y)<br>
documentation (Libraries\matplotlib\examples).<br>
<br>
<br>
<h2>Spyder</h2>

<a href='http://spyderlib.googlecode.com'><img src='http://spyderlib.googlecode.com/files/banner.png' /></a>

Since 2009, a new scientific development environment for Python is available. Inspired from MATLAB's IDE, Spyder is intended to facilitate a migration from MATLAB to Python as it provides essential features for scientific users like the variable explorer (analog to MATLAB's "Workspace") or data import wizard.<br>
<br>
<img src='http://wiki.spyderlib.googlecode.com/hg/Front_Page/screenshot.png' />

So, <a href='http://spyderlib.googlecode.com/'>Spyder</a> is a powerful scientific IDE providing the following<br>
features:<br>
<ul><li>interactive console with:<br>
<ul><li>code completion, brace matching, help (or function arguments) tips, ...<br>
</li><li>global variables browser with GUI-based editors for arrays, lists, dictionaries, and so on<br>
</li><li>import features: from text files, MATLAB files, ...<br>
</li></ul></li><li>external console: executed in a separate process, this console may be used to run application safely (with almost all the interactive console features cited above)<br>
</li><li>editor:<br>
<ul><li>code completion, syntax coloring, code folding, automatic indentation<br>
</li><li>real-time code analysis: pyflakes (integrated) and pylint (plugin)<br>
</li><li>vertical/horizontal separation<br>
</li><li>class/function browser<br>
</li></ul></li><li>find in files feature<br>
</li><li>file explorer<br>
</li><li>object inspector<br>
</li><li>online help browser on installed Python modules (since v1.1.0)<br>
</li><li>project manager/explorer (since v1.1.0)</li></ul>

For more details and screenshots, please visit the <a href='http://spyderlib.googlecode.com/'>Spyder</a> website.<br>
<br>
<br>
<h2>IPython</h2>

For rapid prototyping, one can test simple commands or run scripts<br>
interactively using the powerful features of IPython (<b>Figure 3</b>), an enhanced<br>
Python shell in which – for example – <i>matplotlib</i> features are available<br>
through the <i>pylab</i> interface which offers a syntax very close to MATLAB’s.<br>
<br>
<i><b>Figure 3</b> : Python(x,y) interactive console (IPython with Console 2.0)</i><br>
<img src='http://pythonxy.googlecode.com/files/ipython_pxy_profile.png' />

IPython with <i>matplotlib</i>, <i>numpy</i> and <i>Scipy</i> support can be executed<br>
from its start menu entry (“Python-Matplotlib console”) or from any file<br>
folder by right-clicking on it (“Open Python console here…”), see <b>Figure 4</b>.<br>
<br>
<i><b>Figure 4</b> : Python console integration in Windows Explorer</i><br>
<img src='http://pythonxy.googlecode.com/files/open_python_console_here.png' />

Learn more on this topics in Python(x,y) documentation :<br>
“Using matplotlib interactively” (Library\matplotlib).