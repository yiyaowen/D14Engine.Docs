.. _d14uikit-tutorials-layout_control:

布局控制
========

.. image:: https://raw.githubusercontent.com/yiyaowen/D14Engine.Docs.Img/main/d14uikit/tutorials/layout_control.png

.. note::

  教程中各演示程序的源代码均随导出库一同发放，可在 demo 目录下查看。

自适应布局
----------

在 D14UIKit 中，有两种方法向应用程序中添加新的 UI 对象：使其成为 Panel 的子对象，或使其成为 Layout 的元素。从严格意义上来说，后者的底层实现也是基于前者的，但是 Layout 在内部重写了相关的回调函数，从而能够完成自适应的布局控制。往 Panel 中添加子对象比较直接，我们在这里主要介绍 Layout 的使用方法。

在 D14UIKit 中，有两套内置的 Layout 模型：Constraint（约束布局）和 Grid（网格布局）。顾名思义，Constraint 通过限制元素与布局在平面上各方向的距离来完成布局控制，而 Grid 通过将元素“塞”入布局平面上事先划分好的网格中来完成布局控制。下图是这两种方式的直观对比：

.. image:: https://raw.githubusercontent.com/yiyaowen/D14Engine.Docs.Img/main/d14uikit/tutorials/constraint_vs_grid.png

简单的应用
----------

正如可以将 Panel 作为 MainWindow 的内容一样，我们也可以使用 Layout 来充满窗口的 client 区域：

.. tabs::

    .. tab:: C++

        .. sourcecode:: c++

            MainWindow mwnd(DEMO_NAME);

            GridLayout centerLayout;
            mwnd.setContent(&centerLayout);

            centerLayout.setHorzCellCount(2);

    .. tab:: Python

        .. sourcecode:: python

            mwnd = MainWindow(DEMO_NAME)

            centerLayout = GridLayout()
            mwnd.content = centerLayout

            centerLayout.horzCellCount = 2

GridLayout 的默认具有 1x1 的网格数量，我们将水平方向的网格数设置为 2，分别用来放置 Constraint 和 Grid 的演示元素。为了往 GridLayout 中添加元素，除了需要创建待添加的对象外，还需要填充对应的 GeoInfo 结构体，其中包含了待添加对象的几何信息。对于 GridLayout 的 GeoInfo 结构体来说，其 x, y 字段均为一个 Range 结构体，可以用来指定对象在该方向上以网格为单位的 offset 和 count：

.. tabs::

    .. tab:: C++

        .. sourcecode:: c++

            GridLayout::GeoInfo geoInfo = {};

            ConstraintLayout layout1;
            geoInfo = {};
            geoInfo.x = { 0, 1 };
            geoInfo.y = { 0, 1 };
            centerLayout.addElement(&layout1, geoInfo);

            GridLayout layout2;
            geoInfo = {};
            geoInfo.x = { 1, 1 };
            geoInfo.y = { 0, 1 };
            centerLayout.addElement(&layout2, geoInfo);

    .. tab:: Python

        .. sourcecode:: python

            layout1 = ConstraintLayout()
            geoInfo = GridLayout.GeoInfo()
            geoInfo.x = Range(0, 1)
            geoInfo.y = Range(0, 1)
            centerLayout.addElement(layout1, geoInfo)

            layout2 = GridLayout()
            geoInfo = GridLayout.GeoInfo()
            geoInfo.x = Range(1, 1)
            geoInfo.y = Range(0, 1)
            centerLayout.addElement(layout2, geoInfo)

接着我们创建一个用来演示 Constraint 布局的元素：

.. tabs::

    .. tab:: C++

        .. sourcecode:: c++

            Label lbl_c1(L"C1");
            ConstraintLayout::GeoInfo geoInfo1 = {};
            geoInfo1.keepWidth = false;
            geoInfo1.Left.ToLeft = 20;
            geoInfo1.Right.ToRight = 20;
            geoInfo1.keepHeight = false;
            geoInfo1.Top.ToTop = 20;
            geoInfo1.Bottom.ToTop = 120;
            layout1.addElement(&lbl_c1, geoInfo1);

            lbl_c1.setBkgnColor({ 0, 255, 0 });
            lbl_c1.setBkgnOpacity(0.5f);
            lbl_c1.setHorzAlign(Label::HCenter);

    .. tab:: Python

        .. sourcecode:: python

            lbl_c1 = Label('C1')
            geoInfo1 = ConstraintLayout.GeoInfo()
            geoInfo1.keepWidth = False
            geoInfo1.Left.ToLeft = 20
            geoInfo1.Right.ToRight = 20
            geoInfo1.keepHeight = False
            geoInfo1.Top.ToTop = 20
            geoInfo1.Bottom.ToTop = 120
            layout1.addElement(lbl_c1, geoInfo1)

            lbl_c1.bkgnColor = Color(0, 255, 0)
            lbl_c1.bkgnOpacity = 0.5
            lbl_c1.horzAlign = Label.HCenter

ConstraintLayout 的 GeoInfo 结构体中，除了 Xxx.ToYyy 形式的用于约束距离的字段外，还有 keepWidth 和 keepHeight 可供选择：如果 keep 为 true 值，则待添加的元素会始终保持其原本的尺寸大小，Layout 仅改变其在布局中的相对位置。值得注意的是所有 Xxx.ToYyy 字段都是可选的，对于没有指定的字段，Layout 将不会对该距离进行约束，此外有时也会出现矛盾的约束，例如当同时指定 Top.ToTop = 10 和 Top.ToBottom = 10 时，Layout 将会从中选择一个执行。我们的建议是不去考虑矛盾情况下的实际结果，而是在设计时就确保不出现矛盾的约束条件。

最后是完整的 demo 代码，其中包含重复的创建、布局工作，在此不过多赘述（特别注意将 app 设置为 resizable 来观察窗口大小变化时的自适应布局）：

.. tabs::

    .. tab:: C++

        .. code-block:: c++
            :emphasize-lines: 19, 20

            #include "Application.h"
            #include "ConstraintLayout.h"
            #include "GridLayout.h"
            #include "Label.h"
            #include "MainWindow.h"

            using namespace d14uikit;

            #define DEMO_NAME L"LayoutControl"

            int main(int argc, char* argv[])
            {
                float dpi = 96.0f;
                if (argc >= 2 && strcmp(argv[1], "HighDPI") == 0)
                {
                    dpi = 192.0f;
                }
                Application app(DEMO_NAME, dpi);
                app.setMinSize(app.size());
                app.setResizable(true);

                //------------------------------------------- Initialize UI objects.

                MainWindow mwnd(DEMO_NAME);
                GridLayout centerLayout;
                mwnd.setContent(&centerLayout);
                centerLayout.setHorzCellCount(2);

                GridLayout::GeoInfo geoInfo = {};

                ConstraintLayout layout1;
                geoInfo = {};
                geoInfo.x = { 0, 1 };
                geoInfo.y = { 0, 1 };
                centerLayout.addElement(&layout1, geoInfo);

                ConstraintLayout::GeoInfo geoInfo1 = {};

                Label lbl_c1(L"C1");
                geoInfo1 = {};
                geoInfo1.keepWidth = false;
                geoInfo1.Left.ToLeft = 20;
                geoInfo1.Right.ToRight = 20;
                geoInfo1.keepHeight = false;
                geoInfo1.Top.ToTop = 20;
                geoInfo1.Bottom.ToTop = 120;
                layout1.addElement(&lbl_c1, geoInfo1);
                lbl_c1.setBkgnColor({ 0, 255, 0 });
                lbl_c1.setBkgnOpacity(0.5f);
                lbl_c1.setHorzAlign(Label::HCenter);

                Label lbl_c2(L"C2");
                lbl_c2.setHeight(400);
                geoInfo1 = {};
                geoInfo1.keepWidth = false;
                geoInfo1.Left.ToLeft = 20;
                geoInfo1.Right.ToRight = 20;
                geoInfo1.keepHeight = true;
                geoInfo1.Bottom.ToBottom = 20;
                layout1.addElement(&lbl_c2, geoInfo1);
                lbl_c2.setBkgnColor({ 0, 255, 255 });
                lbl_c2.setBkgnOpacity(0.5f);
                lbl_c2.setHorzAlign(Label::HCenter);

                GridLayout layout2;
                geoInfo = {};
                geoInfo.x = { 1, 1 };
                geoInfo.y = { 0, 1 };
                centerLayout.addElement(&layout2, geoInfo);
                layout2.setHorzCellCount(4);
                layout2.setVertCellCount(4);
                layout2.setHorzMargin(20);
                layout2.setVertMargin(20);

                GridLayout::GeoInfo geoInfo2 = {};

                Label lbl_g1(L"G1");
                geoInfo2 = {};
                geoInfo2.x = { 0, 1 };
                geoInfo2.y = { 0, 1 };
                layout2.addElement(&lbl_g1, geoInfo2);
                lbl_g1.setBkgnColor({ 255, 0, 0 });
                lbl_g1.setBkgnOpacity(0.5f);
                lbl_g1.setHorzAlign(Label::HCenter);

                Label lbl_g2(L"G2");
                geoInfo2 = {};
                geoInfo2.x = { 1, 3 };
                geoInfo2.y = { 0, 2 };
                layout2.addElement(&lbl_g2, geoInfo2);
                lbl_g2.setBkgnColor({ 0, 255, 0 });
                lbl_g2.setBkgnOpacity(0.5f);
                lbl_g2.setHorzAlign(Label::HCenter);

                Label lbl_g3(L"G3");
                geoInfo2 = {};
                geoInfo2.x = { 0, 1 };
                geoInfo2.y = { 1, 3 };
                geoInfo2.spacing.top = 10;
                geoInfo2.spacing.right = 10;
                layout2.addElement(&lbl_g3, geoInfo2);
                lbl_g3.setBkgnColor({ 255, 0, 255 });
                lbl_g3.setBkgnOpacity(0.5f);
                lbl_g3.setHorzAlign(Label::HCenter);

                Label lbl_g4(L"G4");
                lbl_g4.setSize({ 200, 200 });
                geoInfo2 = {};
                geoInfo2.fixedSize = true;
                geoInfo2.x = { 1, 3 };
                geoInfo2.y = { 2, 2 };
                layout2.addElement(&lbl_g4, geoInfo2);
                lbl_g4.setBkgnColor({ 0, 255, 255 });
                lbl_g4.setBkgnOpacity(0.5f);
                lbl_g4.setHorzAlign(Label::HCenter);

                //------------------------------------------- Set UI event callacks.

                return app.run();
            }

    .. tab:: Python

        .. code-block:: python
            :emphasize-lines: 13, 14

            from sys import argv

            from D14UIKit import *

            DEMO_NAME = 'DemoTemplate'

            if __name__ == '__main__':
                dpi = 96.0
                if len(argv) >= 2 and argv[1] == 'HighDPI':
                    dpi = 192.0

                app = Application(DEMO_NAME, dpi)
                app.minSize = app.size
                app.resizable = True

                #------------------------------------------- Initialize UI objects.

                mwnd = MainWindow(DEMO_NAME)
                centerLayout = GridLayout()
                mwnd.content = centerLayout
                centerLayout.horzCellCount = 2

                layout1 = ConstraintLayout()
                geoInfo = GridLayout.GeoInfo()
                geoInfo.x = Range(0, 1)
                geoInfo.y = Range(0, 1)
                centerLayout.addElement(layout1, geoInfo)

                lbl_c1 = Label('C1')
                geoInfo1 = ConstraintLayout.GeoInfo()
                geoInfo1.keepWidth = False
                geoInfo1.Left.ToLeft = 20
                geoInfo1.Right.ToRight = 20
                geoInfo1.keepHeight = False
                geoInfo1.Top.ToTop = 20
                geoInfo1.Bottom.ToTop = 120
                layout1.addElement(lbl_c1, geoInfo1)
                lbl_c1.bkgnColor = Color(0, 255, 0)
                lbl_c1.bkgnOpacity = 0.5
                lbl_c1.horzAlign = Label.HCenter

                lbl_c2 = Label('C2')
                lbl_c2.height = 400
                geoInfo1 = ConstraintLayout.GeoInfo()
                geoInfo1.keepWidth = False
                geoInfo1.Left.ToLeft = 20
                geoInfo1.Right.ToRight = 20
                geoInfo1.keepHeight = True
                geoInfo1.Bottom.ToBottom = 20
                layout1.addElement(lbl_c2, geoInfo1)
                lbl_c2.bkgnColor = Color(0, 255, 255)
                lbl_c2.bkgnOpacity = 0.5
                lbl_c2.horzAlign = Label.HCenter

                layout2 = GridLayout()
                geoInfo = GridLayout.GeoInfo()
                geoInfo.x = Range(1, 1)
                geoInfo.y = Range(0, 1)
                centerLayout.addElement(layout2, geoInfo)
                layout2.horzCellCount = 4
                layout2.vertCellCount = 4
                layout2.horzMargin = 20
                layout2.vertMargin = 20

                lbl_g1 = Label('G1')
                geoInfo2 = GridLayout.GeoInfo()
                geoInfo2.x = Range(0, 1)
                geoInfo2.y = Range(0, 1)
                layout2.addElement(lbl_g1, geoInfo2)
                lbl_g1.bkgnColor = Color(255, 0, 0)
                lbl_g1.bkgnOpacity = 0.5
                lbl_g1.horzAlign = Label.HCenter

                lbl_g2 = Label('G2')
                geoInfo2 = GridLayout.GeoInfo()
                geoInfo2.x = Range(1, 3)
                geoInfo2.y = Range(0, 2)
                layout2.addElement(lbl_g2, geoInfo2)
                lbl_g2.bkgnColor = Color(0, 255, 0)
                lbl_g2.bkgnOpacity = 0.5
                lbl_g2.horzAlign = Label.HCenter

                lbl_g3 = Label('G3')
                geoInfo2 = GridLayout.GeoInfo()
                geoInfo2.x = Range(0, 1)
                geoInfo2.y = Range(1, 3)
                geoInfo2.spacing.top = 10
                geoInfo2.spacing.right = 10
                layout2.addElement(lbl_g3, geoInfo2)
                lbl_g3.bkgnColor = Color(255, 0, 255)
                lbl_g3.bkgnOpacity = 0.5
                lbl_g3.horzAlign = Label.HCenter

                lbl_g4 = Label('G4')
                lbl_g4.size = Size(200, 200)
                geoInfo2 = GridLayout.GeoInfo()
                geoInfo2.fixedSize = True
                geoInfo2.x = Range(1, 3)
                geoInfo2.y = Range(2, 2)
                layout2.addElement(lbl_g4, geoInfo2)
                lbl_g4.bkgnColor = Color(0, 255, 255)
                lbl_g4.bkgnOpacity = 0.5
                lbl_g4.horzAlign = Label.HCenter

                #------------------------------------------- Set UI event callacks.

                exit(app.run())
