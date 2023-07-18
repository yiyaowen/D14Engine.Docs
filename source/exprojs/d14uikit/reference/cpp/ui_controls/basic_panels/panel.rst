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

Panel 是 D14UIKit 中最为基本的 UI 对象，它代表了屏幕上的一块矩形区域，我们可以在其中绘制图像，或者放置其它的 UI 对象（作为子对象）。

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
  * - Point
    - :ref:`absPosition<d14uikit-reference-cpp-ui_controls-panel-isntm-abs_position>` ()
    - const
  * - void
    - :ref:`setPosition<d14uikit-reference-cpp-ui_controls-panel-isntm-set_position>` (const Point& value)
    -
  * - int
    - :ref:`x<d14uikit-reference-cpp-ui_controls-panel-isntm-x>` ()
    - const
  * - int
    - :ref:`absX<d14uikit-reference-cpp-ui_controls-panel-isntm-abs_x>` ()
    - const
  * - void
    - :ref:`setX<d14uikit-reference-cpp-ui_controls-panel-isntm-set_x>` (int value)
    -
  * - int
    - :ref:`y<d14uikit-reference-cpp-ui_controls-panel-isntm-y>` ()
    - const
  * - int
    - :ref:`absY<d14uikit-reference-cpp-ui_controls-panel-isntm-abs_y>` ()
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

.. note::

  每个包含新回调函数的类都持有一个访问受限的 Callback 对象，其中包含有与各回调函数同名的 functor 对象，通过设置这些 functor 对象，即可在不新建子类并重写相应虚函数的前提下实现对回调函数的重写。使用 ``callback`` 方法来引用回调对象：

  .. sourcecode:: c++

    panel.callback().onUpdate = [](Panel* p)
    {
        // do something to update the panel
    };

  相较于原始的回调函数，每个 functor 对象还提供了事件源对象的指针作为额外的第一个参数。

评述
----

* **外观**

  Panel 的背景可以是纯色块：

  .. sourcecode:: c++

    panel.setColor({ 255, 0, 0 });
    panel.setOpacity(1.0f);

  也可以是图像：

  .. sourcecode:: c++

    Image img(L"background.png");
    panel.setImage(&img);

  我们可以同时设置这两种背景，此时图像会显示在纯色背景之上，这在展示带有 Alpha 通道的图像时非常有用。除了背景之外，还可以设置边框：

  .. sourcecode:: c++

    panel.setOutlineColor({ 0, 255, 0 });
    panel.setOutlineOpacity(1.0f);

  边框会显示在图像和纯色背景之上。

* **层级**

  Panel 可以作为全局对象：

  .. sourcecode:: c++

    panel.setGlobal(true);

  也可以作为子对象：

  .. sourcecode:: c++

    panel.setGlobal(false);

  值得注意的是全局对象并非指主窗口 MainWindow 的子对象，而是由应用程序 Application 直接管理的对象。一般来说，主窗口 MainWindow 是直接创建为全局对象的，如果你希望设计某个 UI 对象并使其响应优先级在主窗口 MainWindow 之上（例如对话框），则可以考虑将其设置为全局对象。

  对于处于同一层级的对象（均为全局对象，或均为某对象的子对象），D14UIKit 还提供了优先级设置的功能，例如可以确保 a 显示在 b 之上：

  .. code-block:: c++
    :emphasize-lines: 4

    a.setParent(&panel);
    b.setParent(&panel);

    a.moveAbove(&b);

  或是直接为其指定最高优先级：

  .. sourcecode:: c++

    a.moveTopmost();

详述
----

.. _d14uikit-reference-cpp-ui_controls-panel-ctor-1:

  **Panel()**

Panel 的默认构造函数。

* **备注**

  Panel 默认具有 (0, 0) 的尺寸和 (0, 0) 的坐标（以父对象左上角为原点），背景和边框均为黑色（不透明度 = 0），并具有最低的优先级。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-destory:

  **bool destory()**

释放 UI 对象（引用计数减 1）。

* **返回值**

  类型：**bool**

  .. list-table::
    :width: 100%

    * - true
      - 操作成功
    * - false
      - 操作失败

* **备注**

  D14UIKit 使用引用计数管理 UI 对象，因此该方法不一定会导致析构函数被调用。该方法的典型用途是可以统一地释放任意 UI 对象，这主要是针对在不清楚该 UI 对象的层级关系（是全局对象？或是哪个对象的子对象？）的情况下仍然能够将其释放；值得注意的是，释放操作不一定会成功，这是由于某些特殊的 UI 对象（容器、视图等）会剥夺子对象的自我释放权来方便管理。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-visible:

  **bool visible() const**

判断 UI 对象是否可见。

* **返回值**

  类型：**bool**

  .. list-table::
    :width: 100%

    * - true
      - 可见
    * - false
      - 不可见

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_visible:

  **void setVisible(bool value)**

设置 UI 对象是否可见。

* **参数**

  * ``value``

    类型：**bool**

    .. list-table::
      :width: 100%

      * - true
        - 显示 UI 对象。
      * - false
        - 隐藏 UI 对象。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-enabled:

  **bool enabled() const**

判断是否响应 UI 事件。

* **返回值**

  类型：**bool**

  .. list-table::
    :width: 100%

    * - true
      - 可响应
    * - false
      - 不可响应

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_enabled:

  **void setEnabled(bool value)**

设置是否响应 UI 事件。

* **参数**

  * ``value``

    类型：**bool**

    .. list-table::
      :width: 100%

      * - true
        - 启用对 UI 事件的响应。
      * - false
        - 禁用对 UI 事件的响应。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-size:

  **Size size() const**

获取矩形区域的 DIP 尺寸。

* **返回值**

  类型：**Size**

  以 DIP 为单位的尺寸。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_size:

  **void setSize(const Size& value)**

设置矩形区域的 DIP 尺寸。

* **参数**

  * ``value``

    类型：**const Size&**

    以 DIP 为单位的尺寸。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-width:

  **int width() const**

获取矩形区域的 DIP 宽度。

* **返回值**

  类型：**int**

  以 DIP 为单位的宽度。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_width:

  **void setWidth(int value)**

设置矩形区域的 DIP 宽度。

* **参数**

  * ``value``

    类型：**int**

    以 DIP 为单位的宽度。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-height:

  **int height() const**

获取矩形区域的 DIP 高度。

* **返回值**

  类型：**int**

  以 DIP 为单位的高度。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_height:

  **void setHeight(int value)**

设置矩形区域的 DIP 高度。

* **参数**

  * ``value``

    类型：**int**

    以 DIP 为单位的高度。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-position:

  **Point position() const**

获取矩形区域的相对 DIP 坐标（以父对象左上角为原点）。

* **返回值**

  类型：**Point**

  以 DIP 为单位的坐标。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-abs_position:

  **Point absPosition() const**

获取矩形区域的绝对 DIP 坐标（以根窗口左上角为原点）。

* **返回值**

  类型：**Point**

  以 DIP 为单位的坐标。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_position:

  **void setPosition(const Point& value)**

设置矩形区域的相对 DIP 坐标（以父对象左上角为原点）。

* **参数**

  * ``value``

    类型：**const Point&**

    以 DIP 为单位的坐标。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-x:

  **int x() const**

获取矩形区域的相对 DIP 水平偏移（以父对象左上角为原点）。

* **返回值**

  类型：**int**

  以 DIP 为单位的水平偏移。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-abs_x:

  **int absX() const**

获取矩形区域的绝对 DIP 水平偏移（以根窗口左上角为原点）。

* **返回值**

  类型：**int**

  以 DIP 为单位的水平偏移。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_x:

  **void setX(int value)**

设置矩形区域的相对 DIP 水平偏移（以父对象左上角为原点）。

* **参数**

  * ``value``

    类型：**int**

    以 DIP 为单位的水平偏移。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-y:

  **int y() const**

获取矩形区域的相对 DIP 垂直偏移（以父对象左上角为原点）。

* **返回值**

  类型：**int**

  以 DIP 为单位的垂直偏移。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-abs_y:

  **int absY() const**

获取矩形区域的绝对 DIP 垂直偏移（以根窗口左上角为原点）。

* **返回值**

  类型：**int**

  以 DIP 为单位的垂直偏移。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_y:

  **void setY(int value)**

设置矩形区域的相对 DIP 垂直偏移（以父对象左上角为原点）。

* **参数**

  * ``value``

    类型：**int**

    以 DIP 为单位的垂直偏移。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-color:

  **Color color() const**

获取矩形区域的背景颜色。

* **返回值**

  类型：**Color**

  背景颜色。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_color:

  **void setColor(const Color& value)**

设置矩形区域的背景颜色。

* **参数**

  类型：**const Color&**

  背景颜色。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-opacity:

  **float opacity() const**

获取矩形区域的背景不透明度。

* **返回值**

  类型：**float**

  背景不透明度。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_opacity:

  **void setOpacity(float value)**

设置矩形区域的背景不透明度。

* **参数**

  * ``value``

    类型：**float**

    背景不透明度。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-outline_width:

  **int outlineWidth() const**

获取矩形区域的边框 DIP 宽度。

* **返回值**

  类型：**int**

  以 DIP 为单位的宽度。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_outline_width:

  **void setOutlineWidth(int value)**

设置矩形区域的边框 DIP 宽度。

* **参数**

  * ``value``

    类型：**int**

    以 DIP 为单位的宽度。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-outline_color:

  **Color outlineColor() const**

获取矩形区域的边框颜色。

* **返回值**

  类型：**Color**

  边框颜色。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_outline_color:

  **void setOutlineColor(const Color& value)**

设置矩形区域的边框颜色。

* **参数**

  类型：**const Color&**

  边框颜色。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-outline_opacity:

  **float outlineOpacity() const**

获取矩形区域的边框不透明度。

* **返回值**

  类型：**float**

  边框不透明度。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_outline_opacity:

  **void setOutlineOpacity(float value)**

设置矩形区域的边框不透明度。

* **参数**

  * ``value``

    类型：**float**

    边框不透明度。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-image:

  **Image* image() const**

获取矩形区域的背景图像。

* **返回值**

  类型：**Image***

  背景图像的指针，无背景图像时为空值。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_image:

  **void setImage(Image* imgae)**

设置矩形区域的背景图像。

* **参数**

  * ``image``

    类型：**Image***

    背景图像的指针，传入空值来移除背景图像。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-round_radius:

  **int roundRadius() const**

获取矩形区域的 DIP 圆角半径。

* **返回值**

  类型：**int**

  以 DIP 为单位的半径。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_round_radius:

  **void setRoundRadius(int value)**

设置矩形区域的 DIP 圆角半径。

* **参数**

  * ``value``

    类型：**int**

    以 DIP 为单位的半径。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_global:

  **void setGlobal(bool value)**

设置 UI 对象的层级。

* **参数**

  * ``value``

    类型：**bool**

    .. list-table::
      :width: 100%

      * - true
        - 作为全局对象（由 Application 管理）。
      * - false
        - 作为其它对象的子对象（需要进一步设置）。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_focused:

  **void setFocused(bool value)**

设置 UI 对象是否可以获得焦点。

* **参数**

  * ``value``

    类型：**bool**

    .. list-table::
      :width: 100%

      * - true
        - 可以获得焦点。
      * - false
        - 不可以获得焦点。

* **备注**

  只有当 UI 对象可以获得焦点时才会触发 onGetFocus 和 onLoseFocus 回调函数。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-parent:

  **Panel* parent() const**

获取父 UI 对象。

* **返回值**

  类型：**Panel***

  父 UI 对象的指针，无父对象时为空值。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-set_parent:

  **void setParent(Panel* uiobj)**

设置父 UI 对象。

* **参数**

  * ``uiobj``

    类型：**Panel***

    父 UI 对象的指针，传入空值来取消与父对象的绑定。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-add_child:

  **void addChild(Panel* uiobj)**

添加子 UI 对象。

* **参数**

  * ``uiobj``

    类型：**Panel***

    待添加的子 UI 对象的指针。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-remove_child:

  **void removeChild(Panel* uiobj)**

移除子 UI 对象。

* **参数**

  * ``uiobj``

    类型：**Panel***

    待移除的子 UI 对象的指针。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-move_topmost:

  **void moveTopmost()**

将 UI 对象置于最顶层（给予最高优先级）。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-move_above:

  **void moveAbove(Panel* uiobj)**

将 UI 对象置于其它对象之上（给予更高的优先级）。

* **参数**

  * ``uiobj``

    类型：**Panel***

    具有较低优先级的 UI 对象。

.. _d14uikit-reference-cpp-ui_controls-panel-isntm-move_below:

  **void moveBelow(Panel* uiobj)**

将 UI 对象置于其它对象之下（给予更低的优先级）。

* **参数**

  * ``uiobj``

    类型：**Panel***

    具有较高优先级的 UI 对象。

.. _d14uikit-reference-cpp-ui_controls-panel-virtm-on_update:

  **virtual void onUpdate()**

.. list-table::
  :width: 100%
  :stub-columns: 1

  * - 触发条件
    - 每帧的更新阶段
  * - functor 对象
    - .. sourcecode:: c++

        std::function<void(Panel*)> onUpdate = {};

  * - lambda 模板
    - 通用写法:

      .. sourcecode:: c++

        XXXX.Panel::callback().onUpdate =
        [/*capture list*/](Panel* p)
        {
            // add code here
        };

      需要 Callback.h:

      .. sourcecode:: c++

        XXXX.D14_onUpdate(p, /*capture list*/)
        {
            // add code here
        };

.. _d14uikit-reference-cpp-ui_controls-panel-virtm-on_size:

  **virtual void onSize(SizeEvent* event)**

.. list-table::
  :width: 100%
  :stub-columns: 1

  * - 触发条件
    - 矩形区域的尺寸改变
  * - functor 对象
    - .. sourcecode:: c++

        std::function<void(Panel*, SizeEvent*)> onSize = {};

  * - lambda 模板
    - 通用写法:

      .. sourcecode:: c++

        XXXX.Panel::callback().onSize =
        [/*capture list*/](Panel* p, SizeEvent* e)
        {
            // add code here
        };

      需要 Callback.h:

      .. sourcecode:: c++

        XXXX.D14_onSize(p, e, /*capture list*/)
        {
            // add code here
        };

.. _d14uikit-reference-cpp-ui_controls-panel-virtm-on_move:

  **virtual void onMove(MoveEvent* event)**

.. list-table::
  :width: 100%
  :stub-columns: 1

  * - 触发条件
    - 矩形区域的坐标改变
  * - functor 对象
    - .. sourcecode:: c++

        std::function<void(Panel*, MoveEvent*)> onMove = {};

  * - lambda 模板
    - 通用写法:

      .. sourcecode:: c++

        XXXX.Panel::callback().onMove =
        [/*capture list*/](Panel* p, MoveEvent* e)
        {
            // add code here
        };

      需要 Callback.h:

      .. sourcecode:: c++

        XXXX.D14_onMove(p, e, /*capture list*/)
        {
            // add code here
        };

.. _d14uikit-reference-cpp-ui_controls-panel-virtm-on_change_theme:

  **virtual void onChangeTheme(const std::wstring& name)**

.. list-table::
  :width: 100%
  :stub-columns: 1

  * - 触发条件
    - 应用程序的主题改变
  * - functor 对象
    - .. sourcecode:: c++

        std::function<void(Panel*, const std::wstring&)> onChangeTheme = {};

  * - lambda 模板
    - 通用写法:

      .. sourcecode:: c++

        XXXX.Panel::callback().onChangeTheme =
        [/*capture list*/](Panel* p, const std::wstring& name)
        {
            // add code here
        };

      需要 Callback.h:

      .. sourcecode:: c++

        XXXX.D14_onChangeTheme(p, name, /*capture list*/)
        {
            // add code here
        };

.. _d14uikit-reference-cpp-ui_controls-panel-virtm-on_change_lang_locale:

  **virtual void onChangeLangLocale(const std::wstring& name)**

.. list-table::
  :width: 100%
  :stub-columns: 1

  * - 触发条件
    - 应用程序的语言与区域改变
  * - functor 对象
    - .. sourcecode:: c++

        std::function<void(Panel*, const std::wstring&)> onChangeLangLocale = {};

  * - lambda 模板
    - 通用写法:

      .. sourcecode:: c++

        XXXX.Panel::callback().onChangeLangLocale =
        [/*capture list*/](Panel* p, const std::wstring& name)
        {
            // add code here
        };

      需要 Callback.h:

      .. sourcecode:: c++

        XXXX.D14_onChangeLangLocale(p, name, /*capture list*/)
        {
            // add code here
        };

.. _d14uikit-reference-cpp-ui_controls-panel-virtm-on_get_focus:

  **virtual void onGetFocus()**

.. list-table::
  :width: 100%
  :stub-columns: 1

  * - 触发条件
    - UI 对象获得焦点
  * - functor 对象
    - .. sourcecode:: c++

        std::function<void(Panel*)> onGetFocus = {};

  * - lambda 模板
    - 通用写法:

      .. sourcecode:: c++

        XXXX.Panel::callback().onGetFocus =
        [/*capture list*/](Panel* p)
        {
            // add code here
        };

      需要 Callback.h:

      .. sourcecode:: c++

        XXXX.D14_onGetFocus(p, /*capture list*/)
        {
            // add code here
        };

.. _d14uikit-reference-cpp-ui_controls-panel-virtm-on_lose_focus:

  **virtual void onLoseFocus()**

.. list-table::
  :width: 100%
  :stub-columns: 1

  * - 触发条件
    - UI 对象失去焦点
  * - functor 对象
    - .. sourcecode:: c++

        std::function<void(Panel*)> onLoseFocus = {};

  * - lambda 模板
    - 通用写法:

      .. sourcecode:: c++

        XXXX.Panel::callback().onLoseFocus =
        [/*capture list*/](Panel* p)
        {
            // add code here
        };

      需要 Callback.h:

      .. sourcecode:: c++

        XXXX.D14_onLoseFocus(p, /*capture list*/)
        {
            // add code here
        };

.. _d14uikit-reference-cpp-ui_controls-panel-virtm-on_mouse_enter:

  **virtual void onMouseEnter(MouseMoveEvent* event)**

.. list-table::
  :width: 100%
  :stub-columns: 1

  * - 触发条件
    - 鼠标指针进入矩形区域
  * - functor 对象
    - .. sourcecode:: c++

        std::function<void(Panel*, MouseMoveEvent*)> onMouseEnter = {};

  * - lambda 模板
    - 通用写法:

      .. sourcecode:: c++

        XXXX.Panel::callback().onMouseEnter =
        [/*capture list*/](Panel* p, MouseMoveEvent* e)
        {
            // add code here
        };

      需要 Callback.h:

      .. sourcecode:: c++

        XXXX.D14_onMouseEnter(p, e, /*capture list*/)
        {
            // add code here
        };

.. _d14uikit-reference-cpp-ui_controls-panel-virtm-on_mouse_move:

  **virtual void onMouseMove(MouseMoveEvent* event)**

.. list-table::
  :width: 100%
  :stub-columns: 1

  * - 触发条件
    - 鼠标指针在矩形区域内移动
  * - functor 对象
    - .. sourcecode:: c++

        std::function<void(Panel*, MouseMoveEvent*)> onMouseMove = {};

  * - lambda 模板
    - 通用写法:

      .. sourcecode:: c++

        XXXX.Panel::callback().onMouseMove =
        [/*capture list*/](Panel* p, MouseMoveEvent* e)
        {
            // add code here
        };

      需要 Callback.h:

      .. sourcecode:: c++

        XXXX.D14_onMouseMove(p, e, /*capture list*/)
        {
            // add code here
        };

.. _d14uikit-reference-cpp-ui_controls-panel-virtm-on_mouse_leave:

  **virtual void onMouseLeave(MouseMoveEvent* event)**

.. list-table::
  :width: 100%
  :stub-columns: 1

  * - 触发条件
    - 鼠标指针离开矩形区域
  * - functor 对象
    - .. sourcecode:: c++

        std::function<void(Panel*, MouseMoveEvent*)> onMouseLeave = {};

  * - lambda 模板
    - 通用写法:

      .. sourcecode:: c++

        XXXX.Panel::callback().onMouseLeave =
        [/*capture list*/](Panel* p, MouseMoveEvent* e)
        {
            // add code here
        };

      需要 Callback.h:

      .. sourcecode:: c++

        XXXX.D14_onMouseLeave(p, e, /*capture list*/)
        {
            // add code here
        };

.. _d14uikit-reference-cpp-ui_controls-panel-virtm-on_mouse_button:

  **virtual void onMouseButton(MouseButtonEvent* event)**

.. list-table::
  :width: 100%
  :stub-columns: 1

  * - 触发条件
    - 鼠标指针在矩形区域内，并使用按钮
  * - functor 对象
    - .. sourcecode:: c++

        std::function<void(Panel*, MouseButtonEvent*)> onMouseButton = {};

  * - lambda 模板
    - 通用写法:

      .. sourcecode:: c++

        XXXX.Panel::callback().onMouseButton =
        [/*capture list*/](Panel* p, MouseButtonEvent* e)
        {
            // add code here
        };

      需要 Callback.h:

      .. sourcecode:: c++

        XXXX.D14_onMouseButton(p, e, /*capture list*/)
        {
            // add code here
        };

.. _d14uikit-reference-cpp-ui_controls-panel-virtm-on_mouse_wheel:

  **virtual void onMouseWheel(MouseWheelEvent* event)**

.. list-table::
  :width: 100%
  :stub-columns: 1

  * - 触发条件
    - 鼠标指针在矩形区域内，并使用滚轮
  * - functor 对象
    - .. sourcecode:: c++

        std::function<void(Panel*, MouseWheelEvent*)> onMouseWheel = {};

  * - lambda 模板
    - 通用写法:

      .. sourcecode:: c++

        XXXX.Panel::callback().onMouseWheel =
        [/*capture list*/](Panel* p, MouseWheelEvent* e)
        {
            // add code here
        };

      需要 Callback.h:

      .. sourcecode:: c++

        XXXX.D14_onMouseWheel(p, e, /*capture list*/)
        {
            // add code here
        };

.. _d14uikit-reference-cpp-ui_controls-panel-virtm-on_keyboard:

  **virtual void onKeyboard(KeyboardEvent* event)**

.. list-table::
  :width: 100%
  :stub-columns: 1

  * - 触发条件
    - 鼠标指针在矩形区域内（或 UI 对象获得焦点），并使用键盘
  * - functor 对象
    - .. sourcecode:: c++

        std::function<void(Panel*, KeyboardEvent*)> onKeyboard = {};

  * - lambda 模板
    - 通用写法:

      .. sourcecode:: c++

        XXXX.Panel::callback().onKeyboard =
        [/*capture list*/](Panel* p, KeyboardEvent* e)
        {
            // add code here
        };

      需要 Callback.h:

      .. sourcecode:: c++

        XXXX.D14_onKeyboard(p, e, /*capture list*/)
        {
            // add code here
        };
