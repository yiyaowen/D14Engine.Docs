开发者指南
==========

准备工作
--------

D14UIKit 的开发基于 `Visual Studio`_ 系列工具，因此首先需要通过 Visual Studio Installer 安装以下组件（community 版本即可）：

* C++ 接口： **C++ Desktop Development** （编译器、链接器和 SDK 等）。
* Python 接口： **Python Development**，并勾选 *Python native development tools*。

关于如何在 Visual Studio 中进行 C++ 和 Python 的联合开发，推荐参考这篇 MSDN 文章： `在 Visual Studio 中为 Python 代码编写 C++ 拓展`_。

为了将 UIKit @ D14Engine 打包成 D14UIKit，我们主要采用了以下两项技术：

* C++ 接口： `pimpl idiom`_，用于减少耦合、分离接口与实现。
* Python 接口： `pybind11`_，用于将 C++ 代码导出为 Python 兼容的 Dll。

D14UIKit 基本上是从 D14Engine 的 Common、Renderer 和 UIKit 模块迁移而来，但是也做了一些必要的修改，相关的改动均记录在 **Src/sensitive.txt** 文件中。此外，我们在迁移后的项目根目录下创建了一个新的文件夹 **Exp** 用于存放额外的包装代码。

.. _Visual Studio: https://visualstudio.microsoft.com/
.. _在 Visual Studio 中为 Python 代码编写 C++ 拓展: https://learn.microsoft.com/en-us/visualstudio/python/working-with-c-cpp-python-in-visual-studio?view=vs-2022
.. _pimpl idiom: https://learn.microsoft.com/en-us/cpp/cpp/pimpl-for-compile-time-encapsulation-modern-cpp
.. _pybind11: https://github.com/pybind/pybind11

环境搭建
--------

从 `GitHub`_ 上下载项目代码（使用 depth=1 以减少 .git 的大小）：

.. sourcecode:: bat

   $ git clone https://github.com/yiyaowen/D14UIKit --depth=1

由于 git 对大文件的支持并不完善（git-lfs 免费版限制了容量和带宽），我们在 D14UIKit 中使用了 `Lfs`_ 子模块来维护二进制文件（图像、着色器等）。该模块基于私有服务器，D14UIKit 托管在 ubuntu@d14games.com 上，为了构建项目，首先需要下载 `D14UIKit 二进制资源包`_，然后将其复制到原始项目中。如果在开发时需要上传或更新二进制文件，请联系 yiyaowen@github 获取建立 SSH 连接的密码（执行 Lfs pull/push 操作时需要验证）。

.. _D14UIKit 二进制资源包: https://d14games.com/downloads/developer/D14UIKit.zip

.. note::

   针对不同的开发目标，可以选择获取项目二进制资源的途径。如果仅对源代码进行更改，则无需管理二进制文件，只需进行通常的 git 操作；如果需要更改二进制文件，则需要通过 Lfs 中的 Python 脚本来与托管服务器进行交互。

   .. tabs::

      .. tab:: 仅更改源代码

         点击上方链接下载 D14UIKit 二进制资源包 **D14UIKit.zip**，解压后得到 D14UIKit 文件夹，然后将内容复制到项目根目录下。

      .. tab:: 更改二进制文件

         Lfs 中的脚本基于  py.paramiko 包来建立 SSH 连接：

         .. sourcecode:: bat

            $ pip install paramiko

         在项目的根目录下执行如下命令来下载所需的大文件：

         .. sourcecode:: bat

            $ cd D14UIKit
            $ py Lfs/pull.py

万事俱备，可以着手开发 D14UIKit。整个项目的结构如下：

* **Bin**

  * **Images**
  * **Shaders**

* **Exp** (存放包装代码)

  * **Inc** (C++ 接口)
  * **PyBind** (Python 接口)
  * **.h/.cpp** (实现文件)

* **Inc** (外部头文件)
* **Lfs**
* **Src** (从 D14Engine 迁移的模块)

  * **Commom**
  * **Renderer**
  * **UIKit**
  * **sensitive.txt** (记录对 UIKit @ D14Engine 的改动)

* **Test** (构建后将会复制生成的 D14UIKit.dll 至此)

  * **PyBind** (构建后将会复制生成的 D14UIKit.pyd 至此)

    * **TestMain.py** (用于测试 Python 包装)

  * **TestMain.cpp** (用于测试 C++ 包装)

* **Wrap** (该目录将在运行 package.ps1 进行打包后创建)
* **package.ps1** (用于打包生成 release 版本的包装)
* **杂项文件**

.. note::

   主项目使用 **mypy** 中的 **stubgen** 工具来生成 Python 提示文件：

   .. sourcecode:: bat

      $ pip install mypy

   如果你有更棒的工具，可以对 **package.ps1** 稍加修改来替换它。

使用 Visual Studio 打开 *D14UIKit.sln*，然后在 *视图* 中选择 *解决方案资源管理器*：

* **D14UIKit**

  用于从源代码构建 C++ 包装和 Python 包装的主项目。构建完成后，生成的库、模块将会被复制到相关测试环境下。

* **PyBind**

  用于测试 Python 包装的子项目。通过 *Python native development tools* 和 *Python debugging symbols* 可以很方便地对 Python 代码和 C++ 代码进行联合调试。

* **Test**

  用于测试 C++ 包装的子项目。所有的依赖项（头文件路径、库路径等）都已经设置好，可以很方便地编写测试程序。

.. _GitHub: https://github.com/yiyaowen/D14UIKit
.. _Lfs: https://github.com/yiyaowen/Lfs

构建 C++ 包装
-------------

1. 选择 **D14UIKit** 为启动项目。
2. 在配置方案 **Debug / Rebug / Release (x64)** 中选择一个。
3. 构建、运行项目。

.. note::

   +-------------+------------------+--------------+-----------------+
   | Config Name | Predefined-macro | Optimization | Runtime Library |
   +=============+==================+==============+=================+
   | Debug       | _DEBUG           | /Od          | /MDd            |
   +-------------+------------------+--------------+-----------------+
   | Rebug       | NDEBUG           | /O2          | /MDd            |
   +-------------+------------------+--------------+-----------------+
   | Debug       | NDEBUG           | /O2          | /MD             |
   +-------------+------------------+--------------+-----------------+

   在 Visual C++ 中，你必须指定 /MD 或 /MDd 链接选项来生成 DLL 目标，其中 'M' 代表 'Multi-thread'（多线程），'D' 代表 'DLL-specific'（后缀 'd' 代表 'debug'）。顾名思义，使用 /MDd 选项会链接 debug 版本的 MSVC 库，而 /MD 选项则对应 release 版本的库。由于它们的实现并不相同（例如，/MDd 版本的标准库可能会在出错时输出相关信息而不是直接崩溃来帮助调试，而 /MD 版本的库则被完全优化了），debug 版本的应用程序必须与 /MDd 版本的 DLL 链接，反之亦然。

构建 Python 包装
----------------

1. 选择 **D14UIKit** 为启动项目。
2. 在配置方案 **DPyBind / RPyBind (x64)** 中选择一个。
3. 构建、运行项目。

.. note::

   为了构建 PyBind，必须首先安装 pybind11 包：

   .. sourcecode:: bat

      $ pip install pybind11

   并将以下命令的输出添加到项目的包含路径中：

   .. sourcecode:: bat

      $ py -m pybind11 --includes

   相关的细节，可以参考这篇在 MSDN 上的 `文章`_。

.. _文章: https://learn.microsoft.com/en-us/visualstudio/python/working-with-c-cpp-python-in-visual-studio?view=vs-2022

测试 C++ 包装
-------------

1. 选择 **Test** 为启动项目。
2. 在配置方案 **Debug / Release (x64)** 中选择一个。
3. 编写测试程序，示例如下：

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

4. 构建、运行项目。

测试 Python 包装
----------------

1. 选择 **PyBind** 为启动项目。
2. 在配置方案 **Debug / Release (Any CPU)** 中选择一个。
3. 编写测试脚本，示例如下：

   .. sourcecode:: python

      from D14UIKit import Application, MainWindow

      app = Application()
      mwnd = MainWindow()
      app.run()

4. 使用 Python 解释器运行项目.

.. tip::

   如果你想要在运行 Python 包装时调试 C++ 代码：

   1. 在安装 Python 解释器时勾选 `debugging symbols`_ 选项。
   2. 在 PyBind 项目的 *调试* 属性中勾选 *启用本机代码调试* 选项。

.. _debugging symbols: https://learn.microsoft.com/en-us/visualstudio/python/debugging-symbols-for-mixed-mode-c-cpp-python

打包生成的库、模块
------------------

在 Windows PowerShell 中运行 ``package.ps1 v1_0``，其中版本标签 'v1_0' 将会被添加到打包后的压缩文件名末尾（例如， **d14uikit_xxx_v1_0**），此外还将在项目的根目录下创建或更新包含最终文件的 **Wrap** 子目录。

* **Wrap**

  * **cpp** (最终的 C++ 包装)

    * **include**
    * **lib**

      * **debug** (包含 ``/MDd`` 版本的 DLL)
      * **release** (包含 ``/MD`` 版本的 DLL)
      * **D14UIKit.lib** (公共的库接口定义)

  * **python** (最终的 Python 包装)

    * **D14UIKit.pyd** (Python 动态库模块)
    * **D14UIKit.pyi** (Python 提示文件)

  * **d14uikit_cpp_v1_0.zip** (**cpp** 目录的压缩包)
  * **d14uikit_python_v1_0.zip** (**python** 目录的压缩包)

.. tip::

   如果你对 PowerShell 不太熟悉，可以在命令提示符中运行以下等效命令：

   .. sourcecode:: bat

      $ powershell -f package.ps1 v1_0
