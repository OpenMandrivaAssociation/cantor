%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE Interface for doing Mathematics and Scientific Computing
Name:		cantor
Version:	15.04.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/cantor/
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	analitza-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(libR)
BuildRequires:	pkgconfig(libspectre)
BuildRequires:	pkgconfig(libqalculate)
BuildRequires:	pkgconfig(python)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5Pty)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5KDELibs4Support)

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
%{_libdir}/plugins/*cantor*.so
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
%{_datadir}/appdata/cantor.appdata.xml
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
%{_datadir}/kservices5/cantor
%{_datadir}/kservicetypes5/cantor_assistant.desktop
%{_datadir}/kservicetypes5/cantor_backend.desktop
%{_datadir}/kservicetypes5/cantor_panelplugin.desktop
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

%build
%cmake	-DKDE_INSTALL_USE_QT_SYS_PATH:BOOL=TRUE \
	-DPYTHON_INCLUDE_DIR:PATH=%{_includedir}/python2.7 \
	-DPYTHON_LIBRARY:PATH=%{_libdir}/libpython2.7.so \
	-G Ninja
ninja

%install
DESTDIR="%{buildroot}" ninja install -C build
