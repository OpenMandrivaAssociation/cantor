%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE Interface for doing Mathematics and Scientific Computing
Name:		cantor
Version:	16.04.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/cantor/
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(libR)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(luajit)
BuildRequires:	pkgconfig(libspectre)
BuildRequires:	pkgconfig(libqalculate)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(python2)
BuildRequires:	cmake(Analitza5)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5Pty)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5XmlPatterns)
BuildRequires:	cmake(Qt5Test)

%description
Cantor is a KDE Application aimed to provide a nice Interface
for doing Mathematics and Scientific Computing. It doesn't implement
its own Computation Logic, but instead is built around different
Backends.

%files
%doc README TODO
%doc %{_docdir}/HTML/en/cantor
%{_bindir}/cantor
%{_bindir}/cantor_python3server
%{_bindir}/cantor_rserver
%{_libdir}/libcantor_config.so
%{_libdir}/libcantor_pythonbackend.so
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
%{_datadir}/appdata/org.kde.cantor.appdata.xml
%{_datadir}/config.kcfg/cantor.kcfg
%{_datadir}/config.kcfg/cantor_libs.kcfg
%{_datadir}/config.kcfg/kalgebrabackend.kcfg
%{_datadir}/config.kcfg/luabackend.kcfg
%{_datadir}/config.kcfg/maximabackend.kcfg
%{_datadir}/config.kcfg/octavebackend.kcfg
%{_datadir}/config.kcfg/python2backend.kcfg
%{_datadir}/config.kcfg/python3backend.kcfg
%{_datadir}/config.kcfg/qalculatebackend.kcfg
%{_datadir}/config.kcfg/rserver.kcfg
%{_datadir}/config.kcfg/sagebackend.kcfg
%{_datadir}/config.kcfg/scilabbackend.kcfg
%{_datadir}/kxmlgui5/cantor

#---------------------------------------------

%define cantorlibs_major 6
%define libcantorlibs %mklibname cantorlibs %{cantorlibs_major}

%package -n %{libcantorlibs}
Summary:	Runtime library for cantor
Group:		System/Libraries
Obsoletes:	%{mklibname cantorlibs 0} < %{EVRD}

%description -n %{libcantorlibs}
Runtime library for cantor.

%files -n %{libcantorlibs}
%{_libdir}/libcantorlibs.so.0*
%{_libdir}/libcantorlibs.so.%{cantorlibs_major}

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

#----------------------------------------------------------------------

%prep
%setup -q
# Hardcoded old version path...
sed -i -e 's,luajit-2.0,luajit-2.1,g' src/backends/lua/*.{cpp,h}
# looks for python and python3 rather than python2 and 3
%cmake_kde5 -DPYTHON_EXECUTABLE=%{__python2}

%build
%ninja -C build

%install
%ninja_install -C build
