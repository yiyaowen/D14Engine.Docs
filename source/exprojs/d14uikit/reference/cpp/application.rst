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

.. _d14uikit-reference-cpp-application-isntm-visible:

  **bool visible() const**

.. _d14uikit-reference-cpp-application-isntm-set_visible:

  **void setVisible(bool value)**

.. _d14uikit-reference-cpp-application-isntm-minimized:

  **bool minimized() const**

.. _d14uikit-reference-cpp-application-isntm-set_minimized:

  **void setMinimized(bool value)**

.. _d14uikit-reference-cpp-application-isntm-maximized:

  **bool maximized() const**

.. _d14uikit-reference-cpp-application-isntm-set_maximized:

  **void setMaximized(bool value)**

.. _d14uikit-reference-cpp-application-isntm-size:

  **Size size() const**

.. _d14uikit-reference-cpp-application-isntm-set_size:

  **void setSize(const Size& value)**

.. _d14uikit-reference-cpp-application-isntm-width:

  **int width() const**

.. _d14uikit-reference-cpp-application-isntm-set_width:

  **void setWidth(int value)**

.. _d14uikit-reference-cpp-application-isntm-height:

  **int height() const**

.. _d14uikit-reference-cpp-application-isntm-set_height:

  **void setHeight(int value)**

.. _d14uikit-reference-cpp-application-isntm-position:

  **Point position() const**

.. _d14uikit-reference-cpp-application-isntm-set_position:

  **void setPosition(const Point& value)**

.. _d14uikit-reference-cpp-application-isntm-x:

  **int x() const**

.. _d14uikit-reference-cpp-application-isntm-set_x:

  **void setX(int value)**

.. _d14uikit-reference-cpp-application-isntm-y:

  **int y() const**

.. _d14uikit-reference-cpp-application-isntm-set_y:

  **void setY(int value)**

.. _d14uikit-reference-cpp-application-isntm-min_size:

  **Size minSize() const**

.. _d14uikit-reference-cpp-application-isntm-set_min_size:

  **void setMinSize(const Size& value)**

.. _d14uikit-reference-cpp-application-isntm-min_width:

  **int minWidth() const**

.. _d14uikit-reference-cpp-application-isntm-set_min_width:

  **void setMinWidth(int value)**

.. _d14uikit-reference-cpp-application-isntm-min_height:

  **int minHeight() const**

.. _d14uikit-reference-cpp-application-isntm-set_min_height:

  **void setMinHeight(int value)**

.. _d14uikit-reference-cpp-application-isntm-resizable:

  **bool resizable() const**

.. _d14uikit-reference-cpp-application-isntm-set_resizable:

  **void setResizable(bool value)**

.. _d14uikit-reference-cpp-application-isntm-fullscreen:

  **bool fullscreen() const**

.. _d14uikit-reference-cpp-application-isntm-set_fullscreen:

  **void setFullscreen(bool value)**

.. _d14uikit-reference-cpp-application-isntm-fps:

  **int fps() const**

.. _d14uikit-reference-cpp-application-isntm-low_energy:

  **bool lowEnergy() const**

.. _d14uikit-reference-cpp-application-isntm-set_low_energy:

  **void setLowEnergy(bool value)**

.. _d14uikit-reference-cpp-application-isntm-theme_mode:

  **const std::wstring& themeMode() const**

.. _d14uikit-reference-cpp-application-isntm-set_theme_mode:

  **void setThemeMode(const std::wstring& name)**

.. _d14uikit-reference-cpp-application-isntm-theme_color:

  **Color themeColor() const**

.. _d14uikit-reference-cpp-application-isntm-set_theme_color:

  **void setThemeColor(const Color& value)**

.. _d14uikit-reference-cpp-application-isntm-use_system_theme:

  **bool useSystemTheme() const**

.. _d14uikit-reference-cpp-application-isntm-set_use_system_theme:

  **void setUseSystemTheme(bool value)**

.. _d14uikit-reference-cpp-application-isntm-lang_locale:

  **const std::wstring& langLocale() const**

.. _d14uikit-reference-cpp-application-isntm-set_lang_locale:

  **void setLangLocale(const std::wstring& name)**

.. _d14uikit-reference-cpp-application-isntm-clear_type:

  **bool clearType() const**

.. _d14uikit-reference-cpp-application-isntm-set_clear_type:

  **void setClearType(bool value)**

.. _d14uikit-reference-cpp-application-isntm-text_vert_smooth:

  **bool textVertSmooth() const**

.. _d14uikit-reference-cpp-application-isntm-set_text_vert_smooth:

  **void setTextVertSmooth(bool value)**

.. _d14uikit-reference-cpp-application-isntm-bmp_quality_interp:

  **bool bmpQualityInterp() const**

.. _d14uikit-reference-cpp-application-isntm-set_bmp_quality_interp:

  **void setBmpQualityInterp(bool value)**

.. _d14uikit-reference-cpp-application-isntm-capture:

  **std::unique_ptr<Image> capture() const**
