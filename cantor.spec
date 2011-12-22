Name: cantor
Summary: KDE Interface for doing Mathematics and Scientific Computing
Version: 4.7.95
Release: 1
Group: Graphical desktop/KDE
License: GPLv2
URL: http://edu.kde.org/cantor/
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%{name}-%version.tar.bz2
Patch1: kdeedu-4.6.90-cantor-rpath.patch
BuildRequires: kdelibs4-devel >= 2:%{version}
BuildRequires: pkgconfig(libR)
BuildRequires: pkgconfig(libspectre)

%description
Cantor is a KDE Application aimed to provide a nice Interface 
for doing Mathematics and Scientific Computing. It doesn't implement 
its own Computation Logic, but instead is built around different 
Backends. 

%files 
%_kde_bindir/cantor
%_kde_bindir/cantor_rserver
%_kde_libdir/kde4/cantor_creatematrixassistant.so
%_kde_libdir/kde4/cantor_differentiateassistant.so
%_kde_libdir/kde4/cantor_eigenvaluesassistant.so
%_kde_libdir/kde4/cantor_eigenvectorsassistant.so
%_kde_libdir/kde4/cantor_integrateassistant.so
%_kde_libdir/kde4/cantor_invertmatrixassistant.so
%_kde_libdir/kde4/cantor_maximabackend.so
%_kde_libdir/kde4/cantor_nullbackend.so
%_kde_libdir/kde4/cantor_octavebackend.so
%_kde_libdir/kde4/cantor_runscriptassistant.so
%_kde_libdir/kde4/cantor_sagebackend.so
%_kde_libdir/kde4/cantor_solveassistant.so
%_kde_libdir/kde4/cantor_plot2dassistant.so
%_kde_libdir/kde4/cantor_plot3dassistant.so
%_kde_libdir/kde4/cantor_advancedplotassistant.so
%_kde_libdir/kde4/cantor_helppanelplugin.so
%_kde_libdir/kde4/cantor_variablemanagerplugin.so
%_kde_libdir/kde4/cantor_rbackend.so
%_kde_libdir/kde4/cantor_scilabbackend.so
%_kde_libdir/kde4/libcantorpart.so
%_kde_libdir/libcantor_config.so
%_kde_datadir/applications/kde4/cantor.desktop
%_kde_appsdir/cantor
%_kde_iconsdir/*/*/apps/cantor.*
%_kde_iconsdir/*/*/apps/maximabackend.png
%_kde_iconsdir/*/*/apps/octavebackend.png
%_kde_iconsdir/*/*/apps/rbackend.png
%_kde_iconsdir/*/*/apps/sagebackend.png
%_kde_iconsdir/*/*/apps/qalculatebackend.png
%_kde_iconsdir/*/*/apps/scilabbackend.png
%_kde_configdir/cantor*.knsrc
%_kde_datadir/config.kcfg/cantor.kcfg
%_kde_datadir/config.kcfg/cantor_libs.kcfg
%_kde_datadir/config.kcfg/octavebackend.kcfg
%_kde_datadir/config.kcfg/maximabackend.kcfg
%_kde_datadir/config.kcfg/sagebackend.kcfg
%_kde_datadir/config.kcfg/scilabbackend.kcfg
%_kde_datadir/config.kcfg/rserver.kcfg
%_kde_services/cantor
%_kde_servicetypes/cantor_assistant.desktop
%_kde_servicetypes/cantor_backend.desktop
%_kde_servicetypes/cantor_panelplugin.desktop
%doc README TODO
%doc %_kde_docdir/HTML/en/cantor

#---------------------------------------------

%define cantorlibs_major 0
%define libcantorlibs %mklibname cantorlibs %{cantorlibs_major}

%package -n %libcantorlibs
Summary: Runtime library for cantor
Group: System/Libraries

%description -n %libcantorlibs
Runtime library for cantor

%files -n %libcantorlibs
%_kde_libdir/libcantorlibs.so.%{cantorlibs_major}*
%_kde_libdir/libcantorlibs.so.1

#---------------------------------------------

%package devel
Summary: Devel stuff for %{name}
Group: Development/KDE and Qt
Requires: %libcantorlibs = %version-%release
Conflicts: kdeedu4-devel < 4.6.90

%description  devel
Files needed to build applications based on %{name}.

%files devel
%_kde_libdir/libcantorlibs.so
%_includedir/%{name}

#----------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%cmake_kde4 
%make

%install
%makeinstall_std -C build

