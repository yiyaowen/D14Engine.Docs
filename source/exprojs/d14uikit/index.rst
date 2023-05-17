D14UIKit
========

.. image:: https://raw.githubusercontent.com/yiyaowen/D14Engine.Docs.Img/main/d14uikit/logo.png
   :height: 41

项目概览
--------

D14UIKit 是一个适用于 Windows 桌面环境的 UI 库，提供了 C++ 和 Python 接口。D14UIKit 基于 DirectX 进行高性能图形绘制，适配了在 Windows10/11 中逐渐发展起来的 Fluent Design 界面风格，并将现代 UI 设计理念中的黑暗模式融入了基本功能，从而实现与原生平台的高度契合。借助 D14UIKit 内置的各种 UI 控件对象，可以轻松开发出运行在现代 Windows 平台上的应用程序。

:download:`在 GitHub 上下载最新的 D14UIKit 导出库 <https://github.com/yiyaowen/D14UIKit/releases>`

.. image:: https://raw.githubusercontent.com/yiyaowen/D14Engine.Docs.Img/main/d14uikit/overview.png

快速上手
--------

对于不熟悉 D14UIKit 的开发者们，我们建议先阅读以下教程，以了解整体技术路线和基本使用方法：

* :ref:`d14uikit-tutorial-hello_window`
* :ref:`d14uikit-tutorial-hello_window_dpi`
* :ref:`d14uikit-tutorial-object_oriented`
* :ref:`d14uikit-tutorial-layout_control`
* :ref:`d14uikit-tutorial-basic_callback`
* :ref:`d14uikit-tutorial-modern_theme`
* :ref:`d14uikit-tutorial-advanced_callback`

对于正在使用 D14UIKit 并希望进一步发挥其全部威力的开发者们，我们提供了详细的文档可供查询：

* :ref:`d14uikit-cpp-reference`
* :ref:`d14uikit-python-reference`

技术特色
--------

在许多情况下，我们开发的命令行程序已经具有了简单易用的接口，如果希望进一步为其提供一个可视化界面，此时往往会面临三重困境：

1. 引入的 UI 库过于臃肿，特别是开发环境，有些甚至达到了数 GB 的规模，而命令行程序本身却并不庞大。
2. 即使该 UI 库足够轻量，但仍然避免不了繁琐的环境搭建，添加 GUI 比实现程序原本的功能更加让人烧脑。
3. 许多历史悠久的 UI 库虽然功能丰富，但控件的默认外观还停留在远古时代，想要从零开始设计并不简单。

相比之下，D14UIKit 内部的框架基于 Win32 原生窗口，所有的图形绘制均通过 DirectX 实现，没有复杂的外部依赖，导出的库文件很小。因此当你想要为某个运行在 Windows 平台上的小型项目提供可视化界面，同时又不希望引入的 UI 库喧宾夺主时，D14UIKit 是一个值得考虑的选择。

.. list-table:: 适用于现代 Windows 平台的各 UI 库对比
   :header-rows: 1
   :stub-columns: 1

   * - 特性/名称
     - D14UIKit
     - Qt
     - WinUI
     - Electron
   * - 库体积
     - ■
     - ■■
     - ■■■
     - ■■■
   * - 开发难度
     - ✦
     - ✦✦✦
     - ✦✦✦
     - ✦✦
   * - 运行性能
     - ★★★
     - ★★
     - ★★
     - ★
   * - 系统适配
     - ✓
     - ✗
     - ✓
     - ✗
   * - 可定制化
     - ✗
     - ✓
     - ✓
     - ✓

灵感起源
--------

在 D14Engine 中有一个名为 UIKit 的模块，它最初被设计用来开发引擎的编辑器 GUI 界面，但随着开发的深入，我们逐渐发觉了它作为一个高性能 UI 库的潜力。UIKit 基于原生 C++ 进行开发，其所有的设计均以高性能、高定制化为目标，为了能够灵活地使用它进行自由开发，使用者不仅需要具备相当的 C++ 使用经验，而且需要对 COM、DirectX 等与 Windows 平台绑定的开发技术有一定的了解，为了能够最大限度地发挥 UIKit 的功能，甚至还要求使用者掌握一些 Modern Rendering Pipeline 的知识。一方面，UIKit 的这些特点注定了它不能够轻易上手，即使是对相关技术了如指掌的开发者，在构建对性能、定制化要求不高的应用程序时想必也会毫不犹豫地选择更加易用的 UI 库；另一方面，我们仍然希望能够以舍弃掉少许的性能、自由度为代价，将 UIKit 的强大功能以某种更为简单的方式提供给大家，于是 D14UIKit 便诞生了。因此从某种意义上来说，D14UIKit 在 UIKit @ D14Engine 的基础上进行了修改和完善，是 UIKit 的一层软包装。

.. toctree::
   :maxdepth: 1
   :hidden:

   tutorials/index
   reference/index
   devs/index
