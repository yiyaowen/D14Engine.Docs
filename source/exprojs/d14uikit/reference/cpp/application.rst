.. _d14uikit-reference-cpp-application:

Application
===========

概述
----

.. list-table::
  :width: 100%
  :widths: 30, 70

  * - 头文件
    - Application.h
  * - 继承自
    - NonCopyable

Application 是用于创建 D14UIKit 应用程序的核心类，其封装了基于 DirectX 的渲染器、基于 Win32 消息队列的主窗口和用于管理所有 UI 对象的无序集合。

构造函数
--------

.. list-table::
  :width: 100%

  * - :ref:`Application<d14uikit-reference-cpp-application-ctor-1>` (const std::wstring& name = L"D14UIKit", const std::optional<float>& dpi = std::nullopt)

静态方法
--------

.. list-table::
  :width: 100%
  :widths: 30, 70

  * - Application*
    - :ref:`app<d14uikit-reference-cpp-application-sttcm-app>` ()

实例方法
--------

.. list-table::
  :width: 100%
  :widths: 30, 60, 10

  * - Cursor*
    - :ref:`cursor<d14uikit-reference-cpp-application-isntm-cursor>` ()
    - const
  * - int
    - :ref:`run<d14uikit-reference-cpp-application-isntm-run>` ()
    - const
  * - void
    - :ref:`exit<d14uikit-reference-cpp-application-isntm-exit>` ()
    - const
  * - bool
    - :ref:`visible<d14uikit-reference-cpp-application-isntm-visible>` ()
    - const
  * - void
    - :ref:`setVisible<d14uikit-reference-cpp-application-isntm-set_visible>` (bool value)
    -
  * - bool
    - :ref:`minimized<d14uikit-reference-cpp-application-isntm-minimized>` ()
    - const
  * - void
    - :ref:`setMinimized<d14uikit-reference-cpp-application-isntm-set_minimized>` (bool value)
    -
  * - bool
    - :ref:`maximized<d14uikit-reference-cpp-application-isntm-maximized>` ()
    - const
  * - void
    - :ref:`setMaximized<d14uikit-reference-cpp-application-isntm-set_maximized>` (bool value)
    -
  * - Size
    - :ref:`size<d14uikit-reference-cpp-application-isntm-size>` ()
    - const
  * - void
    - :ref:`setSize<d14uikit-reference-cpp-application-isntm-set_size>` (const Size& value)
    -
  * - int
    - :ref:`width<d14uikit-reference-cpp-application-isntm-width>` ()
    - const
  * - void
    - :ref:`setWidth<d14uikit-reference-cpp-application-isntm-set_width>` (int value)
    -
  * - int
    - :ref:`height<d14uikit-reference-cpp-application-isntm-height>` ()
    - const
  * - void
    - :ref:`setHeight<d14uikit-reference-cpp-application-isntm-set_height>` (int value)
    -
  * - Point
    - :ref:`position<d14uikit-reference-cpp-application-isntm-position>` ()
    - const
  * - void
    - :ref:`setPosition<d14uikit-reference-cpp-application-isntm-set_position>` (const Point& value)
    -
  * - int
    - :ref:`x<d14uikit-reference-cpp-application-isntm-x>` ()
    - const
  * - void
    - :ref:`setX<d14uikit-reference-cpp-application-isntm-set_x>` (int value)
    -
  * - int
    - :ref:`y<d14uikit-reference-cpp-application-isntm-y>` ()
    - const
  * - void
    - :ref:`setY<d14uikit-reference-cpp-application-isntm-set_y>` (int value)
    -
  * - Size
    - :ref:`minSize<d14uikit-reference-cpp-application-isntm-min_size>` ()
    - const
  * - void
    - :ref:`setMinSize<d14uikit-reference-cpp-application-isntm-set_min_size>` (const Size& value)
    -
  * - int
    - :ref:`minWidth<d14uikit-reference-cpp-application-isntm-min_width>` ()
    - const
  * - void
    - :ref:`setMinWidth<d14uikit-reference-cpp-application-isntm-set_min_width>` (int value)
    -
  * - int
    - :ref:`minHeight<d14uikit-reference-cpp-application-isntm-min_height>` ()
    - const
  * - void
    - :ref:`setMinHeight<d14uikit-reference-cpp-application-isntm-set_min_height>` (int value)
    -
  * - bool
    - :ref:`resizable<d14uikit-reference-cpp-application-isntm-resizable>` ()
    - const
  * - void
    - :ref:`setResizable<d14uikit-reference-cpp-application-isntm-set_resizable>` (bool value)
    -
  * - bool
    - :ref:`fullscreen<d14uikit-reference-cpp-application-isntm-fullscreen>` ()
    - const
  * - void
    - :ref:`setFullscreen<d14uikit-reference-cpp-application-isntm-set_fullscreen>` (bool value)
    -
  * - int
    - :ref:`fps<d14uikit-reference-cpp-application-isntm-fps>` ()
    - const
  * - bool
    - :ref:`lowEnergy<d14uikit-reference-cpp-application-isntm-low_energy>` ()
    - const
  * - void
    - :ref:`setLowEnergy<d14uikit-reference-cpp-application-isntm-set_low_energy>` (bool value)
    -
  * - const std::wstring&
    - :ref:`themeMode<d14uikit-reference-cpp-application-isntm-theme_mode>` ()
    - const
  * - void
    - :ref:`setThemeMode<d14uikit-reference-cpp-application-isntm-set_theme_mode>` (const std::wstring& name)
    -
  * - Color
    - :ref:`themeColor<d14uikit-reference-cpp-application-isntm-theme_color>` ()
    - const
  * - void
    - :ref:`setThemeColor<d14uikit-reference-cpp-application-isntm-set_theme_color>` (const Color& value)
    -
  * - bool
    - :ref:`useSystemTheme<d14uikit-reference-cpp-application-isntm-use_system_theme>` ()
    - const
  * - void
    - :ref:`setUseSystemTheme<d14uikit-reference-cpp-application-isntm-set_use_system_theme>` (bool value)
    -
  * - const std::wstring&
    - :ref:`langLocale<d14uikit-reference-cpp-application-isntm-lang_locale>` ()
    - const
  * - void
    - :ref:`setLangLocale<d14uikit-reference-cpp-application-isntm-set_lang_locale>` (const std::wstring& name)
    -
  * - bool
    - :ref:`clearType<d14uikit-reference-cpp-application-isntm-clear_type>` ()
    - const
  * - void
    - :ref:`setClearType<d14uikit-reference-cpp-application-isntm-set_clear_type>` (bool value)
    -
  * - bool
    - :ref:`textVertSmooth<d14uikit-reference-cpp-application-isntm-text_vert_smooth>` ()
    - const
  * - void
    - :ref:`setTextVertSmooth<d14uikit-reference-cpp-application-isntm-set_text_vert_smooth>` (bool value)
    -
  * - bool
    - :ref:`bmpQualityInterp<d14uikit-reference-cpp-application-isntm-bmp_quality_interp>` ()
    - const
  * - void
    - :ref:`setBmpQualityInterp<d14uikit-reference-cpp-application-isntm-set_bmp_quality_interp>` (bool value)
    -
  * - std::unique_ptr<Image>
    - :ref:`capture<d14uikit-reference-cpp-application-isntm-capture>` ()
    - const

评述
----

对于一个标准的 D14UIKit 应用程序来说，Application 的创建是必不可少的，因此在起草一个全新的 D14UIKit 项目时，往往会用到以下模板：

.. code-block:: c++
  :emphasize-lines: 9

  #include "Application.h"

  using namespace d14uikit;

  int main(int argc, char* argv[])
  {
      Application app;

      // Add code here.

      return app.run();
  }

Application 内部封装有一个 Win32 层面的 ``窗口``、一个 DirectX 层面的 ``渲染器`` 以及其它 ``辅助组件``：针对 Win32 窗口，Application 导出了一些和窗口的尺寸、位置等有关的方法；针对 DirectX 渲染器，Application 还导出了一些和帧率、显示等有关的方法；此外 Application 还提供了一些诸如获取鼠标指针对象、改变主题等的方法（这些特性由 D14UIKit 的架构决定）。

详述
----

.. _d14uikit-reference-cpp-application-ctor-1:

  **explicit Application(const std::wstring& name = L"D14UIKit", const std::optional<float>& dpi = std::nullopt)**

Application 的显式构造函数。

* **参数**

  * ``name``

    类型：**const std::wstring&**

    默认值：**L"D14UIKit"**

    应用程序的名称。Application 内部在创建 Win32 窗口时也会用其来注册新的窗口类，并将窗口的标题初始化为该参数，因此这也是该程序在任务栏缩略图、任务管理器等界面中所显示的名称。

  * ``dpi``

    类型：**const std::optional<float>&**

    默认值：**std::nullopt**

    应用程序的缩放。可以为 float 范围内任意大于 0 的值，或传入空值来使用系统当前的缩放设置，该参数的典型值如下：

    .. list-table::
      :header-rows: 1
      :width: 100%

      * - 缩放
        - DPI 值
        - 适用的分辨率（仅供参考）
      * - 100%
        - 96 dpi
        - 1080p（FHD）、2K（QHD）
      * - 150%
        - 144 dpi
        - 2K（QHD）、4K（UHD）
      * - 200%
        - 192 dpi
        - 4K（UHD）、8K（FUHD）

    由于 D14UIKit 在内部使用了离屏渲染（也即 Offscreen Texture）来完成某些 UI 对象的裁剪显示，并依赖于 Direct2D 的 DIP 坐标系统来保证兼容性，因此非 96 dpi 整数倍的 DPI 值可能会导致显示模糊，之所以说“可能”是因为它还取决于 UI 对象的实际尺寸：在 125% 缩放（也即 120 dpi）下，为了渲染一张 100 dip X 100 dip 的图像，只需在后台创建一个 125 px X 125 px 的缓冲区；但是对于一张 90 dip X 90 dip 的图像，缓冲区的大小为 112.5 px X 112.5 px，而像素阵列是离散的，我们只能将其修正为 112 px 或 113 px，然后再将其放大或缩小至相应的屏幕区域（图像模糊）。

    教程 :ref:`d14uikit-tutorials-hello_window_dpi` 对 DPI 进行了简要的介绍。

.. _d14uikit-reference-cpp-application-sttcm-app:

  **static Application* app()**

获取全局 Application 对象的指针。

* **返回值**

  类型：**Application***

  全局 Application 对象的指针。

* **备注**

  在编写某些不带有 app 参数的回调函数时常常会用到该方法。例如点击按钮退出程序的功能：

  .. code-block:: c++
    :emphasize-lines: 3

    button.D14_onMouseButtonRelease(clkp, e, )
    {
        Application::app()->exit();
    };

  该宏定义了一个 lambda，如果不使用此静态方法，则需要确保 app 变量能被 lambda 捕捉到：

  .. code-block:: c++
    :emphasize-lines: 3

    Application app;

    button.D14_onMouseButtonRelease(clkp, e, &)
    {
        app.exit(); // captured by reference
    };

.. _d14uikit-reference-cpp-application-isntm-cursor:

  **Cursor* cursor() const**

获取应用程序创建的 Cursor 对象的指针。

* **返回值**

  类型：**Cursor***

  应用程序创建的 Cursor 对象的指针。

.. _d14uikit-reference-cpp-application-isntm-run:

  **int run() const**

启动应用程序。

* **返回值**

  类型：**int**

  应用程序的退出代码。

* **备注**

  该方法一般只需要在应用程序初始化完毕后调用一次，启动后开始循环处理 Win32 窗口消息，并且在必要时渲染画面。退出代码实际上就是 WM_QUIT 消息携带的 WPARAM 字段。

.. _d14uikit-reference-cpp-application-isntm-exit:

  **void exit() const**

退出应用程序。

* **备注**

  该方法实际上通过发送 WM_QUIT 消息来通知系统终止 Win32 窗口的消息循环。此外它并不接收用于决定退出代码的参数，这是因为调用该方法意味着应用程序是正常终止的。如果需要在应用程序崩溃时通过退出代码来传递信息（不推荐），则只能通过标准库的 exit 系列函数来完成。

.. _d14uikit-reference-cpp-application-isntm-visible:

  **bool visible() const**

判断主窗口是否可见。

* **返回值**

  类型：**bool**

  .. list-table::
    :width: 100%

    * - true
      - 可见
    * - false
      - 不可见

.. _d14uikit-reference-cpp-application-isntm-set_visible:

  **void setVisible(bool value)**

设置主窗口是否可见。

* **参数**

  * ``value``

    类型：**bool**

    .. list-table::
      :width: 100%

      * - true
        - 显示主窗口。
      * - false
        - 隐藏主窗口。

.. _d14uikit-reference-cpp-application-isntm-minimized:

  **bool minimized() const**

获取主窗口的最小化状态。

* **返回值**

  类型：**bool**

  .. list-table::
    :width: 100%

    * - true
      - 最小化
    * - false
      - 非最小化

.. _d14uikit-reference-cpp-application-isntm-set_minimized:

  **void setMinimized(bool value)**

设置主窗口的最小化状态。

* **参数**

  * ``value``

    类型：**bool**

    .. list-table::
      :width: 100%

      * - true
        - 最小化主窗口。如果主窗口已经最小化，则无事发生。
      * - false
        - 如果主窗口已经最小化，则恢复到正常状态；否则无事发生。

.. _d14uikit-reference-cpp-application-isntm-maximized:

  **bool maximized() const**

获取主窗口的最大化状态。

* **返回值**

  类型：**bool**

  .. list-table::
    :width: 100%

    * - true
      - 最大化
    * - false
      - 非最大化

.. _d14uikit-reference-cpp-application-isntm-set_maximized:

  **void setMaximized(bool value)**

设置主窗口的最大化状态。

* **参数**

  * ``value``

    类型：**bool**

    .. list-table::
      :width: 100%

      * - true
        - 最大化主窗口。如果主窗口已经最大化，则无事发生。
      * - false
        - 如果主窗口已经最大化，则恢复到正常状态；否则无事发生。

.. _d14uikit-reference-cpp-application-isntm-size:

  **Size size() const**

获取主窗口的 DIP 尺寸。

* **返回值**

  类型：**Size**

  以 DIP 为单位的尺寸。

.. _d14uikit-reference-cpp-application-isntm-set_size:

  **void setSize(const Size& value)**

设置主窗口的 DIP 尺寸。

* **参数**

  * ``value``

    类型：**const Size&**

    以 DIP 为单位的尺寸。

.. _d14uikit-reference-cpp-application-isntm-width:

  **int width() const**

获取主窗口的 DIP 宽度。

* **返回值**

  类型：**int**

  以 DIP 为单位的宽度。

.. _d14uikit-reference-cpp-application-isntm-set_width:

  **void setWidth(int value)**

设置主窗口的 DIP 宽度。

* **参数**

  * ``value``

    类型：**int**

    以 DIP 为单位的宽度。

.. _d14uikit-reference-cpp-application-isntm-height:

  **int height() const**

获取主窗口的 DIP 高度。

* **返回值**

  类型：**int**

  以 DIP 为单位的高度。

.. _d14uikit-reference-cpp-application-isntm-set_height:

  **void setHeight(int value)**

设置主窗口的 DIP 高度。

* **参数**

  * ``value``

    类型：**int**

    以 DIP 为单位的高度。

.. _d14uikit-reference-cpp-application-isntm-position:

  **Point position() const**

获取主窗口的 DIP 坐标（以屏幕左上角为原点）。

* **返回值**

  类型：**Point**

  以 DIP 为单位的坐标。

.. _d14uikit-reference-cpp-application-isntm-set_position:

  **void setPosition(const Point& value)**

设置主窗口的 DIP 坐标（以屏幕左上角为原点）。

* **参数**

  * ``value``

    类型：**const Point&**

    以 DIP 为单位的坐标。

.. _d14uikit-reference-cpp-application-isntm-x:

  **int x() const**

获取主窗口的 DIP 水平偏移（以屏幕左上角为原点）。

* **返回值**

  类型：**int**

  以 DIP 为单位的水平偏移。

.. _d14uikit-reference-cpp-application-isntm-set_x:

  **void setX(int value)**

设置主窗口的 DIP 水平偏移（以屏幕左上角为原点）。

* **参数**

  * ``value``

    类型：**int**

    以 DIP 为单位的水平偏移。

.. _d14uikit-reference-cpp-application-isntm-y:

  **int y() const**

获取主窗口的 DIP 垂直偏移（以屏幕左上角为原点）。

* **返回值**

  类型：**int**

  以 DIP 为单位的垂直偏移。

.. _d14uikit-reference-cpp-application-isntm-set_y:

  **void setY(int value)**

设置主窗口的 DIP 垂直偏移（以屏幕左上角为原点）。

* **参数**

  * ``value``

    类型：**int**

    以 DIP 为单位的垂直偏移。

.. _d14uikit-reference-cpp-application-isntm-min_size:

  **Size minSize() const**

获取主窗口的 DIP 最小尺寸。

* **返回值**

  类型：**Size**

  以 DIP 为单位的最小尺寸。

.. _d14uikit-reference-cpp-application-isntm-set_min_size:

  **void setMinSize(const Size& value)**

设置主窗口的 DIP 最小尺寸。

* **参数**

  * ``value``

    类型：**const Size&**

    以 DIP 为单位的最小尺寸。

.. _d14uikit-reference-cpp-application-isntm-min_width:

  **int minWidth() const**

获取主窗口的 DIP 最小宽度。

* **返回值**

  类型：**int**

  以 DIP 为单位的最小宽度。

.. _d14uikit-reference-cpp-application-isntm-set_min_width:

  **void setMinWidth(int value)**

设置主窗口的 DIP 最小宽度。

* **参数**

  * ``value``

    类型：**int**

    以 DIP 为单位的最小宽度。

.. _d14uikit-reference-cpp-application-isntm-min_height:

  **int minHeight() const**

获取主窗口的 DIP 最小高度。

* **返回值**

  类型：**int**

  以 DIP 为单位的最小高度。

.. _d14uikit-reference-cpp-application-isntm-set_min_height:

  **void setMinHeight(int value)**

设置主窗口的 DIP 最小高度。

* **参数**

  * ``value``

    类型：**int**

    以 DIP 为单位的最小高度。

.. _d14uikit-reference-cpp-application-isntm-resizable:

  **bool resizable() const**

判断主窗口是否可缩放。

* **返回值**

  类型：**bool**

  .. list-table::
    :width: 100%

    * - true
      - 可缩放
    * - false
      - 不可缩放

.. _d14uikit-reference-cpp-application-isntm-set_resizable:

  **void setResizable(bool value)**

设置主窗口是否可缩放。

* **参数**

  * ``value``

    类型：**bool**

    .. list-table::
      :width: 100%

      * - true
        - 启用主窗口缩放。
      * - false
        - 禁用主窗口缩放。

.. _d14uikit-reference-cpp-application-isntm-fullscreen:

  **bool fullscreen() const**

获取应用程序的显示状态（是否全屏）。

* **返回值**

  类型：**bool**

  .. list-table::
    :width: 100%

    * - true
      - 全屏化
    * - false
      - 窗口化

.. _d14uikit-reference-cpp-application-isntm-set_fullscreen:

  **void setFullscreen(bool value)**

设置应用程序的显示状态（是否全屏）。

* **参数**

  * ``value``

    类型：**bool**

    .. list-table::
      :width: 100%

      * - true
        - 全屏化应用程序。
      * - false
        - 窗口化应用程序。

.. _d14uikit-reference-cpp-application-isntm-fps:

  **int fps() const**

获取应用程序界面的刷新速率。

* **返回值**

  类型：**int**

  以 FPS 为单位的刷新速率。

.. _d14uikit-reference-cpp-application-isntm-low_energy:

  **bool lowEnergy() const**

获取应用程序的工作模式（是否全速渲染）。

* **返回值**

  类型：**bool**

  .. list-table::
    :width: 100%

    * - true
      - 节能模式（适用于界面元素变化不大的静态程序）
    * - false
      - 引擎模式（适用于游戏、视频等复杂的动态程序）

.. _d14uikit-reference-cpp-application-isntm-set_low_energy:

  **void setLowEnergy(bool value)**

设置应用程序的工作模式（是否全速渲染）。

* **参数**

  * ``value``

    类型：**bool**

    .. list-table::
      :width: 100%

      * - true
        - 启用节能模式，只在必要时渲染。
      * - false
        - 启用引擎模式，全速地实时渲染。

.. _d14uikit-reference-cpp-application-isntm-theme_mode:

  **const std::wstring& themeMode() const**

获取应用程序的主题模式。

* **返回值**

  类型：**const std::wstring&**

  .. list-table::
    :width: 100%

    * - Light
      - 浅色模式
    * - Dark
      - 深色模式

.. _d14uikit-reference-cpp-application-isntm-set_theme_mode:

  **void setThemeMode(const std::wstring& name)**

设置应用程序的主题模式。

* **参数**

  * ``name``

    类型：**const std::wstring&**

    主题模式的名称，目前只支持两种：

    .. list-table::
      :width: 100%

      * - Light
        - 切换浅色模式。
      * - Dark
        - 切换深色模式。

.. _d14uikit-reference-cpp-application-isntm-theme_color:

  **Color themeColor() const**

获取应用程序的主题颜色。

* **返回值**

  类型：**Color**

  应用程序的主题颜色。

.. _d14uikit-reference-cpp-application-isntm-set_theme_color:

  **void setThemeColor(const Color& value)**

设置应用程序的主题颜色。

* **参数**

  * ``value``

    类型：**const Color&**

    应用程序的主题颜色

.. _d14uikit-reference-cpp-application-isntm-use_system_theme:

  **bool useSystemTheme() const**

判断应用程序的主题是否跟随系统设置。

* **返回值**

  类型：**bool**

  .. list-table::
    :width: 100%

    * - true
      - 使用系统设置
    * - false
      - 不使用系统设置

.. _d14uikit-reference-cpp-application-isntm-set_use_system_theme:

  **void setUseSystemTheme(bool value)**

设置应用程序的主题是否跟随系统设置。

* **参数**

  * ``value``

    类型：**bool**

    .. list-table::
      :width: 100%

      * - true
        - 使用系统设置，适配模式和颜色。
      * - false
        - 不使用系统设置，用户可自定义。

.. _d14uikit-reference-cpp-application-isntm-lang_locale:

  **const std::wstring& langLocale() const**

获取应用程序的语言与区域。

* **返回值**

  类型：**const std::wstring&**

  xx-yy 式的语言与区域代码，例如：

  .. list-table::
    :width: 100%

    * - en-us
      - 美式英语
    * - zh-cn
      - 简体中文

.. _d14uikit-reference-cpp-application-isntm-set_lang_locale:

  **void setLangLocale(const std::wstring& name)**

设置应用程序的语言与区域。

* **参数**

  * ``name``

    类型：**const std::wstring&**

    xx-yy 式的语言与区域代码，例如：

    .. list-table::
      :width: 100%

      * - en-us
        - 美式英语
      * - zh-cn
        - 简体中文

.. _d14uikit-reference-cpp-application-isntm-clear_type:

  **bool clearType() const**

获取应用程序的字体渲染方案。

* **返回值**

  类型：**bool**

  .. list-table::
    :width: 100%

    * - true
      - ClearType
    * - false
      - Grayscale

.. _d14uikit-reference-cpp-application-isntm-set_clear_type:

  **void setClearType(bool value)**

设置应用程序的字体渲染方案。

* **参数**

  * ``value``

    类型：**bool**

    .. list-table::
      :width: 100%

      * - true
        - 使用 ClearType 技术，额外考虑背景色，彩色平滑。
      * - false
        - 使用 Grayscale 技术，仅考虑字形本身，灰色平滑。

.. _d14uikit-reference-cpp-application-isntm-text_vert_smooth:

  **bool textVertSmooth() const**

判断应用程序是否在垂直方向对字体进行平滑。

* **返回值**

  类型：**bool**

  .. list-table::
    :width: 100%

    * - true
      - 进行垂直平滑
    * - false
      - 不进行垂直平滑

.. _d14uikit-reference-cpp-application-isntm-set_text_vert_smooth:

  **void setTextVertSmooth(bool value)**

设置应用程序是否在垂直方向对字体进行平滑。

* **参数**

  * ``value``

    类型：**bool**

    .. list-table::
      :width: 100%

      * - true
        - 启用垂直平滑，显示更清晰，对性能有要求。
      * - false
        - 禁用垂直平滑，正常地显示，性能要求不高。

.. _d14uikit-reference-cpp-application-isntm-bmp_quality_interp:

  **bool bmpQualityInterp() const**

获取应用程序的图像插值方案。

* **返回值**

  类型：**bool**

  .. list-table::
    :width: 100%

    * - true
      - 高质量三次方插值
    * - false
      - 默认的线性插值

.. _d14uikit-reference-cpp-application-isntm-set_bmp_quality_interp:

  **void setBmpQualityInterp(bool value)**

设置应用程序的图像插值方案。

* **参数**

  * ``value``

    类型：**bool**

    .. list-table::
      :width: 100%

      * - true
        - 使用高质量三次方插值，显示更清晰，对性能有要求。
      * - false
        - 使用默认的线性插值，正常地显示，性能要求不高。

.. _d14uikit-reference-cpp-application-isntm-capture:

  **std::unique_ptr<Image> capture() const**

捕获应用程序主窗口的帧图像。

* **返回值**

  类型：**std::unique_ptr<Image>**

  应用程序主窗口的帧图像。

* **备注**

  通过该方法可以实现高性能截图，例如点击按钮保存图像的功能：

  .. code-block:: c++
    :emphasize-lines: 3

    button.D14_onMouseButtonRelease(clkp, e, )
    {
        auto frame = Application::app()->capture();

        // some intermediate operation

        frame->save(L"Screenshot.png");
    };
