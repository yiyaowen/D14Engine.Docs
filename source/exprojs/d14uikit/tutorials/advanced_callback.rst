.. _d14uikit-tutorials-advanced_callback:

回调函数（进阶）
================

.. image:: https://raw.githubusercontent.com/yiyaowen/D14Engine.Docs.Img/main/d14uikit/tutorials/advanced_callback.png

.. note::

  教程中各演示程序的源代码均随导出库一同发放，可在 demo 目录下查看。

在本节中我们将创建一个画图程序，以演示 D14UIKit 中回调函数的高级用法。

最终考验
--------

进入到本节教程的读者想必已经对 D14UIKit 的开发模式较为熟悉了，因此大家可将本节的演示程序视为一道最终考验的关卡。随导出库一同发放的 demo 目录中含有 AdvancedCallback 程序的源文件/脚本，其中每处代码均有详尽的注释说明。如果你能够完全地理解该程序中每处代码的含义，那么恭喜：你已经正式踏入 D14UIKit 开发的天地了。

后续尝试
--------

作为一个画图程序，该 demo 还处在一个较为粗糙的阶段，例如其不支持更换画笔的颜色，并且画笔的表现也不尽人意。我们总结了一些可以改进的方向，如果读者感兴趣的话，可以继续增强程序的功能：

1. **支持不同的画笔颜色**：

   当前程序只能使用系统主题色作为画笔颜色，也许我们可以设计一个面板，其将画笔颜色作为背景，当我们点击它时会弹出一个对话框供我们选择其它颜色。通过编写一些回调函数似乎能够轻松地实现该功能；至于模态对话框，也许可以考虑一个看不见的 Panel（用于阻断 UI 事件）和一个上层 Window（作为对话框）的组合？

2. **支持不同的画笔风格**：

   作为一个画图程序，仅有一种画笔（Pencil）似乎有点过于单调了，而且当前程序的绘制逻辑比较粗糙（仅仅是在笔触周围生成一个纯色的方块）。在该绘制逻辑下经常会出现断墨的情况（由于鼠标移动事件的离散性），或许该问题可通过基于 cursorPoint 和 lastCursorPoint 来直接绘制连续的直线/曲线进行解决，有关如何将一个抽象的几何图形映射到屏幕上离散的像素点是计算机图形学中的一个基础问题，对此不熟悉的读者可从直线生成算法（如 Bresenham 算法）开始了解。

3. **Photoshop 又如何**：

   画布由一个 Image 对象实现，而 D14UIKit 中的 Image 支持 2U (CPU & GPU) 间的内存映射和复制，因此我们完全可以基于此实现各种各样的数字图像处理算法。Photoshop 又如何！
