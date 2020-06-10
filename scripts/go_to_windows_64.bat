
set ROOT=C:\dev\dbeaver-ce\dbeaver\

cd %ROOT%

dir product\standalone\target\products\org.jkiss.dbeaver.core.product\win32\win32\x86_64\dbeaver\plugins\org.eclipse.tm.terminal.*
dir product\standalone\target\products\org.jkiss.dbeaver.core.product\win32\win32\x86_64\dbeaver\plugins\org.eclipse.cdt.*

REM pause

cd product\standalone\target\products\org.jkiss.dbeaver.core.product\win32\win32\x86_64\dbeaver

cmd.exe
REM dbeaver.exe -consolelog

cd %ROOT%