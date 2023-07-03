.. _d14uikit-tutorial-object_oriented:

面向对象的设计
==============

.. image:: https://raw.githubusercontent.com/yiyaowen/D14Engine.Docs.Img/main/d14uikit/tutorials/object_oriented.png

Retained VS Immediate
---------------------

根据待绘制对象在内存中的状态，一般可以将渲染引擎分为两派：Retained Mode（保留模式）和 Immediate Mode（立即模式）。顾名思义，Retained 的待绘制对象在内存中一般存在有具体的模型，其相关属性的数据具有持久的生命周期，而 Immediate 的待绘制对象在每帧都需要重新处理，其相关属性的数据只需要在每帧开始时确定好即可。这两种渲染模式的区别可以借助“涂鸦游戏”来理解：假设这里有一张白纸，而我们的目标是首先在第一帧呈现“yes”，然后在第二帧呈现“yep”。

* **Retained Mode（保留模式）**

  由于需要在内存中分别管理每个对象，我们势必拥有每个对象的生杀予夺大权，可以自由地控制每个对象的生命周期，该功能类似于一块“橡皮”。因此该模式下我们可使用的工具有：一张白纸、一支铅笔、一块橡皮。为了完成目标，需要进行以下步骤：

  1. *首先在白纸上依次绘制 y, e, s 三个对象*。
  2. *然后使用橡皮擦去 s 这个对象*。
  3. *最后使用铅笔在原本 s 对象的位置绘制 p 对象*。

* **Immediate Mode（立即模式）**

  由于对象无法在多帧之间共享，前一帧的 A 对象和后一帧的 A 对象虽然外观一样，在内存中却不是同一个对象，我们不得不购买一叠白纸来模拟不同的帧。因此该模式下我们可使用的工具有：一叠白纸、一支铅笔。为了完成目标，需要进行以下步骤：

  1. *首先在第一张白纸上依次绘制 y, e, s 三个对象*。
  2. *然后在第二张白纸上依次绘制 y, e, p 三个对象*。
  3. *最后将第二张白纸覆盖在第一张白纸上*。

在存在缓冲区的情况下（即在后台完成绘制后再投射到屏幕上），这两种模式所呈现出的效果是相同的，但是背后的机制却各有缺陷：

* Retained 要求充足的内存空间，而且大量对象的管理往往是一件复杂而又危险的工作。
* Immediate 避不开大量对象的重复绘制，而且流水线式的架构也很难动态地进行变化。

至于两者在工作性能上孰优孰劣，往往不可以一概而论，而是需要具体情况具体分析，根据目标任务的不同特性选择不同的渲染模式：

* 对于动态复杂度极高的任务，Retained 的 OOP 优势让其将 Immediate 远远甩在身后。
* 对于绘制复杂度极高的任务，Immediate 的流水线架构又能让 Retained 难以望其项背。

D14UIKit 的工作方式
-------------------

现代 GPU 硬件特别擅长高数据吞吐、高并行计算，平台图形接口往往直接与 GPU 打交道，得益于硬件特性能够高效地完成图形渲染所需的庞杂的计算工作。相较于 CPU 的逻辑处理功能，高性能计算是 GPU 的特长，过去的图形接口（如 GDI 等）大多具有 Retained 架构，主要依赖于 CPU 进行像素点的绘制，而现代图形接口大多直接采用 Immediate 架构，基于 GPU 进行流水线式的快速渲染。D14UIKit 的底层渲染基于 DirectX 图形接口，特别是 Direct2D 库（Immediate Mode）。

对于 UI 库来说，高动态的任务总是不可避免，因此 D14UIKit 依然在流水线绘制的基础上建立了一套对象管理模型，从而使得开发者能够进行面向对象的 UI 设计。

D14UIKit 的对象模型
---------------------

Panel 是 D14UIKit 中最为基本的 UI 对象，它代表了屏幕上的一块矩形区域，我们可以在其中绘制图像，或者放置其它的 UI 对象（作为子对象）。应用程序往往具有一个主窗口：

.. tabs::

    .. tab:: C++

        .. sourcecode:: c++

            MainWindow mwnd(DEMO_NAME);

    .. tab:: Python

        .. sourcecode:: python

            mwnd = MainWindow(DEMO_NAME)

如前所述，MainWindow 也是一个 Panel 对象，而它的矩形区域被分为了两部分：non-client 区域和 client 区域，non-client 区域包含一个标题栏和一个装饰带，窗口的中央则是 client 区域。值得一提的是，窗口的四周存在一圈 sizing frame，它也属于 non-client 区域。我们往往会用一个 Panel 充满窗口的 client 区域：

.. tabs::

    .. tab:: C++

        .. sourcecode:: c++

            Panel clntArea;
            mwnd.setContent(&clntArea);

    .. tab:: Python

        .. sourcecode:: python

            clntArea = Panel()
            mwnd.content = clntArea

除了以 Panel 为基础的 UI 对象外，D14UIKit 中也存在一些非 UI 对象，这些对象不直接显示在屏幕上，而是包含了一些数据以供其它 UI 对象使用，例如图像和字体等。为了在屏幕上显示一张图像，我们首先需要创建包含有图像数据的 Image 对象，然后再创建用于绘制这些数据的 Panel 对象，并将两者关联起来：

.. tabs::

    .. tab:: C++

        .. sourcecode:: c++

            Image img(L"test.png");

            Panel imgArea;
            imgArea.setParent(&clntArea);
            imgArea.setSize(img.size());
            imgArea.setPosition({ 20, 0 });
            imgArea.setImage(&img);

    .. tab:: Python

        .. sourcecode:: python

            img = Image('test.png')

            imgArea = Panel()
            imgArea.parent = clntArea
            imgArea.size = img.size
            imgArea.position = Point(20, 0)
            imgArea.image = img

演示程序中使用的 test.png 如下：

.. image:: https://d14games.com/downloads/D14Logo.png

类似的，为了绘制文本，我们需要创建一个 Label 对象，并将它和一个 Font 对象关联起来（可选）：

.. tabs::

    .. tab:: C++

        .. sourcecode:: c++

            Label textArea;

            textArea.setParent(&clntArea);
            textArea.setSize({ 200, 100 });
            textArea.setPosition({ 400, 100 });
            textArea.setOutlineWidth(5);
            textArea.setOutlineColor({ 255, 0, 0 });
            textArea.setOutlineOpacity(0.5);
            textArea.setText(L"This is a label");
            textArea.setHorzAlign(Label::HCenter);

            Font::load(
                L"MyFont",
                L"Times New Roman",
                20,
                L"en-us",
                Font::ExtraBold,
                Font::Italic,
                Font::Expanded);

            textArea.setFont(Font(L"MyFont"));

    .. tab:: Python

        .. sourcecode:: python

            textArea = Label()

            textArea.parent = clntArea
            textArea.size = Size(200, 100)
            textArea.position = Point(400, 100)
            textArea.outlineWidth = 5
            textArea.outlineColor = Color(255, 0, 0)
            textArea.outlineOpacity = 0.5
            textArea.text = 'This is a label'
            textArea.horzAlign = Label.HCenter

            Font.load("MyFont", "Times New Roman", 20, "en-us", \
                      Font.ExtraBold, Font.Italic, Font.Expanded)

            textArea.font = Font('MyFont')

值得注意的是，为了创建一个字体对象，我们首先需要通过 Font 的静态方法从系统字体库中导入所需的字体数据，然后再利用导入时设置的别名（MyFont）去创建最终的字体对象。作出这一设计的考虑是：从系统字体库中导入字体数据有一定的性能损耗，因此应用程序在启动时只导入了默认的字体数据。开发者可以根据应用程序的功能在该工作上进行取舍，以换取更高的运行性能。

或者我们也可以直接使用 Label 的默认字体，这样就无需额外创建字体对象：

.. tabs::

    .. tab:: C++

        .. sourcecode:: c++

            Label busyArea;
            busyArea.setParent(&clntArea);
            busyArea.setSize({ 760, 240 });
            busyArea.setPosition({ 20, 300 });
            busyArea.setBkgnColor({ 128, 128, 128 });
            busyArea.setBkgnOpacity(0.5f);
            busyArea.setText(L"Try moving cursor in this area");
            busyArea.setHorzAlign(Label::HCenter);

            busyArea.setFontSize(20);

    .. tab:: Python

        .. sourcecode:: python

            busyArea = Label()
            busyArea.parent = clntArea
            busyArea.size = Size(760, 240)
            busyArea.position = Point(20, 300)
            busyArea.bkgnColor = Color(128, 128, 128)
            busyArea.bkgnOpacity = 0.5
            busyArea.text = 'Try moving cursor in this area'
            busyArea.horzAlign = Label.HCenter

            busyArea.fontSize = 20

除了图像与字体外，UI 对象的回调事件也是一种非 UI 对象，在底层设计中，它基本上是借助现代 C++ 和 Python 中的 functor 概念实现的，因此在 D14UIKit 中设置 UI 对象的回调事件非常直接：

.. tabs::

    .. tab:: C++

        .. sourcecode:: c++

            auto setBusyCursor = [](Panel* p, MouseMoveEvent* e)
            {
                auto cursor = Application::app()->cursor();
                cursor->setIcon(Cursor::Busy);
            };
            busyArea.callback().onMouseMove = setBusyCursor;

    .. tab:: Python

        .. sourcecode:: python

            def setBusyCursor(p, e):
                cursor = Application.app.cursor
                cursor.setIcon(Cursor.Busy)

            busyArea.f_onMouseMove = setBusyCursor
