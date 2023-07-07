.. _d14uikit-reference-cpp-ui_controls-panel:

Panel
=====

概述
----

.. list-table::
    :width: 100%
    :widths: 30, 70

    * - 头文件
      - Panel.h
    * - 继承自
      - NonCopyable

XXXX

构造函数
--------

.. list-table::
    :width: 100%

    * - :ref:`Panel<d14uikit-reference-cpp-ui_controls-panel-ctor-1>` ()

实例方法
--------

.. list-table::
    :width: 100%
    :widths: 30, 60, 10

    * - bool
      - :ref:`destory<d14uikit-reference-cpp-ui_controls-panel-isntm-destory>` ()
      -
    * - bool
      - :ref:`visible<d14uikit-reference-cpp-ui_controls-panel-isntm-visible>` ()
      - const
    * - void
      - :ref:`setVisible<d14uikit-reference-cpp-ui_controls-panel-isntm-set_visible>` (bool value)
      -
    * - bool
      - :ref:`enabled<d14uikit-reference-cpp-ui_controls-panel-isntm-enabled>` ()
      - const
    * - void
      - :ref:`setEnabled<d14uikit-reference-cpp-ui_controls-panel-isntm-set_enabled>` (bool value)
      -
    * - Size
      - :ref:`size<d14uikit-reference-cpp-ui_controls-panel-isntm-size>` ()
      - const
    * - void
      - :ref:`setSize<d14uikit-reference-cpp-ui_controls-panel-isntm-set_size>` (const Size& value)
      -
    * - int
      - :ref:`width<d14uikit-reference-cpp-ui_controls-panel-isntm-width>` ()
      - const
    * - void
      - :ref:`setWidth<d14uikit-reference-cpp-ui_controls-panel-isntm-set_width>` (int value)
      -
    * - int
      - :ref:`height<d14uikit-reference-cpp-ui_controls-panel-isntm-height>` ()
      - const
    * - void
      - :ref:`setHeight<d14uikit-reference-cpp-ui_controls-panel-isntm-set_height>` (int value)
      -
    * - Point
      - :ref:`position<d14uikit-reference-cpp-ui_controls-panel-isntm-position>` ()
      - const
    * - void
      - :ref:`setPosition<d14uikit-reference-cpp-ui_controls-panel-isntm-set_position>` (const Point& value)
      -
    * - int
      - :ref:`x<d14uikit-reference-cpp-ui_controls-panel-isntm-x>` ()
      - const
    * - void
      - :ref:`setX<d14uikit-reference-cpp-ui_controls-panel-isntm-set_x>` (int value)
      -
    * - int
      - :ref:`y<d14uikit-reference-cpp-ui_controls-panel-isntm-y>` ()
      - const
    * - void
      - :ref:`setY<d14uikit-reference-cpp-ui_controls-panel-isntm-set_y>` (int value)
      -
    * - Color
      - :ref:`color<d14uikit-reference-cpp-ui_controls-panel-isntm-color>` ()
      - const
    * - void
      - :ref:`setColor<d14uikit-reference-cpp-ui_controls-panel-isntm-set_color>` (const Color& value)
      -
    * - float
      - :ref:`opacity<d14uikit-reference-cpp-ui_controls-panel-isntm-opacity>` ()
      - const
    * - void
      - :ref:`setOpacity<d14uikit-reference-cpp-ui_controls-panel-isntm-set_opacity>` (float value)
      -
    * - int
      - :ref:`outlineWidth<d14uikit-reference-cpp-ui_controls-panel-isntm-outline_width>` ()
      - const
    * - void
      - :ref:`setOutlineWidth<d14uikit-reference-cpp-ui_controls-panel-isntm-set_outline_width>` (int value)
      -
    * - Color
      - :ref:`outlineColor<d14uikit-reference-cpp-ui_controls-panel-isntm-outline_color>` ()
      - const
    * - void
      - :ref:`setOutlineColor<d14uikit-reference-cpp-ui_controls-panel-isntm-set_outline_color>` (const Color& value)
      -
    * - float
      - :ref:`outlineOpacity<d14uikit-reference-cpp-ui_controls-panel-isntm-outline_opacity>` ()
      - const
    * - void
      - :ref:`setOutlineOpacity<d14uikit-reference-cpp-ui_controls-panel-isntm-set_outline_opacity>` (float value)
      -
    * - Image*
      - :ref:`image<d14uikit-reference-cpp-ui_controls-panel-isntm-image>` ()
      - const
    * - void
      - :ref:`setImage<d14uikit-reference-cpp-ui_controls-panel-isntm-set_image>` (Image* imgae)
      -
    * - int
      - :ref:`roundRadius<d14uikit-reference-cpp-ui_controls-panel-isntm-round_radius>` ()
      - const
    * - void
      - :ref:`setRoundRadius<d14uikit-reference-cpp-ui_controls-panel-isntm-set_round_radius>` (int value)
      -
    * - void
      - :ref:`setGlobal<d14uikit-reference-cpp-ui_controls-panel-isntm-set_global>` (bool value)
      -
    * - void
      - :ref:`setFocused<d14uikit-reference-cpp-ui_controls-panel-isntm-set_focused>` (bool value)
      -
    * - Panel*
      - :ref:`parent<d14uikit-reference-cpp-ui_controls-panel-isntm-parent>` ()
      - const
    * - void
      - :ref:`setParent<d14uikit-reference-cpp-ui_controls-panel-isntm-set_parent>` (Panel* uiobj)
      -
    * - void
      - :ref:`addChild<d14uikit-reference-cpp-ui_controls-panel-isntm-add_child>` (Panel* uiobj)
      -
    * - void
      - :ref:`removeChild<d14uikit-reference-cpp-ui_controls-panel-isntm-remove_child>` (Panel* uiobj)
      -
    * - void
      - :ref:`moveTopmost<d14uikit-reference-cpp-ui_controls-panel-isntm-move_topmost>` ()
      -
    * - void
      - :ref:`moveAbove<d14uikit-reference-cpp-ui_controls-panel-isntm-move_above>` (Panel* uiobj)
      -
    * - void
      - :ref:`moveBelow<d14uikit-reference-cpp-ui_controls-panel-isntm-move_below>` (Panel* uiobj)
      -

回调函数
--------

.. list-table::
    :width: 100%
    :widths: 30, 70

    * - virtual void
      - :ref:`onUpdate<d14uikit-reference-cpp-ui_controls-panel-virtm-on_update>` ()
    * - virtual void
      - :ref:`onSize<d14uikit-reference-cpp-ui_controls-panel-virtm-on_size>` (SizeEvent* event)
    * - virtual void
      - :ref:`onMove<d14uikit-reference-cpp-ui_controls-panel-virtm-on_move>` (MoveEvent* event)
    * - virtual void
      - :ref:`onChangeTheme<d14uikit-reference-cpp-ui_controls-panel-virtm-on_change_theme>` (const std::wstring& name)
    * - virtual void
      - :ref:`onChangeLangLocale<d14uikit-reference-cpp-ui_controls-panel-virtm-on_change_lang_locale>` (const std::wstring& name)
    * - virtual void
      - :ref:`onGetFocus<d14uikit-reference-cpp-ui_controls-panel-virtm-on_get_focus>` ()
    * - virtual void
      - :ref:`onLoseFocus<d14uikit-reference-cpp-ui_controls-panel-virtm-on_lose_focus>` ()
    * - virtual void
      - :ref:`onMouseEnter<d14uikit-reference-cpp-ui_controls-panel-virtm-on_mouse_enter>` (MouseMoveEvent* event)
    * - virtual void
      - :ref:`onMouseMove<d14uikit-reference-cpp-ui_controls-panel-virtm-on_mouse_move>` (MouseMoveEvent* event)
    * - virtual void
      - :ref:`onMouseLeave<d14uikit-reference-cpp-ui_controls-panel-virtm-on_mouse_leave>` (MouseMoveEvent* event)
    * - virtual void
      - :ref:`onMouseButton<d14uikit-reference-cpp-ui_controls-panel-virtm-on_mouse_button>` (MouseButtonEvent* event)
    * - virtual void
      - :ref:`onMouseWheel<d14uikit-reference-cpp-ui_controls-panel-virtm-on_mouse_wheel>` (MouseWheelEvent* event)
    * - virtual void
      - :ref:`onKeyboard<d14uikit-reference-cpp-ui_controls-panel-virtm-on_keyboard>` (KeyboardEvent* event)

评述
----

XXXX

详述
----

.. _d14uikit-reference-cpp-ui_controls-panel-ctor-1:

  **Panel()**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-destory:

  **bool destory()**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-visible:

  **bool visible() const**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_visible:

  **void setVisible(bool value)**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-enabled:

  **bool enabled() const**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_enabled:

  **void setEnabled(bool value)**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-size:

  **Size size() const**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_size:

  **void setSize(const Size& value)**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-width:

  **int width() const**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_width:

  **void setWidth(int value)**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-height:

  **int height() const**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_height:

  **void setHeight(int value)**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-position:

  **Point position() const**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_position:

  **void setPosition(const Point& value)**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-x:

  **int x() const**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_x:

  **void setX(int value)**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-y:

  **int y() const**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_y:

  **void setY(int value)**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-color:

  **Color color() const**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_color:

  **void setColor(const Color& value)**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-opacity:

  **float opacity() const**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_opacity:

  **void setOpacity(float value)**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-outline_width:

  **int outlineWidth() const**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_outline_width:

  **void setOutlineWidth(int value)**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-outline_color:

  **Color outlineColor() const**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_outline_color:

  **void setOutlineColor(const Color& value)**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-outline_opacity:

  **float outlineOpacity() const**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_outline_opacity:

  **void setOutlineOpacity(float value)**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-image:

  **Image* image() const**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_image:

  **void setImage(Image* imgae)**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-round_radius:

  **int roundRadius() const**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_round_radius:

  **void setRoundRadius(int value)**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_global:

  **void setGlobal(bool value)**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_focused:

  **void setFocused(bool value)**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-parent:

  **Panel* parent() const**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_parent:

  **void setParent(Panel* uiobj)**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-add_child:

  **void addChild(Panel* uiobj)**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-remove_child:

  **void removeChild(Panel* uiobj)**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-move_topmost:

  **void moveTopmost()**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-move_above:

  **void moveAbove(Panel* uiobj)**

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-move_below:

  **void moveBelow(Panel* uiobj)**

.. _d14uikit-reference-cpp-ui_controls-panel-virtm-on_update:

  **virtual void onUpdate()**

.. _d14uikit-reference-cpp-ui_controls-panel-virtm-on_size:

  **virtual void onSize(SizeEvent* event)**

.. _d14uikit-reference-cpp-ui_controls-panel-virtm-on_move:

  **virtual void onMove(MoveEvent* event)**

.. _d14uikit-reference-cpp-ui_controls-panel-virtm-on_change_theme:

  **virtual void onChangeTheme(const std::wstring& name)**

.. _d14uikit-reference-cpp-ui_controls-panel-virtm-on_change_lang_locale:

  **virtual void onChangeLangLocale(const std::wstring& name)**

.. _d14uikit-reference-cpp-ui_controls-panel-virtm-on_get_focus:

  **virtual void onGetFocus()**

.. _d14uikit-reference-cpp-ui_controls-panel-virtm-on_lose_focus:

  **virtual void onLoseFocus()**

.. _d14uikit-reference-cpp-ui_controls-panel-virtm-on_mouse_enter:

  **virtual void onMouseEnter(MouseMoveEvent* event)**

.. _d14uikit-reference-cpp-ui_controls-panel-virtm-on_mouse_move:

  **virtual void onMouseMove(MouseMoveEvent* event)**

.. _d14uikit-reference-cpp-ui_controls-panel-virtm-on_mouse_leave:

  **virtual void onMouseLeave(MouseMoveEvent* event)**

.. _d14uikit-reference-cpp-ui_controls-panel-virtm-on_mouse_button:

  **virtual void onMouseButton(MouseButtonEvent* event)**

.. _d14uikit-reference-cpp-ui_controls-panel-virtm-on_mouse_wheel:

  **virtual void onMouseWheel(MouseWheelEvent* event)**

.. _d14uikit-reference-cpp-ui_controls-panel-virtm-on_keyboard:

  **virtual void onKeyboard(KeyboardEvent* event)**
