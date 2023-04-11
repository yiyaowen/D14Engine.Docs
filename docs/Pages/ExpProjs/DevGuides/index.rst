Developer Guides
================

Prerequisite
------------

D14UIKit is developed with `Visual Studio`_ toolchain, these necessary workloads should be installed with Visual Studio Installer before getting started (community version is enough):

* C++ wrapper: **C++ Desktop Development** (compiler, linker and SDK etc.)
* Python wrapper: **Python Development** and *Python native development tools*.

For more information about the mixed-programming of C++ and Python in Visual Studio, please see this article from MSDN: `Write C++ extensions for Python in Visual Studio`_.

To make D14UIKit a wrapper of UIKit @ D14Engine, these basic techniques are used:

* C++ wrapper: `pimpl idiom`_, used to minimize coupling and separate interfaces.
* Python wrapper: `pybind11`_, used to export C++ code to Python compatible Dll.

Basically, D14UIKit is migrated from the Common, Renderer and UIKit parts of D14Engine with some necessary modifications, which are recorded in **Src/sensitive.txt**. A new directory **Exp** is created at the root path of the migrated project, and the wrapper code is placed there.

.. _Visual Studio: https://visualstudio.microsoft.com/
.. _Write C++ extensions for Python in Visual Studio: https://learn.microsoft.com/en-us/visualstudio/python/working-with-c-cpp-python-in-visual-studio?view=vs-2022
.. _pimpl idiom: https://learn.microsoft.com/en-us/cpp/cpp/pimpl-for-compile-time-encapsulation-modern-cpp
.. _pybind11: https://github.com/pybind/pybind11

Getting Started
---------------

Download the repository from `GitHub`_ (use depth=1 to reduce .git size):

.. sourcecode:: bat

   $ git clone https://github.com/yiyaowen/D14UIKit --depth=1

Since git does not support large file well, D14UIKit uses a submodule `Lfs`_ to maintain the binary files (images, shaders etc.). The large file system is based on private server, and D14UIKit uses ubuntu@d14games.com by default. Please contact yiyaowen@github to get the password.

The Lfs scripts use the py.paramiko package to build SSH connection:

.. sourcecode:: bat

   $ pip install paramiko

Enter the root path of the project and download the large files as following:

.. sourcecode:: bat

   $ cd D14UIKit
   $ py lfs/pull.py

Now we can start developing D14UIKit. The project is structured as below:

* **Bin**

  * **Images**
  * **Shaders**

* **Exp** (Wrapper code placed here)

  * **Inc** (C++ interfaces)
  * **PyBind** (Python interfaces)
  * **.h/.cpp** (Implementation files)

* **Inc** (External header files)
* **Lfs**
* **Src** (Migrated parts from D14Engine)

  * **Commom**
  * **Renderer**
  * **UIKit**
  * **sensitive.txt** (Records the modifications from UIKit @ D14Engine)

* **Test** (D14UIKit.dll will be copied here after building)

  * **PyBind** (D14UIKit.pyd will be copied here after building)

    * **TestMain.py** (Used to test Python wrapper)

  * **TestMain.cpp** (Used to test C++ wrapper)

* **package.ps1** (Used to package the release wrappers)

* **Miscellaneous files**

.. note::

   The primary project uses the **stubgen** tool from **mypy**:

   .. sourcecode:: bat

      $ pip install mypy

   You don't have to use this if you have better one.

Open *D14UIKit.sln* with Visual Studio, and then open *View* ➡ *Solution Explorer*:

* **D14UIKit**

  Primary project for building the C++ wrapper and the Python wrapper from the source code. The generated library/module will be copied to the Test environments after building.

* **PyBind**

  Test project for the Python wrapper. You can simply debug the Python code and the C++ code together with the *Python native development tools* and the *Python debugging symbols*.

* **Test**

  Test project for the C++ wrapper. You can simply include the C++ interfaces and write the test program directly. The dependencies (include path, library path etc.) have been set.

.. _GitHub: https://github.com/yiyaowen/D14UIKit
.. _Lfs: https://github.com/yiyaowen/Lfs

Building C++ Wrapper
--------------------

1. Set **D14UIKit** as the startup project.
2. Select **Debug / Release (x64)** configuration.
3. Build / Run the project.

Building Python Wrapper
-------------------------

1. Set **D14UIKit** as the startup project.
2. Select **DPyBind / RPyBind (x64)** configuration.
3. Build / Run the project.

.. note::

   To build PyBind, you need to install pybind11 by:

   .. sourcecode:: bat

      $ pip install pybind11

   and add the following output to the include path:

   .. sourcecode:: bat

      $ py -m pybind11 --includes

   Also see this `article`_ from MSDN for more details.

.. _article: https://learn.microsoft.com/en-us/visualstudio/python/working-with-c-cpp-python-in-visual-studio?view=vs-2022

Testing C++ Wrapper
-------------------

1. Set **Test** as the startup project.
2. Select **Debug / Release (x64)** configuration.
3. Write a test program, for example:

   .. sourcecode:: c++

      #include "Application.h"
      #include "MainWindow.h"

      using namespace d14uikit;

      int main()
      {
          Application app;
          MainWindow mwnd;
          return app.run();
      }

4. Build / Run the project.

Testing Python Wrapper
------------------------

1. Set **PyBind** as the startup project.
2. Select **Debug / Release (Any CPU)** configuration.
3. Write a script, for example:

   .. sourcecode:: python

      from D14UIKit import Application, MainWindow

      app = Application()
      mwnd = MainWindow()
      app.run()

4. Run with a Python interpreter.

.. note::

   Before debugging the Python wrapper:

   1. Install the `debugging symbols`_ for Python interpreter.
   2. Check *Debug* ➡ *Enable native code debugging* option.

.. _debugging symbols: https://learn.microsoft.com/en-us/visualstudio/python/debugging-symbols-for-mixed-mode-c-cpp-python
