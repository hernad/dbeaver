{
    # Pass -D VERSION_SUFFIX=<something> to gyp to override the suffix.
    #
    # The winpty.gyp file ignores the BUILD_INFO.txt file, if it exists.
    #
    # The MSVC generator is the default.  Select the compiler version by
    # passing -G msvs_version=<ver> to gyp.  <ver> is a string like 2013e.
    # See gyp\pylib\gyp\MSVSVersion.py for sample version strings.  You
    # can also pass configurations.gypi to gyp for 32-bit and 64-bit builds.
    # See that file for details.
    #
    # Pass --format=make to gyp to generate a Makefile instead.  The Makefile
    # can be configured by passing variables to make, e.g.:
    #    make -j4 CXX=i686-w64-mingw32-g++ LDFLAGS="-static -static-libgcc -static-libstdc++"

    'variables' : {
        'VERSION_SUFFIX%' : '-dev',
    },
    'target_defaults' : {
        'defines' : [
            'UNICODE',
            '_UNICODE',
            '_WIN32_WINNT=0x0501',
            'NOMINMAX',
            'WINPTY_VERSION=<!(cmd /c "cd .. && type VERSION.txt")',
            'WINPTY_VERSION_SUFFIX=<(VERSION_SUFFIX)',
            'WINPTY_COMMIT_HASH=<!(cmd /c "cd shared && GetCommitHash.cmd")',
        ],
    },
    'targets' : [
        {
            'target_name' : 'winpty-agent',
            'type' : 'executable',
            'include_dirs' : [
                'include',
            ],
            'defines' : [
                'WINPTY_AGENT_ASSERT',
            ],
            'libraries' : [
                '-lshell32',
                '-luser32',
            ],
            'msvs_settings': {
                # Specify this setting here to override a setting from somewhere
                # else, such as node's common.gypi.
                'VCCLCompilerTool': {
                    'ExceptionHandling': '1', # /EHsc
                },
            },
            'sources' : [
                'agent/Agent.h',
                'agent/Agent.cc',
                'agent/ConsoleFont.cc',
                'agent/ConsoleFont.h',
                'agent/ConsoleInput.cc',
                'agent/ConsoleInput.h',
                'agent/ConsoleLine.cc',
                'agent/ConsoleLine.h',
                'agent/Coord.h',
                'agent/DebugShowInput.h',
                'agent/DebugShowInput.cc',
                'agent/DefaultInputMap.h',
                'agent/DefaultInputMap.cc',
                'agent/DsrSender.h',
                'agent/EventLoop.h',
                'agent/EventLoop.cc',
                'agent/InputMap.h',
                'agent/InputMap.cc',
                'agent/LargeConsoleRead.h',
                'agent/LargeConsoleRead.cc',
                'agent/NamedPipe.h',
                'agent/NamedPipe.cc',
                'agent/SimplePool.h',
                'agent/SmallRect.h',
                'agent/Terminal.h',
                'agent/Terminal.cc',
                'agent/UnicodeEncoding.h',
                'agent/Win32Console.cc',
                'agent/Win32Console.h',
                'agent/main.cc',
                'shared/AgentMsg.h',
                'shared/Buffer.h',
                'shared/Buffer.cc',
                'shared/DebugClient.h',
                'shared/DebugClient.cc',
                'shared/OsModule.h',
                'shared/StringBuilder.h',
                'shared/StringUtil.cc',
                'shared/StringUtil.h',
                'shared/UnixCtrlChars.h',
                'shared/WindowsVersion.h',
                'shared/WindowsVersion.cc',
                'shared/WinptyAssert.h',
                'shared/WinptyAssert.cc',
                'shared/WinptyException.h',
                'shared/WinptyException.cc',
                'shared/WinptyVersion.h',
                'shared/WinptyVersion.cc',
                'shared/winpty_snprintf.h',
            ],
        },
        {
            'target_name' : 'winpty',
            'type' : 'shared_library',
            'include_dirs' : [
                'include',
            ],
            'defines' : [
                'COMPILING_WINPTY_DLL',
            ],
            'libraries' : [
                '-ladvapi32',
                '-luser32',
            ],
            'msvs_settings': {
                # Specify this setting here to override a setting from somewhere
                # else, such as node's common.gypi.
                'VCCLCompilerTool': {
                    'ExceptionHandling': '1', # /EHsc
                },
            },
            'sources' : [
                'include/winpty.h',
                'libwinpty/winpty.cc',
                'shared/AgentMsg.h',
                'shared/Buffer.h',
                'shared/Buffer.cc',
                'shared/DebugClient.h',
                'shared/DebugClient.cc',
                'shared/GenRandom.h',
                'shared/GenRandom.cc',
                'shared/OwnedHandle.h',
                'shared/OwnedHandle.cc',
                'shared/OsModule.h',
                'shared/StringBuilder.h',
                'shared/StringUtil.cc',
                'shared/StringUtil.h',
                'shared/WindowsSecurity.cc',
                'shared/WindowsSecurity.h',
                'shared/WindowsVersion.h',
                'shared/WindowsVersion.cc',
                'shared/WinptyAssert.h',
                'shared/WinptyAssert.cc',
                'shared/WinptyException.h',
                'shared/WinptyException.cc',
                'shared/WinptyVersion.h',
                'shared/WinptyVersion.cc',
                'shared/winpty_snprintf.h',
            ],
        },
        {
            'target_name' : 'winpty-debugserver',
            'type' : 'executable',
            'msvs_settings': {
                # Specify this setting here to override a setting from somewhere
                # else, such as node's common.gypi.
                'VCCLCompilerTool': {
                    'ExceptionHandling': '1', # /EHsc
                },
            },
            'sources' : [
                'debugserver/DebugServer.cc',
                'shared/DebugClient.h',
                'shared/DebugClient.cc',
                'shared/OwnedHandle.h',
                'shared/OwnedHandle.cc',
                'shared/OsModule.h',
                'shared/StringBuilder.h',
                'shared/StringUtil.cc',
                'shared/StringUtil.h',
                'shared/WindowsSecurity.h',
                'shared/WindowsSecurity.cc',
                'shared/WindowsVersion.h',
                'shared/WindowsVersion.cc',
                'shared/WinptyAssert.h',
                'shared/WinptyAssert.cc',
                'shared/WinptyException.h',
                'shared/WinptyException.cc',
                'shared/winpty_snprintf.h',
            ],
            'libraries' : [
                '-ladvapi32',
            ],
        }
    ],
}
