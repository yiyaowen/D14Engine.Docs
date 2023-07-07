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

D14UIKit 基本上是从 D14Engine 的 Common、Renderer 和 UIKit 模块迁移而来，但是也做了一些必要的修改，其中源代码层面（Src 目录）的修改记录在 **Src/sensitive.txt** 文件中。此外，我们在迁移后的项目根目录下创建了一个新的文件夹 **Exp** 用于存放额外的包装代码。

.. _Visual Studio: https://visualstudio.microsoft.com/
.. _在 Visual Studio 中为 Python 代码编写 C++ 拓展: https://learn.microsoft.com/en-us/visualstudio/python/working-with-c-cpp-python-in-visual-studio?view=vs-2022
.. _pimpl idiom: https://learn.microsoft.com/en-us/cpp/cpp/pimpl-for-compile-time-encapsulation-modern-cpp
.. _pybind11: https://github.com/pybind/pybind11

环境搭建
--------

从 `GitHub`_ 上下载项目代码（使用 depth=1 以减少 .git 的大小）：

.. sourcecode:: bat

   $ git clone https://github.com/yiyaowen/D14UIKit --depth=1

由于 git 对大文件的支持并不完善（git-lfs 有容量和带宽限制），我们在 D14UIKit 中使用了 `Lfs`_ 子模块来管理项目中的二进制资源。该模块基于私有服务器，D14UIKit 默认托管在 ubuntu@d14games.com 上，为了构建项目，首先需要下载 :download:`D14UIKit 资源包 <https://d14games.com/downloads/developer/D14UIKit.zip>`，然后将其复制到原始项目中。

.. _GitHub: https://github.com/yiyaowen/D14UIKit
.. _Lfs: https://github.com/yiyaowen/Lfs

.. note::

   针对不同的开发目标，可以选择获取构建项目所需的二进制资源的途径。如果仅对源代码进行更改，则只需要进行通常的 git 操作；如果对资源文件进行修改，则还需要通过 Lfs 中的 Python 脚本来与托管服务器进行交互。

   .. tabs::

      .. tab:: 仅更改源代码

         下载二进制资源包 :download:`D14UIKit.zip <https://d14games.com/downloads/developer/D14UIKit.zip>`，并解压、复制到项目根目录中。

      .. tab:: 更改资源文件

         Lfs 中的 Python 脚本基于 py.paramiko 包与托管服务器建立 SSH 连接：

         .. sourcecode:: bat

            $ pip install paramiko

         在项目根目录下执行如下命令下载项目资源文件（相关概念与 git 类似）：

         .. sourcecode:: bat

            $ py Lfs/pull.py

         该文件下载操作需要密码进行验证（请联系 yiyaowen@github 获取）。

         如果需要将更新后的资源文件同步到托管服务器，则需要执行如下操作：

         .. sourcecode:: bat

            $ py Lfs/add.py
            $ py Lfs/push.py

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
* **Out** (该文件夹将在运行 package.ps1 进行打包后创建)
* **Src** (从 D14Engine 迁移的模块)

  * **Commom**
  * **Renderer**
  * **UIKit**
  * **sensitive.txt** (记录对 UIKit @ D14Engine 的改动)

* **Test** (构建后将会复制生成的 D14UIKit.dll 至此)

  * **PyBind** (构建后将会复制生成的 D14UIKit.pyd 至此)

    * **TestMain.py** (用于测试 Python 包装)

  * **TestMain.cpp** (用于测试 C++ 包装)

* **package.ps1** (用于打包生成的各版本包装)
* **其它文件**

.. important::

   主项目使用 **mypy/stubgen** 工具来生成 Python 提示文件：

   .. sourcecode:: bat

      $ pip install mypy

   如果你有更好的工具，可以修改 **package.ps1** 来替换掉它。

使用 Visual Studio 打开 **D14UIKit.sln**，然后在 *视图* 中打开 *解决方案资源管理器*，可以看到项目如下：

* **D14UIKit**

  用于构建 C++ 和 Python 包装的主项目。在构建完成后，生成的模块将会被复制到相关测试环境中。

* **PyBind**

  用于测试 Python 包装的子项目，包含有多个 demo，在 Visual Studio 环境中可以很方便地对 Python 和 C++ 代码进行联合调试与分析。

* **Test**

  用于测试 C++ 包装的子项目，包含有多个 demo，相关的依赖项（头文件/库路径等）均已经配置好，可以直接编写 C++ 程序进行测试。

.. _d14uikit-devs-build_cpp_wrapper:

构建 C++ 包装
-------------

1. 选择 **D14UIKit** 为启动项目。
2. 在配置方案 **Debug / Rebug / Release (x64)** 中选择一个。
3. 构建、运行项目。

.. note::

   .. list-table:: D14UIKit 项目中各配置的对比
      :header-rows: 1
      :width: 100%

      * - 配置名称
        - 预定义宏
        - 优化选项
        - 运行时库
      * - Debug
        - _DEBUG
        - /Od
        - /MDd
      * - Rebug
        - NDEBUG
        - /O2
        - /MDd
      * - Release
        - NDEBUG
        - /O2
        - /MD

   在 Visual C++ 中，必须指定 /MD 或 /MDd 链接选项来配置生成的 DLL 目标，其中 M 代表 Multi-thread，D 代表 DLL-specific（后缀 d 代表 debug）。顾名思义，使用 /MDd 选项会链接 debug 版本的 MSVC 库，而 /MD 选项则对应 release 的版本。由于它们的实现并不相同，例如 /MDd 版本的标准库会在出错时输出相关信息而不是直接崩溃来帮助调试，而 /MD 版本的库则被完全优化了，因此 debug 版本的应用程序必须与 /MDd 版本的 DLL 链接，反之亦然，否则会在运行时出错。

构建 Python 包装
----------------

1. 选择 **D14UIKit** 为启动项目。
2. 在配置方案 **DPyBind / RPyBind (x64)** 中选择一个。
3. 构建、运行项目。

.. important::

   为了构建 PyBind，首先需要安装 pybind11 包：

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

   .. code-block:: c++

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

   .. code-block:: python

      from D14UIKit import Application, MainWindow

      app = Application()
      mwnd = MainWindow()
      app.run()

4. 使用 Python 解释器运行项目.

.. tip::

   如果你想要在运行 Python 包装的同时调试背后的 C++ 代码：

   1. 在安装 Python 解释器时勾选 `debugging symbols`_ 选项。
   2. 在 PyBind 项目的 *调试* 属性中勾选 *启用本机代码调试* 选项。

.. _debugging symbols: https://learn.microsoft.com/en-us/visualstudio/python/debugging-symbols-for-mixed-mode-c-cpp-python

打包生成的模块
--------------

在分别完成 D14UIKit 项目中 Rebug、Release 和 PyRelease 配置的构建后，各包装的模块文件已生成在中间目录，接着需要在 Windows PowerShell 中运行 ``package.ps1 v1_0``，其中版本标签 v1_0 将会被添加到打包后的压缩文件名末尾（例如 **d14uikit_xxx_v1_0**），并创建或更新包含有各版本导出模块的 **Out** 文件夹。

* **Out**

  * **cpp** (导出的 C++ 包装)

    * **demo**
    * **include**
    * **lib**

      * **debug** (包含 ``/MDd`` 版本的 DLL)
      * **release** (包含 ``/MD`` 版本的 DLL)
      * **D14UIKit.lib** (公共的库接口定义)

  * **python** (导出的 Python 包装)

    * **demo**
    * **D14UIKit.pyd** (Python 动态库模块)
    * **D14UIKit.pyi** (Python 提示文件)

  * **d14uikit_cpp_v1_0.zip** (**cpp** 目录的压缩包)
  * **d14uikit_python_v1_0.zip** (**python** 目录的压缩包)

.. tip::

   如果你对 PowerShell 不太熟悉，也可以在命令提示符中运行以下等效命令：

   .. sourcecode:: bat

      $ powershell -f package.ps1 v1_0
