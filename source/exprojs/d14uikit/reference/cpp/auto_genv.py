# Similar to auto_gen.py, but for callbacks (virtual methods).

from sys import argv

from D14UIKit import *

APP_NAME = 'AutoGenV'

if __name__ == '__main__':
    dpi = 96.0
    if len(argv) >= 2 and argv[1] == 'HighDPI':
        dpi = 192.0

    app = Application(APP_NAME, dpi)

    mwnd = MainWindow(APP_NAME)
    clntArea = Panel()
    mwnd.content = clntArea

    # uicod: ui code
    uicodRotBox = RawTextBox()
    uicodRotBox.placeholder.text = 'Example: Panel'

    uicodRotBox.parent = clntArea
    uicodRotBox.size = Size(350, 50)
    uicodRotBox.position = Point(10, 10)
    uicodRotBox.roundRadius = 5
    uicodRotBox.textRect = Rect(5, 5, 345, 45)

    uicodSrcBox = RawTextEditor()
    uicodSrcBox.placeholder.text = '''\
Example:

virtual void onUpdate();

virtual void onSize(SizeEvent* event);

virtual void onMove(MoveEvent* event);'''

    uicodSrcBox.parent = clntArea
    uicodSrcBox.size = Size(350, 484)
    uicodSrcBox.position = Point(10, 70)
    uicodSrcBox.roundRadius = 5
    uicodSrcBox.textRect = Rect(5, 5, 345, 479)

    uicodGenBtn = FilledButton('生成')
    uicodGenBtn.fontFamilyName = '默认'

    uicodGenBtn.parent = clntArea
    uicodGenBtn.size = Size(60, 64)
    uicodGenBtn.position = Point(370, 250)
    uicodGenBtn.roundRadius = 5

    # vertm: virtual method
    vertmDstBox = RawTextEditor()
    vertmDstBox.editable = False
    vertmDstBox.placeholder.text = 'Virtual Method'

    vertmDstBox.parent = clntArea
    vertmDstBox.size = Size(350, 267)
    vertmDstBox.position = Point(440, 10)
    vertmDstBox.roundRadius = 5
    vertmDstBox.textRect = Rect(5, 5, 345, 262)

    # ddesc: detailed description
    ddescDstBox = RawTextEditor()
    ddescDstBox.editable = False
    ddescDstBox.placeholder.text = 'Detailed Description'

    ddescDstBox.parent = clntArea
    ddescDstBox.size = Size(350, 267)
    ddescDstBox.position = Point(440, 287)
    ddescDstBox.roundRadius = 5
    ddescDstBox.textRect = Rect(5, 5, 345, 262)

    def camel2underl(s):
        if s == '':
            return ''
        t = s[0].lower()
        for a in s[1:]:
            if a.isupper():
                t = t + '_' + a.lower()
            else:
                t = t + a
        return t

    def autoGenV(btn, e):
        if e.left:
            root = camel2underl(uicodRotBox.text)
            lines = uicodSrcBox.text.splitlines()
            lines = [l.strip() for l in lines if l != '']
            vertm = list()
            ddesc = list()
            for l in lines:
                l = l[:l.find(';')]
                lpos = l.find('(')
                rpos = l.find(')')
                retAndName = l[:lpos].rsplit(None, 1)
                underlName = camel2underl(retAndName[1])
                paramsInfo = l[lpos:rpos+1]
                suffixInfo = l[rpos+1:].strip()
                # generate virtual method
                vertm.append('    * - ' + retAndName[0] + \
                    '\n      - :ref:`' + retAndName[1] + \
                    '<d14uikit-reference-cpp-ui_controls-' + root + \
                    '-virtm-' + underlName + '>` ' + paramsInfo)
                # generate detailed description
                ddesc.append('.. _d14uikit-reference-cpp-ui_controls-' + \
                             root + '-virtm-' + underlName + \
                            ':\n\n  **' + l + '**')
            vertmDstBox.text = '\n'.join(vertm)
            ddescDstBox.text = '\n\n'.join(ddesc)
    uicodGenBtn.f_onMouseButtonRelease = autoGenV

    exit(app.run())
