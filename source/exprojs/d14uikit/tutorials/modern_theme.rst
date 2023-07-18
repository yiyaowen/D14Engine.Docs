.. _d14uikit-tutorials-modern_theme:

现代化主题
==========

.. image:: https://raw.githubusercontent.com/yiyaowen/D14Engine.Docs.Img/main/d14uikit/tutorials/modern_theme.png

.. note::

  教程中各演示程序的源代码均随导出库一同发放，可在 demo 目录下查看。

深色模式
--------

许多应用程序支持各种花哨的“换肤”操作，而其中最主要的就是深浅色主题的切换，这也是 UI 现代化的一个重要特征。许多研究表明，深色化主题有助于提高注意力、增加沉浸感并减少视觉疲劳，此外对于某些电子屏幕（如 OLED 屏），深色外观能够节省电量。如今越来越多的电子设备使用者习惯于让系统主题随昼夜切换，甚至总是使用深色主题。

D14UIKit 作为一个现代 UI 库，对主题切换有着全面的支持，各种 UI 控件的主题切换是被作为基本用法写入底层架构之中的，因此启用深色主题的操作非常直接：

.. tabs::

    .. tab:: C++

        .. sourcecode:: c++

            app->setThemeMode(L"Dark");

    .. tab:: Python

        .. sourcecode:: python

            app.themeMode = 'Dark'

其中 app 是全局的 Application 对象。

主题切换
--------

在之前的教程中，我们并未演示过如何切换应用程序的主题，而 D14UIKit 默认让应用程序跟随系统当前的主题，因此你创建的演示程序的外观和你当前所使用的系统主题会始终保持一致。在本节中我们将创建一个可以自由地切换主题的应用程序。

首先是窗口的一些设置：

.. tabs::

    .. tab:: C++

        .. sourcecode:: c++

            app.setHeight(300);
            app.setMinSize(app.size());
            app.setResizable(true);

    .. tab:: Python

        .. sourcecode:: python

            app.height = 300
            app.minSize = app.size
            app.resizable = True

然后创建 UI 对象如下：

.. tabs::

    .. tab:: C++

        .. sourcecode:: c++

            MainWindow mwnd(DEMO_NAME);
            ConstraintLayout centerLayout;
            mwnd.setContent(&centerLayout);

            ConstraintLayout::GeoInfo geoInfo = {};

            Label themeLbl(L"Theme mode");
            themeLbl.setHeight(40);
            themeLbl.setHorzAlign(Label::HCenter);
            geoInfo = {};
            geoInfo.keepWidth = false;
            geoInfo.Left.ToLeft = 50;
            geoInfo.Right.ToLeft = 350;
            geoInfo.keepHeight = true;
            geoInfo.Top.ToTop = 100;
            centerLayout.addElement(&themeLbl, geoInfo);

            ComboBox themeSelector;
            themeSelector.setHeight(40);
            geoInfo = {};
            geoInfo.keepWidth = false;
            geoInfo.Left.ToRight = 350;
            geoInfo.Right.ToRight = 50;
            geoInfo.keepHeight = true;
            geoInfo.Top.ToTop = 100;
            centerLayout.addElement(&themeSelector, geoInfo);
            themeSelector.setRoundRadius(5);

            auto menu = themeSelector.dropDownMenu();

            ComboBoxItem items[3];
            items[0].setText(L"Light");
            items[1].setText(L"Dark");
            items[2].setText(L"Use system setting");

            std::list<MenuItem*> pItems;
            for (auto& item : items)
            {
                pItems.push_back(&item);
            }
            menu->appendItem(pItems);

            menu->setWidth(themeSelector.width());
            menu->setHeight(_countof(items) * 40);
            menu->setRoundExtension(5);

            themeSelector.setCurrSelected(2);

    .. tab:: Python

        .. sourcecode:: python

            mwnd = MainWindow(DEMO_NAME)
            centerLayout = ConstraintLayout()
            mwnd.content = centerLayout

            themeLbl = Label('Theme mode')
            themeLbl.height = 40
            themeLbl.horzAlign = Label.HCenter
            geoInfo = ConstraintLayout.GeoInfo()
            geoInfo.keepWidth = False
            geoInfo.Left.ToLeft = 50
            geoInfo.Right.ToLeft = 350
            geoInfo.keepHeight = True
            geoInfo.Top.ToTop = 100
            centerLayout.addElement(themeLbl, geoInfo)

            themeSelector = ComboBox()
            themeSelector.height = 40
            geoInfo = ConstraintLayout.GeoInfo()
            geoInfo.keepWidth = False
            geoInfo.Left.ToRight = 350
            geoInfo.Right.ToRight = 50
            geoInfo.keepHeight = True
            geoInfo.Top.ToTop = 100
            centerLayout.addElement(themeSelector, geoInfo)
            themeSelector.roundRadius = 5

            menu = themeSelector.dropDownMenu

            items = [ComboBoxItem() for i in range(3)]
            items[0].text = 'Light'
            items[1].text = 'Dark'
            items[2].text = 'Use system setting'

            menu.appendItem(items)

            menu.width = themeSelector.width
            menu.height = len(items) * 40
            menu.roundExtension = 5

            themeSelector.setCurrSelected(2)

最后编写回调函数如下：

.. tabs::

    .. tab:: C++

        .. sourcecode:: c++

            themeSelector.D14_onSelectedChange(ComboBox, obj, text)
            {
                auto app = Application::app();
                if (text == L"Light" || text == L"Dark")
                {
                    app->setThemeMode(text);
                }
                else if (text == L"Use system setting")
                {
                    app->setUseSystemTheme(true);
                }
            };

    .. tab:: Python

        .. sourcecode:: python

            def changeThemeMode(obj, text):
                app = Application.app
                if text == 'Light' or text == 'Dark':
                    app.themeMode = text
                elif text == 'Use system setting':
                    app.useSystemTheme = True
            themeSelector.f_onSelectedChange = changeThemeMode
