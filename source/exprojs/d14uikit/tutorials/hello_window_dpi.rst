.. _d14uikit-tutorial-hello_window_dpi:

Hello Window (DPI)
==================

.. image:: https://raw.githubusercontent.com/yiyaowen/D14Engine.Docs.Img/main/d14uikit/tutorials/hello_window_dpi.png

从显示缩放说起
--------------

使用 Windows10/11 的用户也许尝试过更改以下选项（设置/系统/缩放）：

.. image:: https://raw.githubusercontent.com/yiyaowen/D14Engine.Docs.Img/main/d14uikit/tutorials/display_scaling.png

对于 Windows7 及更加古老的系统版本，也可以在控制面板中进行更改（从 Windows XP 开始才支持高 DPI 缩放）。一般来说，100% 缩放对应着 96 dpi，因此 125% 缩放则会按照 120 dpi 来进行显示，从直观上来说，缩放比例越大，应用程序的界面、文字也会随之增大，点阵图像也会越来越模糊（矢量图像则依然清晰）。

DPI: Dots Per Inch
------------------

DPI 意为“每英寸的点数”，其中“英寸”是物理世界中用来衡量距离长短的单位，而“点数”则是虚拟屏幕中的大小单位，其可以指代点阵屏幕上的一个像素，也可以指代印刷平面上的一个油墨点，因此 DPI 是联系物理世界和虚拟屏幕的桥梁，在确定好 DPI 后，可以由物体的实际大小推测其所占据的像素个数，也可以由像素个数计算其实际占据的大小。例如在 96 dpi 的显示设置下，一条 1 英寸长的直线会占据屏幕上的 96 个像素，或者是纸张上的 96 个油墨点。

实际上 DPI 也经常用于描述电子设备的灵敏度，例如一个 1000 dpi 的鼠标，其在平面上每移动 1 英寸，相应的光标就会在屏幕上移动 1000 个像素。此外在 Windows 平台上，还有一个和 DPI 紧密相关的概念 DIP（Device Independent Pixel，设备无关像素，也称逻辑像素），作为逻辑空间的像素单位，一个 dip 往往可以映射到物理空间的多个像素，该单位的引进为通用开发提供了极大的便利，在确定好对象所占用的 DIP 后，Windows 会根据目标设备的 DPI 自动地将其转换为物理像素，从而保证该对象在不同大小、不同分辨率的屏幕上都能被正确地显示出来。

例如一条 100 dip 长的直线，在 96 dpi 的屏幕上会占据 100 个物理像素，而在 120 dpi 的屏幕上则会占据 100 * (120 / 96) = 125 个物理像素。MSDN 上的这篇 `文章`_ 简要地介绍了两者的关系，此外其中有关 Direct2D 和高 DPI 的内容或许对 D14UIKit 的开发也有一定帮助。

.. _文章: https://learn.microsoft.com/en-us/windows/win32/direct2d/direct2d-and-high-dpi#what-is-a-dip

D14UIKit 中的 DPI
-----------------

在 Windodws 中，除了可以在（设置/系统/缩放）中设置系统的全局 DPI 外，每个应用程序（顶层的 Win32 窗口）也可以按照不同的 DPI 进行显示。在 D14UIKit 中，应用程序的 DPI 必须在启动时确定好，运行时无法更改，作出这一设计的考虑是：

1. **DPI 会影响应用程序中大多数图形资源的创建**：

   比如一张 800x600 的图片，固定显示在窗口中央 800 dip X 600 dip 的矩形区域，其在 96 dpi 的屏幕上正常显示，而在 120 dpi 的屏幕上，由于开发时确定好的逻辑尺寸不变，其对应的物理像素区域会相应地扩张，导致图片不得不被放大模糊，此时往往需要准备不同分辨率的图片，根据 DPI 来进行选择。再比如在不同的 DPI 下，界面上相同点数的字体具有不同的实际大小，而字体作为一种图形资源也不得不重新创建。

2. **DPI 一般不会频繁更改，而是随显示设备固定**：

   对于不同的屏幕，总有一个合适的 DPI 设置让界面处于看起来比较舒适的大小，例如 1080p 的屏幕一般会使用 100% 或者 125% 的缩放设置，而 4K 的屏幕也许会考虑使用 200% 乃至更高的缩放设置，但该数值一旦确定后，往往不会再被更改。

在 D14UIKit 中设置应用程序的 DPI 非常直接，只需要在创建 Application 对象时传入第二个参数即可：

.. tabs::

    .. tab:: C++

        .. code-block:: c++
            :emphasize-lines: 15

            #include "Application.h"
            #include "MainWindow.h"

            using namespace d14uikit;

            #define DEMO_NAME L"HelloWindowDPI"

            int main(int argc, char* argv[])
            {
                float dpi = 96.0f;
                if (argc >= 2 && strcmp(argv[1], "HighDPI"))
                {
                    dpi = 192.0f;
                }
                Application app(DEMO_NAME, dpi);

                //------------------------------------------- Initialize UI objects.

                MainWindow mwnd(DEMO_NAME);

                //------------------------------------------- Set UI event callacks.

                return app.run();
            }

    .. tab:: python

        .. code-block:: python
            :emphasize-lines: 12

            from sys import argv

            from D14UIKit import *

            DEMO_NAME = 'HelloWindowDPI'

            if __name__ == '__main__':
                dpi = 96.0
                if len(argv) >= 2 and argv[1] == 'HighDPI':
                    dpi = 192.0

                app = Application(DEMO_NAME, dpi)

                #------------------------------------------- Initialize UI objects.

                mwnd = MainWindow(DEMO_NAME)

                #------------------------------------------- Set UI event callacks.

                exit(app.run())
