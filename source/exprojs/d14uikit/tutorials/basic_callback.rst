.. _d14uikit-tutorials-basic_callback:

回调函数（基础）
================

.. image:: https://raw.githubusercontent.com/yiyaowen/D14Engine.Docs.Img/main/d14uikit/tutorials/basic_callback.png

在本节中我们将创建一个能自定义主窗口标题的应用程序，以演示 D14UIKit 中回调函数的基础用法。

创建 UI 对象
------------

首先初始化应用程序和主窗口（这基本上是模板化的），为了美观我们将窗口的高度设置为 380 dip：

.. tabs::

    .. tab:: C++

        .. code-block:: c++
            :emphasize-lines: 19

            #include "Application.h"
            #include "Callback.h"
            #include "FlatButton.h"
            #include "MainWindow.h"
            #include "TextBox.h"

            using namespace d14uikit;

            #define DEMO_NAME L"BasicCallback"

            int main(int argc, char* argv[])
            {
                float dpi = 96.0f;
                if (argc >= 2 && strcmp(argv[1], "HighDPI"))
                {
                    dpi = 192.0f;
                }
                Application app(DEMO_NAME, dpi);
                app.setHeight(380);

                //------------------------------------------- Initialize UI objects.

                MainWindow mwnd(DEMO_NAME);
                Panel clntArea;
                mwnd.setContent(&clntArea);

                //------------------------------------------- Set UI event callacks.

                return app.run();
            }

    .. tab:: Python

        .. code-block:: python
            :emphasize-lines: 13

            from sys import argv

            from D14UIKit import *

            DEMO_NAME = 'BasicCallback'

            if __name__ == '__main__':
                dpi = 96.0
                if len(argv) >= 2 and argv[1] == 'HighDPI':
                    dpi = 192.0

                app = Application(DEMO_NAME, dpi)
                app.height = 380

                #------------------------------------------- Initialize UI objects.

                mwnd = MainWindow(DEMO_NAME)
                clntArea = Panel()
                mwnd.content = clntArea

                #------------------------------------------- Set UI event callacks.

                exit(app.run())

接着创建一个可编辑文本框，通过输入文本自定义窗口标题；最后再创建一个简单的按钮，用来恢复默认的窗口标题：

.. tabs::

    .. tab:: C++

        .. code-block:: c++
            :emphasize-lines: 8

            TextBox titleInput;
            titleInput.setParent(&clntArea);
            titleInput.setSize({ 400, 50 });
            titleInput.setPosition({ 200, 100 });
            titleInput.setRoundRadius(5);
            titleInput.setTextRect({ 10, 5, 390, 45 });

            auto placer = titleInput.placeholder();
            placer->setText(L"Input window title...");

            FlatButton restoreButton;
            restoreButton.setParent(&clntArea);
            restoreButton.setSize({ 200, 50 });
            restoreButton.setPosition({ 300, 200 });
            restoreButton.setRoundRadius(5);
            restoreButton.setText(L"Restore default");

    .. tab:: Python

        .. code-block:: python
            :emphasize-lines: 8

            titleInput = TextBox()
            titleInput.parent = clntArea
            titleInput.size = Size(400, 50)
            titleInput.position = Point(200, 100)
            titleInput.roundRadius = 5
            titleInput.textRect = Rect(10, 5, 390, 45)

            placer = titleInput.placeholder
            placer.text = 'Input window title...'

            restoreButton = FlatButton()
            restoreButton.parent = clntArea
            restoreButton.size = Size(200, 50)
            restoreButton.position = Point(300, 200)
            restoreButton.roundRadius = 5
            restoreButton.text = 'Restore default'

注意在创建文本框时，为了设置提示文本，我们首先通过 placeholder 方法/属性获取到该文本框内部的提示 Label 对象，然后再调用 Label 的通用方法来设置文本，而不是直接调用 TextBox 提供的方法来完成这一工作。这种 OOP 式的设计在 D14UIKit 中广泛存在，因为许多内置的高级 UI 控件往往都复用了一些基础的 UI 控件，这也从侧面体现了 D14UIKit 内部架构在面向对象层面上的自洽性。

编写回调函数
------------

为了实现输入文本更改窗口标题的功能，我们需要设置 TextBox 的 onTextChange 回调函数，该函数将会在文本框的内容发生变化时被调用：

.. tabs::

    .. tab:: C++

        .. sourcecode:: c++

            titleInput.callback().onTextChange =
            [&](TextBox* obj, const std::wstring& text)
            {
                mwnd.setTitle(text);
            };

    .. tab:: Python

        .. sourcecode:: python

            def changeMwndTitle(obj, text):
                mwnd.title = text
            titleInput.f_onTextChange = changeMwndTitle

与之类似，也可以设置 FlatButton 的 onMouseButtonRelease 回调函数，该函数将会在按钮被点击后调用（连续地完成按下和松开动作）：

.. tabs::

    .. tab:: C++

        .. sourcecode:: c++

            restoreButton.callback().onMouseButtonRelease =
            [&](ClickablePanel* clkp, MouseButtonClickEvent* e)
            {
                titleInput.setText(L"");
                mwnd.setTitle(DEMO_NAME);
            };

    .. tab:: Python

        .. sourcecode:: python

            def restoreMwndTitle(clkp, e):
                titleInput.text = ''
                mwnd.title = DEMO_NAME
            restoreButton.f_onMouseButtonRelease = restoreMwndTitle

注意我们必须首先清空文本框，然后再设置窗口标题，否则 onTextChange 回调函数将会在设置完窗口标题后又将其清空（不妨尝试一下吧）。

C++ 好麻烦！
------------

使用 C++ 的开发者们也许注意到了，相较于 Python 如此简洁的回调函数设置，C++ 一丝不苟的类型让这一过程稍显繁杂，为了编写相应的回调函数，我们不得不去查阅该函数的原型以获取相关的参数和返回值信息，然后再将其复制过来。为了优化使用体验，我们为 C++ 开发者们提供了 **Callback.h** 头文件，其中包含了内置的回调函数的宏定义，通过引入该头文件我们可以稍许简化 C++ 回调函数的设置过程：

.. sourcecode:: c++

    titleInput.D14_onTextChange(TextBox, obj, text, &)
    {
        mwnd.setTitle(text);
    };
    restoreButton.D14_onMouseButtonRelease(clkp, e, &)
    {
        titleInput.setText(L"");
        mwnd.setTitle(DEMO_NAME);
    };

系列宏的最后一个参数为 __VA_ARGS__（可变参数列表），它将会被复制到目标 lambda 的捕获列表中。

.. tip::

    事实上，在现代 C++ 标准下，我们已经可以使用 ``auto`` 关键字来让编译器自动推断 lambda 的参数列表。例如上述回调函数的设置也可以写成：

    .. sourcecode:: c++

        titleInput.callback().onTextChange =
        [&](auto obj, auto text)
        {
            mwnd.setTitle(text);
        };
        restoreButton.callback().onMouseButtonRelease =
        [&](auto clkp, auto e)
        {
            titleInput.setText(L"");
            mwnd.setTitle(DEMO_NAME);
        };

    不过这种写法会导致当前的某些 IDE 无法自动推断出这些参数的类型，从而让代码自动补全失效，希望在不久的将来这些 IDE 能够变得更加智能。
