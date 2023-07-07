D14UIKit
========

.. image:: https://raw.githubusercontent.com/yiyaowen/D14Engine.Docs.Img/main/d14uikit/logo.png
   :height: 41

项目概览
--------

D14UIKit 是一个适用于现代 Windows 桌面环境的 UI 库，提供了 C++ 和 Python 接口。D14UIKit 基于 DirectX 进行高性能图形绘制，适配了在 Windows10/11 中逐渐发展起来的 Fluent Design 界面风格，并将现代 UI 设计理念中的黑暗模式融入了基本功能，从而实现与原生平台的高度契合。借助 D14UIKit 内置的各种 UI 控件对象，可以轻松开发出运行在现代 Windows 平台上的应用程序。

:download:`在 GitHub 上下载最新的 D14UIKit 导出库 <https://github.com/yiyaowen/D14UIKit/releases>`

.. image:: https://raw.githubusercontent.com/yiyaowen/D14Engine.Docs.Img/main/d14uikit/overview.png

快速上手
--------

对于不熟悉 D14UIKit 的开发者们，我们建议先阅读以下教程，以了解整体技术路线和基本使用方法：

* :ref:`d14uikit-tutorials-hello_window`
* :ref:`d14uikit-tutorials-hello_window_dpi`
* :ref:`d14uikit-tutorials-object_oriented`
* :ref:`d14uikit-tutorials-layout_control`
* :ref:`d14uikit-tutorials-basic_callback`
* :ref:`d14uikit-tutorials-modern_theme`
* :ref:`d14uikit-tutorials-advanced_callback`

对于正在使用 D14UIKit 并希望进一步发挥其全部威力的开发者们，我们提供了详细的文档可供查询：

* :ref:`d14uikit-reference-cpp`
* :ref:`d14uikit-reference-python`

技术特色
--------

在许多情况下，我们开发的命令行程序已经具有了简单易用的接口，如果希望进一步为其提供一个可视化界面，在选择 UI 库时往往会面临三重困境：

1. **引入的 UI 库相对于原始的命令行程序来说过于臃肿**：

   很多时候原始的命令行程序只有数 MB 或者数百 KB 的大小，而大多数 UI 库的规模以数十 MB 起步，特别是开发时的环境，有些甚至达到了数 GB 的规模。当今软件开发追求效率，为了加快软件构建的进程，开发者们趋向于选择通用的解决方案，导致许多功能简单的应用程序却占据了大量的存储空间。也许在不久的将来，随着硬件性能的提升和系统架构的优化，应用程序的大小不再是一个需要优化的方向，但 Simple is better than complex 始终是一个不错的准则。

2. **即使该 UI 库足够轻量，却仍免不了繁琐的环境搭建**：

   由于各种各样的限制，比如为了实现跨平台开发时的流程统一，许多 UI 库有着复杂的配置步骤。

3. **使用的 UI 库中各控件的默认外观还停留在远古时代**：

   从 XP 版本开始，Windows 的界面进行了数次更新迭代，这是业界设计风格不断进化的潮流下的大趋势。比如从 Vista 版本开始引入的拟物风格，在 Windows 7 中达到了顶峰，随后的 Windows 8 却一转扁平风格，并在 Windows 10 中不断完善，如今的 Windows 11 更是全面适配了 Fluent Design 风格，致力于提供更加现代化的使用体验。适用于 Windows 的 UI 库中，有些源自官方开发组，随着系统升级不断更新，其余大部分的控件外观或是自成体系，或是仍然停留在过去，并未跟随业界的潮流。UI 的界面风格也许因库而异，但不断随时代更新的那一个总能给用户提供更好的体验。

相比之下，D14UIKit 内部的框架基于 Win32 原生窗口，所有的图形绘制均通过 DirectX 实现，没有复杂的外部依赖，导出的库文件很小，并适配了现代化的界面风格。如果你想为某个运行在 Windows 平台上的小型项目提供可视化界面，同时又不希望引入的 UI 库喧宾夺主时，D14UIKit 是一个值得考虑的选择。

.. list-table:: 适用于现代 Windows 平台的各 UI 库对比
   :header-rows: 1
   :stub-columns: 1
   :width: 100%

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

在 D14Engine 中有一个名为 UIKit 的模块，它最初被用来开发引擎的编辑器界面，但是随着开发的深入，我们逐渐发觉了它作为一个高性能 UI 库的潜力。UIKit 基于原生 C++ 进行开发，其所有的架构设计均以高性能、高定制化为目标，为了能够灵活地使用它进行自由开发，使用者不仅需要具备相当的 C++ 使用经验，而且需要对 COM、DirectX 等与 Windows 平台绑定的开发技术有一定的了解，为了能够最大限度地发挥 UIKit 的功能，甚至还要求使用者掌握一些 Modern Rendering Pipeline 的知识。

一方面，UIKit 的这些特点注定了它不能轻易上手，即使是对相关技术了如指掌的开发者，在构建对运行性能、可定制化要求不高的应用程序时想必也会毫不犹豫地选择更加易用的 UI 库；另一方面，我们仍然希望能够以舍弃掉少许的性能、自由度为代价，将 UIKit 的强大功能以某种更为简单的方式提供给大家，于是 D14UIKit 便诞生了。D14UIKit 在 UIKit 的基础上进行了修改和完善，是 UIKit 的一层软包装。

.. toctree::
   :maxdepth: 1
   :hidden:

   tutorials/index
   reference/index
   devs/index
