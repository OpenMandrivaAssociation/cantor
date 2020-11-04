# Currently julia lives in contrib and cantor lives in main
# Got to disable Julia support by default until one of them moves
%bcond_with julia

%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE Interface for doing Mathematics and Scientific Computing
Name:		cantor
Version:	20.08.3
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/cantor/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(libR)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(luajit)
BuildRequires:	pkgconfig(libspectre)
BuildRequires:	pkgconfig(libqalculate)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(python2)
BuildRequires:	pkgconfig(poppler-qt5)
BuildRequires:	cmake(Analitza5)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5Pty)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5SyntaxHighlighting)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5XmlPatterns)
BuildRequires:	cmake(Qt5Test)
%if %{with julia}
BuildRequires:	julia-devel
%endif

%description
Cantor is a KDE Application aimed to provide a nice Interface
for doing Mathematics and Scientific Computing. It doesn't implement
its own Computation Logic, but instead is built around different
Backends.

%files -f cantor.lang
%{_bindir}/cantor
%{_bindir}/cantor_pythonserver
%{_bindir}/cantor_scripteditor
%if %{with julia}
%{_bindir}/cantor_juliaserver
%{_datadir}/config.kcfg/juliabackend.kcfg
%endif
%{_bindir}/cantor_rserver
%{_libdir}/libcantor_config.so
%{_libdir}/cantor_pythonbackend.so
%{_sysconfdir}/xdg/cantor*
%dir %{_qt5_plugindir}/cantor
%dir %{_qt5_plugindir}/cantor/assistants
%dir %{_qt5_plugindir}/cantor/backends
%dir %{_qt5_plugindir}/cantor/panels
%{_qt5_plugindir}/cantor/assistants/cantor*.so
%{_qt5_plugindir}/cantor/backends/cantor*.so
%{_qt5_plugindir}/cantor/panels/cantor*.so
%{_qt5_plugindir}/libcantorpart.so
%{_datadir}/applications/org.kde.cantor.desktop
%{_datadir}/cantor
%{_iconsdir}/*/*/apps/cantor.*
%{_iconsdir}/*/*/apps/luabackend.png
%{_iconsdir}/*/*/apps/maximabackend.png
%{_iconsdir}/*/*/apps/octavebackend.png
%{_iconsdir}/*/*/apps/pythonbackend.png
%{_iconsdir}/*/*/apps/qalculatebackend.png
%{_iconsdir}/*/*/apps/rbackend.png
%{_iconsdir}/*/*/apps/sagebackend.png
%{_iconsdir}/*/*/apps/scilabbackend.png
%{_iconsdir}/*/*/apps/kalgebrabackend.png
%{_datadir}/config.kcfg/cantor.kcfg
%{_datadir}/config.kcfg/cantor_libs.kcfg
%{_datadir}/config.kcfg/kalgebrabackend.kcfg
%{_datadir}/config.kcfg/luabackend.kcfg
%{_datadir}/config.kcfg/maximabackend.kcfg
%{_datadir}/config.kcfg/octavebackend.kcfg
%{_datadir}/config.kcfg/pythonbackend.kcfg
%{_datadir}/config.kcfg/qalculatebackend.kcfg
%{_datadir}/config.kcfg/rserver.kcfg
%{_datadir}/config.kcfg/sagebackend.kcfg
%{_datadir}/config.kcfg/scilabbackend.kcfg
%{_datadir}/kxmlgui5/cantor
%{_datadir}/icons/hicolor/48x48/apps/juliabackend.png
%{_datadir}/metainfo/org.kde.cantor.appdata.xml

#---------------------------------------------

%define cantorlibs_major 27
%define libcantorlibs %mklibname cantorlibs %{cantorlibs_major}

%package -n %{libcantorlibs}
Summary:	Runtime library for cantor
Group:		System/Libraries
Obsoletes:	%{mklibname cantorlibs 0} < %{EVRD}
Obsoletes:	%{mklibname cantorlibs 6} < %{EVRD}
Obsoletes:	%{mklibname cantorlibs 17} < %{EVRD}
Obsoletes:	%{mklibname cantorlibs 18} < %{EVRD}
Obsoletes:	%{mklibname cantorlibs 19} < %{EVRD}
Obsoletes:	%{mklibname cantorlibs 20} < %{EVRD}
Obsoletes:	%{mklibname cantorlibs 21} < %{EVRD}
Obsoletes:	%{mklibname cantorlibs 22} < %{EVRD}
Obsoletes:	%{mklibname cantorlibs 23} < %{EVRD}
Obsoletes:	%{mklibname cantorlibs 24} < %{EVRD}

%description -n %{libcantorlibs}
Runtime library for cantor.

%files -n %{libcantorlibs}
%{_libdir}/libcantorlibs.so.%{version}
%{_libdir}/libcantorlibs.so.%{cantorlibs_major}*

#---------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libcantorlibs} = %{EVRD}
Conflicts:	kdeedu4-devel < 4.6.90

%description devel
Files needed to build applications based on %{name}.

%files devel
%{_libdir}/libcantorlibs.so
%{_includedir}/%{name}
%{_libdir}/cmake/Cantor

#----------------------------------------------------------------------

%prep
%autosetup -p1
# Hardcoded old version path...
sed -i -e 's,luajit-2.0,luajit-2.1,g' src/backends/lua/*.{cpp,h}
%cmake_kde5 \
	-DPYTHONLIBS3_LIBRARY=$(ls -1 %{_libdir}/libpython3.[0-9]*.so |tail -n1)

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang cantor --with-html
