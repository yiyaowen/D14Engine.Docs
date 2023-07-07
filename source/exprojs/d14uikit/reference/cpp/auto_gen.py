# HOW TO USE:
# Place D14UIKit.pyd and D14UIKit.pyi (optional) in the same path with this script,
# and then run the script with an interpreter of Python.

from sys import argv

from D14UIKit import *

APP_NAME = 'AutoGen'

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

bool destory();

bool visible() const;
void setVisible(bool value);

bool enabled() const;
void setEnabled(bool value);'''

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

    # instm: instance method
    instmDstBox = RawTextEditor()
    instmDstBox.editable = False
    instmDstBox.placeholder.text = 'Instance Method'

    instmDstBox.parent = clntArea
    instmDstBox.size = Size(350, 267)
    instmDstBox.position = Point(440, 10)
    instmDstBox.roundRadius = 5
    instmDstBox.textRect = Rect(5, 5, 345, 262)

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

    def autoGen(btn, e):
        if e.left:
            root = camel2underl(uicodRotBox.text)
            lines = uicodSrcBox.text.splitlines()
            lines = [l.strip() for l in lines if l != '']
            instm = list()
            ddesc = list()
            for l in lines:
                l = l[:l.find(';')]
                lpos = l.find('(')
                rpos = l.find(')')
                retAndName = l[:lpos].rsplit(None, 1)
                underlName = camel2underl(retAndName[1])
                paramsInfo = l[lpos:rpos+1]
                suffixInfo = l[rpos+1:].strip()
                # generate instance method
                instm.append('    * - ' + retAndName[0] + \
                    '\n      - :ref:`' + retAndName[1] + \
                    '<d14uikit-reference-cpp-ui_controls-' + root + \
                    '-isntm-' + underlName + '>` ' + \
                    paramsInfo + '\n      - ' + suffixInfo)
                # generate detailed description
                ddesc.append('.. _d14uikit-reference-cpp-ui_controls-' + \
                             root + '-isntm-' + underlName + \
                            ':\n\n  **' + l + '**')
            instmDstBox.text = '\n'.join(instm)
            ddescDstBox.text = '\n\n'.join(ddesc)
    uicodGenBtn.f_onMouseButtonRelease = autoGen

    exit(app.run())
