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

详述
----

.. _d14uikit-reference-cpp-application-ctor-1:

  **explicit Application(const std::wstring& name = L"D14UIKit", const std::optional<float>& dpi = std::nullopt)**

.. _d14uikit-reference-cpp-application-sttcm-app:

  **static Application* app()**

.. _d14uikit-reference-cpp-application-isntm-cursor:

  **Cursor* cursor() const**

.. _d14uikit-reference-cpp-application-isntm-run:

  **int run() const**

.. _d14uikit-reference-cpp-application-isntm-exit:

  **void exit() const**

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
