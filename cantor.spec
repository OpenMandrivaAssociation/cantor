# Currently julia lives in contrib and cantor lives in main
# Got to disable Julia support by default until one of them moves
%bcond_with julia

%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE Interface for doing Mathematics and Scientific Computing
Name:		cantor
Version:	24.12.3
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://edu.kde.org/cantor/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake ninja
BuildRequires:	pkgconfig(libR)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(luajit)
BuildRequires:	pkgconfig(libspectre)
BuildRequires:	pkgconfig(libqalculate)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(poppler-qt6)
BuildRequires:	pkgconfig(shared-mime-info)
BuildRequires:	cmake(Analitza6)
BuildRequires:	cmake(KF6TextEditor)
BuildRequires:	cmake(KF6Pty)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6Parts)
#BuildRequires:	cmake(KF6KDELibs4Support)
BuildRequires:	cmake(KF6SyntaxHighlighting)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6QmlCore)
BuildRequires:	cmake(Qt6QmlLocalStorage)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Xml)
#BuildRequires:	cmake(Qt6XmlPatterns)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Help)
#BuildRequires:	cmake(Qt6WebEngine)
BuildRequires:	cmake(Qt6WebEngineCore)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	R R-core
# For qhelpgenerator
BuildRequires:	qt6-qttools-assistant
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
%{_datadir}/mime/packages/cantor.xml
%{_datadir}/knsrcfiles/cantor*
%dir %{_libdir}/plugins/cantor_plugins/
#dir %{_libdir}/plugins/cantor_plugins/assistants
#dir %{_libdir}/plugins/cantor_plugins/backends
#dir %{_libdir}/plugins/cantor_plugins/panels
%{_libdir}/plugins/cantor_plugins/assistants/cantor*.so
%{_libdir}/plugins/cantor_plugins/backends/cantor*.so
%{_libdir}/plugins/cantor_plugins/panels/cantor*.so
%{_libdir}/plugins/kf6/parts/cantorpart.so
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
%{_datadir}/config.kcfg/octavebackend.kcfg.in
%{_datadir}/config.kcfg/pythonbackend.kcfg
%{_datadir}/config.kcfg/qalculatebackend.kcfg
%{_datadir}/config.kcfg/rserver.kcfg
%{_datadir}/config.kcfg/sagebackend.kcfg
%{_datadir}/config.kcfg/scilabbackend.kcfg
%{_datadir}/icons/hicolor/48x48/apps/juliabackend.png
%{_datadir}/metainfo/org.kde.cantor.appdata.xml

#---------------------------------------------

%define cantorlibs_major 28
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
Obsoletes:	%{mklibname cantorlibs 27} < %{EVRD}

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
%cmake -Wno-dev \
	-DPYTHONLIBS3_LIBRARY=$(ls -1 %{_libdir}/libpython3.[0-9]*.so |tail -n1) \
	-GNinja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang cantor --with-html
