.. _d14uikit-tutorial-hello_window:

Hello Window
============

.. image:: https://raw.githubusercontent.com/yiyaowen/D14Engine.Docs.Img/main/d14uikit/tutorials/hello_window.png

准备工作
--------

:download:`在 GitHub 上下载最新的 D14UIKit 导出库 <https://github.com/yiyaowen/D14UIKit/releases>`

导出库的目录结构如下：

.. tabs::

    .. tab:: C++

        * **d14uikit_cpp.zip**

          * **demo** (C++ 演示程序源文件)

            * **.cpp**

          * **include** (C++ 包装接口头文件)

            * **.h**

          * **lib** (C++ 包装接口库文件)

            * **debug** (包含使用 ``\MDd`` 选项生成的 DLL)

              * **D14UIKit.dll**

            * **release** (包含使用 ``\MD`` 选项生成的 DLL)

              * **D14UIKit.dll**

            * **D14UIKit.lib** (公共的库接口定义)

        .. note::

           关于 C++ 包装中 ``\MDd`` 和 ``\MD`` 版本 DLL 的区别，在开发者指南的 :ref:`d14uikit-dev-build_cpp_wrapper` 部分有简要的介绍。对于D14UIKit 的使用者（而不是开发者）来说，只需要注意为 Debug 或 Release 版本的应用程序链接相应版本的 DLL 即可。

    .. tab:: Python

        * **d14uikit_python.zip**

          * **demo** (Python 演示程序脚本)

            * **.py**

          * **D14UIKit.pyd** (Python 包装动态库模块)

          * **D14UIKit.pyi** (Python 包装提示文件)

        .. note::

            pyd 文件是 Windows 平台上 Python 的可导入库模块，例如名为 D14UIKit.pyd 的模块可通过 ``import D14UIKit`` 导入；pyi 文件可以帮助编辑器对 Python 代码进行智能提示（例如按下 Tab 补全代码）。

环境搭建
--------

导出库的结构较为简单，按照 C++/Python 项目的经典开发步骤进行操作即可。考虑到教程的完整性，我们也提供了简单的配置示例如下：

.. tabs::

    .. tab:: C++

        将 D14UIKit.lib 和 Debug 版本的 D14UIKit.dll 复制到 d14uikit_cpp 目录下，并创建 HelloWindow.cpp 文件，然后编写代码如下：

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

        以 MSVC 为例，运行如下命令生成 Debug 版本的应用程序（对于 Release 版本的 DLL 和应用程序，需要将 ``/MDd`` 改为 ``/MD``）：

        .. sourcecode:: bat

            $ cl HelloWindow.cpp /std:c++20 /I include /MDd /link D14UIKit.lib

    .. tab:: Python

        在 d14uikit_python 目录下创建 HelloWindow.py 文件，然后编写如下代码并运行脚本：

        .. sourcecode:: python

            from D14UIKit import *

            app = Application()
            mwnd = MainWindow()
            app.run()
